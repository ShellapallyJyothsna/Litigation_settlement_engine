





######################3claude code which is good 
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import model

# # === PAGE CONFIG ===
# st.set_page_config(
#     page_title="Litigation Settlement Analyzer",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # === PREMIUM CSS STYLING ===
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
#     * { margin: 0; padding: 0; box-sizing: border-box; }
    
#     .stApp {
#         background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
#         font-family: 'Poppins', sans-serif;
#         color: #e2e8f0;
#     }
    
#     /* Hide Sidebar */
#     section[data-testid="stSidebar"] { display: none; }
    
#     /* Form Container */
#     .form-container {
#         background: linear-gradient(135deg, #1a1f3a 0%, #0f172a 100%);
#         border: 2px solid #3b82f6;
#         border-radius: 20px;
#         padding: 50px;
#         max-width: 1200px;
#         margin: 40px auto;
#         box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
#     }
    
#     .form-title {
#         font-family: 'Playfair Display', serif;
#         font-size: 3rem;
#         font-weight: 700;
#         background: linear-gradient(135deg, #60a5fa, #3b82f6, #1e40af);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         text-align: center;
#         margin-bottom: 10px;
#         letter-spacing: 1px;
#     }
    
#     .form-subtitle {
#         text-align: center;
#         color: #cbd5e1;
#         margin-bottom: 40px;
#         font-size: 1.1rem;
#     }
    
#     /* Form Sections Grid */
#     .form-section-grid {
#         display: grid;
#         grid-template-columns: repeat(2, 1fr);
#         gap: 25px;
#         margin-bottom: 30px;
#     }
    
#     .form-section-item {
#         background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
#         border: 1.5px solid #334155;
#         border-radius: 14px;
#         padding: 20px;
#         transition: all 0.3s ease;
#     }
    
#     .form-section-item:hover {
#         border-color: #3b82f6;
#         box-shadow: 0 8px 20px rgba(59, 130, 246, 0.15);
#     }
    
#     .form-section-label {
#         color: #60a5fa;
#         font-weight: 700;
#         font-size: 0.85rem;
#         text-transform: uppercase;
#         letter-spacing: 1.2px;
#         margin-bottom: 15px;
#         display: block;
#     }
    
#     /* Input Styling */
#     .stSelectbox div[data-baseweb="select"] > div,
#     .stNumberInput div[data-baseweb="input"] > div,
#     .stSlider {
#         background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
#         border: 1.5px solid #475569 !important;
#         border-radius: 10px !important;
#         color: white !important;
#         transition: all 0.3s ease;
#     }
    
#     .stSelectbox div[data-baseweb="select"] > div:hover,
#     .stNumberInput div[data-baseweb="input"] > div:hover {
#         border-color: #3b82f6 !important;
#         box-shadow: 0 0 15px rgba(59, 130, 246, 0.3) !important;
#     }
    
#     input[type="number"], div[data-baseweb="select"] span {
#         color: #e2e8f0 !important;
#         -webkit-text-fill-color: #e2e8f0 !important;
#         caret-color: #3b82f6 !important;
#         font-weight: 600 !important;
#     }
    
#     ul[data-testid="stSelectboxVirtualDropdown"] {
#         background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 100%) !important;
#         border: 1px solid #334155 !important;
#     }
    
#     li[role="option"] { color: #e2e8f0 !important; }
#     li[role="option"]:hover { background: rgba(59, 130, 246, 0.25) !important; }
    
#     .stCheckbox div[role="checkbox"] {
#         border: 2px solid #475569 !important;
#         background: #1e293b !important;
#     }
    
#     .stCheckbox div[role="checkbox"]:hover { border-color: #3b82f6 !important; }
    
#     /* Submit Button */
#     .form-button-container {
#         display: flex;
#         gap: 15px;
#         margin-top: 40px;
#         justify-content: center;
#     }
    
#     div.stButton > button {
#         background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%);
#         border: none;
#         color: white;
#         font-weight: 800;
#         font-size: 1rem;
#         padding: 16px 40px;
#         text-transform: uppercase;
#         letter-spacing: 1.5px;
#         border-radius: 12px;
#         box-shadow: 0 8px 24px rgba(37, 99, 235, 0.35);
#         transition: all 0.3s ease;
#         min-width: 250px;
#     }
    
#     div.stButton > button:hover {
#         transform: translateY(-3px);
#         box-shadow: 0 12px 36px rgba(37, 99, 235, 0.5);
#     }
    
#     /* Dashboard Header */
#     .dashboard-header {
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px solid #3b82f6;
#         border-radius: 16px;
#         padding: 40px;
#         margin-bottom: 30px;
#         box-shadow: 0 12px 40px rgba(59, 130, 246, 0.15);
#         display: grid;
#         grid-template-columns: 1fr 1fr;
#         gap: 30px;
#         align-items: center;
#     }
    
#     .dashboard-title {
#         font-family: 'Playfair Display', serif;
#         font-size: 2.5rem;
#         font-weight: 700;
#         background: linear-gradient(135deg, #60a5fa, #3b82f6);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 15px;
#     }
    
#     .dashboard-subtitle {
#         color: #cbd5e1;
#         font-size: 1rem;
#         line-height: 1.6;
#     }
    
#     .recommendation-panel {
#         background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
#         border: 2px solid #3b82f6;
#         border-radius: 12px;
#         padding: 25px;
#         text-align: center;
#     }
    
#     .recommendation-text {
#         font-size: 1.3rem;
#         font-weight: 800;
#         color: #60a5fa;
#         margin-bottom: 10px;
#     }
    
#     .recommendation-subtext {
#         color: #94a3b8;
#         font-size: 0.95rem;
#     }
    
#     /* KPI Cards */
#     .kpi-row {
#         display: grid;
#         grid-template-columns: repeat(4, 1fr);
#         gap: 20px;
#         margin-bottom: 30px;
#     }
    
#     .kpi-card {
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px solid #334155;
#         border-radius: 14px;
#         padding: 24px;
#         transition: all 0.3s ease;
#         box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
#     }
    
#     .kpi-card:hover {
#         border-color: #3b82f6;
#         transform: translateY(-8px);
#         box-shadow: 0 16px 40px rgba(59, 130, 246, 0.25);
#     }
    
#     .kpi-label {
#         font-size: 0.75rem;
#         color: #94a3b8;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1.5px;
#         margin-bottom: 10px;
#     }
    
#     .kpi-value {
#         font-size: 2.2rem;
#         color: #f1f5f9;
#         font-weight: 800;
#         font-family: 'Playfair Display', serif;
#         margin-bottom: 8px;
#     }
    
#     .kpi-subtext {
#         font-size: 0.85rem;
#         color: #cbd5e1;
#         font-weight: 500;
#     }
    
#     /* Driver Analysis Container */
#     .driver-analysis {
#         display: grid;
#         grid-template-columns: 1fr 1fr;
#         gap: 30px;
#         margin-bottom: 30px;
#     }
    
#     .driver-section {
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px solid #334155;
#         border-radius: 14px;
#         padding: 25px;
#     }
    
#     .driver-section-title {
#         font-weight: 700;
#         font-size: 1.2rem;
#         margin-bottom: 20px;
#         padding-bottom: 12px;
#         border-bottom: 2px solid #3b82f6;
#     }
    
#     .driver-item {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         padding: 12px 16px;
#         background: #0a0e27;
#         border-radius: 8px;
#         margin-bottom: 10px;
#         border-left: 4px solid #3b82f6;
#     }
    
#     .driver-name {
#         color: #cbd5e1;
#         font-weight: 600;
#         flex: 1;
#         font-size: 0.95rem;
#     }
    
#     .driver-value {
#         font-weight: 800;
#         padding: 6px 12px;
#         border-radius: 6px;
#         font-size: 0.9rem;
#     }
    
#     .driver-pos {
#         color: #fecaca;
#         background: rgba(220, 38, 38, 0.2);
#         border: 1px solid #dc2626;
#     }
    
#     .driver-neg {
#         color: #bbf7d0;
#         background: rgba(22, 163, 74, 0.2);
#         border: 1px solid #16a34a;
#     }
    
#     /* Alert Boxes */
#     .alert-box {
#         background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%);
#         border-left: 5px solid #dc2626;
#         border-radius: 10px;
#         padding: 16px;
#         margin: 12px 0;
#         color: #fecaca;
#         font-weight: 600;
#         box-shadow: 0 8px 24px rgba(220, 38, 38, 0.15);
#     }
    
#     .section-header {
#         font-size: 1.5rem;
#         font-weight: 700;
#         color: #f1f5f9;
#         margin: 30px 0 20px 0;
#         padding-bottom: 10px;
#         border-bottom: 2px solid #3b82f6;
#         font-family: 'Playfair Display', serif;
#     }
    
#     header { visibility: hidden; }
#     footer { visibility: hidden; }
#     #MainMenu { visibility: hidden; }
#     </style>
# """, unsafe_allow_html=True)

# # === INITIALIZE SESSION STATE ===
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False

# # === FORM STATE ===
# if not st.session_state.submitted:
#     st.markdown("""
#         <div class='form-container'>
#             <div class='form-title'>⚖️ Litigation Settlement Analyzer</div>
#             <div class='form-subtitle'>AI-Powered Settlement Valuation & Strategy Intelligence</div>
#     """, unsafe_allow_html=True)
    
#     with st.form("litigation_form"):
#         # === A. LITIGATION & EXPOSURE ===
#         st.markdown("<span class='form-section-label'>🏛️ A. Litigation & Exposure</span>", unsafe_allow_html=True)
        
#         form_col1, form_col2 = st.columns(2)
#         with form_col1:
#             jurisdiction = st.selectbox("Jurisdiction", 
#                 ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'])
#         with form_col2:
#             venue_win_rate = st.slider("Defense Win Rate in Venue", 0.0, 1.0, 0.45)
        
#         form_col3, form_col4 = st.columns(2)
#         with form_col3:
#             attorney_firm = st.selectbox("Opposing Counsel",
#                 ['Morgan & Morgan', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner'])
#         with form_col4:
#             attorney_score = st.slider("Attorney Aggressiveness", 0, 100, 65)
        
#         form_col5, _ = st.columns(2)
#         with form_col5:
#             provider_type = st.selectbox("Primary Provider",
#                 ['PT', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Chiropractor'])
        
#         st.markdown("---")
        
#         # === B. ECONOMIC DAMAGES ===
#         st.markdown("<span class='form-section-label'>💰 B. Economic Damages</span>", unsafe_allow_html=True)
        
#         form_col6, form_col7 = st.columns(2)
#         with form_col6:
#             wage_loss = st.number_input("Wage Loss Exposure ($)", 5000, 500000, 25000)
#         with form_col7:
#             impairment = st.slider("Permanent Impairment (%)", 0, 100, 15)
        
#         form_col8, form_col9 = st.columns(2)
#         with form_col8:
#             medical_trajectory = st.selectbox("Medical Cost Trajectory",
#                 ['Low', 'Moderate', 'High', 'Escalating'])
#         with form_col9:
#             future_medical = st.checkbox("Future Medical Exposure?", value=True)
        
#         form_col10, _ = st.columns(2)
#         with form_col10:
#             demand = st.number_input("Plaintiff Demand ($) [0=Auto-simulate]", 0, 2000000, 0)
        
#         st.markdown("---")
        
#         # === C. BEHAVIORAL PROGRESSION ===
#         st.markdown("<span class='form-section-label'>📊 C. Behavioral Progression</span>", unsafe_allow_html=True)
        
#         form_col11, form_col12 = st.columns(2)
#         with form_col11:
#             days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
#         with form_col12:
#             days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)
        
#         form_col13, form_col14 = st.columns(2)
#         with form_col13:
#             treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
#         with form_col14:
#             provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)
        
#         form_col15, _ = st.columns(2)
#         with form_col15:
#             opioid = st.checkbox("Opioid Prescription Indicator?")
        
#         st.markdown("---")
        
#         # === D. CLAIMANT PROFILE ===
#         st.markdown("<span class='form-section-label'>👤 D. Claimant Profile</span>", unsafe_allow_html=True)
        
#         form_col16, form_col17 = st.columns(2)
#         with form_col16:
#             employment = st.selectbox("Employment Status",
#                 ['Active', 'Terminated', 'Retired', 'Leave of Absence'])
#         with form_col17:
#             benefit = st.selectbox("Benefit Status",
#                 ['TTD', 'PPD', 'Medical Only'])
        
#         form_col18, _ = st.columns(2)
#         with form_col18:
#             msa = st.checkbox("Medicare Set-Aside (MSA) Required?")
        
#         st.markdown("---")
        
#         # === E. MEDICAL PROFILE ===
#         st.markdown("<span class='form-section-label'>🏥 E. Medical Profile</span>", unsafe_allow_html=True)
        
#         form_col19, form_col20 = st.columns(2)
#         with form_col19:
#             comorbidity = st.selectbox("Comorbidities",
#                 ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions'])
#         with form_col20:
#             odg = st.selectbox("ODG Guidelines Adherence",
#                 ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds'])
        
#         st.markdown("---")
        
#         # === F. LITIGATION INTELLIGENCE ===
#         st.markdown("<span class='form-section-label'>📋 F. Litigation Intelligence</span>", unsafe_allow_html=True)
        
#         form_col21, form_col22 = st.columns(2)
#         with form_col21:
#             attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
#         with form_col22:
#             attorney_type = st.selectbox("Attorney Settlement Tendency",
#                 ['Early Settlement', 'Balanced', 'Trial-Oriented'])
        
#         form_col23, _ = st.columns(2)
#         with form_col23:
#             judge = st.selectbox("Judge Propensity (if assigned)",
#                 ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned'])
        
#         st.markdown("---")
        
#         # Submit Button
#         submitted = st.form_submit_button("🚀 ANALYZE CASE", use_container_width=True)
#         if submitted:
#             # Store all form values in session state
#             st.session_state.jurisdiction = jurisdiction
#             st.session_state.venue_win_rate = venue_win_rate
#             st.session_state.attorney_firm = attorney_firm
#             st.session_state.attorney_score = attorney_score
#             st.session_state.provider_type = provider_type
#             st.session_state.wage_loss = wage_loss
#             st.session_state.impairment = impairment
#             st.session_state.medical_trajectory = medical_trajectory
#             st.session_state.future_medical = future_medical
#             st.session_state.demand = demand
#             st.session_state.days_filed = days_filed
#             st.session_state.days_attorney = days_attorney
#             st.session_state.treatment_duration = treatment_duration
#             st.session_state.opioid = opioid
#             st.session_state.provider_shopping = provider_shopping
#             st.session_state.employment = employment
#             st.session_state.benefit = benefit
#             st.session_state.msa = msa
#             st.session_state.comorbidity = comorbidity
#             st.session_state.odg = odg
#             st.session_state.attorney_winrate = attorney_winrate
#             st.session_state.attorney_type = attorney_type
#             st.session_state.judge = judge
#             st.session_state.submitted = True
#             st.rerun()
    
#     st.markdown("</div>", unsafe_allow_html=True)

# # === DASHBOARD VIEW ===
# else:
#     # Get form data from session state
#     inputs = {
#         "Jurisdiction": st.session_state.jurisdiction,
#         "Venue_Win_Rate": st.session_state.venue_win_rate,
#         "Plaintiff_Attorney": st.session_state.attorney_firm,
#         "Attorney_Score": st.session_state.attorney_score,
#         "Provider_Type": st.session_state.provider_type,
#         "Wage_Loss_Exposure": st.session_state.wage_loss,
#         "Impairment_Rating": st.session_state.impairment,
#         "Medical_Trajectory": st.session_state.medical_trajectory,
#         "Future_Medical": 1 if st.session_state.future_medical else 0,
#         "Demand_Amount": st.session_state.demand,
#         "Days_Since_Filed": st.session_state.days_filed,
#         "Days_Attorney_Engaged": st.session_state.days_attorney,
#         "Treatment_Duration": st.session_state.treatment_duration,
#         "Opioid_Indicator": 1 if st.session_state.opioid else 0,
#         "Provider_Shopping": st.session_state.provider_shopping,
#         "Employment_Status": st.session_state.employment,
#         "Benefit_Status": st.session_state.benefit,
#         "MSA_Flag": 1 if st.session_state.msa else 0,
#         "Comorbidities": st.session_state.comorbidity,
#         "Guidelines_Adherence": st.session_state.odg,
#         "Attorney_Win_Rate": st.session_state.attorney_winrate,
#         "Attorney_Tendency": st.session_state.attorney_type,
#         "Judge_Propensity": st.session_state.judge
#     }
    
#     # Extract variables for use in dashboard
#     jurisdiction = st.session_state.jurisdiction
#     attorney_score = st.session_state.attorney_score
#     venue_win_rate = st.session_state.venue_win_rate
#     days_filed = st.session_state.days_filed
#     employment = st.session_state.employment
#     opioid = st.session_state.opioid
#     impairment = st.session_state.impairment
    
#     res = model.predict_case(inputs)
    
#     # === DASHBOARD HEADER ===
#     rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
#     col_header_left, col_header_right = st.columns(2)
    
#     with col_header_left:
#         st.markdown(f"""
#             <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
#             <div class='dashboard-subtitle'>{res['action_desc']}<br>
#             📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> • ⚠️ Risk: <b>{res['risk_label']}</b></div>
#         """, unsafe_allow_html=True)
    
#     with col_header_right:
#         st.markdown(f"""
#             <div class='recommendation-panel'>
#                 <div class='recommendation-text'>MODEL CONFIDENCE</div>
#                 <div class='recommendation-subtext'>89% • Based on {22} litigation attributes</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # === KPI CARDS ===
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>💵 Target Settlement</div>
#                 <div class='kpi-value'>${res['prediction']/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Range: ${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>⏱️ Est. Duration</div>
#                 <div class='kpi-value'>{res['days']}d</div>
#                 <div class='kpi-subtext'>≈ {res['months']:.1f} months</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col3:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>📊 Total Exposure</div>
#                 <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Verdict + Defense</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col4:
#         savings_color = "#16a34a" if res['savings'] > 0 else "#dc2626"
#         st.markdown(f"""
#             <div class='kpi-card' style='border-bottom: 4px solid {savings_color};'>
#                 <div class='kpi-label'>💰 ROI Savings</div>
#                 <div class='kpi-value' style='color: {savings_color};'>${abs(res['savings'])/1000:.0f}K</div>
#                 <div class='kpi-subtext'>{("Settlement ✓" if res['savings'] > 0 else "Litigation ✓")}</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === DRIVER ANALYSIS (Like Image) ===
#     st.markdown("<div class='section-header'>📈 Key Driver Analysis for This Claim</div>", unsafe_allow_html=True)
    
#     col_drivers_left, col_drivers_right = st.columns(2)
    
#     with col_drivers_left:
#         st.markdown("<div style='color: #fecaca; font-weight: 700; font-size: 1.1rem; margin-bottom: 15px;'>🔴 Positive Drivers (↑ Settlement Pressure)</div>", unsafe_allow_html=True)
#         pos_drivers = [d for d in res['drivers'] if d[2] == 'pos']
#         for name, val, _ in pos_drivers[:5]:
#             st.markdown(f"""
#                 <div class='driver-item'>
#                     <span class='driver-name'>{name}</span>
#                     <span class='driver-value driver-pos'>+${val:,.0f}</span>
#                 </div>
#             """, unsafe_allow_html=True)
    
#     with col_drivers_right:
#         st.markdown("<div style='color: #bbf7d0; font-weight: 700; font-size: 1.1rem; margin-bottom: 15px;'>🟢 Negative Drivers (↓ Defense Advantage)</div>", unsafe_allow_html=True)
#         neg_drivers = [d for d in res['drivers'] if d[2] == 'neg']
#         if neg_drivers:
#             for name, val, _ in neg_drivers[:5]:
#                 st.markdown(f"""
#                     <div class='driver-item'>
#                         <span class='driver-name'>{name}</span>
#                         <span class='driver-value driver-neg'>−${abs(val):,.0f}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#         else:
#             st.markdown("<div style='color: #94a3b8; padding: 15px; text-align: center;'><i>No mitigating factors identified</i></div>", unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === RISK ALERTS ===
#     st.markdown("<div class='section-header'>🚨 Critical Risk Alerts</div>", unsafe_allow_html=True)
    
#     alert_cols = st.columns(2)
    
#     with alert_cols[0]:
#         if attorney_score > 80:
#             st.markdown("""
#                 <div class='alert-box'>
#                 🔥 <b>HIGH-AGGRESSION ATTORNEY</b><br>
#                 History of trial escalation. Adversarial discovery expected.
#                 </div>
#             """, unsafe_allow_html=True)
        
#         if venue_win_rate < 0.40:
#             st.markdown("""
#                 <div class='alert-box'>
#                 ⚖️ <b>UNFAVORABLE VENUE</b><br>
#                 Defense win rate <40%. Jury pool bias present.
#                 </div>
#             """, unsafe_allow_html=True)
        
#         if days_filed > 365:
#             st.markdown("""
#                 <div class='alert-box'>
#                 📅 <b>STALE CLAIM</b><br>
#                 >12 months since filing. Settlement window closing.
#                 </div>
#             """, unsafe_allow_html=True)
    
#     with alert_cols[1]:
#         if employment == 'Terminated':
#             st.markdown("""
#                 <div class='alert-box'>
#                 😠 <b>TERMINATED EMPLOYEE</b><br>
#                 Higher emotional damages expected. Risk premium applies.
#                 </div>
#             """, unsafe_allow_html=True)
        
#         if opioid:
#             st.markdown("""
#                 <div class='alert-box'>
#                 💊 <b>OPIOID INDICATOR</b><br>
#                 Increased settlement floor due to addiction narratives.
#                 </div>
#             """, unsafe_allow_html=True)
        
#         if impairment > 20:
#             st.markdown("""
#                 <div class='alert-box'>
#                 ⚕️ <b>HIGH IMPAIRMENT</b><br>
#                 Non-economic damages baseline significantly raised.
#                 </div>
#             """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === STRATEGIC RECOMMENDATION ===
#     st.markdown("<div class='section-header'>🎯 Recommended Strategy</div>", unsafe_allow_html=True)
    
#     if res['action'] == 'SETTLE':
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
#             Settlement is economically superior. Litigation exposure (<b>${res['exposure']:,.0f}</b>) exceeds plaintiff recovery (<b>${res['demand']:,.0f}</b>).<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
#             • <b>Opening Offer:</b> ${res['range_low']:,.0f} – ${int(res['prediction']*0.95):,.0f}<br>
#             • <b>Walk-Away Price:</b> ${res['range_high']:,.0f}<br>
#             • <b>Savings vs Litigation:</b> ${res['savings']:,.0f}
#             </div>
#         """, unsafe_allow_html=True)
#     elif res['action'] == 'LITIGATE':
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
#             Plaintiff demand (<b>${res['demand']:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
#             • <b>Expected Defense Costs:</b> ${res['defense_cost']:,.0f}<br>
#             • <b>Anticipated Verdict:</b> ${res['prediction']:,.0f}<br>
#             • <b>Do Not Settle Above:</b> ${int(res['exposure']*0.9):,.0f}
#             </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
#             Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
#             • <b>Test Offer:</b> ${int(res['prediction']*0.85):,.0f}<br>
#             • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
#             • <b>Re-evaluate:</b> Quarterly or on significant developments
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     st.markdown("")
    
#     # === VISUALIZATIONS ===
#     st.markdown("<div class='section-header'>📊 Predictive Analytics & Confidence Intervals</div>", unsafe_allow_html=True)
    
#     viz_col1, viz_col2 = st.columns(2)
    
#     with viz_col1:
#         # Gauge Chart - Settlement Value Prediction
#         fig_gauge = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=int(res['prediction']),
#             number={'font': {'size': 32, 'color': "#e2e8f0"}, 'prefix': "$"},
#             domain={'x': [0, 1], 'y': [0, 1]},
#             gauge={
#                 'axis': {'range': [0, int(res['range_high']*1.4)], 'tickwidth': 1, 'tickcolor': "#334155"},
#                 'bar': {'color': "#3b82f6", 'thickness': 0.3},
#                 'bgcolor': "#0a0e27",
#                 'borderwidth': 2,
#                 'bordercolor': "#334155",
#                 'steps': [
#                     {'range': [0, res['range_low']], 'color': "#1e3a8a"},
#                     {'range': [res['range_low'], res['range_high']], 'color': "#1e40af"},
#                     {'range': [res['range_high'], int(res['range_high']*1.4)], 'color': "#7f1d1d"}
#                 ],
#             }
#         ))
#         fig_gauge.update_layout(
#             height=320,
#             margin=dict(l=20, r=20, t=40, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             font=dict(color='#e2e8f0', family='Poppins'),
#             title={'text': 'Settlement Value Prediction', 'font': {'size': 16, 'color': '#cbd5e1'}}
#         )
#         st.plotly_chart(fig_gauge, use_container_width=True)
    
#     with viz_col2:
#         # Box Plot - Settlement Range & Confidence
#         fig_box = go.Figure()
        
#         # Add box plot for confidence interval
#         fig_box.add_trace(go.Box(
#             y=[res['range_low'], res['prediction'], res['range_high']],
#             name='Settlement Range',
#             marker_color='#3b82f6',
#             boxmean='sd',
#             showlegend=False
#         ))
        
#         fig_box.update_layout(
#             height=320,
#             title={'text': 'Confidence Interval (88%-112%)', 'font': {'size': 16, 'color': '#cbd5e1'}},
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             font=dict(color='#e2e8f0', family='Poppins'),
#             yaxis_title='Amount ($)',
#             yaxis_title_font=dict(color='#cbd5e1'),
#             margin=dict(l=20, r=20, t=40, b=20)
#         )
#         st.plotly_chart(fig_box, use_container_width=True)
    
#     st.markdown("")
    
    # # === ZOPA CURVE ===
    # st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
    # mu = res['prediction']
    # sigma = mu * 0.12
    # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
    # y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    # fig_zopa = go.Figure()
    
    # # Full distribution curve
    # fig_zopa.add_trace(go.Scatter(
    #     x=x, y=y,
    #     mode='lines',
    #     line=dict(color='#64748B', width=2),
    #     fill='tozeroy',
    #     fillcolor='rgba(59, 130, 246, 0.1)',
    #     name='Distribution'
    # ))
    
    # # Safe settlement zone
    # x_safe = np.linspace(res['range_low'], res['range_high'], 150)
    # y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
    # fig_zopa.add_trace(go.Scatter(
    #     x=x_safe, y=y_safe,
    #     mode='lines',
    #     line=dict(width=0),
    #     fill='tozeroy',
    #     fillcolor='rgba(22, 163, 74, 0.5)',
    #     name='Safe Zone'
    # ))
    
    # fig_zopa.update_layout(
    #     height=350,
    #     showlegend=True,
    #     paper_bgcolor='rgba(0,0,0,0)',
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     font=dict(color='#e2e8f0', family='Poppins'),
    #     margin=dict(l=50, r=50, t=40, b=40),
    #     xaxis_title='Settlement Amount ($)',
    #     yaxis_title='Probability Density',
    #     hovermode='x unified'
    # )
    # st.plotly_chart(fig_zopa, use_container_width=True)
    
    # st.markdown("")
    
#     # === RESET BUTTON ===
#     if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="reset_button"):
#         st.session_state.submitted = False
#         st.rerun()


























###########current version
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Initialize Azure Client
client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_DEPLOYMENT_ENDPOINT"), 
    api_key=os.getenv("OPENAI_API_KEY"),  
    api_version="2024-12-01-preview"
)

# === PAGE CONFIG ===
st.set_page_config(
    page_title="Litigation Settlement Analyzer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === PREMIUM CSS STYLING ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    /* === NEUTRAL CHARCOAL THEME (No Blue) === */
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        font-family: 'Poppins', sans-serif;
        color: #e2e8f0;
    }
    /* Make the Form Container a Lighter Grey to pop */
    .form-container {
        background: linear-gradient(135deg, #27272a 0%, #3f3f46 100%) !important;
        border: 1px solid #52525b !important; /* Neutral Grey Border */
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
        padding: 50px;
        border-radius: 20px;
        max-width: 1200px;
        margin: 40px auto;
    }
    
    /* Hide Sidebar */
    section[data-testid="stSidebar"] { display: none; }
    
    /* Form Container */
    .form-container {
        background: linear-gradient(135deg, #1a1f3a 0%, #0f172a 100%);
        border: 2px solid #3b82f6;
        border-radius: 20px;
        padding: 50px;
        max-width: 1200px;
        margin: 40px auto;
        box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
    }
    
    .form-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #60a5fa, #3b82f6, #1e40af);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    
    .form-subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 40px;
        font-size: 1.1rem;
    }
    
    /* Form Sections Grid */
    .form-section-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 25px;
        margin-bottom: 30px;
    }
    
    .form-section-item {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1.5px solid #334155;
        border-radius: 14px;
        padding: 20px;
        transition: all 0.3s ease;
    }
    
    .form-section-item:hover {
        border-color: #3b82f6;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.15);
    }
    
    .form-section-label {
        color: #60a5fa;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 15px;
        display: block;
    }
    
    /* Input Styling */
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput div[data-baseweb="input"] > div,
    .stSlider {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
        border: 1.5px solid #475569 !important;
        border-radius: 10px !important;
        color: white !important;
        transition: all 0.3s ease;
    }
    
    .stSelectbox div[data-baseweb="select"] > div:hover,
    .stNumberInput div[data-baseweb="input"] > div:hover {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.3) !important;
    }
    
    input[type="number"], div[data-baseweb="select"] span {
        color: #e2e8f0 !important;
        -webkit-text-fill-color: #e2e8f0 !important;
        caret-color: #3b82f6 !important;
        font-weight: 600 !important;
    }
    
    ul[data-testid="stSelectboxVirtualDropdown"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 100%) !important;
        border: 1px solid #334155 !important;
    }
    
    li[role="option"] { color: #e2e8f0 !important; }
    li[role="option"]:hover { background: rgba(59, 130, 246, 0.25) !important; }
    
    .stCheckbox div[role="checkbox"] {
        border: 2px solid #475569 !important;
        background: #1e293b !important;
    }
    
    .stCheckbox div[role="checkbox"]:hover { border-color: #3b82f6 !important; }
    
    /* Submit Button */
    .form-button-container {
        display: flex;
        gap: 15px;
        margin-top: 40px;
        justify-content: center;
    }
    
    div.stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%);
        border: none;
        color: white;
        font-weight: 800;
        font-size: 1rem;
        padding: 16px 40px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.35);
        transition: all 0.3s ease;
        min-width: 250px;
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 36px rgba(37, 99, 235, 0.5);
    }
    
    /* Dashboard Header */
    .dashboard-header {
        background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
        border: 2px solid #3b82f6;
        border-radius: 16px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 12px 40px rgba(59, 130, 246, 0.15);
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        align-items: center;
    }
    
    .dashboard-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
    }
    
    .dashboard-subtitle {
        color: #cbd5e1;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .recommendation-panel {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        border: 2px solid #3b82f6;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
    }
    
    .recommendation-text {
        font-size: 1.3rem;
        font-weight: 800;
        color: #60a5fa;
        margin-bottom: 10px;
    }
    
    .recommendation-subtext {
        color: #94a3b8;
        font-size: 0.95rem;
    }
    
    /* KPI Cards */
    .kpi-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-bottom: 30px;
    }
    
    .kpi-card {
        background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
        border: 2px solid #334155;
        border-radius: 14px;
        padding: 24px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }
    
    .kpi-card:hover {
        border-color: #3b82f6;
        transform: translateY(-8px);
        box-shadow: 0 16px 40px rgba(59, 130, 246, 0.25);
    }
    
    .kpi-value {
        font-size: 1.8rem; /* Reduced from 2.2rem to fit better */
        color: #f1f5f9;
        font-weight: 800;
        margin: 5px 0; /* Reduced margin */
        font-family: 'Playfair Display', serif;
        letter-spacing: 0.5px; /* Reduced spacing */
        white-space: nowrap; /* Prevents wrapping */
    }
    
    .kpi-label {
        font-size: 0.7rem; /* Slightly smaller label */
        color: #94a3b8;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    
    .kpi-subtext {
        font-size: 0.85rem;
        color: #cbd5e1;
        font-weight: 500;
    }
    
    /* Driver Analysis Container */
    .driver-analysis {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 30px;
    }
    
    .driver-section {
        background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
        border: 2px solid #334155;
        border-radius: 14px;
        padding: 25px;
    }
    
    .driver-section-title {
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 20px;
        padding-bottom: 12px;
        border-bottom: 2px solid #3b82f6;
    }
    
    .driver-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
        background: #0a0e27;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #3b82f6;
    }
    
    .driver-name {
        color: #cbd5e1;
        font-weight: 600;
        flex: 1;
        font-size: 0.95rem;
    }
    
    .driver-value {
        font-weight: 800;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 0.9rem;
    }
    
    .driver-pos {
        color: #fecaca;
        background: rgba(220, 38, 38, 0.2);
        border: 1px solid #dc2626;
    }
    
    .driver-neg {
        color: #bbf7d0;
        background: rgba(22, 163, 74, 0.2);
        border: 1px solid #16a34a;
    }
    
    /* Alert Boxes */
    .alert-box {
        background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%);
        border-left: 5px solid #dc2626;
        border-radius: 10px;
        padding: 16px;
        margin: 12px 0;
        color: #fecaca;
        font-weight: 600;
        box-shadow: 0 8px 24px rgba(220, 38, 38, 0.15);
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f1f5f9;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #3b82f6;
        font-family: 'Playfair Display', serif;
    }
    
    header { visibility: hidden; }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    

    /* Force all Streamlit input labels to be White */
    label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
        color: #e2e8f0 !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.8px !important;
    }

    /* Ensure text typed inside numbers/selects is White */
    input[type="number"], div[data-baseweb="select"] span {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# === INITIALIZE SESSION STATE ===
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# === FORM STATE ===
if not st.session_state.submitted:
    st.markdown("""
        <div class='form-container'>
            <div class='form-title'>⚖️ Litigation Settlement Analyzer</div>
            <div class='form-subtitle'>AI-Powered Settlement Valuation & Strategy Intelligence</div>
    """, unsafe_allow_html=True)
    
    with st.container(): # Changed from st.form to st.container to allow dynamic interactions
        # === A. LITIGATION & EXPOSURE ===
        st.markdown("<span class='form-section-label'>🏛️ A. Litigation & Exposure</span>", unsafe_allow_html=True)
        
        form_col1, form_col2 = st.columns(2)
        with form_col1:
            jurisdiction = st.selectbox("Jurisdiction", 
                ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'])
        with form_col2:
            venue_win_rate = st.slider("Defense Win Rate in Venue", 0.0, 1.0, 0.45)
        
        form_col3, form_col4 = st.columns(2)
        with form_col3:
            attorney_firm = st.selectbox("Opposing Counsel",
                ['Morgan & Morgan', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner'])
        with form_col4:
            attorney_score = st.slider("Attorney Aggressiveness", 0, 100, 65)
        
        form_col5, _ = st.columns(2)
        with form_col5:
            provider_type = st.selectbox("Primary Provider",
                ['PT', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Chiropractor'])
        
        st.markdown("---")
        
        # === B. ECONOMIC DAMAGES ===
        st.markdown("<span class='form-section-label'>💰 B. Economic Damages</span>", unsafe_allow_html=True)
        
        form_col6, form_col7 = st.columns(2)
        with form_col6:
            wage_loss = st.number_input("Wage Loss Exposure ($)", 5000, 500000, 25000)
        with form_col7:
            impairment = st.slider("Permanent Impairment (%)", 0, 100, 15)
        
        form_col8, form_col9 = st.columns(2)
        with form_col8:
            medical_trajectory = st.selectbox("Medical Cost Trajectory",
                ['Low', 'Moderate', 'High', 'Escalating'])
        with form_col9:
            future_medical = st.checkbox("Future Medical Exposure?", value=True)
        
        form_col10, _ = st.columns(2)
        with form_col10:
            # 1. Toggle: Does a demand exist?
            has_demand = st.checkbox("Has a formal demand been received?", value=False)
            
            # 2. Logic: Show input ONLY if checked. Otherwise, pass 0.
            if has_demand:
                demand = st.number_input("Enter Plaintiff Demand ($)", 
                                       min_value=0, max_value=10000000, value=150000, step=5000)
            else:
                demand = 0 # Passes 0 to backend
                # CHANGED: Updated message to reflect the actual output (Likelihood)
                st.info("ℹ️ No demand entered. System will calculate 'Likelihood of Acceptance' at the predicted value.")
        
        st.markdown("---")
        
        # === C. BEHAVIORAL PROGRESSION ===
        st.markdown("<span class='form-section-label'>📊 C. Behavioral Progression</span>", unsafe_allow_html=True)
        
        form_col11, form_col12 = st.columns(2)
        with form_col11:
            days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
        with form_col12:
            days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)
        
        form_col13, form_col14 = st.columns(2)
        with form_col13:
            treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
        with form_col14:
            provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)
        
        form_col15, _ = st.columns(2)
        with form_col15:
            opioid = st.checkbox("Opioid Prescription Indicator?")
        
        st.markdown("---")
        
        # === D. CLAIMANT PROFILE ===
        st.markdown("<span class='form-section-label'>👤 D. Claimant Profile</span>", unsafe_allow_html=True)
        
        form_col16, form_col17 = st.columns(2)
        with form_col16:
            employment = st.selectbox("Employment Status",
                ['Active', 'Terminated', 'Retired', 'Leave of Absence'])
        with form_col17:
            benefit = st.selectbox("Benefit Status",
                ['TTD', 'PPD', 'Medical Only'])
        
        form_col18, _ = st.columns(2)
        with form_col18:
            msa = st.checkbox("Medicare Set-Aside (MSA) Required?")
        
        st.markdown("---")
        
        # === E. MEDICAL PROFILE ===
        st.markdown("<span class='form-section-label'>🏥 E. Medical Profile</span>", unsafe_allow_html=True)
        
        form_col19, form_col20 = st.columns(2)
        with form_col19:
            comorbidity = st.selectbox("Comorbidities",
                ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions'])
        with form_col20:
            odg = st.selectbox("ODG Guidelines Adherence",
                ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds'])
        
        st.markdown("---")
        
        # === F. LITIGATION INTELLIGENCE ===
        st.markdown("<span class='form-section-label'>📋 F. Litigation Intelligence</span>", unsafe_allow_html=True)
        
        form_col21, form_col22 = st.columns(2)
        with form_col21:
            attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
        with form_col22:
            attorney_type = st.selectbox("Attorney Settlement Tendency",
                ['Early Settlement', 'Balanced', 'Trial-Oriented'])
        
        form_col23, _ = st.columns(2)
        with form_col23:
            judge = st.selectbox("Judge Propensity (if assigned)",
                ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned'])
        
        st.markdown("---")
        
        # Submit Button
        submitted = st.button("🚀 ANALYZE CASE", use_container_width=True)
        if submitted:
            # Store all form values in session state
            st.session_state.jurisdiction = jurisdiction
            st.session_state.venue_win_rate = venue_win_rate
            st.session_state.attorney_firm = attorney_firm
            st.session_state.attorney_score = attorney_score
            st.session_state.provider_type = provider_type
            st.session_state.wage_loss = wage_loss
            st.session_state.impairment = impairment
            st.session_state.medical_trajectory = medical_trajectory
            st.session_state.future_medical = future_medical
            st.session_state.demand = demand
            st.session_state.days_filed = days_filed
            st.session_state.days_attorney = days_attorney
            st.session_state.treatment_duration = treatment_duration
            st.session_state.opioid = opioid
            st.session_state.provider_shopping = provider_shopping
            st.session_state.employment = employment
            st.session_state.benefit = benefit
            st.session_state.msa = msa
            st.session_state.comorbidity = comorbidity
            st.session_state.odg = odg
            st.session_state.attorney_winrate = attorney_winrate
            st.session_state.attorney_type = attorney_type
            st.session_state.judge = judge
            st.session_state.submitted = True
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# === DASHBOARD VIEW ===
else:
    import model

    # Get form data from session state
    inputs = {
        "Jurisdiction": st.session_state.jurisdiction,
        "Venue_Win_Rate": st.session_state.venue_win_rate,
        "Plaintiff_Attorney": st.session_state.attorney_firm,
        "Attorney_Score": st.session_state.attorney_score,
        "Provider_Type": st.session_state.provider_type,
        "Wage_Loss_Exposure": st.session_state.wage_loss,
        "Impairment_Rating": st.session_state.impairment,
        "Medical_Trajectory": st.session_state.medical_trajectory,
        "Future_Medical": 1 if st.session_state.future_medical else 0,
        "Demand_Amount": st.session_state.demand,
        "Days_Since_Filed": st.session_state.days_filed,
        "Days_Attorney_Engaged": st.session_state.days_attorney,
        "Treatment_Duration": st.session_state.treatment_duration,
        "Opioid_Indicator": 1 if st.session_state.opioid else 0,
        "Provider_Shopping": st.session_state.provider_shopping,
        "Employment_Status": st.session_state.employment,
        "Benefit_Status": st.session_state.benefit,
        "MSA_Flag": 1 if st.session_state.msa else 0,
        "Comorbidities": st.session_state.comorbidity,
        "Guidelines_Adherence": st.session_state.odg,
        "Attorney_Win_Rate": st.session_state.attorney_winrate,
        "Attorney_Tendency": st.session_state.attorney_type,
        "Judge_Propensity": st.session_state.judge
    }
    
    # Extract variables for use in dashboard
    jurisdiction = st.session_state.jurisdiction
    attorney_score = st.session_state.attorney_score
    venue_win_rate = st.session_state.venue_win_rate
    days_filed = st.session_state.days_filed
    employment = st.session_state.employment
    opioid = st.session_state.opioid
    impairment = st.session_state.impairment
    
    res = model.predict_case(inputs)
    # === 1. CALCULATE CONFIDENCE SCORE (DEFINE IT HERE) ===
    confidence_score = 90
    
    # Apply penalties based on inputs
    if inputs['Attorney_Score'] > 80: confidence_score -= 10
    if inputs['Medical_Trajectory'] == 'Escalating': confidence_score -= 15
    if inputs['Days_Since_Filed'] < 60: confidence_score -= 10
    if inputs['Judge_Propensity'] == 'Not Yet Assigned': confidence_score -= 5
    
    # Cap between 0 and 100
    confidence_score = max(0, min(100, confidence_score))
    
    # Define Label for Header
    conf_label_header = "High Confidence" if confidence_score >= 80 else "Medium Confidence"
    # === DASHBOARD HEADER ===
    rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
    col_header_left, col_header_right = st.columns(2)
    
    with col_header_left:
        st.markdown(f"""
            <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
            <div class='dashboard-subtitle'>{res['action_desc']}<br>
            📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </b></div>
        """, unsafe_allow_html=True)
    
    # with col_header_right:
    #     st.markdown(f"""
    #         <div class='recommendation-panel'>
    #             <div class='recommendation-text'>MODEL CONFIDENCE</div>
    #             <div class='recommendation-subtext'>89% • Based on {22} litigation attributes</div>
    #         </div>
    #     """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # === KPI CARDS ===
    col1, col2, col3, col4 = st.columns(4)
    
    # with col1:
    #     st.markdown(f"""
    #         <div class='kpi-card'>
    #             <div class='kpi-label'>💵 Target Settlement</div>
    #             <div class='kpi-value'>${res['prediction']/1000:.0f}K</div>
    #             <div class='kpi-subtext'>Range: ${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
    #         </div>
    #     """, unsafe_allow_html=True)
    with col1:
        # SWAPPED: Range is now the Big Value, Target is the Subtext
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>💵 Settlement Range</div>
                <div class='kpi-value'>${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
                <div class='kpi-subtext'>Estimated value: ${res['prediction']/1000:.0f}K</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        # 1. Calculate Base Confidence Score (0-100%)
        base_score = 90
        
        # Penalties (reduce the base score)
        if inputs['Attorney_Score'] > 80: base_score -= 10
        if inputs['Medical_Trajectory'] == 'Escalating': base_score -= 15
        if inputs['Days_Since_Filed'] < 60: base_score -= 10
        if inputs['Judge_Propensity'] == 'Not Yet Assigned': base_score -= 5
        
        # 2. Calculate the Interval (Width of the range)
        # If the case is risky, the interval is wider (more uncertainty)
        interval_width = 5 
        if base_score < 75: interval_width = 10 
        
        low_ci = max(base_score - interval_width, 10)
        high_ci = min(base_score + interval_width, 99)
        
        # 3. Determine Color
        if low_ci >= 75:
            conf_color = "#16a34a" # Green
            label_text = "Strong Predictability"
        elif low_ci >= 55:
            conf_color = "#f59e0b" # Orange
            label_text = "Moderate Certainty"
        else:
            conf_color = "#dc2626" # Red
            label_text = "Low Data Density"

        # 4. Render Card
        st.markdown(f"""
            <div class='kpi-card' style='border-bottom: 4px solid {conf_color};'>
                <div class='kpi-label'>📉 Confidence Interval</div>
                <div class='kpi-value' style='color: {conf_color};'>{low_ci}% – {high_ci}%</div>
                <div class='kpi-subtext'>{label_text}</div>
            </div>
        """, unsafe_allow_html=True)
    
    
    
    
    with col3:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>⏱️ Est. Duration</div>
                <div class='kpi-value'>{res['days']}d</div>
                <div class='kpi-subtext'>≈ {res['months']:.1f} months</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>📊 Total Exposure</div>
                <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
                <div class='kpi-subtext'>Verdict + Defense</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
    # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
    # Only show this section if NO demand was entered (Simulated)
    if res['demand_source'] == 'Simulated':
        st.markdown("<div class='section-header'>🤝 Negotiation Intelligence</div>", unsafe_allow_html=True)
        
        prob = res['acceptance_likelihood']
        
        # Color Logic for the Bar
        if prob >= 70: 
            p_color = "#16a34a" # Green
            p_msg = "High probability of early resolution at Target Value."
        elif prob >= 40: 
            p_color = "#f59e0b" # Orange
            p_msg = "Moderate resistance expected. May require mediation."
        else: 
            p_color = "#dc2626" # Red
            p_msg = "Low probability. Opposing counsel likely to push for trial."

        # 1. Render the Full-Width Probability Bar
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%); border: 1px solid #3b82f6; border-radius: 12px; padding: 25px; margin-bottom: 20px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
                    <span style='color: #cbd5e1; font-weight: 600;'>Likelihood of Acceptance at Target Value (${res['prediction']:,.0f})</span>
                    <span style='color: {p_color}; font-weight: 800; font-size: 1.2rem;'>{prob}%</span>
                </div>
                <div style='width: 100%; background-color: #334155; border-radius: 10px; height: 12px;'>
                    <div style='width: {prob}%; background-color: {p_color}; height: 12px; border-radius: 10px; transition: width 1s ease;'></div>
                </div>
                <div style='color: #94a3b8; font-size: 0.9rem; margin-top: 15px;'>
                    <i>Strategy Note: {p_msg}</i>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 2. Acceptance Curve Visualization (Added Graph)
        st.markdown("<h5 style='color: #cbd5e1; margin-bottom: 10px;'>📉 Offer vs. Acceptance Probability Curve</h5>", unsafe_allow_html=True)
        
        target = res['prediction']
        
        # Create a range of offers (from 50% to 150% of the target value)
        x_vals = np.linspace(target * 0.5, target * 1.5, 100)
        
        # MATH: Dynamic Sigmoid Curve logic
        k = 10 / target 
        prob_safe = max(1, min(99, prob)) # Safety clamp
        
        # Shift curve based on probability score
        shift = target + (np.log(100/prob_safe - 1) / k)
        
        # Generate Y values (0-100%)
        y_vals = 100 / (1 + np.exp(-k * (x_vals - shift)))
        
        fig_curve = go.Figure()
        
        # The Curve Line
        fig_curve.add_trace(go.Scatter(
            x=x_vals, y=y_vals,
            mode='lines',
            line=dict(color='#60A5FA', width=4),
            fill='tozeroy',
            fillcolor='rgba(96, 165, 250, 0.1)',
            name='Acceptance Chance'
        ))
        
        # The "You Are Here" Marker
        fig_curve.add_trace(go.Scatter(
            x=[target], y=[prob],
            mode='markers',
            marker=dict(color='#F59E0B', size=15, line=dict(color='white', width=2)),
            name='Current Target',
            hoverinfo='text',
            hovertext=f"Target: ${target:,.0f}<br>Probability: {prob}%"
        ))

        fig_curve.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=30, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="Offer Amount ($)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), showgrid=False, tickprefix="$"),
            yaxis=dict(title="Probability (%)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), range=[0, 105], showgrid=True, gridcolor='#334155'),
            showlegend=False,
            hovermode="x unified"
        )
        
        st.plotly_chart(fig_curve, use_container_width=True)
    # === DRIVER ANALYSIS (Like Image) ===
    # # === 7. EXPLAINABILITY & STRATEGIC ANALYSIS (SHAP-STYLE FEATURE IMPORTANCE) ===
    # st.markdown("<div class='section-header'>📈 Model Explainability & Strategic Analysis</div>", unsafe_allow_html=True)
    
    # # 1. Extract all variables from inputs dictionary
    # attorney_score = inputs['Attorney_Score']
    # venue_win_rate = inputs['Venue_Win_Rate']
    # impairment = inputs['Impairment_Rating']
    # wage_loss = inputs['Wage_Loss_Exposure']
    # employment = inputs['Employment_Status']
    # opioid = inputs['Opioid_Indicator']
    # days_filed = inputs['Days_Since_Filed']
    # medical_trajectory = inputs['Medical_Trajectory']
    # future_medical = inputs['Future_Medical']
    # attorney_type = inputs['Attorney_Tendency']
    
    # # 2. Determine Risk Level
    # if confidence_score >= 80:
    #     risk_level = "LOW RISK"
    #     risk_emoji = "🟢 GREEN"
    # elif confidence_score >= 60:
    #     risk_level = "MEDIUM RISK"
    #     risk_emoji = "🟡 YELLOW"
    # else:
    #     risk_level = "HIGH RISK"
    #     risk_emoji = "🔴 RED"
    
    # # 3. CALCULATE FEATURE CONTRIBUTIONS (SHAP-STYLE)
    # feature_contributions = {}
    
    # # A. LITIGATION & EXPOSURE FEATURES
    # if attorney_score > 70:
    #     feature_contributions['Attorney Score'] = {
    #         'value': attorney_score,
    #         'impact': (attorney_score - 50) * 250,
    #         'direction': 'positive',
    #         'explanation': f"High attorney aggressiveness ({attorney_score}/100) increases settlement pressure"
    #     }
    # else:
    #     direction_val = 'negative' if attorney_score < 50 else 'neutral'
    #     feature_contributions['Attorney Score'] = {
    #         'value': attorney_score,
    #         'impact': (attorney_score - 50) * 250,
    #         'direction': direction_val,
    #         'explanation': f"Moderate attorney profile ({attorney_score}/100) suggests manageable litigation"
    #     }
    
    # if venue_win_rate < 0.50:
    #     feature_contributions['Venue Win Rate'] = {
    #         'value': venue_win_rate,
    #         'impact': (0.50 - venue_win_rate) * 150000,
    #         'direction': 'positive',
    #         'explanation': f"Unfavorable venue ({venue_win_rate*100:.0f}% defense win rate) increases plaintiff leverage"
    #     }
    # else:
    #     feature_contributions['Venue Win Rate'] = {
    #         'value': venue_win_rate,
    #         'impact': (0.50 - venue_win_rate) * 150000,
    #         'direction': 'negative',
    #         'explanation': f"Favorable venue ({venue_win_rate*100:.0f}% defense win rate) supports lower settlement"
    #     }
    
    # # B. ECONOMIC DAMAGES FEATURES
    # if impairment > 20:
    #     feature_contributions['Impairment Rating'] = {
    #         'value': impairment,
    #         'impact': impairment * 1800,
    #         'direction': 'positive',
    #         'explanation': f"High permanent impairment ({impairment}%) significantly raises non-economic damages"
    #     }
    
    # if wage_loss > 50000:
    #     feature_contributions['Wage Loss'] = {
    #         'value': wage_loss,
    #         'impact': (wage_loss - 25000) * 0.3,
    #         'direction': 'positive',
    #         'explanation': f"High wage loss exposure (${wage_loss:,}) increases indemnity component"
    #     }
    
    # # C. BEHAVIORAL FEATURES
    # if employment == 'Terminated':
    #     feature_contributions['Employment Status'] = {
    #         'value': employment,
    #         'impact': 18000,
    #         'direction': 'positive',
    #         'explanation': "Terminated employment status elevates emotional damages demands"
    #     }
    
    # if opioid == 1:
    #     feature_contributions['Opioid Indicator'] = {
    #         'value': 'Yes',
    #         'impact': 12000,
    #         'direction': 'positive',
    #         'explanation': "Opioid usage creates narrative risk and settlement floor escalation"
    #     }
    
    # if days_filed > 365:
    #     feature_contributions['Days Open'] = {
    #         'value': days_filed,
    #         'impact': (days_filed - 180) * 15,
    #         'direction': 'positive',
    #         'explanation': f"Long duration ({days_filed} days) increases cumulative exposure"
    #     }
    
    # # D. MEDICAL FEATURES
    # if medical_trajectory == 'Escalating':
    #     feature_contributions['Medical Trajectory'] = {
    #         'value': medical_trajectory,
    #         'impact': 25000,
    #         'direction': 'positive',
    #         'explanation': "Escalating medical costs suggest chronic condition trajectory"
    #     }
    # elif medical_trajectory == 'Low':
    #     feature_contributions['Medical Trajectory'] = {
    #         'value': medical_trajectory,
    #         'impact': -12000,
    #         'direction': 'negative',
    #         'explanation': "Low medical trajectory indicates quick recovery expectations"
    #     }
    
    # if future_medical == 1:
    #     feature_contributions['Future Medical'] = {
    #         'value': 'Yes',
    #         'impact': 15000,
    #         'direction': 'positive',
    #         'explanation': "Future medical exposure requires higher settlement reserves"
    #     }
    
    # # E. LITIGATION INTELLIGENCE FEATURES
    # if attorney_type == 'Trial-Oriented':
    #     feature_contributions['Attorney Type'] = {
    #         'value': attorney_type,
    #         'impact': 20000,
    #         'direction': 'positive',
    #         'explanation': "Trial-oriented counsel increases litigation costs and risk premium"
    #     }
    # else:
    #     feature_contributions['Attorney Type'] = {
    #         'value': attorney_type,
    #         'impact': -10000,
    #         'direction': 'negative',
    #         'explanation': "Settlement-oriented counsel creates early resolution opportunities"
    #     }
    
    # # 4. SORT FEATURES BY IMPACT (SHAP-STYLE)
    # sorted_features = sorted(feature_contributions.items(), key=lambda x: abs(x[1]['impact']), reverse=True)
    
    # # 5. CALCULATE BASE VALUE
    # base_prediction = res['prediction']
    
    # # 6. RENDER SHAP-STYLE EXPLANATION
    # with st.container():
    #     st.markdown(f"## 🧾 Why This Claim Is {risk_level} {risk_emoji}")
    #     st.markdown(f"**Base Settlement Value:** ${base_prediction:,.0f}")
    #     st.divider()
        
    #     st.markdown("### 🔬 Feature Contribution Analysis (SHAP-Style)")
        
    #     # Create two columns for positive/negative impacts
    #     col_pos, col_neg = st.columns(2)
        
    #     with col_pos:
    #         st.markdown("#### 🔴 Increasing Pressure (Positive Impact)")
    #         pos_features = [f for f in sorted_features if f[1]['direction'] == 'positive']
            
    #         if pos_features:
    #             for feature_name, feature_data in pos_features[:5]:
    #                 impact_val = feature_data['impact']
    #                 pct_change = (impact_val / base_prediction) * 100
                    
    #                 st.write(f"**{feature_name}**")
    #                 st.write(f"Value: `{feature_data['value']}`")
    #                 st.write(f"Impact: **+${impact_val:,.0f}** (+{pct_change:.1f}%)")
    #                 st.caption(f"💡 {feature_data['explanation']}")
    #                 st.write("")
    #         else:
    #             st.info("No pressure-increasing factors detected")
        
    #     with col_neg:
    #         st.markdown("#### 🟢 Mitigating Defense (Negative Impact)")
    #         neg_features = [f for f in sorted_features if f[1]['direction'] == 'negative']
            
    #         if neg_features:
    #             for feature_name, feature_data in neg_features[:5]:
    #                 impact_val = feature_data['impact']
    #                 pct_change = (impact_val / base_prediction) * 100
                    
    #                 st.write(f"**{feature_name}**")
    #                 st.write(f"Value: `{feature_data['value']}`")
    #                 st.write(f"Impact: **${impact_val:,.0f}** ({pct_change:.1f}%)")
    #                 st.caption(f"💡 {feature_data['explanation']}")
    #                 st.write("")
    #         else:
    #             st.info("No mitigating factors detected")
        
    #     st.divider()
        
    #     # 7. SUMMARY
    #     top_driver = sorted_features[0] if sorted_features else None
        
    #     if top_driver:
    #         st.markdown("### 📊 Key Insight")
    #         st.markdown(
    #             f"🎯 **Primary Driver:** {top_driver[0]}\n\n"
    #             f"The single largest factor affecting this claim is **{top_driver[0]}** "
    #             f"(Contributing **+${abs(top_driver[1]['impact']):,.0f}** or **{abs(top_driver[1]['impact'])/base_prediction*100:.1f}%** of the prediction).\n\n"
    #             f"**Why:** {top_driver[1]['explanation']}"
    #         )
        
    #     # 8. RECOMMENDATION
    #     st.markdown("### 🎯 Strategic Recommendation")
        
    #     if confidence_score >= 75:
    #         rec = "✅ **SETTLE** - Risk factors are identifiable and manageable through early negotiation."
    #     elif confidence_score >= 55:
    #         rec = "⚡ **STRATEGIZE** - Balance of factors requires careful negotiation strategy."
    #     else:
    #         rec = "⚔️ **LITIGATE** - Multiple high-risk factors warrant trial preparation."
        
    #     st.success(rec)
    # === 7. EXPLAINABILITY & STRATEGIC ANALYSIS (SHAP-STYLE SIMPLIFIED) ===
    st.markdown("<div class='section-header'>📈 Model Explainability & Strategic Analysis</div>", unsafe_allow_html=True)
    
    # Extract variables from inputs
    attorney_score = inputs['Attorney_Score']
    venue_win_rate = inputs['Venue_Win_Rate']
    impairment = inputs['Impairment_Rating']
    wage_loss = inputs['Wage_Loss_Exposure']
    employment = inputs['Employment_Status']
    opioid = inputs['Opioid_Indicator']
    days_filed = inputs['Days_Since_Filed']
    medical_trajectory = inputs['Medical_Trajectory']
    future_medical = inputs['Future_Medical']
    attorney_type = inputs['Attorney_Tendency']
    
    # Calculate feature importance scores - ALWAYS include meaningful features
    feature_importance = []
    
    # ALWAYS calculate base factors (don't use high thresholds)
    # Attorney contribution
    attorney_impact = (attorney_score - 40) * 150  # Scale from base
    feature_importance.append(('Attorney Score', attorney_score, attorney_impact, f'{attorney_score}/100 aggressiveness'))
    
    # Venue contribution
    venue_impact = (0.50 - venue_win_rate) * 80000  # Negative venue = higher impact
    feature_importance.append(('Venue Win Rate', f'{int(venue_win_rate*100)}%', venue_impact, f'{int(venue_win_rate*100)}% defense win rate'))
    
    # Impairment contribution (MAJOR DRIVER)
    if impairment > 0:
        impair_impact = impairment * 1500
        feature_importance.append(('Impairment Rating', f'{impairment}%', impair_impact, f'{impairment}% permanent injury'))
    
    # Wage loss contribution
    if wage_loss > 0:
        wage_impact = wage_loss * 0.6
        feature_importance.append(('Wage Loss Exposure', f'${wage_loss:,}', wage_impact, f'Lost wages: ${wage_loss:,}'))
    
    # Employment status (binary impact)
    if employment == 'Terminated':
        feature_importance.append(('Employment Status', employment, 25000, 'Terminated = emotional damages premium'))
    else:
        feature_importance.append(('Employment Status', employment, 0, 'Standard employment relationship'))
    
    # Opioid indicator
    if opioid == 1:
        feature_importance.append(('Opioid Indicator', 'Yes', 14000, 'Opioid usage increases narrative risk'))
    else:
        feature_importance.append(('Opioid Indicator', 'No', 0, 'No opioid complications'))
    
    # Medical trajectory
    if medical_trajectory == 'Escalating':
        traj_impact = 20000
    elif medical_trajectory == 'High':
        traj_impact = 12000
    elif medical_trajectory == 'Moderate':
        traj_impact = 5000
    else:
        traj_impact = -3000
    feature_importance.append(('Medical Trajectory', medical_trajectory, traj_impact, f'{medical_trajectory} medical costs'))
    
    # Days filed contribution
    if days_filed > 0:
        days_impact = (days_filed / 365) * 8000  # Scale by years
        feature_importance.append(('Days Since Filed', days_filed, days_impact, f'{days_filed} days open'))
    
    # Attorney type
    if attorney_type == 'Trial-Oriented':
        att_type_impact = 16000
    elif attorney_type == 'Balanced':
        att_type_impact = 4000
    else:
        att_type_impact = -5000
    feature_importance.append(('Attorney Type', attorney_type, att_type_impact, f'{attorney_type} approach'))
    
    # Future medical
    if future_medical == 1:
        feature_importance.append(('Future Medical', 'Yes', 10000, 'Requires settlement reserves'))
    else:
        feature_importance.append(('Future Medical', 'No', 0, 'No future medical needed'))
    
    # Sort by absolute impact value (descending)
    feature_importance = sorted(feature_importance, key=lambda x: abs(x[2]), reverse=True)
    
    # Filter out zero-impact factors
    feature_importance = [f for f in feature_importance if abs(f[2]) > 500]
    
    base_value = res['prediction']
    
    # RENDER CLEAN EXPLANATION
    st.markdown(f"## 🧾 What Drove the ${base_value:,.0f} Prediction")
    st.divider()
    
    st.markdown("### Top Factors Contributing to Settlement Value")
    
    for i, (feature, value, impact, desc) in enumerate(feature_importance[:6], 1):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write(f"**{i}. {feature}**")
            st.caption(f"Value: `{value}` • {desc}")
        
        with col2:
            impact_pct = (abs(impact) / base_value) * 100 if base_value > 0 else 0
            color = "🔴" if impact > 0 else "🟢"
            st.write(f"{color} ${abs(impact):,.0f}\n({impact_pct:.1f}%)")
    
    st.divider()
    
    # Build narrative summary
    if len(feature_importance) >= 3:
        top_3 = feature_importance[:3]
        
        summary_text = f"""
### 📊 Why This Settlement Value

**The model considered {len(feature_importance)} key factors:**

1. **{top_3[0][0]}** ({top_3[0][1]})  
   Contribution: ${abs(top_3[0][2]):,.0f} ({abs(top_3[0][2])/base_value*100:.1f}%)  
   → {top_3[0][3]}

2. **{top_3[1][0]}** ({top_3[1][1]})  
   Contribution: ${abs(top_3[1][2]):,.0f} ({abs(top_3[1][2])/base_value*100:.1f}%)  
   → {top_3[1][3]}

3. **{top_3[2][0]}** ({top_3[2][1]})  
   Contribution: ${abs(top_3[2][2]):,.0f} ({abs(top_3[2][2])/base_value*100:.1f}%)  
   → {top_3[2][3]}

**Result:** These three factors account for **{sum([abs(f[2]) for f in top_3])/base_value*100:.1f}%** of the final ${base_value:,.0f} prediction.
        """
        st.markdown(summary_text)
    
    st.divider()
    
    # Final recommendation
    st.markdown("### 🎯 Recommendation")
    
    if confidence_score >= 75:
        st.success("✅ **SETTLE** - Key factors clearly support settlement negotiations.")
    elif confidence_score >= 55:
        st.warning("⚡ **STRATEGIZE** - Mixed factors require careful case management.")
    else:
        st.error("⚔️ **LITIGATE** - High-risk factors warrant trial preparation.")
    # === RISK ALERTS ===
    
    
    # === STRATEGIC RECOMMENDATION ===
    st.markdown("<div class='section-header'>🎯 Recommended Strategy</div>", unsafe_allow_html=True)
    
    if res['action'] == 'SETTLE':
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
            Settlement is economically superior. Litigation exposure (<b>${res['exposure']:,.0f}</b>) exceeds plaintiff recovery (<b>${res['demand']:,.0f}</b>).<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
            • <b>Opening Offer:</b> ${res['range_low']:,.0f} – ${int(res['prediction']*0.95):,.0f}<br>
            • <b>Walk-Away Price:</b> ${res['range_high']:,.0f}<br>
            • <b>Savings vs Litigation:</b> ${res['savings']:,.0f}
            </div>
        """, unsafe_allow_html=True)
    elif res['action'] == 'LITIGATE':
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
            Plaintiff demand (<b>${res['demand']:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
            • <b>Expected Defense Costs:</b> ${res['defense_cost']:,.0f}<br>
            • <b>Anticipated Verdict:</b> ${res['prediction']:,.0f}<br>
            • <b>Do Not Settle Above:</b> ${int(res['exposure']*0.9):,.0f}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
            Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
            • <b>Test Offer:</b> ${int(res['prediction']*0.85):,.0f}<br>
            • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
            • <b>Re-evaluate:</b> Quarterly or on significant developments
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("")
    
    # # === VISUALIZATIONS ===
    # st.markdown("<div class='section-header'>📊 Predictive Analytics & Confidence Intervals</div>", unsafe_allow_html=True)
    
    # viz_col1, viz_col2 = st.columns(2)
    
    # with viz_col1:
    #     # Gauge Chart - Settlement Value Prediction
    #     fig_gauge = go.Figure(go.Indicator(
    #         mode="gauge+number",
    #         value=int(res['prediction']),
    #         number={'font': {'size': 32, 'color': "#e2e8f0"}, 'prefix': "$"},
    #         domain={'x': [0, 1], 'y': [0, 1]},
    #         gauge={
    #             'axis': {'range': [0, int(res['range_high']*1.4)], 'tickwidth': 1, 'tickcolor': "#334155"},
    #             'bar': {'color': "#3b82f6", 'thickness': 0.3},
    #             'bgcolor': "#0a0e27",
    #             'borderwidth': 2,
    #             'bordercolor': "#334155",
    #             'steps': [
    #                 {'range': [0, res['range_low']], 'color': "#1e3a8a"},
    #                 {'range': [res['range_low'], res['range_high']], 'color': "#1e40af"},
    #                 {'range': [res['range_high'], int(res['range_high']*1.4)], 'color': "#7f1d1d"}
    #             ],
    #         }
    #     ))
    #     fig_gauge.update_layout(
    #         height=320,
    #         margin=dict(l=20, r=20, t=40, b=20),
    #         paper_bgcolor='rgba(0,0,0,0)',
    #         plot_bgcolor='rgba(0,0,0,0)',
    #         font=dict(color='#e2e8f0', family='Poppins'),
    #         title={'text': 'Settlement Value Prediction', 'font': {'size': 16, 'color': '#cbd5e1'}}
    #     )
    #     st.plotly_chart(fig_gauge, use_container_width=True)
    
    # with viz_col2:
    #     # Box Plot - Settlement Range & Confidence
    #     fig_box = go.Figure()
        
    #     # Add box plot for confidence interval
    #     fig_box.add_trace(go.Box(
    #         y=[res['range_low'], res['prediction'], res['range_high']],
    #         name='Settlement Range',
    #         marker_color='#3b82f6',
    #         boxmean='sd',
    #         showlegend=False
    #     ))
        
    #     fig_box.update_layout(
    #         height=320,
    #         title={'text': 'Confidence Interval (88%-112%)', 'font': {'size': 16, 'color': '#cbd5e1'}},
    #         paper_bgcolor='rgba(0,0,0,0)',
    #         plot_bgcolor='rgba(0,0,0,0)',
    #         font=dict(color='#e2e8f0', family='Poppins'),
    #         yaxis_title='Amount ($)',
    #         yaxis_title_font=dict(color='#cbd5e1'),
    #         margin=dict(l=20, r=20, t=40, b=20)
    #     )
    #     st.plotly_chart(fig_box, use_container_width=True)
    
    # st.markdown("")
    # === 8. VISUALIZATIONS (Box Plot Only) ===
    # === 8. VISUALIZATIONS (Improved Box Plot) ===
    st.markdown("<div class='section-header'>📊 Predictive Analytics & Settlement Range</div>", unsafe_allow_html=True)
    
    # 1. Prepare Data for a "Full" Box Plot
    # We synthesize Q1/Q3 to give the box volume (visual appeal)
    # Logic: The Box covers the middle 50% of the range, Whiskers cover 100%
    pred = res['prediction']
    low = res['range_low']
    high = res['range_high']
    
    q1 = pred - (pred - low) * 0.4  # 40% towards the bottom
    q3 = pred + (high - pred) * 0.4 # 40% towards the top
    
    fig_box = go.Figure()
    
    # 2. Add the Horizontal Box Trace
    fig_box.add_trace(go.Box(
        q1=[q1], median=[pred], q3=[q3], 
        lowerfence=[low], upperfence=[high],
        name="Settlement Value",
        marker_color='#60A5FA', # Brand Blue
        fillcolor='rgba(96, 165, 250, 0.2)', # Transparent Fill
        orientation='h', # Horizontal is better for money ranges
        hoverinfo='x+name'
    ))
    
    # 3. Add Annotation for the Target
    fig_box.add_annotation(
        x=pred, y=0.3,
        text=f"<b>Target: ${pred/1000:.0f}K</b>",
        showarrow=False,
        font=dict(color="#F1F5F9", size=14),
        yshift=10
    )

    # 4. Premium Layout Styling
    fig_box.update_layout(
        height=250, # Compact height
        title={
            'text': f'Projected Settlement Range (Model Confidence: {confidence_score}%)', 
            'font': {'size': 15, 'color': '#cbd5e1'}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e2e8f0', family='Poppins'),
        xaxis=dict(
            title="Settlement Amount ($)",
            title_font=dict(color='#94a3b8', size=12),
            tickfont=dict(color='#cbd5e1'),
            tickprefix="$",
            showgrid=True,
            gridcolor='#334155'
        ),
        yaxis=dict(showticklabels=False), # Hide Y labels (it's just one box)
        margin=dict(l=20, r=20, t=60, b=40),
        showlegend=False
    )
    
    st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("")
    
    # === ZOPA CURVE ===
    # # === 9. ZOPA CURVE (Dynamic) ===
    # st.markdown("<div class='section-header'>📈 Settlement Distribution Analysis</div>", unsafe_allow_html=True)
    
    # # Ensure variables exist (Safety check)
    # mu = res.get('prediction', 0)
    # low_b = res.get('range_low', mu*0.9)
    # high_b = res.get('range_high', mu*1.1)
    
    # # 1. Logic: Calculate shape based on Confidence
    # # If confidence_score isn't defined yet, default to 90
    # curr_conf = locals().get('confidence_score', 90) 
    
    # # Map Confidence (0-100) to Sigma Width (0.20-0.05)
    # # High Confidence = Narrow Curve. Low Confidence = Wide Curve.
    # sigma_pct = 0.20 - ((curr_conf - 50) / 50 * 0.15)
    # sigma_pct = max(0.05, min(0.20, sigma_pct))
    # sigma = mu * sigma_pct
    
    # # 2. Create Data Points
    # x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
    # y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    # # 3. Build Plot
    # fig_zopa = go.Figure()
    
    # # A. The Bell Curve
    # fig_zopa.add_trace(go.Scatter(
    #     x=x, y=y,
    #     mode='lines',
    #     line=dict(color='#60A5FA', width=3),
    #     fill='tozeroy',
    #     fillcolor='rgba(59, 130, 246, 0.15)',
    #     name='Probability',
    #     hoverinfo='skip'
    # ))
    
    # # B. The Target Line (Vertical)
    # fig_zopa.add_vline(x=mu, line_width=2, line_dash="dash", line_color="#F1F5F9")
    # fig_zopa.add_annotation(
    #     x=mu, y=max(y)*0.95,
    #     text=f"Target: ${mu/1000:.0f}K",
    #     showarrow=False,
    #     font=dict(color="white", size=12),
    #     yshift=10
    # )

    # # C. The Safe Zone (Green Shaded Area)
    # fig_zopa.add_vrect(
    #     x0=low_b, x1=high_b,
    #     fillcolor="#16a34a", opacity=0.1,
    #     layer="below", line_width=0,
    #     annotation_text="Confidence Interval", 
    #     annotation_position="top left",
    #     annotation_font_color="#16a34a"
    # )
    
    # # 4. Final Layout & Render
    # fig_zopa.update_layout(
    #     height=320,
    #     paper_bgcolor='rgba(0,0,0,0)',
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     font=dict(color='#e2e8f0', family='Poppins'),
    #     margin=dict(l=20, r=20, t=30, b=20),
    #     xaxis=dict(
    #         showgrid=False, 
    #         title="Settlement Amount ($)",
    #         title_font=dict(color='#94a3b8'),
    #         tickprefix="$",
    #         showticklabels=True
    #     ),
    #     yaxis=dict(
    #         showgrid=False, 
    #         showticklabels=False
    #     ),
    #     showlegend=False
    # )
    
    # # THIS IS THE MISSING LINE THAT MAKES IT APPEAR:
    # st.plotly_chart(fig_zopa, use_container_width=True)
    # === ZOPA CURVE ===
    st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
    mu = res['prediction']
    sigma = mu * 0.12
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    fig_zopa = go.Figure()
    
    # Full distribution curve
    fig_zopa.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='#64748B', width=2),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.1)',
        name='Distribution'
    ))
    
    # Safe settlement zone
    x_safe = np.linspace(res['range_low'], res['range_high'], 150)
    y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
    fig_zopa.add_trace(go.Scatter(
        x=x_safe, y=y_safe,
        mode='lines',
        line=dict(width=0),
        fill='tozeroy',
        fillcolor='rgba(22, 163, 74, 0.5)',
        name='Safe Zone'
    ))
    
    fig_zopa.update_layout(
        height=350,
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e2e8f0', family='Poppins'),
        margin=dict(l=50, r=50, t=40, b=40),
        xaxis_title='Settlement Amount ($)',
        yaxis_title='Probability Density',
        hovermode='x unified'
    )
    st.plotly_chart(fig_zopa, use_container_width=True)
    
    st.markdown("")

    
    # === RESET BUTTON ===
    if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="reset_button"):
        st.session_state.submitted = False
        st.rerun()












