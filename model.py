






















#######3working well
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.pipeline import Pipeline

# # Global model variable
# _MODEL = None

# def load_and_train():
#     """
#     Loads the Enhanced Enterprise Litigation Dataset and trains the AI Valuation Engine.
#     Predicts settlement amounts based on 18+ case attributes.
#     """
#     global _MODEL
    
#     try:
#         df = pd.read_csv("synthetic_litigation_db_enhanced.csv")
#     except FileNotFoundError:
#         print("❌ Error: synthetic_litigation_db_enhanced.csv not found.")
#         print("   Please run the data generation script first.")
#         return None

#     # === FEATURES & TARGET ===
#     X = df.drop(columns=['Settlement_Amount', 'Action_Recommendation'])
#     y = df['Settlement_Amount']
    
#     # Identify categorical and numeric columns
#     cat_cols = [c for c in X.columns if X[c].dtype == 'object']
#     num_cols = [c for c in X.columns if X[c].dtype != 'object']
    
#     # === PREPROCESSING PIPELINE ===
#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('num', StandardScaler(), num_cols),
#             ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
#         ],
#         remainder='drop'
#     )
    
#     # === BUILD MODEL PIPELINE ===
#     model = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(
#             n_estimators=250,
#             learning_rate=0.08,
#             max_depth=5,
#             min_samples_split=5,
#             min_samples_leaf=2,
#             random_state=42,
#             subsample=0.9
#         ))
#     ])
    
#     print("🔄 Training AI Valuation Engine...")
#     model.fit(X, y)
#     _MODEL = model
#     print("✅ Model Trained Successfully.")
#     return model


# def calculate_drivers(inputs, prediction):
#     """
#     Calculates financial drivers showing what factors increased/decreased the settlement value.
#     Returns list of tuples: (driver_name, impact_amount, type)
#     """
#     drivers = []
    
#     # === POSITIVE DRIVERS (Increase Settlement) ===
    
#     # 1. Attorney Aggressiveness
#     if inputs['Attorney_Score'] > 75:
#         impact = prediction * ((inputs['Attorney_Score'] - 50) / 200)
#         drivers.append(("Aggressive Counsel Premium", impact, "pos"))
    
#     # 2. Impairment Rating (Major Cost Driver)
#     if inputs['Impairment_Rating'] > 15:
#         impact = inputs['Impairment_Rating'] * 1800
#         drivers.append(("High Permanent Impairment", impact, "pos"))
    
#     # 3. Jurisdiction Risk
#     if inputs['Venue_Win_Rate'] < 0.45:
#         impact = prediction * 0.15
#         drivers.append(("Unfavorable Venue History", impact, "pos"))
    
#     # 4. Employment Status (Terminated = Higher Demand)
#     if inputs['Employment_Status'] == 'Terminated':
#         impact = prediction * 0.25
#         drivers.append(("Terminated Employee Premium", impact, "pos"))
    
#     # 5. Opioid Indicator
#     if inputs['Opioid_Indicator'] == 1:
#         drivers.append(("Opioid Usage Risk Factor", 10500, "pos"))
    
#     # 6. Long Duration (Stale Claim)
#     if inputs['Days_Since_Filed'] > 365:
#         impact = inputs['Days_Since_Filed'] * 10
#         drivers.append(("Extended Claim Duration", impact, "pos"))
    
#     # 7. Medical Complexity
#     if inputs['Guidelines_Adherence'] == 'Significantly Exceeds':
#         impact = prediction * 0.12
#         drivers.append(("Aggressive Medical Treatment", impact, "pos"))
    
#     # 8. Provider Shopping (Multiple providers = complexity)
#     if inputs['Provider_Shopping'] > 2:
#         drivers.append(("Provider Shopping Flag", 7500, "pos"))
    
#     # 9. Comorbidities
#     if inputs['Comorbidities'] != 'None':
#         drivers.append(("Comorbidity Complexity", 6000, "pos"))
    
#     # 10. Attorney Trial Tendency
#     if inputs['Attorney_Tendency'] == 'Trial-Oriented':
#         impact = prediction * 0.18
#         drivers.append(("Trial-Ready Attorney", impact, "pos"))
    
#     # === NEGATIVE DRIVERS (Decrease Settlement / Defense Advantage) ===
    
#     # 1. Favorable Venue
#     if inputs['Venue_Win_Rate'] > 0.60:
#         impact = prediction * 0.10
#         drivers.append(("Strong Defense Venue", -impact, "neg"))
    
#     # 2. Early Resolution
#     if inputs['Days_Since_Filed'] < 90:
#         drivers.append(("Early Claim Resolution", -5000, "neg"))
    
#     # 3. Good Medical Adherence (Within Guidelines)
#     if inputs['Guidelines_Adherence'] == 'Within Guidelines':
#         drivers.append(("Adherent Medical Management", -4500, "neg"))
    
#     # 4. No MSA Flag (Simplifies settlement)
#     if inputs['MSA_Flag'] == 0:
#         drivers.append(("No Medicare Complications", -3000, "neg"))
    
#     # 5. Settlement-Oriented Attorney
#     if inputs['Attorney_Tendency'] == 'Early Settlement':
#         impact = prediction * 0.08
#         drivers.append(("Settlement-Prone Counsel", -impact, "neg"))
    
#     # FALLBACK: Ensure list is never empty
#     if len(drivers) == 0:
#         drivers.append(("Base Liability Assessment", prediction * 0.15, "pos"))
    
#     # Sort by impact magnitude (highest first)
#     drivers = sorted(drivers, key=lambda x: abs(x[1]), reverse=True)
    
#     return drivers[:6]  # Return top 6 drivers


# def predict_case(input_dict):
#     """
#     THE MAIN API FUNCTION.
    
#     Takes raw case inputs (18 attributes) and returns a comprehensive dictionary
#     with settlement prediction, confidence intervals, duration, exposure, strategy,
#     risk flags, and explainability (drivers).
    
#     Args:
#         input_dict: Dictionary with all case attributes
    
#     Returns:
#         Dictionary with prediction metrics for dashboard rendering
#     """
    
#     # Load model if not already loaded
#     if _MODEL is None:
#         load_and_train()
    
#     # === STEP 1: PREPARE INPUT FOR PREDICTION ===
#     # Fill in missing fields with defaults if not provided
#     default_fields = {
#         'Provider_Type': 'PT',
#         'Medical_Trajectory': 'Moderate',
#         'Treatment_Duration': 90,
#         'Days_Attorney_Engaged': input_dict.get('Days_Since_Filed', 180) - 30,
#         'Attorney_Win_Rate': 0.55
#     }
    
#     # Merge defaults with provided input
#     complete_input = {**default_fields, **input_dict}
    
#     input_df = pd.DataFrame([complete_input])
    
#     # === STEP 2: AI SETTLEMENT PREDICTION ===
#     pred_val = _MODEL.predict(input_df)[0]
#     pred_val = max(pred_val, 25000)  # Floor at $25K
    
#     # === STEP 3: CONFIDENCE INTERVALS ===
#     low_bound = pred_val * 0.88
#     high_bound = pred_val * 1.12
    
#     # === STEP 4: DURATION ESTIMATION (Heuristic) ===
#     # === STEP 4: DURATION ESTIMATION (Heuristic V2) ===
#     # 1. Start with a baseline (Standard claim = ~4 months)
#     pred_days = 120 
    
#     # 2. Add Time for Attorney Complexity
#     if input_dict['Attorney_Tendency'] == 'Trial-Oriented': 
#         pred_days += 180  # Trials take significantly longer (+6 months)
#     elif input_dict['Attorney_Score'] > 80: 
#         pred_days += 90   # Aggressive attorneys drag out discovery (+3 months)

#     # 3. Add Time for Medical Complexity
#     if input_dict['Medical_Trajectory'] == 'Escalating': 
#         pred_days += 100  # Complications extend timeline
#     if input_dict['Future_Medical'] == 1: 
#         pred_days += 45   # Negotiating future medicals takes time
#     if input_dict['Impairment_Rating'] > 20:
#         pred_days += 60   # High impairment = longer wait for MMI
#     if input_dict['Opioid_Indicator'] == 1:
#         pred_days += 60   # Opioids delay recovery & settlement

#     # 4. Add Time for Jurisdiction
#     if input_dict['Jurisdiction'] in ['New York', 'California', 'Illinois']: 
#         pred_days += 75   # "Slow Court" Penalty
#     elif input_dict['Jurisdiction'] in ['Florida', 'Texas']:
#         pred_days -= 30   # "Fast Court" Bonus (Efficiency)
        
#     # 5. Add Time for Behavioral Factors
#     if input_dict['Employment_Status'] == 'Terminated':
#         pred_days += 45   # "Spite Factor" - Employee drags it out

#     # 6. Add randomness (Real life isn't perfect)
#     pred_days = int(pred_days * np.random.uniform(0.9, 1.1))
    
#     # Sanity Check: Ensure no claim is faster than 90 days
#     pred_days = max(90, pred_days)

#     # 7. Convert to Months
#     pred_months = round(pred_days / 30, 1)
    
#     # === STEP 5: DEFENSE COST CALCULATION ===
#     # Base cost depends on jurisdiction severity
#     if input_dict['Jurisdiction'] in ['New York', 'California', 'Illinois']:
#         defense_base = 50000
#     elif input_dict['Jurisdiction'] in ['Florida', 'Texas']:
#         defense_base = 35000
#     else:
#         defense_base = 20000
    
#     # Multiplier based on attorney aggressiveness
#     if input_dict['Attorney_Score'] > 80:
#         defense_base *= 1.8  # Very aggressive = 80% higher costs
#     elif input_dict['Attorney_Score'] > 65:
#         defense_base *= 1.4  # Moderately aggressive
#     elif input_dict['Attorney_Score'] > 50:
#         defense_base *= 1.1  # Standard
    
#     # Trial-oriented attorneys drive costs up
#     if input_dict['Attorney_Tendency'] == 'Trial-Oriented':
#         defense_base *= 1.3
    
#     defense_cost = int(defense_base)
    
#     # === STEP 6: TOTAL EXPOSURE (Risk Calculation) ===
#     total_exposure = int(pred_val + defense_cost)
    
#     # === STEP 7: PLAINTIFF DEMAND LOGIC ===
#     if input_dict['Demand_Amount'] > 0:
#         # Use actual demand if provided
#         active_demand = input_dict['Demand_Amount']
#         demand_source = "Actual"
#     else:
#         # Simulate demand based on attorney profile
#         if input_dict['Attorney_Score'] > 80:
#             demand_multiplier = 2.2  # Very aggressive: demand 2.2x value
#         elif input_dict['Attorney_Score'] > 65:
#             demand_multiplier = 1.6  # Moderate: demand 1.6x value
#         else:
#             demand_multiplier = 1.15  # Passive: demand close to value
        
#         # Increase demand if employment is terminated
#         if input_dict['Employment_Status'] == 'Terminated':
#             demand_multiplier *= 1.3
        
#         active_demand = int(pred_val * demand_multiplier)
#         demand_source = "Simulated"
    
#     # === STEP 8: ROI & RECOMMENDATION ===
#     savings = int(total_exposure - active_demand)
    
#     if savings > 100000:
#         action = "SETTLE"
#         action_desc = "Strong settlement case. High ROI."
#         is_safe = True
#     elif savings > 25000:
#         action = "SETTLE"
#         action_desc = "Favorable settlement dynamics."
#         is_safe = True
#     elif savings > -50000:
#         action = "STRATEGIZE"
#         action_desc = "Borderline case. Requires careful negotiation."
#         is_safe = None
#     else:
#         action = "LITIGATE"
#         action_desc = "Fight is more economical than settlement."
#         is_safe = False
    
#     # === STEP 9: LITIGATION RISK SCORE ===
#     risk_score = input_dict['Attorney_Score']  # Start with attorney aggressiveness
    
#     # Adjust for venue
#     if input_dict['Venue_Win_Rate'] < 0.40:
#         risk_score += 15
#     elif input_dict['Venue_Win_Rate'] > 0.65:
#         risk_score -= 10
    
#     # Adjust for impairment
#     if input_dict['Impairment_Rating'] > 25:
#         risk_score += 10
    
#     # Cap at 100
#     risk_score = min(risk_score, 100)
    
#     # Risk label
#     if risk_score > 75:
#         risk_label = "🔴 HIGH RISK"
#     elif risk_score > 50:
#         risk_label = "🟡 MEDIUM RISK"
#     else:
#         risk_label = "🟢 LOW RISK"
    
#     # === STEP 10: CALCULATE DRIVERS ===
#     drivers = calculate_drivers(input_dict, pred_val)
    
#     # === RETURN COMPREHENSIVE RESULT ===
#     return {
#         # Settlement Prediction
#         "prediction": pred_val,
#         "range_low": low_bound,
#         "range_high": high_bound,
        
#         # Duration
#         "days": pred_days,
#         "months": pred_months,
        
#         # Financial Exposure
#         "exposure": total_exposure,
#         "defense_cost": defense_cost,
#         "demand": active_demand,
#         "demand_source": demand_source,
        
#         # ROI & Strategy
#         "savings": savings,
#         "action": action,
#         "action_desc": action_desc,
#         "is_safe": is_safe,
        
#         # Risk Assessment
#         "risk_score": risk_score,
#         "risk_label": risk_label,
        
#         # Explainability
#         "drivers": drivers
#     }


# # === RUN ON IMPORT ===
# if __name__ == "__main__":
#     print("\n" + "="*60)
#     print("LITIGATION SETTLEMENT VALUATION ENGINE")
#     print("="*60)
    
#     # Train model
#     load_and_train()
    
#     # Test with sample case
#     print("\n🧪 TESTING WITH SAMPLE CASE...")
    
#     test_case = {
#         "Jurisdiction": "New York",
#         "Venue_Win_Rate": 0.42,
#         "Plaintiff_Attorney": "Morgan & Morgan",
#         "Attorney_Score": 78,
#         "Provider_Type": "PT",
#         "Wage_Loss_Exposure": 35000,
#         "Impairment_Rating": 18,
#         "Medical_Trajectory": "High",
#         "Future_Medical": 1,
#         "Demand_Amount": 0,
#         "Days_Since_Filed": 220,
#         "Days_Attorney_Engaged": 200,
#         "Treatment_Duration": 120,
#         "Opioid_Indicator": 1,
#         "Provider_Shopping": 2,
#         "Employment_Status": "Terminated",
#         "Benefit_Status": "PPD (Permanent Partial Disability)",
#         "MSA_Flag": 1,
#         "Comorbidities": "Diabetes",
#         "Guidelines_Adherence": "Exceeds Guidelines",
#         "Attorney_Win_Rate": 0.58,
#         "Judge_Propensity": "Neutral",
#         "Attorney_Tendency": "Trial-Oriented"
#     }
    
#     result = predict_case(test_case)
    
#     print("\n📊 PREDICTION RESULTS:")
#     print(f"   Target Settlement: ${result['prediction']:,.0f}")
#     print(f"   Range: ${result['range_low']:,.0f} – ${result['range_high']:,.0f}")
#     print(f"   Est. Duration: {result['days']} days (~{result['months']:.1f} months)")
#     print(f"   Total Exposure: ${result['exposure']:,.0f} (Defense: ${result['defense_cost']:,.0f})")
#     print(f"   Plaintiff Demand: ${result['demand']:,.0f}")
#     print(f"   ROI Savings: ${result['savings']:,.0f}")
#     print(f"   Recommendation: {result['action']}")
#     print(f"   Risk Level: {result['risk_label']}")
#     print("\n📈 TOP DRIVERS:")
#     for name, val, dtype in result['drivers'][:3]:
#         sign = "+" if dtype == "pos" else "−"
#         print(f"   {sign} {name}: ${abs(val):,.0f}")
    
#     print("\n" + "="*60)















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
    """
    
    # Load model if not already loaded
    if _MODEL is None:
        load_and_train()
    
    # === STEP 1: PREPARE INPUT FOR PREDICTION ===
    default_fields = {
        'Provider_Type': 'PT',
        'Medical_Trajectory': 'Moderate',
        'Treatment_Duration': 90,
        'Days_Attorney_Engaged': input_dict.get('Days_Since_Filed', 180) - 30,
        'Attorney_Win_Rate': 0.55
    }
    
    complete_input = {**default_fields, **input_dict}
    input_df = pd.DataFrame([complete_input])
    
    # === STEP 2: AI SETTLEMENT PREDICTION ===
    pred_val = _MODEL.predict(input_df)[0]
    pred_val = max(pred_val, 25000)  # Floor at $25K
    
    # === STEP 3: CONFIDENCE INTERVALS ===
    low_bound = pred_val * 0.88
    high_bound = pred_val * 1.12
    
    # === STEP 4: DURATION ESTIMATION (Heuristic V2) ===
    # 1. Start with a baseline (Standard claim = ~4 months)
    pred_days = 120 
    
    # 2. Add Time for Attorney Complexity
    if input_dict['Attorney_Tendency'] == 'Trial-Oriented': 
        pred_days += 180  # Trials take significantly longer (+6 months)
    elif input_dict['Attorney_Score'] > 80: 
        pred_days += 90   # Aggressive attorneys drag out discovery (+3 months)

    # 3. Add Time for Medical Complexity
    if input_dict['Medical_Trajectory'] == 'Escalating': 
        pred_days += 100  # Complications extend timeline
    if input_dict['Future_Medical'] == 1: 
        pred_days += 45   # Negotiating future medicals takes time
    if input_dict['Impairment_Rating'] > 20:
        pred_days += 60   # High impairment = longer wait for MMI
    if input_dict['Opioid_Indicator'] == 1:
        pred_days += 60   # Opioids delay recovery & settlement

    # 4. Add Time for Jurisdiction
    if input_dict['Jurisdiction'] in ['New York', 'California', 'Illinois']: 
        pred_days += 75   # "Slow Court" Penalty
    elif input_dict['Jurisdiction'] in ['Florida', 'Texas']:
        pred_days -= 30   # "Fast Court" Bonus (Efficiency)
        
    # 5. Add Time for Behavioral Factors
    if input_dict['Employment_Status'] == 'Terminated':
        pred_days += 45   # "Spite Factor" - Employee drags it out

    # 6. Add randomness (Real life isn't perfect)
    pred_days = int(pred_days * np.random.uniform(0.9, 1.1))
    
    # Sanity Check: Ensure no claim is faster than 90 days
    pred_days = max(90, pred_days)

    # 7. Convert to Months
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
    risk_score = input_dict['Attorney_Score'] 
    
    # Adjust for venue
    if input_dict['Venue_Win_Rate'] < 0.40: risk_score += 15
    elif input_dict['Venue_Win_Rate'] > 0.65: risk_score -= 10
    
    # Adjust for impairment
    if input_dict['Impairment_Rating'] > 25: risk_score += 10
    
    # Cap at 100
    risk_score = min(risk_score, 100)
    
    # Risk label
    if risk_score > 75: risk_label = "🔴 HIGH RISK"
    elif risk_score > 50: risk_label = "🟡 MEDIUM RISK"
    else: risk_label = "🟢 LOW RISK"
    
    # === STEP 10: CALCULATE DRIVERS ===
    drivers = calculate_drivers(input_dict, pred_val)

    # === STEP 11: CALCULATE ACCEPTANCE LIKELIHOOD ===
    # Logic: What is the chance they accept the "Target Settlement" amount without litigation?
    
    # Base Probability: 65% chance a standard attorney accepts a fair offer
    acceptance_prob = 65
    
    # Adjust based on Attorney Profile
    if input_dict['Attorney_Tendency'] == 'Trial-Oriented': 
        acceptance_prob -= 20 # They prefer fighting
    elif input_dict['Attorney_Tendency'] == 'Early Settlement': 
        acceptance_prob += 15 # They want quick cash
        
    # Adjust based on Leverage
    if input_dict['Attorney_Score'] > 80: acceptance_prob -= 15 # Aggressive attorneys hold out
    if input_dict['Venue_Win_Rate'] < 0.40: acceptance_prob -= 10 # Plaintiff feels strong in this venue
    
    # Cap between 5% and 95%
    acceptance_prob = max(5, min(95, acceptance_prob))
    
    # === RETURN COMPREHENSIVE RESULT ===
    return {
        "prediction": pred_val,
        "range_low": low_bound,
        "range_high": high_bound,
        "days": pred_days,
        "months": pred_months,
        "exposure": total_exposure,
        "defense_cost": defense_cost,
        "demand": active_demand,
        "demand_source": demand_source,
        "savings": savings,
        "action": action,
        "action_desc": action_desc,
        "is_safe": is_safe,
        "risk_score": risk_score,
        "risk_label": risk_label,
        "drivers": drivers,
        "acceptance_likelihood": acceptance_prob # <--- NEW KEY
    }

# === RUN ON IMPORT ===
if __name__ == "__main__":
    print("\n" + "="*60)
    print("LITIGATION SETTLEMENT VALUATION ENGINE")
    print("="*60)
    
    load_and_train()