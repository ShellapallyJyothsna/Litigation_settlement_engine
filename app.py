



########3without time
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# # --- 1. PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="ClaimSight AI | Enterprise",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. FIXED CSS STYLING ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

#     /* A. REMOVE DEFAULT PADDING */
#     .block-container {
#         padding-top: 1rem !important;
#         padding-bottom: 2rem !important;
#         max-width: 95% !important;
#     }
#     header {visibility: hidden;}

#     /* B. MAIN BACKGROUND */
#     [data-testid="stAppViewContainer"] {
#         background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 228, 255) 90%);
#         font-family: 'Inter', sans-serif;
#     }

#     /* C. SIDEBAR STYLING (Dark Mode) */
#     section[data-testid="stSidebar"] {
#         background-color: #0F172A !important;
#         border-right: 1px solid #1E293B;
#     }

#     /* --- INPUT TEXT VISIBILITY FIX --- */
#     .stSelectbox div[data-baseweb="select"] > div,
#     .stNumberInput div[data-baseweb="input"] > div {
#         background-color: #1E293B !important;
#         border: 1px solid #475569 !important;
#         color: white !important;
#     }
#     input[type="number"], 
#     div[data-baseweb="select"] span, 
#     div[data-baseweb="select"] div {
#         color: #FFFFFF !important;
#         -webkit-text-fill-color: #FFFFFF !important;
#         caret-color: #FFFFFF !important;
#         font-weight: 600 !important;
#     }
#     ul[data-testid="stSelectboxVirtualDropdown"] {
#         background-color: #0F172A !important;
#     }
#     li[role="option"] div {
#         color: white !important;
#     }
    
#     /* Expander Headers (Dark) */
#     .streamlit-expanderHeader {
#         background-color: #1E293B !important;
#         color: #FFFFFF !important;
#         border: 1px solid #334155;
#         border-radius: 8px;
#     }
#     .streamlit-expanderHeader p, .streamlit-expanderHeader span, .streamlit-expanderHeader svg {
#         color: #FFFFFF !important;
#         fill: #FFFFFF !important;
#     }
    
#     /* Sidebar Labels */
#     section[data-testid="stSidebar"] label, 
#     section[data-testid="stSidebar"] h1, 
#     section[data-testid="stSidebar"] h2, 
#     section[data-testid="stSidebar"] p {
#         color: #94A3B8 !important;
#     }

#     /* D. NAVBAR STYLING */
#     .navbar {
#         background: rgba(255, 255, 255, 0.9);
#         backdrop-filter: blur(10px);
#         border-bottom: 1px solid rgba(255, 255, 255, 0.3);
#         padding: 15px 30px;
#         border-radius: 12px;
#         margin-bottom: 20px;
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
#     }
#     .navbar-brand {
#         font-size: 1.8rem;
#         font-weight: 800;
#         background: -webkit-linear-gradient(45deg, #2563EB, #1D4ED8);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#     }
#     .navbar-status {
#         background-color: #D1FAE5;
#         color: #065F46;
#         padding: 5px 12px;
#         border-radius: 20px;
#         font-size: 0.8rem;
#         font-weight: 600;
#         border: 1px solid #10B981;
#     }

#     /* E. GLASS CARDS */
#     .glass-card {
#         background: rgba(255, 255, 255, 0.85);
#         backdrop-filter: blur(12px);
#         border-radius: 16px;
#         border: 1px solid rgba(255, 255, 255, 0.6);
#         padding: 20px;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
#         margin-bottom: 15px;
#         transition: transform 0.3s ease;
#         min-height: 180px;
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#     }
#     .glass-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
#     }
#     .metric-label {
#         color: #64748B;
#         font-size: 0.75rem;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         margin-bottom: 5px;
#     }
#     .metric-value {
#         color: #0F172A;
#         font-size: 1.8rem;
#         font-weight: 800;
#         margin: 5px 0;
#         white-space: nowrap;
#     }

#     /* F. CUSTOM TABS */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: rgba(255,255,255,0.5);
#         padding: 10px;
#         border-radius: 12px;
#         margin-bottom: 20px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         background-color: transparent;
#         border: none;
#         font-weight: 600;
#     }
#     .stTabs [aria-selected="true"] {
#         background-color: white !important;
#         border-radius: 8px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#         color: #2563EB !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. LOAD ENGINE ---
# @st.cache_resource
# def load_engine():
#     try:
#         df = pd.read_csv("synthetic_workers_comp_data.csv")
#     except FileNotFoundError:
#         return None
    
#     X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'])
#     y = df['Settlement Payout']
    
#     categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
#     numeric_features = ['Wage Information', 'Attorney Aggressiveness']

#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('num', 'passthrough', numeric_features),
#             ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#         ])

#     model = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
#     ])
#     model.fit(X, y)
#     return model

# engine = load_engine()

# # --- 4. SIDEBAR (EXPANDERS CLOSED BY DEFAULT) ---
# with st.sidebar:
#     st.markdown("## ⚖️ Litigation Settlement")
#     st.markdown("<div style='color: #94A3B8; margin-bottom: 20px;'>Litigation Intelligence Suite v1.0</div>", unsafe_allow_html=True)
    
#     # CHANGED: expanded=False
#     with st.expander("👤 CLAIMANT PROFILE", expanded=False):
#         state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
#         wage = st.number_input("Weekly Wage ($)", value=900, step=50)

#     # CHANGED: expanded=False
#     with st.expander("🏥 MEDICAL PROFILE", expanded=False):
#         body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#         injury_nature = st.selectbox("Injury Type", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
#         medical_cat = st.radio("Treatment", ['PT/Conservative', 'Surgery'])
#         cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])

#     # CHANGED: expanded=False
#     with st.expander("⚖️ LITIGATION PROFILE", expanded=False):
#         attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#         aggressiveness = st.slider("Aggression Index", 1, 10, 5)

# # --- 5. LOGIC ---
# # if engine:
# #     input_data = pd.DataFrame({
# #         'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
# #         'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
# #         'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
# #     })
# #     predicted_val = engine.predict(input_data)[0]
# #     lower = predicted_val * 0.88
# #     upper = predicted_val * 1.12
# #     defense_cost = (45000 if state in ['New York', 'California'] else 15000) * (1.5 if aggressiveness > 7 else 1.0)
# #     total_risk = predicted_val + defense_cost
# #     savings = total_risk - predicted_val
# #     is_settle = savings > 0
# # --- 5. LOGIC (UPDATED WITH ROI CALCULATOR) ---
# if engine:
#     # 1. Create Input Data
#     input_data = pd.DataFrame({
#         'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
#         'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
#         'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
#     })

#     # 2. Get AI Prediction
#     predicted_val = engine.predict(input_data)[0]
#     lower = predicted_val * 0.88
#     upper = predicted_val * 1.12

#     # 3. Calculate Defense Costs (Cost to Fight)
#     # Base cost is higher in NY/CA. Aggressive attorneys increase cost by 50%.
#     defense_base = 45000 if state in ['New York', 'California'] else 15000
#     defense_multiplier = 1.5 if aggressiveness > 7 else 1.0
#     defense_cost = defense_base * defense_multiplier

#     # 4. Calculate Total Exposure (The "Walk Away" Cost)
#     # If we lose in court, we pay the Verdict + Our Lawyers
#     total_risk = predicted_val + defense_cost

#     # 5. Simulate Plaintiff Demand (The "Greedy Attorney" Logic)
#     # If Aggressiveness is High (8-10), they demand WAY more than the claim is worth.
#     # If Aggressiveness is Low, they demand near the fair value.
#     demand_multiplier = 1.0
#     if aggressiveness >= 8:
#         demand_multiplier = 2.5  # They want 2.5x value (Unreasonable)
#     elif aggressiveness >= 6:
#         demand_multiplier = 1.5  # They want 1.5x value (Pushy)
#     elif aggressiveness >= 4:
#         demand_multiplier = 1.1  # They want 10% extra (Standard)
    
#     plaintiff_demand = predicted_val * demand_multiplier

#     # 6. Calculate ROI / Savings
#     # Formula: (Cost to Fight) - (Cost to Pay Demand)
#     # If Savings is NEGATIVE, it means fighting is cheaper than paying their crazy demand.
#     savings = total_risk - plaintiff_demand
#     is_settle = savings > 0

# # --- 6. MAIN DASHBOARD ---
# st.markdown(f"""
#     <div class="navbar">
#         <div class="navbar-brand">Litigation Settlement</div>
#         <div style="display: flex; gap: 20px; align-items: center;">
#             <div style="color: #64748B; font-size: 0.9rem;"><b>Case ID:</b> #82910-X</div>
#             <div class="navbar-status">● LIVE ANALYSIS</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# c1, c2, c3, c4 = st.columns(4)

# with c1:
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Target Settlement</div>
#         <div class="metric-value">${predicted_val:,.0f}</div>
#         <div style="color: #64748B; font-size: 0.8rem;">Range: ${lower:,.0f} - ${upper:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Total Exposure</div>
#         <div class="metric-value">${total_risk:,.0f}</div>
#         <div style="color: #EF4444; font-size: 0.8rem;">Verdict + Defense Fees</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     rec_color = "#10B981" if is_settle else "#EF4444"
#     rec_text = "SETTLE NOW" if is_settle else "LITIGATE"
#     st.markdown(f"""
#     <div class="glass-card" style="border-bottom: 4px solid {rec_color}">
#         <div class="metric-label">AI Recommendation</div>
#         <div class="metric-value" style="color: {rec_color}">{rec_text}</div>
#         <div style="color: #64748B; font-size: 0.8rem;">ROI Positive</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c4:
#     risk_color = "#F59E0B" if aggressiveness > 7 else "#10B981"
#     risk_txt = "HIGH RISK" if aggressiveness > 7 else "STANDARD"
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Litigation Score</div>
#         <div class="metric-value" style="color: {risk_color}">{risk_txt}</div>
#         <div style="color: #64748B; font-size: 0.8rem;">Attorney Profile</div>
#     </div>
#     """, unsafe_allow_html=True)

# tab1, tab2 = st.tabs(["📈 STRATEGY & PROBABILITY", "💰 FINANCIAL WATERFALL"])

# with tab1:
#     col_L, col_R = st.columns([2, 1])
#     with col_L:
#         x_vals = np.linspace(predicted_val * 0.6, predicted_val * 1.4, 100)
#         y_vals = 1 / (1 + np.exp(-0.00005 * (x_vals - predicted_val * 0.95))) * 100
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=x_vals, y=y_vals, fill='tozeroy', line=dict(color='#2563EB', width=4), name='Acceptance'))
#         fig.add_vline(x=predicted_val, line_dash="dash", line_color="#64748B")
#         fig.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_title="Offer Amount ($)", yaxis_title="Probability (%)", hovermode="x unified")
#         st.plotly_chart(fig, use_container_width=True)
#     with col_R:
#         st.markdown(f"""
#         <div class="glass-card" style="background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%); min-height: 350px;">
#             <h4 style="margin-top:0; color: #1E293B;">💡 Strategic Insight</h4>
#             <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
#             The model has identified a <b>{int(savings/predicted_val*100) if predicted_val else 0}% savings opportunity</b> by settling early.
#             <br><br>
#             <b>Defense Cost Analysis:</b><br>
#             Jurisdiction: <span style="color:#2563EB"><b>{state}</b></span><br>
#             Est. Legal Fees: <span style="color:#EF4444"><b>${defense_cost:,.0f}</b></span>
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# with tab2:
#     base = predicted_val * 0.35
#     indemnity = predicted_val * 0.25
#     geo = predicted_val * 0.15 if state in ['New York', 'California'] else 0
#     att_premium = predicted_val * 0.20 if aggressiveness > 6 else 0
#     misc = predicted_val - (base + indemnity + geo + att_premium)
#     fig_waterfall = go.Figure(go.Waterfall(
#         orientation = "v",
#         measure = ["relative", "relative", "relative", "relative", "relative", "total"],
#         x = ["Base Medical", "Indemnity", "Jurisdiction", "Attorney Risk", "Misc", "Total"],
#         y = [base, indemnity, geo, att_premium, misc, predicted_val],
#         connector = {"line":{"color":"rgb(63, 63, 63)"}},
#         decreasing = {"marker":{"color":"#EF4444"}},
#         increasing = {"marker":{"color":"#2563EB"}},
#         totals = {"marker":{"color":"#1E293B"}}
#     ))
#     fig_waterfall.update_layout(height=450, title="Cost Driver Analysis", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
#     st.plotly_chart(fig_waterfall, use_container_width=True)


























# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# # --- 1. PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="ClaimSight AI | Enterprise",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. FIXED CSS STYLING (Dark Sidebar + Glass UI) ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

#     /* A. REMOVE DEFAULT PADDING */
#     .block-container {
#         padding-top: 1rem !important;
#         padding-bottom: 2rem !important;
#         max-width: 95% !important;
#     }
#     header {visibility: hidden;}

#     /* B. MAIN BACKGROUND */
#     [data-testid="stAppViewContainer"] {
#         background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 228, 255) 90%);
#         font-family: 'Inter', sans-serif;
#     }

#     /* C. SIDEBAR STYLING (Dark Mode) */
#     section[data-testid="stSidebar"] {
#         background-color: #0F172A !important;
#         border-right: 1px solid #1E293B;
#     }

#     /* --- INPUT TEXT VISIBILITY FIX --- */
#     .stSelectbox div[data-baseweb="select"] > div,
#     .stNumberInput div[data-baseweb="input"] > div {
#         background-color: #1E293B !important;
#         border: 1px solid #475569 !important;
#         color: white !important;
#     }
#     input[type="number"], 
#     div[data-baseweb="select"] span, 
#     div[data-baseweb="select"] div {
#         color: #FFFFFF !important;
#         -webkit-text-fill-color: #FFFFFF !important;
#         caret-color: #FFFFFF !important;
#         font-weight: 600 !important;
#     }
#     ul[data-testid="stSelectboxVirtualDropdown"] {
#         background-color: #0F172A !important;
#     }
#     li[role="option"] div {
#         color: white !important;
#     }
    
#     /* Expander Headers (Dark) */
#     .streamlit-expanderHeader {
#         background-color: #1E293B !important;
#         color: #FFFFFF !important;
#         border: 1px solid #334155;
#         border-radius: 8px;
#     }
#     .streamlit-expanderHeader p, .streamlit-expanderHeader span, .streamlit-expanderHeader svg {
#         color: #FFFFFF !important;
#         fill: #FFFFFF !important;
#     }
    
#     /* Sidebar Labels */
#     section[data-testid="stSidebar"] label, 
#     section[data-testid="stSidebar"] h1, 
#     section[data-testid="stSidebar"] h2, 
#     section[data-testid="stSidebar"] p {
#         color: #94A3B8 !important;
#     }

#     /* D. NAVBAR STYLING */
#     .navbar {
#         background: rgba(255, 255, 255, 0.9);
#         backdrop-filter: blur(10px);
#         border-bottom: 1px solid rgba(255, 255, 255, 0.3);
#         padding: 15px 30px;
#         border-radius: 12px;
#         margin-bottom: 20px;
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
#     }
#     .navbar-brand {
#         font-size: 1.8rem;
#         font-weight: 800;
#         background: -webkit-linear-gradient(45deg, #2563EB, #1D4ED8);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#     }
#     .navbar-status {
#         background-color: #D1FAE5;
#         color: #065F46;
#         padding: 5px 12px;
#         border-radius: 20px;
#         font-size: 0.8rem;
#         font-weight: 600;
#         border: 1px solid #10B981;
#     }

#     /* E. GLASS CARDS */
#     .glass-card {
#         background: rgba(255, 255, 255, 0.85);
#         backdrop-filter: blur(12px);
#         border-radius: 16px;
#         border: 1px solid rgba(255, 255, 255, 0.6);
#         padding: 20px;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
#         margin-bottom: 15px;
#         transition: transform 0.3s ease;
#         min-height: 180px;
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#     }
#     .glass-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
#     }
#     .metric-label {
#         color: #64748B;
#         font-size: 0.75rem;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         margin-bottom: 5px;
#     }
#     .metric-value {
#         color: #0F172A;
#         font-size: 1.8rem;
#         font-weight: 800;
#         margin: 5px 0;
#         white-space: nowrap;
#     }

#     /* F. CUSTOM TABS */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: rgba(255,255,255,0.5);
#         padding: 10px;
#         border-radius: 12px;
#         margin-bottom: 20px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         background-color: transparent;
#         border: none;
#         font-weight: 600;
#     }
#     .stTabs [aria-selected="true"] {
#         background-color: white !important;
#         border-radius: 8px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#         color: #2563EB !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. TRAIN DUAL MODELS (Cost & Time) ---
# @st.cache_resource
# def load_engines():
#     try:
#         df = pd.read_csv("synthetic_workers_comp_data.csv")
#     except FileNotFoundError:
#         # Fallback if data isn't generated yet
#         st.error("Error: 'synthetic_workers_comp_data.csv' not found. Please run the data generator script first.")
#         return None, None
    
#     # We now drop both Targets from the Features
#     X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Days_to_Settle', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'], errors='ignore')
    
#     # Target 1: Cost
#     y_cost = df['Settlement Payout']
#     # Target 2: Time
#     y_time = df['Days_to_Settle']
    
#     categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
#     numeric_features = ['Wage Information', 'Attorney Aggressiveness']

#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('num', 'passthrough', numeric_features),
#             ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#         ])

#     # Model for Cost
#     model_cost = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
#     ])
#     model_cost.fit(X, y_cost)
    
#     # Model for Time
#     model_time = Pipeline(steps=[
#         ('preprocessor', preprocessor),
#         ('regressor', GradientBoostingRegressor(n_estimators=200, random_state=42))
#     ])
#     model_time.fit(X, y_time)
    
#     return model_cost, model_time

# engine_cost, engine_time = load_engines()

# # --- 4. SIDEBAR INPUTS ---
# with st.sidebar:
#     st.markdown("## ⚖️ Litigation Settlement")
#     st.markdown("<div style='color: #94A3B8; margin-bottom: 20px;'>Litigation Intelligence Suite v4.0</div>", unsafe_allow_html=True)
    
#     with st.expander("👤 CLAIMANT PROFILE", expanded=False):
#         state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
#         wage = st.number_input("Weekly Wage ($)", value=900, step=50)

#     with st.expander("🏥 MEDICAL PROFILE", expanded=False):
#         body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#         injury_nature = st.selectbox("Injury Type", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
#         medical_cat = st.radio("Treatment", ['PT/Conservative', 'Surgery'])
#         cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])

#     with st.expander("⚖️ LITIGATION PROFILE", expanded=True):
#         attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#         aggressiveness = st.slider("Aggression Index", 1, 10, 5)
#         st.markdown("---")
#         # --- NEW INPUT FIELD FOR DEAL AMOUNT ---
#         claimant_demand = st.number_input("Claimant Demand / Deal ($)", value=0, step=1000, help="Enter the amount the claimant is asking for.")

# # --- 5. LOGIC ENGINE ---
# if engine_cost:
#     input_data = pd.DataFrame({
#         'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
#         'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
#         'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
#     })
    
#     # 1. Predictions
#     predicted_val = engine_cost.predict(input_data)[0]
#     predicted_days = engine_time.predict(input_data)[0]
#     predicted_months = predicted_days / 30
    
#     lower = predicted_val * 0.88
#     upper = predicted_val * 1.12

#     # 2. Defense Cost Calc
#     defense_base = 45000 if state in ['New York', 'California'] else 15000
#     defense_multiplier = 1.5 if aggressiveness > 7 else 1.0
#     defense_cost = defense_base * defense_multiplier

#     # 3. Total Exposure
#     total_risk = predicted_val + defense_cost

#     # 4. ROI Logic (Uses User Input if available)
#     if claimant_demand > 0:
#         active_demand = claimant_demand
#         is_simulated = False
#     else:
#         # Fallback to simulated demand based on aggression
#         demand_multiplier = 2.5 if aggressiveness >= 8 else (1.5 if aggressiveness >= 6 else 1.1)
#         active_demand = predicted_val * demand_multiplier
#         is_simulated = True
    
#     savings = total_risk - active_demand
#     is_settle = savings > 0

# # --- 6. MAIN DASHBOARD ---
# st.markdown(f"""
#     <div class="navbar">
#         <div class="navbar-brand">Litigation Settlement</div>
#         <div style="display: flex; gap: 20px; align-items: center;">
#             <div style="color: #64748B; font-size: 0.9rem;"><b>Case ID:</b> #82910-X</div>
#             <div class="navbar-status">● LIVE ANALYSIS</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # --- KPI ROW ---
# c1, c2, c3, c4 = st.columns(4)

# with c1:
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Target Settlement</div>
#         <div class="metric-value">${predicted_val:,.0f}</div>
#         <div style="color: #64748B; font-size: 0.8rem;">Range: ${lower:,.0f} - ${upper:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Est. Duration</div>
#         <div class="metric-value">{int(predicted_days):,} Days</div>
#         <div style="color: #64748B; font-size: 0.8rem;">~{predicted_months:.1f} Months to Close</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown(f"""
#     <div class="glass-card">
#         <div class="metric-label">Total Exposure</div>
#         <div class="metric-value">${total_risk:,.0f}</div>
#         <div style="color: #EF4444; font-size: 0.8rem;">Verdict + Defense Fees</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c4:
#     rec_color = "#10B981" if is_settle else "#EF4444"
#     rec_text = "SETTLE NOW" if is_settle else "LITIGATE"
    
#     roi_label = "ROI vs Deal" if not is_simulated else "ROI vs Demand"
    
#     st.markdown(f"""
#     <div class="glass-card" style="border-bottom: 4px solid {rec_color}">
#         <div class="metric-label">AI Recommendation</div>
#         <div class="metric-value" style="color: {rec_color}">{rec_text}</div>
#         <div style="color: #64748B; font-size: 0.8rem;">{roi_label}: ${savings:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# # --- TABS (Only one remaining) ---
# # We use st.container or just place the content directly below the KPIs if only one view is desired.
# # To keep the visual style of a distinct section, we use the single tab.
# tab1 = st.tabs(["📈 STRATEGY & PROBABILITY"])[0] 

# with tab1:
#     col_L, col_R = st.columns([2, 1])
#     with col_L:
#         # Probability Curve
#         x_vals = np.linspace(predicted_val * 0.6, predicted_val * 1.4, 100)
#         y_vals = 1 / (1 + np.exp(-0.00005 * (x_vals - predicted_val * 0.95))) * 100
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=x_vals, y=y_vals, fill='tozeroy', line=dict(color='#2563EB', width=4), name='Acceptance'))
#         fig.add_vline(x=predicted_val, line_dash="dash", line_color="#64748B")
#         fig.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_title="Offer Amount ($)", yaxis_title="Probability (%)", hovermode="x unified")
#         st.plotly_chart(fig, use_container_width=True)
    
#     with col_R:
#         # Dynamic Strategy Text
#         if is_settle:
#             strategy_color = "#166534" # Dark Green
#             bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%)"
#             title = "✅ Positive ROI Strategy"
#             conclusion = f"Settling now saves the company <b>${savings:,.0f}</b> and avoids a {int(predicted_months)}-month legal battle."
#         else:
#             strategy_color = "#991B1B" # Dark Red
#             bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #FEF2F2 100%)"
#             title = "🛡️ Negative ROI Alert"
#             conclusion = f"Do not pay. Their demand of <b>${active_demand:,.0f}</b> exceeds the cost to fight (<b>${total_risk:,.0f}</b>). Proceed to litigation."

#         st.markdown(f"""
#         <div class="glass-card" style="background: {bg_grad}; min-height: 350px;">
#             <h4 style="margin-top:0; color: {strategy_color};">{title}</h4>
#             <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
#             The claimant is asking for <b>${active_demand:,.0f}</b>.
#             <br><br>
#             <b>Defense Cost Analysis:</b><br>
#             Jurisdiction: <span style="color:#2563EB"><b>{state}</b></span><br>
#             Est. Legal Fees: <span style="color:#EF4444"><b>${defense_cost:,.0f}</b></span>
#             <br><br>
#             <b>Conclusion:</b> {conclusion}
#             </p>
#         </div>
#         """, unsafe_allow_html=True)













# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# # --- 1. PAGE CONFIG ---
# st.set_page_config(
#     page_title="ClaimSight AI | Enterprise",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. FIXED CSS STYLING ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

#     /* Global Layout */
#     .block-container {padding-top: 1rem !important; padding-bottom: 2rem !important; max-width: 95% !important;}
#     header {visibility: hidden;}
#     [data-testid="stAppViewContainer"] {
#         background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 228, 255) 90%);
#         font-family: 'Inter', sans-serif;
#     }

#     /* DARK SIDEBAR STYLING */
#     section[data-testid="stSidebar"] {background-color: #0F172A !important; border-right: 1px solid #1E293B;}
    
#     /* INPUT BOX VISIBILITY FIX */
#     .stSelectbox div[data-baseweb="select"] > div, .stNumberInput div[data-baseweb="input"] > div {
#         background-color: #1E293B !important; 
#         border: 1px solid #475569 !important; 
#         color: white !important;
#     }
#     input[type="number"], div[data-baseweb="select"] span, div[data-baseweb="select"] div {
#         color: #FFFFFF !important; 
#         -webkit-text-fill-color: #FFFFFF !important;
#         caret-color: #FFFFFF !important;
#         font-weight: 600 !important;
#     }
#     ul[data-testid="stSelectboxVirtualDropdown"] {background-color: #0F172A !important;}
#     li[role="option"] div {color: white !important;}

#     /* Expander Headers */
#     .streamlit-expanderHeader {background-color: #1E293B !important; color: #FFFFFF !important; border: 1px solid #334155; border-radius: 8px;}
#     .streamlit-expanderHeader p, .streamlit-expanderHeader span, .streamlit-expanderHeader svg {color: #FFFFFF !important; fill: #FFFFFF !important;}

#     /* Sidebar Labels */
#     section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] h2 {color: #94A3B8 !important;}

#     /* NAVBAR & CARDS */
#     .navbar {background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); padding: 15px 30px; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);}
#     .navbar-brand {font-size: 1.8rem; font-weight: 800; background: -webkit-linear-gradient(45deg, #2563EB, #1D4ED8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    
#     /* GLASS CARDS (With Hover Animation) */
#     .glass-card {
#         background: rgba(255, 255, 255, 0.85); 
#         backdrop-filter: blur(12px); 
#         border-radius: 16px; 
#         border: 1px solid rgba(255, 255, 255, 0.6); 
#         padding: 20px; 
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05); 
#         min-height: 180px; 
#         display: flex; 
#         flex-direction: column; 
#         justify-content: center;
#         transition: transform 0.3s ease, box-shadow 0.3s ease; 
#     }
#     .glass-card:hover {
#         transform: translateY(-5px); 
#         box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
#     }
#     .metric-label {color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;}
#     .metric-value {color: #0F172A; font-size: 1.8rem; font-weight: 800; white-space: nowrap;}
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. TRAIN DUAL MODELS ---
# @st.cache_resource
# def load_engines():
#     try:
#         df = pd.read_csv("synthetic_workers_comp_data.csv")
#     except FileNotFoundError: return None, None
    
#     X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Days_to_Settle', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'], errors='ignore')
#     y_cost = df['Settlement Payout']
#     y_time = df['Days_to_Settle']
    
#     categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
#     numeric_features = ['Wage Information', 'Attorney Aggressiveness']

#     preprocessor = ColumnTransformer(transformers=[
#         ('num', 'passthrough', numeric_features),
#         ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#     ])

#     model_cost = Pipeline(steps=[('prep', preprocessor), ('reg', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))])
#     model_cost.fit(X, y_cost)
    
#     model_time = Pipeline(steps=[('prep', preprocessor), ('reg', GradientBoostingRegressor(n_estimators=200, random_state=42))])
#     model_time.fit(X, y_time)
    
#     return model_cost, model_time

# engine_cost, engine_time = load_engines()

# # --- 4. SIDEBAR ---
# with st.sidebar:
#     st.markdown("## ⚖️ Litigation Settlement")
#     st.markdown("<div style='color: #94A3B8; margin-bottom: 20px;'>Litigation Intelligence Suite v5.0</div>", unsafe_allow_html=True)
    
#     with st.expander("👤 CLAIMANT PROFILE", expanded=False):
#         state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
#         wage = st.number_input("Weekly Wage ($)", value=900, step=50)

#     with st.expander("🏥 MEDICAL PROFILE", expanded=False):
#         body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#         injury_nature = st.selectbox("Injury Type", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
#         medical_cat = st.radio("Treatment", ['PT/Conservative', 'Surgery'])
#         cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])

#     with st.expander("⚖️ LITIGATION PROFILE", expanded=True):
#         attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#         aggressiveness = st.slider("Aggression Index", 1, 10, 5)
#         st.markdown("---")
#         claimant_demand = st.number_input("Claimant Demand / Deal ($)", value=0, step=1000, help="Enter the amount the claimant is asking for.")

# # --- 5. LOGIC ENGINE ---
# if engine_cost:
#     input_data = pd.DataFrame({
#         'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
#         'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
#         'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
#     })
    
#     # Predictions
#     predicted_val = engine_cost.predict(input_data)[0]
#     predicted_days = engine_time.predict(input_data)[0]
#     predicted_months = predicted_days / 30
    
#     lower = predicted_val * 0.88
#     upper = predicted_val * 1.12

#     # Defense Cost
#     defense_base = 45000 if state in ['New York', 'California'] else 15000
#     defense_multiplier = 1.5 if aggressiveness > 7 else 1.0
#     defense_cost = defense_base * defense_multiplier

#     # Total Exposure
#     total_risk = predicted_val + defense_cost

#     # ROI Logic
#     if claimant_demand > 0:
#         active_demand = claimant_demand
#         is_simulated = False
#     else:
#         demand_multiplier = 2.5 if aggressiveness >= 8 else (1.5 if aggressiveness >= 6 else 1.1)
#         active_demand = predicted_val * demand_multiplier
#         is_simulated = True
    
#     savings = total_risk - active_demand
#     is_settle = savings > 0

#     # Litigation Score Logic
#     if aggressiveness >= 8:
#         lit_score = "HIGH RISK"
#         lit_color = "#EF4444" 
#         gauge_val = 90
#     elif aggressiveness >= 5:
#         lit_score = "MEDIUM RISK"
#         lit_color = "#F59E0B" 
#         gauge_val = 60
#     else:
#         lit_score = "LOW RISK"
#         lit_color = "#10B981" 
#         gauge_val = 25

# # --- 6. MAIN DASHBOARD ---
# st.markdown(f"""
#     <div class="navbar">
#         <div class="navbar-brand">Litigation Settlement</div>
#         <div style="display: flex; gap: 20px; align-items: center;">
#             <div style="color: #64748B; font-size: 0.9rem;"><b>Case ID:</b> #82910-X</div>
#             <div class="navbar-status">● LIVE ANALYSIS</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # KPI ROW
# c1, c2, c3, c4 = st.columns(4)
# with c1:
#     st.markdown(f"""<div class="glass-card"><div class="metric-label">Target Settlement</div><div class="metric-value">${predicted_val:,.0f}</div><div style="color: #64748B; font-size: 0.8rem;">Range: ${lower:,.0f} - ${upper:,.0f}</div></div>""", unsafe_allow_html=True)
# with c2:
#     st.markdown(f"""<div class="glass-card"><div class="metric-label">Est. Duration</div><div class="metric-value">{int(predicted_days):,} Days</div><div style="color: #64748B; font-size: 0.8rem;">~{predicted_months:.1f} Months to Close</div></div>""", unsafe_allow_html=True)
# with c3:
#     st.markdown(f"""<div class="glass-card"><div class="metric-label">Total Exposure</div><div class="metric-value">${total_risk:,.0f}</div><div style="color: #EF4444; font-size: 0.8rem;">Verdict + Defense Fees</div></div>""", unsafe_allow_html=True)
# with c4:
#     rec_color = "#10B981" if is_settle else "#EF4444"
#     rec_text = "SETTLE NOW" if is_settle else "LITIGATE"
#     roi_label = "ROI vs Deal" if not is_simulated else "ROI vs Demand"
#     st.markdown(f"""<div class="glass-card" style="border-bottom: 4px solid {rec_color}"><div class="metric-label">AI Recommendation</div><div class="metric-value" style="color: {rec_color}">{rec_text}</div><div style="color: #64748B; font-size: 0.8rem;">{roi_label}: ${savings:,.0f}</div></div>""", unsafe_allow_html=True)

# # --- STRATEGY SECTION (Replaces Tabs) ---
# st.markdown("### 📊 Strategy & Risk Analysis")

# col_L, col_R = st.columns([1, 2])

# with col_L:
#     # GAUGE CHART WITH TEXT LABEL
#     st.markdown(f"##### 🛡️ Litigation Score")
#     fig_gauge = go.Figure(go.Indicator(
#         mode = "gauge", # Text only, no number
#         value = gauge_val,
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         gauge = {
#             'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
#             'bar': {'color': lit_color},
#             'bgcolor': "white",
#             'borderwidth': 2,
#             'bordercolor': "gray",
#             'steps': [
#                 {'range': [0, 40], 'color': "#D1FAE5"},
#                 {'range': [40, 75], 'color': "#FEF3C7"},
#                 {'range': [75, 100], 'color': "#FEE2E2"}],
#         }
#     ))
    
#     # Add Text Annotation in Center
#     fig_gauge.update_layout(
#         height=280, 
#         margin=dict(l=20, r=20, t=30, b=20), 
#         paper_bgcolor='rgba(0,0,0,0)',
#         annotations=[dict(x=0.5, y=0.25, text=lit_score, showarrow=False, font=dict(size=20, color=lit_color, weight="bold"))]
#     )
#     st.plotly_chart(fig_gauge, use_container_width=True)

# with col_R:
#     # BAR CHART
#     st.markdown(f"##### 🎯 Negotiation Success Probability")
    
#     low_offer = predicted_val * 0.85
#     target_offer = predicted_val
#     high_offer = predicted_val * 1.15
    
#     prob_low = 1 / (1 + np.exp(-0.00005 * (low_offer - predicted_val * 0.95))) * 100
#     prob_target = 1 / (1 + np.exp(-0.00005 * (target_offer - predicted_val * 0.95))) * 100
#     prob_high = 1 / (1 + np.exp(-0.00005 * (high_offer - predicted_val * 0.95))) * 100
    
#     fig_bar = go.Figure()
#     fig_bar.add_trace(go.Bar(
#         y=['Aggressive Offer', 'Fair Market Value', 'Overpayment'],
#         x=[prob_low, prob_target, prob_high],
#         orientation='h',
#         marker=dict(color=['#EF4444', '#3B82F6', '#10B981']),
#         text=[f"${low_offer:,.0f}<br>({int(prob_low)}% Chance)", 
#               f"${target_offer:,.0f}<br>({int(prob_target)}% Chance)", 
#               f"${high_offer:,.0f}<br>({int(prob_high)}% Chance)"],
#         textposition='auto',
#     ))
#     fig_bar.update_layout(
#         height=300,
#         xaxis_title="Probability of Acceptance (%)",
#         xaxis=dict(range=[0, 100]),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         margin=dict(l=20, r=20, t=30, b=20)
#     )
#     st.plotly_chart(fig_bar, use_container_width=True)

# # --- FINAL STRATEGY CARD ---
# if is_settle:
#     strategy_color = "#166534" # Dark Green
#     bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%)"
#     title = "✅ Positive ROI Strategy"
#     conclusion = f"Settling now saves the company <b>${savings:,.0f}</b> and avoids a {int(predicted_months)}-month legal battle."
# else:
#     strategy_color = "#991B1B" # Dark Red
#     bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #FEF2F2 100%)"
#     title = "🛡️ Negative ROI Alert"
#     conclusion = f"Do not pay. Their demand of <b>${active_demand:,.0f}</b> exceeds the cost to fight (<b>${total_risk:,.0f}</b>). Proceed to litigation."

# st.markdown(f"""
# <div class="glass-card" style="background: {bg_grad}; border-left: 5px solid {strategy_color};">
#     <h3 style="margin-top:0; color: {strategy_color};">{title}</h3>
#     <p style="color: #475569; font-size: 1rem; line-height: 1.6;">
#     The claimant is asking for <b>${active_demand:,.0f}</b>.
#     <br><br>
#     <b>Defense Cost Analysis:</b><br>
#     Jurisdiction: <span style="color:#2563EB"><b>{state}</b></span> (Est. Legal Fees: <span style="color:#EF4444"><b>${defense_cost:,.0f}</b></span>)
#     <br><br>
#     <b>Conclusion:</b> {conclusion}
#     </p>
# </div>
# """, unsafe_allow_html=True)

















#####3with gemini
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import model  # <--- IMPORTING YOUR BACKEND LOGIC

# # --- 1. PAGE CONFIG ---
# st.set_page_config(
#     page_title="Litigation Command Center",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. CSS STYLING (The Enterprise Look) ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
#     .stApp { background-color: #F8FAFC; font-family: 'Inter', sans-serif; }
    
#     /* Sidebar */
#     section[data-testid="stSidebar"] { background-color: #0F172A; border-right: 1px solid #334155; }
#     [data-testid="stSidebar"] * { color: #F1F5F9; }
    
#     /* Inputs */
#     .stSelectbox div[data-baseweb="select"] > div, .stNumberInput input {
#         background-color: #1E293B !important; color: white !important; border: 1px solid #475569;
#     }
    
#     /* Cards */
#     .glass-card {
#         background: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); min-height: 160px;
#     }
#     .metric-label { font-size: 0.8rem; color: #64748B; font-weight: 600; text-transform: uppercase; }
#     .metric-val { font-size: 1.8rem; color: #0F172A; font-weight: 800; margin: 5px 0; }
    
#     /* Drivers */
#     .driver-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #F1F5F9; }
#     .d-pos { color: #DC2626; font-weight: bold; }
#     .d-neg { color: #16A34A; font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. SIDEBAR INPUTS (A-F) ---
# with st.sidebar:
#     st.markdown("### ⚖️ Command Center v2")
#     with st.form("main_form"):
#         with st.expander("A. Litigation & Venue", expanded=True):
#             jurisdiction = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Illinois'])
#             win_rate = st.slider("Venue Win Rate", 0.0, 1.0, 0.45)
#             atty_firm = st.selectbox("Plaintiff Firm", ['Morgan & Morgan', 'Binder & Binder', 'Solo Practitioner'])
#             atty_score = st.slider("Attorney Score", 0, 100, 65)

#         with st.expander("B. Damages", expanded=False):
#             wage_loss = st.number_input("Wage Loss Exposure ($)", value=15000)
#             impairment = st.number_input("Impairment %", 0, 100, 15)
#             demand = st.number_input("Current Demand ($)", value=0)

#         with st.expander("C. Behavioral", expanded=False):
#             days_filed = st.number_input("Days Since Filed", value=180)
#             opioid = st.checkbox("Opioid History?")
#             shops = st.number_input("Provider Shops", 0, 10, 1)

#         with st.expander("D. Profile", expanded=False):
#             emp_stat = st.selectbox("Employment", ['Active', 'Terminated', 'Retired'])
#             ben_stat = st.selectbox("Benefit", ['TTD', 'PPD'])
#             msa = st.checkbox("MSA Flag?")

#         with st.expander("E. Medical", expanded=False):
#             comorb = st.selectbox("Comorbidity", ['None', 'Obesity', 'Diabetes'])
#             guides = st.selectbox("ODG Adherence", ['Within Guidelines', 'Exceeds Guidelines'])

#         with st.expander("F. Intel", expanded=False):
#             judge = st.selectbox("Judge", ['Pro-Defense', 'Neutral', 'Pro-Labor'])
#             atty_type = st.selectbox("Attorney Type", ['Early Settlement', 'Trial-Oriented'])

#         submitted = st.form_submit_button("RUN ANALYSIS")
#         if submitted: st.session_state['submitted'] = True

# # --- 4. MAIN DASHBOARD ---
# if st.session_state.get('submitted', False):
    
#     # 1. Package Data
#     inputs = {
#         "Jurisdiction": jurisdiction, "Venue_Win_Rate": win_rate, "Plaintiff_Attorney": atty_firm,
#         "Attorney_Score": atty_score, "Wage_Loss_Exposure": wage_loss, "Impairment_Rating": impairment,
#         "Future_Medical": 1, "Days_Since_Filed": days_filed, "Opioid_Indicator": 1 if opioid else 0,
#         "Provider_Shopping": shops, "Employment_Status": emp_stat, "Benefit_Status": ben_stat,
#         "MSA_Flag": 1 if msa else 0, "Comorbidities": comorb, "Guidelines_Adherence": guides,
#         "Judge_Propensity": judge, "Attorney_Tendency": atty_type, "Litigation_Propensity": atty_type,
#         "Demand_Amount": demand
#     }

#     # 2. CALL THE BACKEND (No logic here!)
#     res = model.predict_case(inputs)

#     # 3. RENDER UI
#     st.markdown("## 🛡️ Litigation Strategy Dashboard")
    
#     # KPI Row
#     c1, c2, c3, c4 = st.columns(4)
#     with c1:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Target Settlement</div><div class="metric-val">${res['prediction']:,.0f}</div><small>Range: ${res['range_low']:,.0f} - ${res['range_high']:,.0f}</small></div>""", unsafe_allow_html=True)
#     with c2:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Est. Duration</div><div class="metric-val">{res['days']} Days</div><small>~{res['months']:.1f} Months</small></div>""", unsafe_allow_html=True)
#     with c3:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Total Exposure</div><div class="metric-val">${res['exposure']:,.0f}</div><small style="color:#EF4444">Verdict + Defense ($ {res['defense_cost']:,.0f})</small></div>""", unsafe_allow_html=True)
#     with c4:
#         color = "#16A34A" if res['is_safe'] else "#DC2626"
#         st.markdown(f"""<div class="glass-card" style="border-bottom: 4px solid {color}"><div class="metric-label">Recommendation</div><div class="metric-val" style="color:{color}">{res['action']}</div><small>Savings: ${res['savings']:,.0f}</small></div>""", unsafe_allow_html=True)

#     # Charts & Explainability
#     st.markdown("### 📊 Risk & Explainability")
#     col_L, col_R = st.columns([1, 2])

#     with col_L:
#         # Gauge Chart
#         fig = go.Figure(go.Indicator(
#             mode="gauge", value=res['risk_score'],
#             gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#334155"},
#                    'steps': [{'range': [0, 50], 'color': "#D1FAE5"}, {'range': [50, 80], 'color': "#FEF3C7"}, {'range': [80, 100], 'color': "#FEE2E2"}]}
#         ))
#         fig.update_layout(height=250, margin=dict(t=30, b=30, l=30, r=30), paper_bgcolor='rgba(0,0,0,0)',
#                           annotations=[dict(text=res['risk_label'], x=0.5, y=0.25, showarrow=False, font=dict(size=20, weight="bold"))])
#         st.plotly_chart(fig, use_container_width=True)

#     with col_R:
#         # Explainability List
#         st.markdown("#### 🔍 Top Cost Drivers")
#         for name, val, dtype in res['drivers']:
#             color = "d-pos" if dtype == 'pos' else "d-neg"
#             sign = "+" if dtype == 'pos' else ""
#             st.markdown(f"""
#             <div class="driver-row">
#                 <span>{name}</span>
#                 <span class="{color}">{sign}${abs(val):,.0f}</span>
#             </div>
#             """, unsafe_allow_html=True)

# elif not st.session_state.get('submitted', False):
#     st.markdown("<div style='text-align:center; padding:50px; color:#64748B;'><h3>Waiting for Case Data...</h3><p>Enter details in the sidebar and click RUN ANALYSIS</p></div>", unsafe_allow_html=True)









# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import model  # Imports your backend logic

# # --- 1. PAGE CONFIG ---
# st.set_page_config(
#     page_title="Litigation Command Center",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. ADVANCED CSS STYLING ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
#     /* GLOBAL SETTINGS */
#     .stApp { background-color: #F8FAFC; font-family: 'Inter', sans-serif; }
    
#     /* --- SIDEBAR REDESIGN --- */
#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #020617 0%, #0F172A 100%);
#         border-right: 1px solid #1E293B;
#     }
    
#     .sidebar-title {
#         color: white; font-size: 1.5rem; font-weight: 800;
#         background: -webkit-linear-gradient(45deg, #60A5FA, #3B82F6);
#         -webkit-background-clip: text; -webkit-text-fill-color: transparent;
#         margin-bottom: 5px;
#     }
    
#     /* Expander Styling */
#     .streamlit-expanderHeader {
#         background: linear-gradient(90deg, #1E293B 0%, #0F172A 100%);
#         border: 1px solid #334155;
#         border-radius: 8px;
#         color: #F8FAFC !important;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .streamlit-expanderHeader:hover {
#         border-color: #3B82F6;
#         color: #60A5FA !important;
#     }
#     .streamlit-expanderHeader svg { fill: #94A3B8 !important; }
    
#     /* Input Fields */
#     .stSelectbox div[data-baseweb="select"] > div, 
#     .stNumberInput div[data-baseweb="input"] > div {
#         background-color: #020617 !important; 
#         border: 1px solid #334155 !important;
#         color: white !important;
#         border-radius: 6px;
#     }
#     /* Input Text Color Fix */
#     input[type="number"], div[data-baseweb="select"] span, div[data-baseweb="select"] div {
#         color: #E2E8F0 !important;
#         -webkit-text-fill-color: #E2E8F0 !important;
#         caret-color: #3B82F6 !important;
#     }
    
#     ul[data-testid="stSelectboxVirtualDropdown"] {
#         background-color: #0F172A !important;
#         border: 1px solid #334155;
#     }
#     li[role="option"] div { color: #F1F5F9 !important; }
    
#     [data-testid="stSidebar"] label {
#         color: #94A3B8 !important;
#         font-size: 0.75rem;
#         text-transform: uppercase;
#         letter-spacing: 0.5px;
#     }

#     /* Submit Button */
#     div.stButton > button {
#         background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
#         border: none;
#         color: white;
#         font-weight: 700;
#         padding: 12px;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
#         transition: transform 0.2s;
#     }
#     div.stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 15px rgba(37, 99, 235, 0.5);
#     }

#     /* --- GLASS CARDS (Main Area) --- */
#     .glass-card {
#         background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); min-height: 160px;
#         transition: transform 0.3s ease;
#     }
#     .metric-label { font-size: 0.75rem; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
#     .metric-val { font-size: 2rem; color: #0F172A; font-weight: 800; margin: 8px 0; }
    
#     /* Drivers Section */
#     .driver-container {
#         background-color: #F8FAFC;
#         border-radius: 8px;
#         padding: 15px;
#         border: 1px solid #E2E8F0;
#     }
#     .driver-row { 
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 12px 0; border-bottom: 1px solid #E2E8F0; font-size: 0.95rem; 
#     }
#     .d-pos { color: #DC2626; font-weight: 700; background: #FEF2F2; padding: 4px 10px; border-radius: 6px; }
#     .d-neg { color: #16A34A; font-weight: 700; background: #F0FDF4; padding: 4px 10px; border-radius: 6px; }
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. SIDEBAR INPUTS ---
# with st.sidebar:
#     st.markdown('<div class="sidebar-title">⚡ CLAIM SIGHT</div>', unsafe_allow_html=True)
#     st.markdown("<div style='color: #64748B; margin-bottom: 25px; font-size: 0.8rem;'>AI Litigation Intelligence Suite v2.2</div>", unsafe_allow_html=True)
    
#     with st.form("main_form"):
#         with st.expander("🏛️ A. Litigation & Venue", expanded=True):
#             jurisdiction = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Illinois'])
#             win_rate = st.slider("Venue Win Rate (%)", 0.0, 1.0, 0.45)
#             atty_firm = st.selectbox("Plaintiff Firm", ['Morgan & Morgan', 'Binder & Binder', 'Solo Practitioner'])
#             atty_score = st.slider("Attorney Score", 0, 100, 65)

#         with st.expander("💰 B. Economic Damages", expanded=False):
#             wage_loss = st.number_input("Wage Loss Exposure ($)", value=15000)
#             impairment = st.number_input("Impairment Rating (%)", 0, 100, 15)
#             demand = st.number_input("Current Demand ($)", value=0)

#         with st.expander("🕵️ C. Behavioral Indicators", expanded=False):
#             days_filed = st.number_input("Days Since Filed", value=180)
#             opioid = st.checkbox("Opioid History Flag")
#             shops = st.number_input("Provider Shopping Count", 0, 10, 1)

#         with st.expander("👤 D. Claimant Profile", expanded=False):
#             emp_stat = st.selectbox("Employment", ['Active', 'Terminated', 'Retired'])
#             ben_stat = st.selectbox("Benefit Type", ['TTD', 'PPD'])
#             msa = st.checkbox("Medicare Set-Aside (MSA)")

#         with st.expander("🏥 E. Medical Complexity", expanded=False):
#             comorb = st.selectbox("Comorbidities", ['None', 'Obesity', 'Diabetes'])
#             guides = st.selectbox("ODG Guidelines", ['Within Guidelines', 'Exceeds Guidelines'])

#         with st.expander("⚖️ F. Legal Intelligence", expanded=False):
#             judge = st.selectbox("Judge Propensity", ['Pro-Defense', 'Neutral', 'Pro-Labor'])
#             atty_type = st.selectbox("Attorney Strategy", ['Early Settlement', 'Trial-Oriented'])

#         st.markdown("<br>", unsafe_allow_html=True)
#         submitted = st.form_submit_button("🚀 RUN ANALYSIS")
#         if submitted: st.session_state['submitted'] = True

# # --- 4. MAIN DASHBOARD ---
# if st.session_state.get('submitted', False):
    
#     # 1. Package Data
#     inputs = {
#         "Jurisdiction": jurisdiction, "Venue_Win_Rate": win_rate, "Plaintiff_Attorney": atty_firm,
#         "Attorney_Score": atty_score, "Wage_Loss_Exposure": wage_loss, "Impairment_Rating": impairment,
#         "Future_Medical": 1, "Days_Since_Filed": days_filed, "Opioid_Indicator": 1 if opioid else 0,
#         "Provider_Shopping": shops, "Employment_Status": emp_stat, "Benefit_Status": ben_stat,
#         "MSA_Flag": 1 if msa else 0, "Comorbidities": comorb, "Guidelines_Adherence": guides,
#         "Judge_Propensity": judge, "Attorney_Tendency": atty_type, 
#         "Demand_Amount": demand
#     }

#     # 2. CALL THE BACKEND
#     res = model.predict_case(inputs)

#     # 3. HEADER
#     st.markdown(f"## 🛡️ Strategy: <span style='color:{'#16A34A' if res['is_safe'] else '#DC2626'}'>{res['action']}</span>", unsafe_allow_html=True)
#     st.markdown("---")
    
#     # 4. KPI ROW
#     c1, c2, c3, c4 = st.columns(4)
#     with c1:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Target Settlement</div><div class="metric-val">${res['prediction']:,.0f}</div><small style="color:#64748B">Range: ${res['range_low']:,.0f} - ${res['range_high']:,.0f}</small></div>""", unsafe_allow_html=True)
#     with c2:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Est. Duration</div><div class="metric-val">{res['days']} Days</div><small style="color:#64748B">~{res['months']:.1f} Months to Close</small></div>""", unsafe_allow_html=True)
#     with c3:
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Total Exposure</div><div class="metric-val">${res['exposure']:,.0f}</div><small style="color:#EF4444">Verdict + Defense ($ {res['defense_cost']:,.0f})</small></div>""", unsafe_allow_html=True)
#     with c4:
#         # Trust Score Logic
#         trust = 95 if days_filed > 90 else 70
#         trust_color = "#16A34A" if trust > 80 else "#F59E0B"
#         st.markdown(f"""<div class="glass-card"><div class="metric-label">Model Confidence</div><div class="metric-val" style="color:{trust_color}">{trust}%</div><small style="color:#64748B">Based on Data Completeness</small></div>""", unsafe_allow_html=True)

#     # 5. CHARTS & DRIVERS
#     st.markdown("### 📊 Risk & Explainability")
#     col_L, col_R = st.columns([1, 2])

#     with col_L:
#         # Gauge Chart (Risk)
#         fig_gauge = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=res['risk_score'],
#             number={'font': {'size': 40, 'color': "#1E293B"}},
#             gauge={
#                 'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#334155"},
#                 'bar': {'color': "#1E293B", 'thickness': 0.25},
#                 'bgcolor': "white",
#                 'borderwidth': 2,
#                 'bordercolor': "#E2E8F0",
#                 'steps': [
#                     {'range': [0, 40], 'color': "#3B82F6"},
#                     {'range': [40, 75], 'color': "#F59E0B"},
#                     {'range': [75, 100], 'color': "#EF4444"}],
#             }
#         ))
#         fig_gauge.update_layout(height=250, margin=dict(t=30, b=30, l=30, r=30), paper_bgcolor='rgba(0,0,0,0)',
#                           annotations=[dict(text=res['risk_label'], x=0.5, y=0.15, showarrow=False, font=dict(size=18, weight="bold", color="#64748B"))])
#         st.plotly_chart(fig_gauge, use_container_width=True)

#     with col_R:
#         # Drivers List
#         st.markdown("#### 🔍 Top Cost Drivers")
        
#         display_drivers = res['drivers']
#         if not display_drivers:
#             display_drivers = [("Standard Claim Base", res['prediction']*0.1, "pos"), ("Venue Adjustment", res['prediction']*0.05, "neg")]

#         st.markdown('<div class="driver-container">', unsafe_allow_html=True)
#         for name, val, dtype in display_drivers:
#             color = "d-pos" if dtype == 'pos' else "d-neg"
#             sign = "+" if dtype == 'pos' else ""
#             st.markdown(f"""
#             <div class="driver-row">
#                 <span style="font-weight:500; color:#334155;">{name}</span>
#                 <span class="{color}">{sign}${abs(val):,.0f}</span>
#             </div>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     # --- ZOPA BELL CURVE (ADDED HERE) ---
#     st.markdown("#### 📉 Safe Settlement Zone (ZOPA)")
    
#     mu = res['prediction']
#     sigma = mu * 0.12 
#     x = np.linspace(mu - 3*sigma, mu + 3*sigma, 200)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
#     fig_zopa = go.Figure()
#     # Full Curve
#     fig_zopa.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#64748B', width=2), fill='tozeroy', fillcolor='rgba(203, 213, 225, 0.3)', name='Distribution'))
    
#     # Safe Zone
#     x_safe = np.linspace(res['range_low'], res['range_high'], 100)
#     y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
#     fig_zopa.add_trace(go.Scatter(x=x_safe, y=y_safe, mode='lines', line=dict(width=0), fill='tozeroy', fillcolor='rgba(22, 163, 74, 0.6)', name='Safe Zone'))
    
#     # Target Line
#     fig_zopa.add_vline(x=mu, line_dash="dash", line_color="#0F172A", annotation_text="Target")

#     fig_zopa.update_layout(
#         height=300, showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         margin=dict(l=20, r=20, t=20, b=20), 
#         xaxis=dict(showgrid=False, title="Settlement Amount ($)"), 
#         yaxis=dict(showgrid=False, showticklabels=False)
#     )
#     st.plotly_chart(fig_zopa, use_container_width=True)

# elif not st.session_state.get('submitted', False):
#     st.markdown("<div style='text-align:center; padding:50px; color:#64748B;'><h3>Waiting for Case Data...</h3><p>Enter details in the sidebar and click RUN ANALYSIS</p></div>", unsafe_allow_html=True)










#########full react
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import model

# # === PAGE CONFIG ===
# st.set_page_config(
#     page_title="Litigation Command Center",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
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
    
#     /* === SIDEBAR PREMIUM STYLING === */
#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #010409 0%, #0a0e27 50%, #1a1f3a 100%);
#         border-right: 3px solid #3b82f6;
#         box-shadow: 8px 0 40px rgba(59, 130, 246, 0.2);
#     }
    
#     section[data-testid="stSidebar"] > div > div:first-child {
#         padding-top: 30px;
#     }
    
#     [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
#         color: #fff !important;
#         font-weight: 800;
#         background: linear-gradient(135deg, #60a5fa, #3b82f6, #1e40af);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         font-family: 'Playfair Display', serif;
#         letter-spacing: 1px;
#     }
    
#     [data-testid="stSidebar"] label {
#         color: #cbd5e1 !important;
#         font-size: 0.7rem !important;
#         text-transform: uppercase !important;
#         letter-spacing: 1.2px !important;
#         font-weight: 700 !important;
#     }
    
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
#         border-radius: 8px !important;
#     }
    
#     li[role="option"] {
#         color: #e2e8f0 !important;
#     }
    
#     li[role="option"]:hover {
#         background: rgba(59, 130, 246, 0.25) !important;
#     }
    
#     .streamlit-expanderHeader {
#         background: linear-gradient(90deg, #1e293b 0%, #0a0e27 100%) !important;
#         border: 1.5px solid #334155 !important;
#         border-radius: 10px !important;
#         color: #e2e8f0 !important;
#         font-weight: 700 !important;
#         padding: 12px !important;
#         transition: all 0.3s ease;
#     }
    
#     .streamlit-expanderHeader:hover {
#         border-color: #3b82f6 !important;
#         background: linear-gradient(90deg, #1e293b 0%, #1e3a8a 100%) !important;
#         box-shadow: 0 0 15px rgba(59, 130, 246, 0.2) !important;
#     }
    
#     .streamlit-expanderHeader svg {
#         fill: #60a5fa !important;
#     }
    
#     .stCheckbox div[role="checkbox"] {
#         border: 2px solid #475569 !important;
#         border-radius: 6px !important;
#         background: #1e293b !important;
#     }
    
#     .stCheckbox div[role="checkbox"]:hover {
#         border-color: #3b82f6 !important;
#     }
    
#     div.stButton > button {
#         background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%);
#         border: none;
#         color: white;
#         font-weight: 800;
#         font-size: 0.95rem;
#         padding: 14px 24px;
#         text-transform: uppercase;
#         letter-spacing: 1.2px;
#         width: 100%;
#         border-radius: 10px;
#         box-shadow: 0 8px 24px rgba(37, 99, 235, 0.35);
#         transition: all 0.3s ease;
#         margin-top: 15px;
#     }
    
#     div.stButton > button:hover {
#         transform: translateY(-3px);
#         box-shadow: 0 12px 36px rgba(37, 99, 235, 0.5);
#         background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%);
#     }
    
#     .header-section {
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px solid #3b82f6;
#         border-radius: 16px;
#         padding: 30px;
#         margin-bottom: 25px;
#         box-shadow: 0 12px 40px rgba(59, 130, 246, 0.15);
#     }
    
#     .header-title {
#         font-family: 'Playfair Display', serif;
#         font-size: 2.8rem;
#         font-weight: 700;
#         background: linear-gradient(135deg, #60a5fa, #3b82f6, #1e40af);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 10px;
#         letter-spacing: 1px;
#     }
    
#     .header-subtitle {
#         color: #cbd5e1;
#         font-size: 1rem;
#         font-weight: 400;
#     }
    
#     .kpi-card {
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px solid #334155;
#         border-radius: 14px;
#         padding: 24px;
#         min-height: 180px;
#         display: flex;
#         flex-direction: column;
#         justify-content: space-between;
#         transition: all 0.3s ease;
#         box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
#     }
    
#     .kpi-card:hover {
#         border-color: #3b82f6;
#         box-shadow: 0 16px 40px rgba(59, 130, 246, 0.25);
#         transform: translateY(-8px);
#         background: linear-gradient(135deg, #1e293b 0%, #1e3a8a 100%);
#     }
    
#     .kpi-label {
#         font-size: 0.75rem;
#         color: #94a3b8;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1.5px;
#         margin-bottom: 8px;
#     }
    
#     .kpi-value {
#         font-size: 2.2rem;
#         color: #f1f5f9;
#         font-weight: 800;
#         margin: 8px 0;
#         font-family: 'Playfair Display', serif;
#         letter-spacing: 1px;
#     }
    
#     .kpi-subtext {
#         font-size: 0.85rem;
#         color: #cbd5e1;
#         margin-top: auto;
#         font-weight: 500;
#     }
    
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
    
#     .success-box {
#         background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%);
#         border-left: 5px solid #16a34a;
#         border-radius: 10px;
#         padding: 16px;
#         margin: 12px 0;
#         color: #bbf7d0;
#         font-weight: 600;
#         box-shadow: 0 8px 24px rgba(22, 163, 74, 0.15);
#     }
    
#     .warning-box {
#         background: linear-gradient(135deg, #92400e 0%, #a16207 100%);
#         border-left: 5px solid #f59e0b;
#         border-radius: 10px;
#         padding: 16px;
#         margin: 12px 0;
#         color: #fcd34d;
#         font-weight: 600;
#         box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15);
#     }
    
#     .section-header {
#         font-size: 1.6rem;
#         font-weight: 700;
#         color: #f1f5f9;
#         margin: 28px 0 18px 0;
#         padding-bottom: 10px;
#         border-bottom: 2px solid #3b82f6;
#         font-family: 'Playfair Display', serif;
#         letter-spacing: 0.5px;
#     }
    
#     .driver-item {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         padding: 14px 16px;
#         background: linear-gradient(90deg, #1e293b 0%, #0a0e27 100%);
#         border: 1px solid #334155;
#         border-radius: 10px;
#         margin-bottom: 10px;
#         transition: all 0.3s ease;
#     }
    
#     .driver-item:hover {
#         border-color: #3b82f6;
#         box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
#     }
    
#     .driver-name {
#         color: #cbd5e1;
#         font-weight: 600;
#         flex: 1;
#     }
    
#     .driver-pos {
#         color: #fecaca;
#         font-weight: 800;
#         background: linear-gradient(135deg, #7f1d1d, #6b2121);
#         padding: 6px 12px;
#         border-radius: 6px;
#         font-size: 0.9rem;
#         box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
#     }
    
#     .driver-neg {
#         color: #bbf7d0;
#         font-weight: 800;
#         background: linear-gradient(135deg, #166534, #1b7a3a);
#         padding: 6px 12px;
#         border-radius: 6px;
#         font-size: 0.9rem;
#         box-shadow: 0 4px 12px rgba(22, 163, 74, 0.2);
#     }
    
#     .blank-state {
#         text-align: center;
#         padding: 80px 20px;
#         background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%);
#         border: 2px dashed #334155;
#         border-radius: 16px;
#         margin-top: 40px;
#     }
    
#     .blank-state h2 {
#         color: #60a5fa;
#         font-family: 'Playfair Display', serif;
#         font-size: 2rem;
#         margin-bottom: 15px;
#     }
    
#     .blank-state p {
#         color: #94a3b8;
#         font-size: 1.1rem;
#     }
    
#     header { visibility: hidden; }
#     footer { visibility: hidden; }
#     #MainMenu { visibility: hidden; }
    
#     </style>
# """, unsafe_allow_html=True)

# # === INITIALIZE SESSION STATE ===
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False

# # === SIDEBAR FORM ===
# with st.sidebar:
#     st.markdown("### ⚖️ COMMAND CENTER")
#     st.markdown("<p style='color: #60a5fa; font-size: 0.85rem; font-weight: 600; letter-spacing: 1px;'>LITIGATION INTELLIGENCE v4.0</p>", unsafe_allow_html=True)
#     st.markdown("---")
    
#     with st.form("litigation_form"):
#         with st.expander("🏛️ A. Litigation & Exposure", expanded=True):
#             jurisdiction = st.selectbox("Jurisdiction", 
#                 ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'],
#                 help="Select jurisdiction where case is filed")
#             venue_win_rate = st.slider("Defense Win Rate in Venue", 0.0, 1.0, 0.45, 0.05,
#                 help="Historical defense win rate in this jurisdiction")
#             attorney_firm = st.selectbox("Opposing Counsel",
#                 ['Morgan & Morgan', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner', 'Medium Firm'])
#             attorney_score = st.slider("Attorney Aggressiveness (0-100)", 0, 100, 65,
#                 help="0=Passive, 100=Highly Aggressive")
#             provider_type = st.selectbox("Primary Provider",
#                 ['PT', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Chiropractor'])

#         with st.expander("💰 B. Economic Damages", expanded=False):
#             wage_loss = st.number_input("Wage Loss Exposure ($)", 5000, 500000, 25000, 1000)
#             impairment = st.slider("Permanent Impairment (%)", 0, 100, 15)
#             medical_trajectory = st.selectbox("Medical Cost Trajectory",
#                 ['Low', 'Moderate', 'High', 'Escalating'])
#             future_medical = st.checkbox("Future Medical Exposure?", value=True)
#             demand = st.number_input("Plaintiff Demand ($) [0=Auto-simulate]", 0, 2000000, 0, 5000)

#         with st.expander("📊 C. Behavioral Progression", expanded=False):
#             days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180, 10)
#             days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150, 10)
#             treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90, 10)
#             opioid = st.checkbox("Opioid Prescription Indicator?")
#             provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)

#         with st.expander("👤 D. Claimant Profile", expanded=False):
#             employment = st.selectbox("Employment Status",
#                 ['Active', 'Terminated', 'Retired', 'Leave of Absence'])
#             benefit = st.selectbox("Benefit Status",
#                 ['TTD (Total Temporary Disability)', 'PPD (Permanent Partial Disability)', 'Medical Only'])
#             msa = st.checkbox("Medicare Set-Aside (MSA) Required?")

#         with st.expander("🏥 E. Medical Profile", expanded=False):
#             comorbidity = st.selectbox("Comorbidities",
#                 ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions'])
#             odg = st.selectbox("ODG Guidelines Adherence",
#                 ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds'])

#         with st.expander("📋 F. Litigation Intelligence", expanded=False):
#             attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55, 0.05)
#             attorney_type = st.selectbox("Attorney Settlement Tendency",
#                 ['Early Settlement', 'Balanced', 'Trial-Oriented'])
#             judge = st.selectbox("Judge Propensity (if assigned)",
#                 ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned'])

#         st.markdown("---")
#         submitted = st.form_submit_button("🚀 RUN ANALYSIS", use_container_width=True)
#         if submitted:
#             st.session_state.submitted = True

# # === BLANK STATE ===
# if not st.session_state.submitted:
#     st.markdown("""
#         <div class='blank-state'>
#             <h2>⏳ Ready to Analyze</h2>
#             <p>Enter claim details in the left panel and click <b>RUN ANALYSIS</b> to generate predictions</p>
#         </div>
#     """, unsafe_allow_html=True)

# # === DASHBOARD ===
# else:
#     inputs = {
#         "Jurisdiction": jurisdiction,
#         "Venue_Win_Rate": venue_win_rate,
#         "Plaintiff_Attorney": attorney_firm,
#         "Attorney_Score": attorney_score,
#         "Provider_Type": provider_type,
#         "Wage_Loss_Exposure": wage_loss,
#         "Impairment_Rating": impairment,
#         "Medical_Trajectory": medical_trajectory,
#         "Future_Medical": 1 if future_medical else 0,
#         "Demand_Amount": demand,
#         "Days_Since_Filed": days_filed,
#         "Days_Attorney_Engaged": days_attorney,
#         "Treatment_Duration": treatment_duration,
#         "Opioid_Indicator": 1 if opioid else 0,
#         "Provider_Shopping": provider_shopping,
#         "Employment_Status": employment,
#         "Benefit_Status": benefit,
#         "MSA_Flag": 1 if msa else 0,
#         "Comorbidities": comorbidity,
#         "Guidelines_Adherence": odg,
#         "Attorney_Win_Rate": attorney_winrate,
#         "Attorney_Tendency": attorney_type,
#         "Judge_Propensity": judge
#     }
    
#     res = model.predict_case(inputs)
    
#     # === HEADER ===
#     rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
#     st.markdown(f"""
#         <div class='header-section'>
#             <div class='header-title'>{rec_emoji} {res['action']}</div>
#             <div class='header-subtitle'>{res['action_desc']} • Jurisdiction: <b>{jurisdiction}</b> • Risk Level: <b>{res['risk_label']}</b></div>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # === KPI ROW ===
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
#                 <div class='kpi-subtext'>≈ {res['months']:.1f} months to close</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col3:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>📊 Total Exposure</div>
#                 <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Verdict + Defense (${res['defense_cost']/1000:.0f}K)</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col4:
#         savings_text = f"${res['savings']/1000:.0f}K"
#         savings_label = "SETTLEMENT ✓" if res['savings'] > 0 else "LITIGATION ✓"
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>💰 ROI Impact</div>
#                 <div class='kpi-value' style='color: {"#16a34a" if res['savings'] > 0 else "#dc2626"};'>{savings_text}</div>
#                 <div class='kpi-subtext'>{savings_label}</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === RISK ALERTS ===
#     st.markdown("<div class='section-header'>🚨 Critical Risk Assessment</div>", unsafe_allow_html=True)
    
#     alert_cols = st.columns(2)
#     with alert_cols[0]:
#         if attorney_score > 80:
#             st.markdown("<div class='alert-box'>🔥 HIGH-AGGRESSION ATTORNEY<br>History of trial escalation. Expect adversarial discovery & extended litigation.</div>", unsafe_allow_html=True)
#         if venue_win_rate < 0.40:
#             st.markdown("<div class='alert-box'>⚖️ UNFAVORABLE VENUE<br>Defense win rate <40%. Jury pool bias and judge predisposition present.</div>", unsafe_allow_html=True)
#         if days_filed > 365:
#             st.markdown("<div class='alert-box'>📅 STALE CLAIM<br>>12 months since filing. Extended exposure. Settlement window closing.</div>", unsafe_allow_html=True)
    
#     with alert_cols[1]:
#         if employment == 'Terminated':
#             st.markdown("<div class='alert-box'>😠 TERMINATED EMPLOYEE<br>Higher emotional damages. Recommend early settlement window strategy.</div>", unsafe_allow_html=True)
#         if opioid:
#             st.markdown("<div class='alert-box'>💊 OPIOID INDICATOR<br>Increased settlement floor due to addiction/dependency narratives.</div>", unsafe_allow_html=True)
#         if impairment > 20:
#             st.markdown("<div class='alert-box'>⚕️ HIGH IMPAIRMENT<br>Permanent injury claim. Non-economic damages baseline raised.</div>", unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === STRATEGIC RECOMMENDATION ===
#     st.markdown("<div class='section-header'>🎯 Recommended Strategy</div>", unsafe_allow_html=True)
    
#     if res['action'] == 'SETTLE':
#         st.markdown(f"""
#             <div class='success-box'>
#             <b>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
#             Financial analysis shows settlement is economically superior. Total litigation exposure 
#             (<b>${res['exposure']:,.0f}</b>) exceeds plaintiff recovery (<b>${res['demand']:,.0f}</b>).<br><br>
#             <b>📋 Action Plan:</b><br>
#             • Initiate negotiations within <b>7-10 days</b><br>
#             • Opening offer: <b>${res['range_low']:,.0f} – ${int(res['prediction']*0.95):,.0f}</b><br>
#             • Settlement ceiling: <b>${res['range_high']:,.0f}</b><br>
#             • Model confidence: <b>89%</b>
#             </div>
#         """, unsafe_allow_html=True)
#     elif res['action'] == 'LITIGATE':
#         st.markdown(f"""
#             <div class='alert-box'>
#             <b>⚔️ PROCEED TO LITIGATION</b><br><br>
#             Plaintiff demand (<b>${res['demand']:,.0f}</b>) significantly exceeds exposure cost. 
#             Trial is economically justified.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • Prepare for trial timeline: <b>{res['days']} days</b><br>
#             • Expected defense costs: <b>${res['defense_cost']:,.0f}</b><br>
#             • Anticipated verdict: <b>${res['prediction']:,.0f}</b><br>
#             • Do not settle above: <b>${int(res['exposure']*0.9):,.0f}</b>
#             </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#             <div class='warning-box'>
#             <b>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
#             Borderline case requiring careful analysis. Settlement vs litigation economics nearly equivalent.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • Conduct Independent Medical Exam (IME)<br>
#             • Test settlement at: <b>${int(res['prediction']*0.85):,.0f}</b><br>
#             • Monitor demand trajectory & attorney behavior<br>
#             • Re-evaluate quarterly
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === COST DRIVERS ===
#     st.markdown("<div class='section-header'>📈 Settlement Drivers Analysis</div>", unsafe_allow_html=True)
    
#     driver_cols = st.columns(2)
    
#     with driver_cols[0]:
#         st.markdown("<b style='color: #fecaca; font-size: 1.1rem;'>↑ Increasing Pressure (Positive Drivers)</b>")
#         pos_drivers = [d for d in res['drivers'] if d[2] == 'pos']
#         for name, val, _ in pos_drivers[:4]:
#             st.markdown(f"""
#                 <div class='driver-item'>
#                     <span class='driver-name'>{name}</span>
#                     <span class='driver-pos'>+${val:,.0f}</span>
#                 </div>
#             """, unsafe_allow_html=True)
    
#     with driver_cols[1]:
#         st.markdown("<b style='color: #bbf7d0; font-size: 1.1rem;'>↓ Defense Advantage (Negative Drivers)</b>")
#         neg_drivers = [d for d in res['drivers'] if d[2] == 'neg']
#         if neg_drivers:
#             for name, val, _ in neg_drivers[:4]:
#                 st.markdown(f"""
#                     <div class='driver-item'>
#                         <span class='driver-name'>{name}</span>
#                         <span class='driver-neg'>−${abs(val):,.0f}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#         else:
#             st.markdown("<div style='color: #94a3b8; padding: 14px; text-align: center;'><i>No mitigating factors identified</i></div>", unsafe_allow_html=True)
    
#     st.markdown("")
    
#     # === VISUALIZATIONS ===
#     st.markdown("<div class='section-header'>📊 Predictive Analytics</div>", unsafe_allow_html=True)
    
#     viz_cols = st.columns(2)
    
#     with viz_cols[0]:
#         # Gauge Chart
#         fig_gauge = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=int(res['prediction']),
#             number={'font': {'size': 30, 'color': "#e2e8f0"}, 'prefix': "$", 'suffix': "K"},
#             domain={'x': [0, 1], 'y': [0, 1]},
#             gauge={
#                 'axis': {'range': [0, int(res['range_high']*1.3)], 'tickwidth': 1, 'tickcolor': "#334155"},
#                 'bar': {'color': "#3b82f6", 'thickness': 0.25},
#                 'bgcolor': "#0a0e27",
#                 'borderwidth': 2,
#                 'bordercolor': "#334155",
#                 'steps': [
#                     {'range': [0, res['range_low']], 'color': "#1e3a8a"},
#                     {'range': [res['range_low'], res['range_high']], 'color': "#1e40af"},
#                     {'range': [res['range_high'], int(res['range_high']*1.3)], 'color': "#7f1d1d"}
#                 ],
#             }
#         ))
#         fig_gauge.update_layout(
#             height=300,
#             margin=dict(l=20, r=20, t=20, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             font=dict(color='#e2e8f0', family='Poppins'))






















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
    
#     # === ZOPA CURVE ===
#     st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
#     mu = res['prediction']
#     sigma = mu * 0.12
#     x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
#     fig_zopa = go.Figure()
    
#     # Full distribution curve
#     fig_zopa.add_trace(go.Scatter(
#         x=x, y=y,
#         mode='lines',
#         line=dict(color='#64748B', width=2),
#         fill='tozeroy',
#         fillcolor='rgba(59, 130, 246, 0.1)',
#         name='Distribution'
#     ))
    
#     # Safe settlement zone
#     x_safe = np.linspace(res['range_low'], res['range_high'], 150)
#     y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
#     fig_zopa.add_trace(go.Scatter(
#         x=x_safe, y=y_safe,
#         mode='lines',
#         line=dict(width=0),
#         fill='tozeroy',
#         fillcolor='rgba(22, 163, 74, 0.5)',
#         name='Safe Zone'
#     ))
    
#     fig_zopa.update_layout(
#         height=350,
#         showlegend=True,
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         font=dict(color='#e2e8f0', family='Poppins'),
#         margin=dict(l=50, r=50, t=40, b=40),
#         xaxis_title='Settlement Amount ($)',
#         yaxis_title='Probability Density',
#         hovermode='x unified'
#     )
#     st.plotly_chart(fig_zopa, use_container_width=True)
    
#     st.markdown("")
    
#     # === RESET BUTTON ===
#     if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="reset_button"):
#         st.session_state.submitted = False
#         st.rerun()


























###########current version
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

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
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        font-family: 'Poppins', sans-serif;
        color: #e2e8f0;
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
    
    .kpi-label {
        font-size: 0.75rem;
        color: #94a3b8;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }
    
    .kpi-value {
        font-size: 2.2rem;
        color: #f1f5f9;
        font-weight: 800;
        font-family: 'Playfair Display', serif;
        margin-bottom: 8px;
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
    
    with st.form("litigation_form"):
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
            demand = st.number_input("Plaintiff Demand ($) [0=Auto-simulate]", 0, 2000000, 0)
        
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
        submitted = st.form_submit_button("🚀 ANALYZE CASE", use_container_width=True)
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
    
    # === DASHBOARD HEADER ===
    rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
    col_header_left, col_header_right = st.columns(2)
    
    with col_header_left:
        st.markdown(f"""
            <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
            <div class='dashboard-subtitle'>{res['action_desc']}<br>
            📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> • ⚠️ Risk: <b>{res['risk_label']}</b></div>
        """, unsafe_allow_html=True)
    
    with col_header_right:
        st.markdown(f"""
            <div class='recommendation-panel'>
                <div class='recommendation-text'>MODEL CONFIDENCE</div>
                <div class='recommendation-subtext'>89% • Based on {22} litigation attributes</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # === KPI CARDS ===
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>💵 Target Settlement</div>
                <div class='kpi-value'>${res['prediction']/1000:.0f}K</div>
                <div class='kpi-subtext'>Range: ${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>⏱️ Est. Duration</div>
                <div class='kpi-value'>{res['days']}d</div>
                <div class='kpi-subtext'>≈ {res['months']:.1f} months</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>📊 Total Exposure</div>
                <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
                <div class='kpi-subtext'>Verdict + Defense</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        savings_color = "#16a34a" if res['savings'] > 0 else "#dc2626"
        st.markdown(f"""
            <div class='kpi-card' style='border-bottom: 4px solid {savings_color};'>
                <div class='kpi-label'>💰 ROI Savings</div>
                <div class='kpi-value' style='color: {savings_color};'>${abs(res['savings'])/1000:.0f}K</div>
                <div class='kpi-subtext'>{("Settlement ✓" if res['savings'] > 0 else "Litigation ✓")}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # === DRIVER ANALYSIS (Like Image) ===
    st.markdown("<div class='section-header'>📈 Key Driver Analysis for This Claim</div>", unsafe_allow_html=True)
    
    col_drivers_left, col_drivers_right = st.columns(2)
    
    with col_drivers_left:
        st.markdown("<div style='color: #fecaca; font-weight: 700; font-size: 1.1rem; margin-bottom: 15px;'>🔴 Positive Drivers (↑ Settlement Pressure)</div>", unsafe_allow_html=True)
        pos_drivers = [d for d in res['drivers'] if d[2] == 'pos']
        for name, val, _ in pos_drivers[:5]:
            st.markdown(f"""
                <div class='driver-item'>
                    <span class='driver-name'>{name}</span>
                    <span class='driver-value driver-pos'>+${val:,.0f}</span>
                </div>
            """, unsafe_allow_html=True)
    
    with col_drivers_right:
        st.markdown("<div style='color: #bbf7d0; font-weight: 700; font-size: 1.1rem; margin-bottom: 15px;'>🟢 Negative Drivers (↓ Defense Advantage)</div>", unsafe_allow_html=True)
        neg_drivers = [d for d in res['drivers'] if d[2] == 'neg']
        if neg_drivers:
            for name, val, _ in neg_drivers[:5]:
                st.markdown(f"""
                    <div class='driver-item'>
                        <span class='driver-name'>{name}</span>
                        <span class='driver-value driver-neg'>−${abs(val):,.0f}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='color: #94a3b8; padding: 15px; text-align: center;'><i>No mitigating factors identified</i></div>", unsafe_allow_html=True)
    
    st.markdown("")
    
    # === RISK ALERTS ===
    st.markdown("<div class='section-header'>🚨 Critical Risk Alerts</div>", unsafe_allow_html=True)
    
    alert_cols = st.columns(2)
    
    with alert_cols[0]:
        if attorney_score > 80:
            st.markdown("""
                <div class='alert-box'>
                🔥 <b>HIGH-AGGRESSION ATTORNEY</b><br>
                History of trial escalation. Adversarial discovery expected.
                </div>
            """, unsafe_allow_html=True)
        
        if venue_win_rate < 0.40:
            st.markdown("""
                <div class='alert-box'>
                ⚖️ <b>UNFAVORABLE VENUE</b><br>
                Defense win rate <40%. Jury pool bias present.
                </div>
            """, unsafe_allow_html=True)
        
        if days_filed > 365:
            st.markdown("""
                <div class='alert-box'>
                📅 <b>STALE CLAIM</b><br>
                >12 months since filing. Settlement window closing.
                </div>
            """, unsafe_allow_html=True)
    
    with alert_cols[1]:
        if employment == 'Terminated':
            st.markdown("""
                <div class='alert-box'>
                😠 <b>TERMINATED EMPLOYEE</b><br>
                Higher emotional damages expected. Risk premium applies.
                </div>
            """, unsafe_allow_html=True)
        
        if opioid:
            st.markdown("""
                <div class='alert-box'>
                💊 <b>OPIOID INDICATOR</b><br>
                Increased settlement floor due to addiction narratives.
                </div>
            """, unsafe_allow_html=True)
        
        if impairment > 20:
            st.markdown("""
                <div class='alert-box'>
                ⚕️ <b>HIGH IMPAIRMENT</b><br>
                Non-economic damages baseline significantly raised.
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("")
    
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
    
    # === VISUALIZATIONS ===
    st.markdown("<div class='section-header'>📊 Predictive Analytics & Confidence Intervals</div>", unsafe_allow_html=True)
    
    viz_col1, viz_col2 = st.columns(2)
    
    with viz_col1:
        # Gauge Chart - Settlement Value Prediction
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=int(res['prediction']),
            number={'font': {'size': 32, 'color': "#e2e8f0"}, 'prefix': "$"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, int(res['range_high']*1.4)], 'tickwidth': 1, 'tickcolor': "#334155"},
                'bar': {'color': "#3b82f6", 'thickness': 0.3},
                'bgcolor': "#0a0e27",
                'borderwidth': 2,
                'bordercolor': "#334155",
                'steps': [
                    {'range': [0, res['range_low']], 'color': "#1e3a8a"},
                    {'range': [res['range_low'], res['range_high']], 'color': "#1e40af"},
                    {'range': [res['range_high'], int(res['range_high']*1.4)], 'color': "#7f1d1d"}
                ],
            }
        ))
        fig_gauge.update_layout(
            height=320,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family='Poppins'),
            title={'text': 'Settlement Value Prediction', 'font': {'size': 16, 'color': '#cbd5e1'}}
        )
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with viz_col2:
        # Box Plot - Settlement Range & Confidence
        fig_box = go.Figure()
        
        # Add box plot for confidence interval
        fig_box.add_trace(go.Box(
            y=[res['range_low'], res['prediction'], res['range_high']],
            name='Settlement Range',
            marker_color='#3b82f6',
            boxmean='sd',
            showlegend=False
        ))
        
        fig_box.update_layout(
            height=320,
            title={'text': 'Confidence Interval (88%-112%)', 'font': {'size': 16, 'color': '#cbd5e1'}},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family='Poppins'),
            yaxis_title='Amount ($)',
            yaxis_title_font=dict(color='#cbd5e1'),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("")
    
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












