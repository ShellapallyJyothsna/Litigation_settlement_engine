import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

# --- 1. LOAD DATA ---
# Load the data you just generated
df = pd.read_csv("synthetic_workers_comp_data.csv")

# Separate Features (X) and Target (y)
# We want to predict 'Settlement Payout' based on the claim details
X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'])
# NOTE: We drop 'Medical Cost' and 'Indemnity Paid' because in a REAL new claim, 
# you don't know the final paid amounts yet. You only know the "Reserves" or initial estimates.
# For this demo, we predict based on the "Facts" (Injury, State, Attorney, Wage).

y = df['Settlement Payout']

# --- 2. BUILD THE PIPELINE ---
# We need to turn text (State, Body Part) into numbers for the AI
categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
numeric_features = ['Wage Information', 'Attorney Aggressiveness']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Initialize the Model (Gradient Boosting is excellent for tabular insurance data)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
])

# --- 3. TRAIN THE MODEL ---
print("Training the Litigation Engine...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pipeline.fit(X_train, y_train)

# Evaluate
predictions = model_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Model Trained! Average Error (MAE): ${round(mae, 2)}")
print("-" * 30)

# --- 4. THE PREDICTION ENGINE (User Interface Logic) ---
# This function simulates what the Claims Adjuster would see

def predict_settlement(claim_details):
    # A. Predict the specific number
    input_df = pd.DataFrame([claim_details])
    predicted_value = model_pipeline.predict(input_df)[0]
    
    # B. Calculate Recommended Range (based on model error margin)
    # In real life, you'd use Quantile Regression, but this is a good approximation
    low_bound = predicted_value * 0.85
    high_bound = predicted_value * 1.10
    
    # C. Confidence Score Logic
    # If the input data is standard, confidence is high. 
    # If it's an outlier (e.g. Wage is huge), confidence drops.
    confidence = "High"
    if claim_details['Wage Information'] > 3000 or claim_details['Attorney Aggressiveness'] > 9:
        confidence = "Medium" # Harder to predict extreme cases
        
    # D. Likelihood to Accept (Logic: If offer > prediction, high likelihood)
    # This is a derived metric for the UI
    market_value = predicted_value
    
    return {
        "Expected Settlement": round(predicted_value, 2),
        "Recommended Range": f"${round(low_bound, 2):,} - ${round(high_bound, 2):,}",
        "Confidence Score": confidence,
        "Key Driver": f"Attorney Aggr: {claim_details['Attorney Aggressiveness']} & Injury: {claim_details['Injury Nature']}"
    }

# --- 5. TEST THE ENGINE WITH A NEW CLAIM ---
# Let's simulate a new case coming in:
new_claim = {
    'State': 'New York',
    'Body Part': 'Back',
    'Injury Nature': 'Fracture', # Serious injury
    'Cause of Injury': 'Lifting',
    'Wage Information': 1200.00,
    'Comorbidity': False,
    'Attorney Firm': 'Firm C', # The expensive firm
    'Attorney Aggressiveness': 9, # Very aggressive
    'Medical Bill Categories': 'Surgery'
}

result = predict_settlement(new_claim)


# --- 6. NEGOTIATION STRATEGY MODULE ---

def calculate_negotiation_strategy(predicted_value, claim_details):
    print("\n--- NEGOTIATION STRATEGY ANALYSIS ---")
    
    # ---------------------------------------------------------
    # A. LIKELIHOOD OF ACCEPTANCE (The "Sigmoid" Curve)
    # ---------------------------------------------------------
    # Logic: 
    # - If Offer == Predicted Value, chance is ~50-60%.
    # - If Offer < Predicted, chance drops rapidly.
    # - If Offer > Predicted, chance approaches 100%.
    
    # We create 5 price points to show the adjuster
    offers = [0.8, 0.9, 1.0, 1.1, 1.2] # 80% to 120% of value
    
    print(f"\n1. Likelihood of Acceptance Curve (Target: ${predicted_value:,.0f})")
    print(f"{'Offer Amount':<15} | {'% Chance':<10} | {'Strategy'}")
    print("-" * 45)
    
    for pct in offers:
        offer_amt = predicted_value * pct
        
        # The Math: Sigmoid Function centered on the Predicted Value
        # 'k' is the steepness. Higher k = harder to get acceptance on low offers.
        k = 0.00005 
        
        # Shift the curve so that offering the exact predicted value gives ~60% acceptance
        # (People usually accept the "fair" market value)
        prob = 1 / (1 + np.exp(-k * (offer_amt - predicted_value * 0.95)))
        prob_pct = round(prob * 100, 1)
        
        # Strategy Tag
        if prob_pct < 30: tag = "Lowball (Risk of Anger)"
        elif prob_pct < 60: tag = "Aggressive Opening"
        elif prob_pct < 85: tag = "Fair / Settlement Zone"
        else: tag = "Overpayment"
        
        print(f"${offer_amt:,.0f}<15 | {prob_pct}%      | {tag}")

    # ---------------------------------------------------------
    # B. SAVINGS VS LITIGATION (The "ROI" Calculator)
    # ---------------------------------------------------------
    # Logic: Is (Settlement Now) < (Predicted Judgment + Future Defense Costs)?
    
    # Estimate Future Defense Costs (based on stage of claim)
    # If just starting (New York), costs are high.
    future_defense_cost = 0
    if claim_details['State'] in ['New York', 'California']:
        future_defense_cost = 45000 # Expensive states
    else:
        future_defense_cost = 15000
        
    # If attorney is aggressive, defense costs double (more motions/depositions)
    if claim_details['Attorney Aggressiveness'] > 7:
        future_defense_cost *= 1.5
        
    total_exposure_if_waiting = predicted_value + future_defense_cost
    recommended_settlement = predicted_value # The "Fair" price
    
    savings = total_exposure_if_waiting - recommended_settlement
    
    print(f"\n2. Litigation Cost-Benefit Analysis")
    print(f"   Predicted Liability if Trial:   ${predicted_value:,.0f}")
    print(f"   (+) Est. Future Defense Costs:  ${future_defense_cost:,.0f}")
    print(f"   (=) Total Risk Exposure:        ${total_exposure_if_waiting:,.0f}")
    print("-" * 40)
    
    if savings > 0:
        print(f"   RECOMMENDATION: SETTLE NOW.")
        print(f"   Why? Settling at ${recommended_settlement:,.0f} avoids ${future_defense_cost:,.0f} in legal fees.")
    else:
        print(f"   RECOMMENDATION: CONTINUE LITIGATION.")
        print(f"   Why? The demand is likely higher than the cost to defend.")

# --- EXECUTE MODULE ---
# Pass the previous results into this new function
calculate_negotiation_strategy(result['Expected Settlement'], new_claim)

print("--- LIGATION ENGINE OUTPUT ---")
print(f"Case Context: {new_claim['Injury Nature']} to {new_claim['Body Part']} in {new_claim['State']}")
print(f"Represented by: {new_claim['Attorney Firm']} (Aggressiveness: {new_claim['Attorney Aggressiveness']})")
print("\nPREDICTIONS:")
for k, v in result.items():
    print(f"{k}: {v}")