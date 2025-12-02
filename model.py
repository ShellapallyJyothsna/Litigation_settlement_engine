# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import mean_absolute_error

# # --- 1. LOAD DATA ---
# # Load the data you just generated
# df = pd.read_csv("synthetic_workers_comp_data.csv")

# # Separate Features (X) and Target (y)
# # We want to predict 'Settlement Payout' based on the claim details
# X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'])
# # NOTE: We drop 'Medical Cost' and 'Indemnity Paid' because in a REAL new claim, 
# # you don't know the final paid amounts yet. You only know the "Reserves" or initial estimates.
# # For this demo, we predict based on the "Facts" (Injury, State, Attorney, Wage).

# y = df['Settlement Payout']

# # --- 2. BUILD THE PIPELINE ---
# # We need to turn text (State, Body Part) into numbers for the AI
# categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
# numeric_features = ['Wage Information', 'Attorney Aggressiveness']

# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', 'passthrough', numeric_features),
#         ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#     ])

# # Initialize the Model (Gradient Boosting is excellent for tabular insurance data)
# model_pipeline = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
# ])

# # --- 3. TRAIN THE MODEL ---
# print("Training the Litigation Engine...")
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model_pipeline.fit(X_train, y_train)

# # Evaluate
# predictions = model_pipeline.predict(X_test)
# mae = mean_absolute_error(y_test, predictions)
# print(f"Model Trained! Average Error (MAE): ${round(mae, 2)}")
# print("-" * 30)

# # --- 4. THE PREDICTION ENGINE (User Interface Logic) ---
# # This function simulates what the Claims Adjuster would see

# def predict_settlement(claim_details):
#     # A. Predict the specific number
#     input_df = pd.DataFrame([claim_details])
#     predicted_value = model_pipeline.predict(input_df)[0]
    
#     # B. Calculate Recommended Range (based on model error margin)
#     # In real life, you'd use Quantile Regression, but this is a good approximation
#     low_bound = predicted_value * 0.85
#     high_bound = predicted_value * 1.10
    
#     # C. Confidence Score Logic
#     # If the input data is standard, confidence is high. 
#     # If it's an outlier (e.g. Wage is huge), confidence drops.
#     confidence = "High"
#     if claim_details['Wage Information'] > 3000 or claim_details['Attorney Aggressiveness'] > 9:
#         confidence = "Medium" # Harder to predict extreme cases
        
#     # D. Likelihood to Accept (Logic: If offer > prediction, high likelihood)
#     # This is a derived metric for the UI
#     market_value = predicted_value
    
#     return {
#         "Expected Settlement": round(predicted_value, 2),
#         "Recommended Range": f"${round(low_bound, 2):,} - ${round(high_bound, 2):,}",
#         "Confidence Score": confidence,
#         "Key Driver": f"Attorney Aggr: {claim_details['Attorney Aggressiveness']} & Injury: {claim_details['Injury Nature']}"
#     }

# # --- 5. TEST THE ENGINE WITH A NEW CLAIM ---
# # Let's simulate a new case coming in:
# new_claim = {
#     'State': 'New York',
#     'Body Part': 'Back',
#     'Injury Nature': 'Fracture', # Serious injury
#     'Cause of Injury': 'Lifting',
#     'Wage Information': 1200.00,
#     'Comorbidity': False,
#     'Attorney Firm': 'Firm C', # The expensive firm
#     'Attorney Aggressiveness': 9, # Very aggressive
#     'Medical Bill Categories': 'Surgery'
# }

# result = predict_settlement(new_claim)


# # --- 6. NEGOTIATION STRATEGY MODULE ---

# def calculate_negotiation_strategy(predicted_value, claim_details):
#     print("\n--- NEGOTIATION STRATEGY ANALYSIS ---")
    
#     # ---------------------------------------------------------
#     # A. LIKELIHOOD OF ACCEPTANCE (The "Sigmoid" Curve)
#     # ---------------------------------------------------------
#     # Logic: 
#     # - If Offer == Predicted Value, chance is ~50-60%.
#     # - If Offer < Predicted, chance drops rapidly.
#     # - If Offer > Predicted, chance approaches 100%.
    
#     # We create 5 price points to show the adjuster
#     offers = [0.8, 0.9, 1.0, 1.1, 1.2] # 80% to 120% of value
    
#     print(f"\n1. Likelihood of Acceptance Curve (Target: ${predicted_value:,.0f})")
#     print(f"{'Offer Amount':<15} | {'% Chance':<10} | {'Strategy'}")
#     print("-" * 45)
    
#     for pct in offers:
#         offer_amt = predicted_value * pct
        
#         # The Math: Sigmoid Function centered on the Predicted Value
#         # 'k' is the steepness. Higher k = harder to get acceptance on low offers.
#         k = 0.00005 
        
#         # Shift the curve so that offering the exact predicted value gives ~60% acceptance
#         # (People usually accept the "fair" market value)
#         prob = 1 / (1 + np.exp(-k * (offer_amt - predicted_value * 0.95)))
#         prob_pct = round(prob * 100, 1)
        
#         # Strategy Tag
#         if prob_pct < 30: tag = "Lowball (Risk of Anger)"
#         elif prob_pct < 60: tag = "Aggressive Opening"
#         elif prob_pct < 85: tag = "Fair / Settlement Zone"
#         else: tag = "Overpayment"
        
#         print(f"${offer_amt:,.0f}<15 | {prob_pct}%      | {tag}")

#     # ---------------------------------------------------------
#     # B. SAVINGS VS LITIGATION (The "ROI" Calculator)
#     # ---------------------------------------------------------
#     # Logic: Is (Settlement Now) < (Predicted Judgment + Future Defense Costs)?
    
#     # Estimate Future Defense Costs (based on stage of claim)
#     # If just starting (New York), costs are high.
#     future_defense_cost = 0
#     if claim_details['State'] in ['New York', 'California']:
#         future_defense_cost = 45000 # Expensive states
#     else:
#         future_defense_cost = 15000
        
#     # If attorney is aggressive, defense costs double (more motions/depositions)
#     if claim_details['Attorney Aggressiveness'] > 7:
#         future_defense_cost *= 1.5
        
#     total_exposure_if_waiting = predicted_value + future_defense_cost
#     recommended_settlement = predicted_value # The "Fair" price
    
#     savings = total_exposure_if_waiting - recommended_settlement
    
#     print(f"\n2. Litigation Cost-Benefit Analysis")
#     print(f"   Predicted Liability if Trial:   ${predicted_value:,.0f}")
#     print(f"   (+) Est. Future Defense Costs:  ${future_defense_cost:,.0f}")
#     print(f"   (=) Total Risk Exposure:        ${total_exposure_if_waiting:,.0f}")
#     print("-" * 40)
    
#     if savings > 0:
#         print(f"   RECOMMENDATION: SETTLE NOW.")
#         print(f"   Why? Settling at ${recommended_settlement:,.0f} avoids ${future_defense_cost:,.0f} in legal fees.")
#     else:
#         print(f"   RECOMMENDATION: CONTINUE LITIGATION.")
#         print(f"   Why? The demand is likely higher than the cost to defend.")

# # --- EXECUTE MODULE ---
# # Pass the previous results into this new function
# calculate_negotiation_strategy(result['Expected Settlement'], new_claim)

# print("--- LIGATION ENGINE OUTPUT ---")
# print(f"Case Context: {new_claim['Injury Nature']} to {new_claim['Body Part']} in {new_claim['State']}")
# print(f"Represented by: {new_claim['Attorney Firm']} (Aggressiveness: {new_claim['Attorney Aggressiveness']})")
# print("\nPREDICTIONS:")
# for k, v in result.items():
#     print(f"{k}: {v}")











#######previous version
# import pandas as pd
# import numpy as np
# import joblib # Used to save the model to disk
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import mean_absolute_error

# # --- 1. LOAD & PREPARE DATA ---
# def load_and_train():
#     print("⏳ Loading data and training AI models...")
#     df = pd.read_csv("synthetic_workers_comp_data.csv")

#     # Features (Inputs)
#     X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Days_to_Settle'])
    
#     # Targets (Outputs)
#     y_cost = df['Settlement Payout']
#     y_time = df['Days_to_Settle'] # NEW TARGET

#     # Preprocessing Pipeline
#     categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
#     numeric_features = ['Wage Information', 'Attorney Aggressiveness']

#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('num', 'passthrough', numeric_features),
#             ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#         ])

#     # --- TRAIN COST MODEL ---
#     model_cost = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
#     ])
#     model_cost.fit(X, y_cost)
#     print("✅ Cost Model Trained.")

#     # --- TRAIN TIME MODEL (NEW) ---
#     model_time = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(n_estimators=200, random_state=42))
#     ])
#     model_time.fit(X, y_time)
#     print("✅ Time Model Trained.")
    
#     return model_cost, model_time

# # Execute Training
# model_cost, model_time = load_and_train()

# # --- 2. PREDICTION ENGINE FUNCTION ---
# def predict_claim(claim_input, user_demand=0):
#     """
#     This function takes the raw inputs + the user's demand (optional)
#     and returns all the calculated metrics.
#     """
#     input_df = pd.DataFrame([claim_input])
    
#     # A. AI Predictions
#     pred_cost = model_cost.predict(input_df)[0]
#     pred_days = model_time.predict(input_df)[0]
    
#     # B. Calculate Ranges
#     low_bound = pred_cost * 0.88
#     high_bound = pred_cost * 1.12
    
#     # C. Calculate Defense Costs (Rule-Based)
#     state = claim_input['State']
#     aggression = claim_input['Attorney Aggressiveness']
    
#     base_defense = 45000 if state in ['New York', 'California'] else 15000
#     multiplier = 1.5 if aggression > 7 else 1.0
#     defense_fees = base_defense * multiplier
    
#     # D. Total Exposure
#     total_exposure = pred_cost + defense_fees
    
#     # E. ROI / Strategy Logic
#     # If user provided a demand, use it. Otherwise, simulate one.
#     if user_demand > 0:
#         active_demand = user_demand
#         is_simulated = False
#     else:
#         # Fallback Simulation
#         sim_mult = 2.5 if aggression >= 8 else (1.5 if aggression >= 6 else 1.1)
#         active_demand = pred_cost * sim_mult
#         is_simulated = True
        
#     savings = total_exposure - active_demand
#     recommendation = "SETTLE" if savings > 0 else "LITIGATE"
    
#     return {
#         "Target Settlement": round(pred_cost, 2),
#         "Range Low": round(low_bound, 2),
#         "Range High": round(high_bound, 2),
#         "Est Duration (Days)": int(pred_days),
#         "Est Duration (Months)": round(pred_days / 30, 1),
#         "Total Exposure": round(total_exposure, 2),
#         "Defense Fees": round(defense_fees, 2),
#         "Plaintiff Demand": round(active_demand, 2),
#         "Recommendation": recommendation,
#         "ROI Savings": round(savings, 2),
#         "Is Simulated Demand": is_simulated
#     }

# # --- 3. TEST THE BACKEND ---
# # This part only runs if you run 'python model.py' directly
# if __name__ == "__main__":
#     print("\n--- TESTING BACKEND LOGIC ---")
    
#     test_case = {
#         'State': 'New York',
#         'Body Part': 'Back',
#         'Injury Nature': 'Fracture',
#         'Cause of Injury': 'Lifting',
#         'Wage Information': 1200.00,
#         'Attorney Firm': 'Firm C',
#         'Attorney Aggressiveness': 6, # Moderate Aggression
#         'Medical Bill Categories': 'Surgery'
#     }
    
#     # Scenario 1: No User Input (AI Simulates Demand)
#     result = predict_claim(test_case, user_demand=0)
#     print(f"\n[Scenario 1] Simulated Demand:")
#     print(f"Target: ${result['Target Settlement']:,.0f}")
#     print(f"Time: {result['Est Duration (Days)']} Days")
#     print(f"Rec: {result['Recommendation']} (Savings: ${result['ROI Savings']:,.0f})")

#     # Scenario 2: User Inputs a High Demand (Should trigger Litigate)
#     print(f"\n[Scenario 2] User Enters $250,000 Demand:")
#     result_high = predict_claim(test_case, user_demand=250000)
#     print(f"Target: ${result_high['Target Settlement']:,.0f}")
#     print(f"Rec: {result_high['Recommendation']} (Savings: ${result_high['ROI Savings']:,.0f})")











##########33with gemini
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.pipeline import Pipeline

# # Global variables to hold the trained model
# _MODEL = None

# def load_and_train():
#     """
#     Loads the Enterprise Dataset and trains the Valuation Engine.
#     """
#     global _MODEL
    
#     try:
#         df = pd.read_csv("synthetic_litigation_db.csv")
#     except FileNotFoundError:
#         print("❌ Error: synthetic_litigation_db.csv not found.")
#         return None

#     # Features & Target
#     X = df.drop(columns=['Settlement_Amount', 'Action_Recommendation'])
#     y = df['Settlement_Amount']
    
#     # Preprocessing
#     cat_cols = [c for c in X.columns if X[c].dtype == 'object']
#     num_cols = [c for c in X.columns if X[c].dtype != 'object']
    
#     preprocessor = ColumnTransformer(transformers=[
#         ('num', StandardScaler(), num_cols),
#         ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
#     ])
    
#     # Pipeline
#     model = Pipeline(steps=[
#         ('prep', preprocessor),
#         ('reg', GradientBoostingRegressor(n_estimators=200, random_state=42))
#     ])
    
#     model.fit(X, y)
#     _MODEL = model
#     print("✅ Model Trained Successfully.")
#     return model

# def calculate_drivers(inputs, prediction):
#     """
#     Calculates specific financial drivers. 
#     Includes fallback logic so the list is never empty.
#     """
#     drivers = []
    
#     # 1. Attorney Impact
#     score = inputs['Attorney_Score']
#     if score > 60:
#         # Dynamic scaling: Higher score = Higher cost
#         impact = prediction * ((score - 50) / 200) 
#         drivers.append(("Aggressive Counsel Premium", impact, "pos"))
    
#     # 2. Jurisdiction Impact
#     if inputs['Venue_Win_Rate'] < 0.50:
#         impact = prediction * 0.08
#         drivers.append(("High-Risk Jurisdiction", impact, "pos"))
#     elif inputs['Venue_Win_Rate'] > 0.65:
#         impact = prediction * 0.05
#         drivers.append(("Favorable Venue History", -impact, "neg"))
        
#     # 3. Medical Impact
#     if inputs['Impairment_Rating'] > 10:
#         impact = inputs['Impairment_Rating'] * 1200
#         drivers.append(("Permanent Impairment Load", impact, "pos"))
        
#     # 4. Behavioral Driver
#     if inputs['Opioid_Indicator'] == 1:
#         drivers.append(("Opioid Usage Risk", 8500, "pos"))
        
#     # 5. Timing
#     if inputs['Days_Since_Filed'] > 365:
#         drivers.append(("Long Duration Penalty", 5000, "pos"))
#     elif inputs['Days_Since_Filed'] < 90:
#         drivers.append(("Early Resolution Window", -4000, "neg"))
        
#     # 6. Fallback (If list is empty, show base drivers)
#     if not drivers:
#         drivers.append(("Base Liability Value", prediction * 0.1, "pos"))
        
#     return drivers

# def predict_case(input_dict):
#     """
#     The Main API Function.
#     Takes raw inputs -> Returns a Dictionary of all Dashboard Metrics.
#     """
#     if _MODEL is None:
#         load_and_train()
    
#     # 1. Convert Dictionary to DataFrame for Prediction
#     input_df = pd.DataFrame([input_dict])
    
#     # 2. AI Prediction (Cost)
#     pred_val = _MODEL.predict(input_df)[0]
    
#     # 3. Time Prediction (Heuristic logic)
#     base_days = 180
#     if input_dict['Attorney_Tendency'] == 'Trial-Oriented': base_days += 200
#     if input_dict['Impairment_Rating'] > 15: base_days += 90
#     pred_days = int(base_days * 1.1)
#     pred_months = pred_days / 30
    
#     # 4. Range Calculation (Confidence Interval)
#     low_bound = pred_val * 0.88
#     high_bound = pred_val * 1.12
    
#     # 5. Total Exposure (Risk Logic)
#     defense_base = 15000
#     if input_dict['Jurisdiction'] in ['New York', 'California', 'Illinois']: 
#         defense_base = 45000
#     if input_dict['Attorney_Score'] > 70: 
#         defense_base *= 1.5
    
#     total_exposure = pred_val + defense_base
    
#     # 6. Recommendation Logic
#     demand = input_dict.get('Demand_Amount', 0)
#     if demand == 0:
#         # Simulate demand if user didn't enter one
#         demand = pred_val * (1.5 if input_dict['Attorney_Score'] > 70 else 1.1)
    
#     savings = total_exposure - demand
    
#     if savings > 0:
#         action = "SETTLE"
#         action_desc = "Demand is below Total Exposure."
#         is_safe = True
#     else:
#         action = "LITIGATE"
#         action_desc = "Demand exceeds Risk Cost."
#         is_safe = False
        
#     # 7. Litigation Score (Gauge Value)
#     lit_score = input_dict['Attorney_Score']
#     if lit_score > 80: 
#         risk_label = "HIGH RISK"
#         risk_color = "#EF4444"
#     elif lit_score > 50: 
#         risk_label = "MEDIUM RISK"
#         risk_color = "#F59E0B"
#     else: 
#         risk_label = "LOW RISK"
#         risk_color = "#10B981"

#     # 8. Get Drivers
#     drivers = calculate_drivers(input_dict, pred_val)

#     return {
#         "prediction": pred_val,
#         "range_low": low_bound,
#         "range_high": high_bound,
#         "days": pred_days,
#         "months": pred_months,
#         "exposure": total_exposure,
#         "defense_cost": defense_base,
#         "demand": demand,
#         "savings": savings,
#         "action": action,
#         "action_desc": action_desc,
#         "is_safe": is_safe,
#         "risk_score": lit_score,
#         "risk_label": risk_label,
#         "risk_color": risk_color,
#         "drivers": drivers
#     }



























import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

# Global model variable
_MODEL = None

def load_and_train():
    """
    Loads the Enhanced Enterprise Litigation Dataset and trains the AI Valuation Engine.
    Predicts settlement amounts based on 18+ case attributes.
    """
    global _MODEL
    
    try:
        df = pd.read_csv("synthetic_litigation_db_enhanced.csv")
    except FileNotFoundError:
        print("❌ Error: synthetic_litigation_db_enhanced.csv not found.")
        print("   Please run the data generation script first.")
        return None

    # === FEATURES & TARGET ===
    X = df.drop(columns=['Settlement_Amount', 'Action_Recommendation'])
    y = df['Settlement_Amount']
    
    # Identify categorical and numeric columns
    cat_cols = [c for c in X.columns if X[c].dtype == 'object']
    num_cols = [c for c in X.columns if X[c].dtype != 'object']
    
    # === PREPROCESSING PIPELINE ===
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
        ],
        remainder='drop'
    )
    
    # === BUILD MODEL PIPELINE ===
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', GradientBoostingRegressor(
            n_estimators=250,
            learning_rate=0.08,
            max_depth=5,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            subsample=0.9
        ))
    ])
    
    print("🔄 Training AI Valuation Engine...")
    model.fit(X, y)
    _MODEL = model
    print("✅ Model Trained Successfully.")
    return model


def calculate_drivers(inputs, prediction):
    """
    Calculates financial drivers showing what factors increased/decreased the settlement value.
    Returns list of tuples: (driver_name, impact_amount, type)
    """
    drivers = []
    
    # === POSITIVE DRIVERS (Increase Settlement) ===
    
    # 1. Attorney Aggressiveness
    if inputs['Attorney_Score'] > 75:
        impact = prediction * ((inputs['Attorney_Score'] - 50) / 200)
        drivers.append(("Aggressive Counsel Premium", impact, "pos"))
    
    # 2. Impairment Rating (Major Cost Driver)
    if inputs['Impairment_Rating'] > 15:
        impact = inputs['Impairment_Rating'] * 1800
        drivers.append(("High Permanent Impairment", impact, "pos"))
    
    # 3. Jurisdiction Risk
    if inputs['Venue_Win_Rate'] < 0.45:
        impact = prediction * 0.15
        drivers.append(("Unfavorable Venue History", impact, "pos"))
    
    # 4. Employment Status (Terminated = Higher Demand)
    if inputs['Employment_Status'] == 'Terminated':
        impact = prediction * 0.25
        drivers.append(("Terminated Employee Premium", impact, "pos"))
    
    # 5. Opioid Indicator
    if inputs['Opioid_Indicator'] == 1:
        drivers.append(("Opioid Usage Risk Factor", 10500, "pos"))
    
    # 6. Long Duration (Stale Claim)
    if inputs['Days_Since_Filed'] > 365:
        impact = inputs['Days_Since_Filed'] * 10
        drivers.append(("Extended Claim Duration", impact, "pos"))
    
    # 7. Medical Complexity
    if inputs['Guidelines_Adherence'] == 'Significantly Exceeds':
        impact = prediction * 0.12
        drivers.append(("Aggressive Medical Treatment", impact, "pos"))
    
    # 8. Provider Shopping (Multiple providers = complexity)
    if inputs['Provider_Shopping'] > 2:
        drivers.append(("Provider Shopping Flag", 7500, "pos"))
    
    # 9. Comorbidities
    if inputs['Comorbidities'] != 'None':
        drivers.append(("Comorbidity Complexity", 6000, "pos"))
    
    # 10. Attorney Trial Tendency
    if inputs['Attorney_Tendency'] == 'Trial-Oriented':
        impact = prediction * 0.18
        drivers.append(("Trial-Ready Attorney", impact, "pos"))
    
    # === NEGATIVE DRIVERS (Decrease Settlement / Defense Advantage) ===
    
    # 1. Favorable Venue
    if inputs['Venue_Win_Rate'] > 0.60:
        impact = prediction * 0.10
        drivers.append(("Strong Defense Venue", -impact, "neg"))
    
    # 2. Early Resolution
    if inputs['Days_Since_Filed'] < 90:
        drivers.append(("Early Claim Resolution", -5000, "neg"))
    
    # 3. Good Medical Adherence (Within Guidelines)
    if inputs['Guidelines_Adherence'] == 'Within Guidelines':
        drivers.append(("Adherent Medical Management", -4500, "neg"))
    
    # 4. No MSA Flag (Simplifies settlement)
    if inputs['MSA_Flag'] == 0:
        drivers.append(("No Medicare Complications", -3000, "neg"))
    
    # 5. Settlement-Oriented Attorney
    if inputs['Attorney_Tendency'] == 'Early Settlement':
        impact = prediction * 0.08
        drivers.append(("Settlement-Prone Counsel", -impact, "neg"))
    
    # FALLBACK: Ensure list is never empty
    if len(drivers) == 0:
        drivers.append(("Base Liability Assessment", prediction * 0.15, "pos"))
    
    # Sort by impact magnitude (highest first)
    drivers = sorted(drivers, key=lambda x: abs(x[1]), reverse=True)
    
    return drivers[:6]  # Return top 6 drivers


def predict_case(input_dict):
    """
    THE MAIN API FUNCTION.
    
    Takes raw case inputs (18 attributes) and returns a comprehensive dictionary
    with settlement prediction, confidence intervals, duration, exposure, strategy,
    risk flags, and explainability (drivers).
    
    Args:
        input_dict: Dictionary with all case attributes
    
    Returns:
        Dictionary with prediction metrics for dashboard rendering
    """
    
    # Load model if not already loaded
    if _MODEL is None:
        load_and_train()
    
    # === STEP 1: PREPARE INPUT FOR PREDICTION ===
    # Fill in missing fields with defaults if not provided
    default_fields = {
        'Provider_Type': 'PT',
        'Medical_Trajectory': 'Moderate',
        'Treatment_Duration': 90,
        'Days_Attorney_Engaged': input_dict.get('Days_Since_Filed', 180) - 30,
        'Attorney_Win_Rate': 0.55
    }
    
    # Merge defaults with provided input
    complete_input = {**default_fields, **input_dict}
    
    input_df = pd.DataFrame([complete_input])
    
    # === STEP 2: AI SETTLEMENT PREDICTION ===
    pred_val = _MODEL.predict(input_df)[0]
    pred_val = max(pred_val, 25000)  # Floor at $25K
    
    # === STEP 3: CONFIDENCE INTERVALS ===
    low_bound = pred_val * 0.88
    high_bound = pred_val * 1.12
    
    # === STEP 4: DURATION ESTIMATION (Heuristic) ===
    base_days = 180
    
    # Add time for attorney tendency
    if input_dict['Attorney_Tendency'] == 'Trial-Oriented':
        base_days += 250
    elif input_dict['Attorney_Tendency'] == 'Balanced':
        base_days += 100
    
    # Add time for high impairment
    if input_dict['Impairment_Rating'] > 20:
        base_days += 120
    
    # Add time for long claim duration
    if input_dict['Days_Since_Filed'] > 365:
        base_days += 100
    
    # Add time for complex medical
    if input_dict['Guidelines_Adherence'] == 'Significantly Exceeds':
        base_days += 80
    
    pred_days = int(base_days * np.random.uniform(0.95, 1.05))
    pred_months = round(pred_days / 30, 1)
    
    # === STEP 5: DEFENSE COST CALCULATION ===
    # Base cost depends on jurisdiction severity
    if input_dict['Jurisdiction'] in ['New York', 'California', 'Illinois']:
        defense_base = 50000
    elif input_dict['Jurisdiction'] in ['Florida', 'Texas']:
        defense_base = 35000
    else:
        defense_base = 20000
    
    # Multiplier based on attorney aggressiveness
    if input_dict['Attorney_Score'] > 80:
        defense_base *= 1.8  # Very aggressive = 80% higher costs
    elif input_dict['Attorney_Score'] > 65:
        defense_base *= 1.4  # Moderately aggressive
    elif input_dict['Attorney_Score'] > 50:
        defense_base *= 1.1  # Standard
    
    # Trial-oriented attorneys drive costs up
    if input_dict['Attorney_Tendency'] == 'Trial-Oriented':
        defense_base *= 1.3
    
    defense_cost = int(defense_base)
    
    # === STEP 6: TOTAL EXPOSURE (Risk Calculation) ===
    total_exposure = int(pred_val + defense_cost)
    
    # === STEP 7: PLAINTIFF DEMAND LOGIC ===
    if input_dict['Demand_Amount'] > 0:
        # Use actual demand if provided
        active_demand = input_dict['Demand_Amount']
        demand_source = "Actual"
    else:
        # Simulate demand based on attorney profile
        if input_dict['Attorney_Score'] > 80:
            demand_multiplier = 2.2  # Very aggressive: demand 2.2x value
        elif input_dict['Attorney_Score'] > 65:
            demand_multiplier = 1.6  # Moderate: demand 1.6x value
        else:
            demand_multiplier = 1.15  # Passive: demand close to value
        
        # Increase demand if employment is terminated
        if input_dict['Employment_Status'] == 'Terminated':
            demand_multiplier *= 1.3
        
        active_demand = int(pred_val * demand_multiplier)
        demand_source = "Simulated"
    
    # === STEP 8: ROI & RECOMMENDATION ===
    savings = int(total_exposure - active_demand)
    
    if savings > 100000:
        action = "SETTLE"
        action_desc = "Strong settlement case. High ROI."
        is_safe = True
    elif savings > 25000:
        action = "SETTLE"
        action_desc = "Favorable settlement dynamics."
        is_safe = True
    elif savings > -50000:
        action = "STRATEGIZE"
        action_desc = "Borderline case. Requires careful negotiation."
        is_safe = None
    else:
        action = "LITIGATE"
        action_desc = "Fight is more economical than settlement."
        is_safe = False
    
    # === STEP 9: LITIGATION RISK SCORE ===
    risk_score = input_dict['Attorney_Score']  # Start with attorney aggressiveness
    
    # Adjust for venue
    if input_dict['Venue_Win_Rate'] < 0.40:
        risk_score += 15
    elif input_dict['Venue_Win_Rate'] > 0.65:
        risk_score -= 10
    
    # Adjust for impairment
    if input_dict['Impairment_Rating'] > 25:
        risk_score += 10
    
    # Cap at 100
    risk_score = min(risk_score, 100)
    
    # Risk label
    if risk_score > 75:
        risk_label = "🔴 HIGH RISK"
    elif risk_score > 50:
        risk_label = "🟡 MEDIUM RISK"
    else:
        risk_label = "🟢 LOW RISK"
    
    # === STEP 10: CALCULATE DRIVERS ===
    drivers = calculate_drivers(input_dict, pred_val)
    
    # === RETURN COMPREHENSIVE RESULT ===
    return {
        # Settlement Prediction
        "prediction": pred_val,
        "range_low": low_bound,
        "range_high": high_bound,
        
        # Duration
        "days": pred_days,
        "months": pred_months,
        
        # Financial Exposure
        "exposure": total_exposure,
        "defense_cost": defense_cost,
        "demand": active_demand,
        "demand_source": demand_source,
        
        # ROI & Strategy
        "savings": savings,
        "action": action,
        "action_desc": action_desc,
        "is_safe": is_safe,
        
        # Risk Assessment
        "risk_score": risk_score,
        "risk_label": risk_label,
        
        # Explainability
        "drivers": drivers
    }


# === RUN ON IMPORT ===
if __name__ == "__main__":
    print("\n" + "="*60)
    print("LITIGATION SETTLEMENT VALUATION ENGINE")
    print("="*60)
    
    # Train model
    load_and_train()
    
    # Test with sample case
    print("\n🧪 TESTING WITH SAMPLE CASE...")
    
    test_case = {
        "Jurisdiction": "New York",
        "Venue_Win_Rate": 0.42,
        "Plaintiff_Attorney": "Morgan & Morgan",
        "Attorney_Score": 78,
        "Provider_Type": "PT",
        "Wage_Loss_Exposure": 35000,
        "Impairment_Rating": 18,
        "Medical_Trajectory": "High",
        "Future_Medical": 1,
        "Demand_Amount": 0,
        "Days_Since_Filed": 220,
        "Days_Attorney_Engaged": 200,
        "Treatment_Duration": 120,
        "Opioid_Indicator": 1,
        "Provider_Shopping": 2,
        "Employment_Status": "Terminated",
        "Benefit_Status": "PPD (Permanent Partial Disability)",
        "MSA_Flag": 1,
        "Comorbidities": "Diabetes",
        "Guidelines_Adherence": "Exceeds Guidelines",
        "Attorney_Win_Rate": 0.58,
        "Judge_Propensity": "Neutral",
        "Attorney_Tendency": "Trial-Oriented"
    }
    
    result = predict_case(test_case)
    
    print("\n📊 PREDICTION RESULTS:")
    print(f"   Target Settlement: ${result['prediction']:,.0f}")
    print(f"   Range: ${result['range_low']:,.0f} – ${result['range_high']:,.0f}")
    print(f"   Est. Duration: {result['days']} days (~{result['months']:.1f} months)")
    print(f"   Total Exposure: ${result['exposure']:,.0f} (Defense: ${result['defense_cost']:,.0f})")
    print(f"   Plaintiff Demand: ${result['demand']:,.0f}")
    print(f"   ROI Savings: ${result['savings']:,.0f}")
    print(f"   Recommendation: {result['action']}")
    print(f"   Risk Level: {result['risk_label']}")
    print("\n📈 TOP DRIVERS:")
    for name, val, dtype in result['drivers'][:3]:
        sign = "+" if dtype == "pos" else "−"
        print(f"   {sign} {name}: ${abs(val):,.0f}")
    
    print("\n" + "="*60)