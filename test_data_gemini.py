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
import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and set seeds for reproducibility
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# --- HELPER FUNCTIONS ---

def generate_random_date(start_date, end_date):
    if start_date >= end_date:
        return start_date
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def log_normal_cost(mean, stddev):
    # Generates realistic insurance costs (skewed distribution)
    return round(np.random.lognormal(mean, stddev), 2)

# --- MAIN GENERATOR FUNCTION ---

def generate_claim_data():
    # 1. INDEPENDENT VARIABLES (The Inputs)
    claim_number = random.randint(100000, 999999)
    doi = generate_random_date(datetime(2018, 1, 1), datetime(2023, 1, 1))
    fnol_date = generate_random_date(doi, datetime.now())
    
    # Demographics & Policy
    employer_size = random.choices(['Small', 'Medium', 'Large'], weights=[0.2, 0.5, 0.3])[0]
    class_code = random.choice(['8810', '9079', '5403', '5645', '8742']) 
    wage_info = round(np.random.lognormal(6.8, 0.4), 2) 
    
    # Injury Details
    body_part = random.choice(['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
    injury_nature = random.choices(
        ['Strain', 'Fracture', 'Sprain', 'Contusion', 'Laceration'], 
        weights=[0.5, 0.15, 0.2, 0.1, 0.05]
    )[0]
    
    cause_of_injury = random.choice(['Slip/Fall', 'Repetitive Motion', 'Lifting', 'Struck By'])
    comorbidity = random.choice([True, False])
    
    # Legal / Jurisdiction
    state = random.choice(['California', 'Texas', 'New York', 'Florida', 'Georgia'])
    attorney_firm = random.choice(['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
    attorney_aggressiveness = random.randint(1, 10) 
    litigation_start_date = generate_random_date(fnol_date, datetime.now())

    # ---------------------------------------------------------
    # 2. DEPENDENT VARIABLES (The "Engine" Logic)
    # ---------------------------------------------------------

    # A. Base Severity Cost
    severity_map = {'Strain': 8000, 'Contusion': 3000, 'Laceration': 4500, 'Sprain': 12000, 'Fracture': 45000}
    base_val = severity_map.get(injury_nature, 5000)
    
    if body_part in ['Back', 'Neck']: base_val *= 1.5
    if comorbidity: base_val *= 1.4

    # B. Medical Costs
    medical_cost = round(base_val * np.random.uniform(0.8, 1.2), 2)
    medical_bill_categories = 'Surgery' if medical_cost > 30000 else 'PT/Conservative'
    if medical_bill_categories == 'Surgery': medical_cost *= 2.0 

    # C. Jurisdiction Factor
    state_multipliers = {'California': 1.5, 'New York': 1.4, 'Florida': 1.1, 'Georgia': 0.85, 'Texas': 0.8}
    loc_factor = state_multipliers.get(state, 1.0)

    # D. The Litigation Factor
    attorney_multiplier = 1.0 + (attorney_aggressiveness * 0.08) 
    if attorney_firm == 'Firm A': attorney_multiplier *= 1.2
    elif attorney_firm == 'Firm C': attorney_multiplier *= 1.5

    # E. Calculate Financial Outcomes
    indemnity_paid = round((wage_info * 0.66) * np.random.randint(10, 104), 2) 
    predicted_settlement = (medical_cost + indemnity_paid) * loc_factor * attorney_multiplier
    settlement_payout = round(predicted_settlement * np.random.uniform(0.95, 1.05), 2)
    legal_fees = round(settlement_payout * 0.18, 2)

    # ---------------------------------------------------------
    #  >>> NEW SECTION: TIME CALCULATION (Days to Settle) <<<
    # ---------------------------------------------------------
    
    # 1. Base Duration: Simple case = 90 days
    days = 90
    
    # 2. Add time for Medical Complexity
    if medical_bill_categories == 'Surgery': 
        days += 120  # Surgery adds ~4 months
    if body_part == 'Back': 
        days += 60   # Back injuries linger
        
    # 3. Add time for Litigation (Aggression drags it out)
    # Example: Aggression 10 adds 300 days!
    litigation_drag = attorney_aggressiveness * 30 
    days += litigation_drag
    
    # 4. Add time for Slow Courts (NY/CA)
    if state in ['New York', 'California']:
        days += 60
        
    # 5. Add Randomness (Real life is messy)
    days_to_settle = int(days * np.random.uniform(0.8, 1.2))

    # ---------------------------------------------------------

    return {
        "Claim Number": claim_number,
        "DOI": doi,
        "State": state,
        "Body Part": body_part,
        "Injury Nature": injury_nature,
        "Cause of Injury": cause_of_injury,
        "Wage Information": wage_info,
        "Comorbidity": comorbidity,
        "Attorney Firm": attorney_firm,
        "Attorney Aggressiveness": attorney_aggressiveness, 
        "Medical Bill Categories": medical_bill_categories, 
        "Medical Cost": medical_cost,      
        "Indemnity Paid": indemnity_paid,  
        "Legal Fees": legal_fees,          
        "Settlement Payout": settlement_payout,
        "Days_to_Settle": days_to_settle  # <--- ADDED THIS NEW COLUMN
    }

# --- EXECUTION ---

print("Generating 2,000 realistic claims with TIME data...")
# Increased to 2000 to give the model more data points
data = [generate_claim_data() for _ in range(2000)]

df = pd.DataFrame(data)

# Save to CSV (This overwrites your old one)
df.to_csv("synthetic_workers_comp_data.csv", index=False)

print("\nData Generation Complete. First 5 rows:")
print(df[['Settlement Payout', 'Days_to_Settle', 'Attorney Aggressiveness']].head())