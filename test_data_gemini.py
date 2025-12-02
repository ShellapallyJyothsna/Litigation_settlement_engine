# import pandas as pd
# import numpy as np
# import random
# from faker import Faker
# from datetime import datetime, timedelta

# # Initialize Faker and set seeds for reproducibility
# fake = Faker()
# Faker.seed(42)
# np.random.seed(42)
# random.seed(42)

# # --- HELPER FUNCTIONS ---

# def generate_random_date(start_date, end_date):
#     if start_date >= end_date:
#         return start_date
#     return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# def log_normal_cost(mean, stddev):
#     # Generates realistic insurance costs (skewed distribution)
#     return round(np.random.lognormal(mean, stddev), 2)

# # --- MAIN GENERATOR FUNCTION ---

# def generate_claim_data():
#     # 1. INDEPENDENT VARIABLES (The Inputs)
#     # These are generated randomly because they are the "facts" of the case.
    
#     claim_number = random.randint(100000, 999999)
#     doi = generate_random_date(datetime(2018, 1, 1), datetime(2023, 1, 1))
#     fnol_date = generate_random_date(doi, datetime.now())
    
#     # Demographics & Policy
#     employer_size = random.choices(['Small', 'Medium', 'Large'], weights=[0.2, 0.5, 0.3])[0]
#     class_code = random.choice(['8810', '9079', '5403', '5645', '8742']) # Real WC codes
#     wage_info = round(np.random.lognormal(6.8, 0.4), 2) # Avg ~$900/week
    
#     # Injury Details
#     body_part = random.choice(['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#     injury_nature = random.choices(
#         ['Strain', 'Fracture', 'Sprain', 'Contusion', 'Laceration'], 
#         weights=[0.5, 0.15, 0.2, 0.1, 0.05]
#     )[0]
    
#     cause_of_injury = random.choice(['Slip/Fall', 'Repetitive Motion', 'Lifting', 'Struck By'])
#     comorbidity = random.choice([True, False])
    
#     # Legal / Jurisdiction
#     state = random.choice(['California', 'Texas', 'New York', 'Florida', 'Georgia'])
#     attorney_firm = random.choice(['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#     attorney_aggressiveness = random.randint(1, 10) # 1 = Passive, 10 = Shark
#     litigation_start_date = generate_random_date(fnol_date, datetime.now())

#     # ---------------------------------------------------------
#     # 2. DEPENDENT VARIABLES (The "Engine" Logic)
#     # These are CALCULATED based on the inputs above, not random.
#     # This creates the patterns for the ML model to find.
#     # ---------------------------------------------------------

#     # A. Base Severity Cost (Correlated to Injury Nature)
#     severity_map = {
#         'Strain': 8000, 
#         'Contusion': 3000, 
#         'Laceration': 4500, 
#         'Sprain': 12000, 
#         'Fracture': 45000 # Fractures are expensive
#     }
#     base_val = severity_map.get(injury_nature, 5000)
    
#     # Adjust for Body Part (Back/Neck are costlier/complex)
#     if body_part in ['Back', 'Neck']:
#         base_val *= 1.5
    
#     # Adjust for Comorbidities (Diabetes/Obesity complicates healing)
#     if comorbidity:
#         base_val *= 1.4

#     # B. Medical Costs (Log-Normal variation around the Base Severity)
#     # We use the base_val as the "mu" (mean) anchor for the distribution
#     medical_cost = round(base_val * np.random.uniform(0.8, 1.2), 2)
    
#     medical_bill_categories = 'Surgery' if medical_cost > 30000 else 'PT/Conservative'
#     if medical_bill_categories == 'Surgery':
#         medical_cost *= 2.0 # Surgery doubles the cost

#     # C. Jurisdiction Factor (State Laws)
#     state_multipliers = {
#         'California': 1.5, # High cost state
#         'New York': 1.4,
#         'Florida': 1.1,
#         'Georgia': 0.85,
#         'Texas': 0.8       # Low cost state
#     }
#     loc_factor = state_multipliers.get(state, 1.0)

#     # D. The Litigation Factor (Attorney Impact)
#     # The stronger the attorney (aggressiveness), the higher the settlement
#     attorney_multiplier = 1.0 + (attorney_aggressiveness * 0.08) # Adds 8% per aggression point
    
#     # Firm-specific behavior (Hidden feature for ML to find)
#     if attorney_firm == 'Firm A': # "The Settlement Mill"
#         attorney_multiplier *= 1.2
#     elif attorney_firm == 'Firm C': # "The Trial Specialists"
#         attorney_multiplier *= 1.5

#     # E. Calculate Outcomes
#     # 1. Indemnity (Lost Wages)
#     indemnity_paid = round((wage_info * 0.66) * np.random.randint(10, 104), 2) # 10 to 104 weeks
    
#     # 2. Settlement Payout (The "Truth")
#     # Core Formula: (Medical + Indemnity) * Location * Attorney Pressure
#     predicted_settlement = (medical_cost + indemnity_paid) * loc_factor * attorney_multiplier
    
#     # Add a little noise (5-10%) so it's not a perfect math equation (real life is messy)
#     settlement_payout = round(predicted_settlement * np.random.uniform(0.95, 1.05), 2)
    
#     # 3. Legal Fees (Usually ~15-20% of settlement)
#     legal_fees = round(settlement_payout * 0.18, 2)

#     return {
#         "Claim Number": claim_number,
#         "DOI": doi,
#         "State": state,
#         "Body Part": body_part,
#         "Injury Nature": injury_nature,
#         "Cause of Injury": cause_of_injury,
#         "Wage Information": wage_info,
#         "Comorbidity": comorbidity,
#         "Attorney Firm": attorney_firm,
#         "Attorney Aggressiveness": attorney_aggressiveness, # Feature
#         "Medical Bill Categories": medical_bill_categories, # Feature
#         "Medical Cost": medical_cost,      # Feature/Target
#         "Indemnity Paid": indemnity_paid,  # Feature
#         "Legal Fees": legal_fees,          # Target 1
#         "Settlement Payout": settlement_payout # Target 2 (Main Objective)
#     }

# # --- EXECUTION ---

# # Generate 1,000 rows
# print("Generating 1,000 realistic claims...")
# data = [generate_claim_data() for _ in range(1000)]

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # Save to CSV
# df.to_csv("synthetic_workers_comp_data.csv", index=False)

# # Preview
# print("\nData Generation Complete. First 5 rows:")
# print(df.head())

# # Quick correlation check to prove the engine works
# print("\nCorrelation Check (Aggressiveness vs Payout):")
# print(df[['Attorney Aggressiveness', 'Settlement Payout']].corr())










##with time
# import pandas as pd
# import numpy as np
# import random
# from faker import Faker
# from datetime import datetime, timedelta

# # Initialize Faker and set seeds for reproducibility
# fake = Faker()
# Faker.seed(42)
# np.random.seed(42)
# random.seed(42)

# # --- HELPER FUNCTIONS ---

# def generate_random_date(start_date, end_date):
#     if start_date >= end_date:
#         return start_date
#     return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# def log_normal_cost(mean, stddev):
#     # Generates realistic insurance costs (skewed distribution)
#     return round(np.random.lognormal(mean, stddev), 2)

# # --- MAIN GENERATOR FUNCTION ---

# def generate_claim_data():
#     # 1. INDEPENDENT VARIABLES (The Inputs)
#     claim_number = random.randint(100000, 999999)
#     doi = generate_random_date(datetime(2018, 1, 1), datetime(2023, 1, 1))
#     fnol_date = generate_random_date(doi, datetime.now())
    
#     # Demographics & Policy
#     employer_size = random.choices(['Small', 'Medium', 'Large'], weights=[0.2, 0.5, 0.3])[0]
#     class_code = random.choice(['8810', '9079', '5403', '5645', '8742']) 
#     wage_info = round(np.random.lognormal(6.8, 0.4), 2) 
    
#     # Injury Details
#     body_part = random.choice(['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#     injury_nature = random.choices(
#         ['Strain', 'Fracture', 'Sprain', 'Contusion', 'Laceration'], 
#         weights=[0.5, 0.15, 0.2, 0.1, 0.05]
#     )[0]
    
#     cause_of_injury = random.choice(['Slip/Fall', 'Repetitive Motion', 'Lifting', 'Struck By'])
#     comorbidity = random.choice([True, False])
    
#     # Legal / Jurisdiction
#     state = random.choice(['California', 'Texas', 'New York', 'Florida', 'Georgia'])
#     attorney_firm = random.choice(['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#     attorney_aggressiveness = random.randint(1, 10) 
#     litigation_start_date = generate_random_date(fnol_date, datetime.now())

#     # ---------------------------------------------------------
#     # 2. DEPENDENT VARIABLES (The "Engine" Logic)
#     # ---------------------------------------------------------

#     # A. Base Severity Cost
#     severity_map = {'Strain': 8000, 'Contusion': 3000, 'Laceration': 4500, 'Sprain': 12000, 'Fracture': 45000}
#     base_val = severity_map.get(injury_nature, 5000)
    
#     if body_part in ['Back', 'Neck']: base_val *= 1.5
#     if comorbidity: base_val *= 1.4

#     # B. Medical Costs
#     medical_cost = round(base_val * np.random.uniform(0.8, 1.2), 2)
#     medical_bill_categories = 'Surgery' if medical_cost > 30000 else 'PT/Conservative'
#     if medical_bill_categories == 'Surgery': medical_cost *= 2.0 

#     # C. Jurisdiction Factor
#     state_multipliers = {'California': 1.5, 'New York': 1.4, 'Florida': 1.1, 'Georgia': 0.85, 'Texas': 0.8}
#     loc_factor = state_multipliers.get(state, 1.0)

#     # D. The Litigation Factor
#     attorney_multiplier = 1.0 + (attorney_aggressiveness * 0.08) 
#     if attorney_firm == 'Firm A': attorney_multiplier *= 1.2
#     elif attorney_firm == 'Firm C': attorney_multiplier *= 1.5

#     # E. Calculate Financial Outcomes
#     indemnity_paid = round((wage_info * 0.66) * np.random.randint(10, 104), 2) 
#     predicted_settlement = (medical_cost + indemnity_paid) * loc_factor * attorney_multiplier
#     settlement_payout = round(predicted_settlement * np.random.uniform(0.95, 1.05), 2)
#     legal_fees = round(settlement_payout * 0.18, 2)

#     # ---------------------------------------------------------
#     #  >>> NEW SECTION: TIME CALCULATION (Days to Settle) <<<
#     # ---------------------------------------------------------
    
#     # 1. Base Duration: Simple case = 90 days
#     days = 90
    
#     # 2. Add time for Medical Complexity
#     if medical_bill_categories == 'Surgery': 
#         days += 120  # Surgery adds ~4 months
#     if body_part == 'Back': 
#         days += 60   # Back injuries linger
        
#     # 3. Add time for Litigation (Aggression drags it out)
#     # Example: Aggression 10 adds 300 days!
#     litigation_drag = attorney_aggressiveness * 30 
#     days += litigation_drag
    
#     # 4. Add time for Slow Courts (NY/CA)
#     if state in ['New York', 'California']:
#         days += 60
        
#     # 5. Add Randomness (Real life is messy)
#     days_to_settle = int(days * np.random.uniform(0.8, 1.2))

#     # ---------------------------------------------------------

#     return {
#         "Claim Number": claim_number,
#         "DOI": doi,
#         "State": state,
#         "Body Part": body_part,
#         "Injury Nature": injury_nature,
#         "Cause of Injury": cause_of_injury,
#         "Wage Information": wage_info,
#         "Comorbidity": comorbidity,
#         "Attorney Firm": attorney_firm,
#         "Attorney Aggressiveness": attorney_aggressiveness, 
#         "Medical Bill Categories": medical_bill_categories, 
#         "Medical Cost": medical_cost,      
#         "Indemnity Paid": indemnity_paid,  
#         "Legal Fees": legal_fees,          
#         "Settlement Payout": settlement_payout,
#         "Days_to_Settle": days_to_settle  # <--- ADDED THIS NEW COLUMN
#     }

# # --- EXECUTION ---

# print("Generating 2,000 realistic claims with TIME data...")
# # Increased to 2000 to give the model more data points
# data = [generate_claim_data() for _ in range(2000)]

# df = pd.DataFrame(data)

# # Save to CSV (This overwrites your old one)
# df.to_csv("synthetic_workers_comp_data.csv", index=False)

# print("\nData Generation Complete. First 5 rows:")
# print(df[['Settlement Payout', 'Days_to_Settle', 'Attorney Aggressiveness']].head())













#########with gemini
# import pandas as pd
# import numpy as np
# import random
# from faker import Faker

# fake = Faker()
# np.random.seed(42)
# random.seed(42)

# def generate_complex_claim():
#     # --- A. LITIGATION & COMPLEXITY ---
#     jurisdiction = random.choice(['New York', 'California', 'Texas', 'Florida', 'Illinois'])
#     venue_win_rate = round(np.random.uniform(0.30, 0.70), 2) # Defense win rate
    
#     attorney_firm = random.choice(['Morgan & Morgan', 'Binder & Binder', 'Local High-Vol Firm', 'Solo Practitioner'])
#     attorney_score = random.randint(30, 95) # 0-100 Trellis Score
    
#     # --- B. ECONOMIC DAMAGES ---
#     wage_loss_exposure = round(np.random.lognormal(9, 0.5), 2) 
#     impairment_rating = random.randint(0, 40) 
#     future_medical_flag = random.choice([0, 1])
#     demand_amount = round(np.random.uniform(50000, 500000), 2) # Added simulated demand
    
#     # --- C. BEHAVIORAL INDICATORS ---
#     days_since_filed = random.randint(30, 700)
#     attorney_engaged_days = int(days_since_filed * np.random.uniform(0.5, 0.9))
#     opioid_indicator = random.choice([0, 1]) 
#     provider_shopping_count = random.choice([1, 1, 1, 2, 3, 4]) 
    
#     # --- D. CLAIMANT PROFILE ---
#     employment_status = random.choice(['Active', 'Terminated', 'Retired', 'Leave of Absence'])
#     benefit_status = random.choice(['TTD', 'PPD', 'Medical Only'])
#     msa_flag = random.choice([0, 1]) 
    
#     # --- E. MEDICAL PROFILE ---
#     comorbidities = random.choices(['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple'], weights=[0.5, 0.2, 0.1, 0.1, 0.1])[0]
#     guidelines_adherence = random.choice(['Within Guidelines', 'Exceeds Guidelines'])
    
#     # --- F. TRELLIS/LITIGATION PROFILE ---
#     judge_propensity = random.choice(['Pro-Defense', 'Neutral', 'Pro-Labor'])
#     attorney_tendency = random.choice(['Early Settlement', 'Trial-Oriented', 'High Volume/Churn'])

#     # --- CALCULATE "TRUTH" VALUES (The Cost Logic) ---
#     base_value = 15000
    
#     # 1. Injury Impact
#     base_value += (impairment_rating * 2500) 
    
#     # 2. Behavioral Impact
#     if opioid_indicator: base_value *= 1.3
#     # FIX IS HERE: Added the # comment symbol
#     if employment_status == 'Terminated': base_value *= 1.4 # (Anger premium)
#     if provider_shopping_count > 2: base_value *= 1.2
    
#     # 3. Litigation Impact
#     if attorney_tendency == 'Trial-Oriented': base_value *= 1.5
#     if judge_propensity == 'Pro-Labor': base_value *= 1.2
#     if venue_win_rate < 0.40: base_value *= 1.3 
    
#     # 4. Medical Impact
#     if comorbidities != 'None': base_value *= 1.25
    
#     # Final Calculation
#     predicted_settlement = round(base_value * np.random.uniform(0.9, 1.1), 0)
    
#     # Strategy Logic 
#     action_rec = "Settle"
#     if attorney_tendency == 'Trial-Oriented' and venue_win_rate > 0.6:
#         action_rec = "Strategize"
#     elif predicted_settlement > 150000:
#         action_rec = "Manage"

#     return {
#         "Jurisdiction": jurisdiction,
#         "Venue_Win_Rate": venue_win_rate,
#         "Plaintiff_Attorney": attorney_firm,
#         "Attorney_Score": attorney_score,
#         "Wage_Loss_Exposure": wage_loss_exposure,
#         "Impairment_Rating": impairment_rating,
#         "Future_Medical": future_medical_flag,
#         "Demand_Amount": demand_amount,
#         "Days_Since_Filed": days_since_filed,
#         "Opioid_Indicator": opioid_indicator,
#         "Provider_Shopping": provider_shopping_count,
#         "Employment_Status": employment_status,
#         "Benefit_Status": benefit_status,
#         "MSA_Flag": msa_flag,
#         "Comorbidities": comorbidities,
#         "Guidelines_Adherence": guidelines_adherence,
#         "Judge_Propensity": judge_propensity,
#         "Attorney_Tendency": attorney_tendency,
#         "Settlement_Amount": predicted_settlement, # TARGET
#         "Action_Recommendation": action_rec
#     }

# # Generate 2,500 Rows
# print("Generating Enterprise Litigation Dataset...")
# data = [generate_complex_claim() for _ in range(2500)]
# df = pd.DataFrame(data)
# df.to_csv("synthetic_litigation_db.csv", index=False)
# print("✅ Database Created: synthetic_litigation_db.csv")
# print(df.head(3))
































import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seeds for reproducibility
np.random.seed(42)
random.seed(42)

def generate_enhanced_claim():
    """
    Generates a realistic workers' compensation litigation claim with 18 attributes.
    All outputs are calculated/correlated to create meaningful patterns for ML.
    """
    
    # === INDEPENDENT VARIABLES (Randomly Generated) ===
    
    # A. LITIGATION & VENUE
    jurisdiction = random.choice(['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'])
    venue_win_rate = round(np.random.uniform(0.30, 0.75), 2)  # Defense win rate in this jurisdiction
    
    attorney_firm = random.choices(
        ['Morgan & Morgan', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner', 'Medium Firm'],
        weights=[0.2, 0.15, 0.3, 0.2, 0.15]
    )[0]
    
    attorney_score = random.randint(35, 92)  # 0-100 Trellis/skill score
    
    provider_type = random.choices(
        ['PT', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Chiropractor', 'Emergency Medicine'],
        weights=[0.3, 0.25, 0.15, 0.15, 0.1, 0.05]
    )[0]
    
    # B. ECONOMIC DAMAGES
    wage_loss_exposure = round(np.random.lognormal(9.5, 0.6), 0)  # $15K to $150K range
    impairment_rating = random.randint(0, 40)  # Whole body impairment %
    
    medical_trajectory = random.choices(
        ['Low', 'Moderate', 'High', 'Escalating'],
        weights=[0.25, 0.45, 0.2, 0.1]
    )[0]
    
    future_medical_flag = random.choices([0, 1], weights=[0.35, 0.65])[0]  # 65% have future medical
    
    # Simulated demand (realistic based on jurisdiction & attorney profile)
    base_demand = wage_loss_exposure + (impairment_rating * 5000)
    demand_multiplier = 1.0 + (attorney_score / 100) * 1.2  # More aggressive = higher demand
    demand_amount = round(base_demand * demand_multiplier * np.random.uniform(0.85, 1.15), 0)
    
    # C. BEHAVIORAL PROGRESSION
    days_filed = random.randint(30, 800)  # How long claim has been open
    days_attorney_engaged = int(days_filed * np.random.uniform(0.3, 0.95))  # When did attorney get involved
    treatment_duration = random.randint(10, 400)  # Days of active treatment
    
    opioid_indicator = random.choices([0, 1], weights=[0.72, 0.28])[0]  # 28% with opioids
    provider_shopping = random.randint(1, 8)  # Number of different providers seen
    
    # D. CLAIMANT PROFILE
    employment_status = random.choices(
        ['Active', 'Terminated', 'Retired', 'Leave of Absence'],
        weights=[0.55, 0.25, 0.15, 0.05]
    )[0]
    
    benefit_status = random.choices(
        ['TTD (Total Temporary Disability)', 'PPD (Permanent Partial Disability)', 'Medical Only'],
        weights=[0.4, 0.4, 0.2]
    )[0]
    
    msa_flag = random.choices([0, 1], weights=[0.7, 0.3])[0]  # 30% require Medicare Set-Aside
    
    # E. MEDICAL COMPLEXITY
    comorbidity = random.choices(
        ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions'],
        weights=[0.5, 0.2, 0.1, 0.1, 0.1]
    )[0]
    
    odg_adherence = random.choices(
        ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds'],
        weights=[0.6, 0.25, 0.15]
    )[0]
    
    # F. LITIGATION INTELLIGENCE
    attorney_win_rate = round(np.random.uniform(0.35, 0.78), 2)
    attorney_tendency = random.choices(
        ['Early Settlement', 'Balanced', 'Trial-Oriented'],
        weights=[0.25, 0.45, 0.3]
    )[0]
    
    judge_propensity = random.choices(
        ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned'],
        weights=[0.2, 0.4, 0.25, 0.15]
    )[0]
    
    # === DEPENDENT VARIABLES (Calculated Settlement Logic) ===
    
    # Base settlement value
    base_settlement = 35000
    
    # 1. Wage loss component (40% of settlement)
    wage_component = wage_loss_exposure * 0.4
    base_settlement += wage_component
    
    # 2. Impairment component (Major driver)
    impairment_component = impairment_rating * 2500
    base_settlement += impairment_component
    
    # 3. Jurisdiction factor
    jurisdiction_multipliers = {
        'New York': 1.45,
        'California': 1.50,
        'Illinois': 1.35,
        'Pennsylvania': 1.25,
        'Texas': 0.80,
        'Florida': 1.10
    }
    jurisdiction_mult = jurisdiction_multipliers.get(jurisdiction, 1.0)
    base_settlement *= jurisdiction_mult
    
    # 4. Attorney aggressiveness factor
    attorney_multiplier = 1.0 + (attorney_score / 100) * 0.5
    base_settlement *= attorney_multiplier
    
    # 5. Behavioral factors
    if opioid_indicator:
        base_settlement *= 1.25  # Opioid cases settle higher
    
    if employment_status == 'Terminated':
        base_settlement *= 1.35  # Emotional damages for terminated workers
    
    if provider_shopping > 3:
        base_settlement *= 1.15  # Multiple providers = complexity
    
    if treatment_duration > 200:
        base_settlement *= 1.20  # Long treatment = higher settlement
    
    # 6. Medical complexity
    if comorbidity != 'None':
        base_settlement *= 1.18
    
    if odg_adherence == 'Significantly Exceeds':
        base_settlement *= 1.22
    elif odg_adherence == 'Exceeds Guidelines':
        base_settlement *= 1.10
    
    # 7. Litigation profile
    if attorney_tendency == 'Trial-Oriented':
        base_settlement *= 1.25  # Trial attorneys get higher settlements
    
    if judge_propensity == 'Pro-Labor':
        base_settlement *= 1.20
    elif judge_propensity == 'Pro-Defense':
        base_settlement *= 0.85
    
    if venue_win_rate < 0.40:
        base_settlement *= 1.28  # Unfavorable venue = higher settlement
    elif venue_win_rate > 0.65:
        base_settlement *= 0.90  # Favorable venue = lower settlement
    
    # 8. Future medical flag
    if future_medical_flag:
        base_settlement *= 1.15
    
    # 9. MSA flag
    if msa_flag:
        base_settlement *= 1.08  # MSA adds complexity/cost
    
    # 10. Add realistic noise (5-15% variance)
    noise = np.random.uniform(0.95, 1.15)
    settlement_amount = round(base_settlement * noise, 0)
    
    # Ensure floor/ceiling
    settlement_amount = max(settlement_amount, 25000)  # Floor at $25K
    settlement_amount = min(settlement_amount, 1000000)  # Ceiling at $1M
    
    # === DETERMINE ACTION RECOMMENDATION ===
    # Simple logic for synthetic data
    if settlement_amount > 300000:
        action_rec = "Manage"  # High-value, needs careful handling
    elif settlement_amount > 150000:
        action_rec = "Strategize"  # Medium-high, negotiation needed
    else:
        action_rec = "Settle"  # Lower value, settle early
    
    return {
        # A. Litigation & Exposure
        "Jurisdiction": jurisdiction,
        "Venue_Win_Rate": venue_win_rate,
        "Plaintiff_Attorney": attorney_firm,
        "Attorney_Score": attorney_score,
        "Provider_Type": provider_type,
        
        # B. Economic Damages
        "Wage_Loss_Exposure": wage_loss_exposure,
        "Impairment_Rating": impairment_rating,
        "Medical_Trajectory": medical_trajectory,
        "Future_Medical": future_medical_flag,
        "Demand_Amount": demand_amount,
        
        # C. Behavioral Progression
        "Days_Since_Filed": days_filed,
        "Days_Attorney_Engaged": days_attorney_engaged,
        "Treatment_Duration": treatment_duration,
        "Opioid_Indicator": opioid_indicator,
        "Provider_Shopping": provider_shopping,
        
        # D. Claimant Profile
        "Employment_Status": employment_status,
        "Benefit_Status": benefit_status,
        "MSA_Flag": msa_flag,
        
        # E. Medical Profile
        "Comorbidities": comorbidity,
        "Guidelines_Adherence": odg_adherence,
        
        # F. Litigation Intelligence
        "Attorney_Win_Rate": attorney_win_rate,
        "Attorney_Tendency": attorney_tendency,
        "Judge_Propensity": judge_propensity,
        
        # TARGETS
        "Settlement_Amount": settlement_amount,
        "Action_Recommendation": action_rec
    }


# === EXECUTION ===
print("="*70)
print("SYNTHETIC LITIGATION DATASET GENERATOR")
print("="*70)
print("\n🔄 Generating 3,500 realistic litigation claims...")

# Generate data
data = [generate_enhanced_claim() for _ in range(3500)]
df = pd.DataFrame(data)

# Save to CSV
output_file = "synthetic_litigation_db_enhanced.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Dataset Created: {output_file}")
print(f"   Total Records: {len(df):,}")
print(f"   Features: {len(df.columns)}")

# === DISPLAY STATISTICS ===
print("\n📊 DATASET STATISTICS:")
print(f"\n   Settlement Amount (Target):")
print(f"      Min:  ${df['Settlement_Amount'].min():,.0f}")
print(f"      Median: ${df['Settlement_Amount'].median():,.0f}")
print(f"      Mean: ${df['Settlement_Amount'].mean():,.0f}")
print(f"      Max: ${df['Settlement_Amount'].max():,.0f}")
print(f"      Std Dev: ${df['Settlement_Amount'].std():,.0f}")

print(f"\n   Attribute Distributions:")
print(f"      Attorney Score (Mean): {df['Attorney_Score'].mean():.1f}")
print(f"      Impairment Rating (Mean): {df['Impairment_Rating'].mean():.1f}%")
print(f"      Days Since Filed (Mean): {df['Days_Since_Filed'].mean():.0f}")
print(f"      Wage Loss (Mean): ${df['Wage_Loss_Exposure'].mean():,.0f}")

print(f"\n   Categorical Breakdowns:")
print(f"      Jurisdictions: {df['Jurisdiction'].nunique()}")
print(f"      Attorney Firms: {df['Plaintiff_Attorney'].nunique()}")
print(f"      Action Recommendations: {df['Action_Recommendation'].value_counts().to_dict()}")
print(f"      Opioid Indicator: {(df['Opioid_Indicator'].sum() / len(df) * 100):.1f}% positive")
print(f"      MSA Flag: {(df['MSA_Flag'].sum() / len(df) * 100):.1f}% positive")

print(f"\n   Correlation (Attorney Score vs Settlement):")
corr = df[['Attorney_Score', 'Settlement_Amount']].corr().iloc[0, 1]
print(f"      {corr:.3f} (Expected positive correlation)")

print(f"\n   Correlation (Impairment Rating vs Settlement):")
corr = df[['Impairment_Rating', 'Settlement_Amount']].corr().iloc[0, 1]
print(f"      {corr:.3f} (Expected positive correlation)")

# Display sample rows
print(f"\n📋 SAMPLE CLAIMS (First 3 Rows):")
print(df.head(3).to_string())

print("\n" + "="*70)
print("✨ Data generation complete. Ready for model training!")
print("="*70)