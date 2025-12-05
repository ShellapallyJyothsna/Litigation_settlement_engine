
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