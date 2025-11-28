



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













import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="ClaimSight AI | Enterprise",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. FIXED CSS STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* Global Layout */
    .block-container {padding-top: 1rem !important; padding-bottom: 2rem !important; max-width: 95% !important;}
    header {visibility: hidden;}
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 228, 255) 90%);
        font-family: 'Inter', sans-serif;
    }

    /* DARK SIDEBAR STYLING */
    section[data-testid="stSidebar"] {background-color: #0F172A !important; border-right: 1px solid #1E293B;}
    
    /* INPUT BOX VISIBILITY FIX */
    .stSelectbox div[data-baseweb="select"] > div, .stNumberInput div[data-baseweb="input"] > div {
        background-color: #1E293B !important; 
        border: 1px solid #475569 !important; 
        color: white !important;
    }
    input[type="number"], div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #FFFFFF !important; 
        -webkit-text-fill-color: #FFFFFF !important;
        caret-color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    ul[data-testid="stSelectboxVirtualDropdown"] {background-color: #0F172A !important;}
    li[role="option"] div {color: white !important;}

    /* Expander Headers */
    .streamlit-expanderHeader {background-color: #1E293B !important; color: #FFFFFF !important; border: 1px solid #334155; border-radius: 8px;}
    .streamlit-expanderHeader p, .streamlit-expanderHeader span, .streamlit-expanderHeader svg {color: #FFFFFF !important; fill: #FFFFFF !important;}

    /* Sidebar Labels */
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] h2 {color: #94A3B8 !important;}

    /* NAVBAR & CARDS */
    .navbar {background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); padding: 15px 30px; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);}
    .navbar-brand {font-size: 1.8rem; font-weight: 800; background: -webkit-linear-gradient(45deg, #2563EB, #1D4ED8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    
    /* GLASS CARDS (With Hover Animation) */
    .glass-card {
        background: rgba(255, 255, 255, 0.85); 
        backdrop-filter: blur(12px); 
        border-radius: 16px; 
        border: 1px solid rgba(255, 255, 255, 0.6); 
        padding: 20px; 
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05); 
        min-height: 180px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
    }
    .glass-card:hover {
        transform: translateY(-5px); 
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
    }
    .metric-label {color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;}
    .metric-value {color: #0F172A; font-size: 1.8rem; font-weight: 800; white-space: nowrap;}
    </style>
""", unsafe_allow_html=True)

# --- 3. TRAIN DUAL MODELS ---
@st.cache_resource
def load_engines():
    try:
        df = pd.read_csv("synthetic_workers_comp_data.csv")
    except FileNotFoundError: return None, None
    
    X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Days_to_Settle', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'], errors='ignore')
    y_cost = df['Settlement Payout']
    y_time = df['Days_to_Settle']
    
    categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
    numeric_features = ['Wage Information', 'Attorney Aggressiveness']

    preprocessor = ColumnTransformer(transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

    model_cost = Pipeline(steps=[('prep', preprocessor), ('reg', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))])
    model_cost.fit(X, y_cost)
    
    model_time = Pipeline(steps=[('prep', preprocessor), ('reg', GradientBoostingRegressor(n_estimators=200, random_state=42))])
    model_time.fit(X, y_time)
    
    return model_cost, model_time

engine_cost, engine_time = load_engines()

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚖️ Litigation Settlement")
    st.markdown("<div style='color: #94A3B8; margin-bottom: 20px;'>Litigation Intelligence Suite v5.0</div>", unsafe_allow_html=True)
    
    with st.expander("👤 CLAIMANT PROFILE", expanded=False):
        state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
        wage = st.number_input("Weekly Wage ($)", value=900, step=50)

    with st.expander("🏥 MEDICAL PROFILE", expanded=False):
        body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
        injury_nature = st.selectbox("Injury Type", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
        medical_cat = st.radio("Treatment", ['PT/Conservative', 'Surgery'])
        cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])

    with st.expander("⚖️ LITIGATION PROFILE", expanded=True):
        attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
        aggressiveness = st.slider("Aggression Index", 1, 10, 5)
        st.markdown("---")
        claimant_demand = st.number_input("Claimant Demand / Deal ($)", value=0, step=1000, help="Enter the amount the claimant is asking for.")

# --- 5. LOGIC ENGINE ---
if engine_cost:
    input_data = pd.DataFrame({
        'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
        'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
        'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
    })
    
    # Predictions
    predicted_val = engine_cost.predict(input_data)[0]
    predicted_days = engine_time.predict(input_data)[0]
    predicted_months = predicted_days / 30
    
    lower = predicted_val * 0.88
    upper = predicted_val * 1.12

    # Defense Cost
    defense_base = 45000 if state in ['New York', 'California'] else 15000
    defense_multiplier = 1.5 if aggressiveness > 7 else 1.0
    defense_cost = defense_base * defense_multiplier

    # Total Exposure
    total_risk = predicted_val + defense_cost

    # ROI Logic
    if claimant_demand > 0:
        active_demand = claimant_demand
        is_simulated = False
    else:
        demand_multiplier = 2.5 if aggressiveness >= 8 else (1.5 if aggressiveness >= 6 else 1.1)
        active_demand = predicted_val * demand_multiplier
        is_simulated = True
    
    savings = total_risk - active_demand
    is_settle = savings > 0

    # Litigation Score Logic
    if aggressiveness >= 8:
        lit_score = "HIGH RISK"
        lit_color = "#EF4444" 
        gauge_val = 90
    elif aggressiveness >= 5:
        lit_score = "MEDIUM RISK"
        lit_color = "#F59E0B" 
        gauge_val = 60
    else:
        lit_score = "LOW RISK"
        lit_color = "#10B981" 
        gauge_val = 25

# --- 6. MAIN DASHBOARD ---
st.markdown(f"""
    <div class="navbar">
        <div class="navbar-brand">Litigation Settlement</div>
        <div style="display: flex; gap: 20px; align-items: center;">
            <div style="color: #64748B; font-size: 0.9rem;"><b>Case ID:</b> #82910-X</div>
            <div class="navbar-status">● LIVE ANALYSIS</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# KPI ROW
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""<div class="glass-card"><div class="metric-label">Target Settlement</div><div class="metric-value">${predicted_val:,.0f}</div><div style="color: #64748B; font-size: 0.8rem;">Range: ${lower:,.0f} - ${upper:,.0f}</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="glass-card"><div class="metric-label">Est. Duration</div><div class="metric-value">{int(predicted_days):,} Days</div><div style="color: #64748B; font-size: 0.8rem;">~{predicted_months:.1f} Months to Close</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="glass-card"><div class="metric-label">Total Exposure</div><div class="metric-value">${total_risk:,.0f}</div><div style="color: #EF4444; font-size: 0.8rem;">Verdict + Defense Fees</div></div>""", unsafe_allow_html=True)
with c4:
    rec_color = "#10B981" if is_settle else "#EF4444"
    rec_text = "SETTLE NOW" if is_settle else "LITIGATE"
    roi_label = "ROI vs Deal" if not is_simulated else "ROI vs Demand"
    st.markdown(f"""<div class="glass-card" style="border-bottom: 4px solid {rec_color}"><div class="metric-label">AI Recommendation</div><div class="metric-value" style="color: {rec_color}">{rec_text}</div><div style="color: #64748B; font-size: 0.8rem;">{roi_label}: ${savings:,.0f}</div></div>""", unsafe_allow_html=True)

# --- STRATEGY SECTION (Replaces Tabs) ---
st.markdown("### 📊 Strategy & Risk Analysis")

col_L, col_R = st.columns([1, 2])

with col_L:
    # GAUGE CHART WITH TEXT LABEL
    st.markdown(f"##### 🛡️ Litigation Score")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge", # Text only, no number
        value = gauge_val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': lit_color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': "#D1FAE5"},
                {'range': [40, 75], 'color': "#FEF3C7"},
                {'range': [75, 100], 'color': "#FEE2E2"}],
        }
    ))
    
    # Add Text Annotation in Center
    fig_gauge.update_layout(
        height=280, 
        margin=dict(l=20, r=20, t=30, b=20), 
        paper_bgcolor='rgba(0,0,0,0)',
        annotations=[dict(x=0.5, y=0.25, text=lit_score, showarrow=False, font=dict(size=20, color=lit_color, weight="bold"))]
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_R:
    # BAR CHART
    st.markdown(f"##### 🎯 Negotiation Success Probability")
    
    low_offer = predicted_val * 0.85
    target_offer = predicted_val
    high_offer = predicted_val * 1.15
    
    prob_low = 1 / (1 + np.exp(-0.00005 * (low_offer - predicted_val * 0.95))) * 100
    prob_target = 1 / (1 + np.exp(-0.00005 * (target_offer - predicted_val * 0.95))) * 100
    prob_high = 1 / (1 + np.exp(-0.00005 * (high_offer - predicted_val * 0.95))) * 100
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        y=['Aggressive Offer', 'Fair Market Value', 'Overpayment'],
        x=[prob_low, prob_target, prob_high],
        orientation='h',
        marker=dict(color=['#EF4444', '#3B82F6', '#10B981']),
        text=[f"${low_offer:,.0f}<br>({int(prob_low)}% Chance)", 
              f"${target_offer:,.0f}<br>({int(prob_target)}% Chance)", 
              f"${high_offer:,.0f}<br>({int(prob_high)}% Chance)"],
        textposition='auto',
    ))
    fig_bar.update_layout(
        height=300,
        xaxis_title="Probability of Acceptance (%)",
        xaxis=dict(range=[0, 100]),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- FINAL STRATEGY CARD ---
if is_settle:
    strategy_color = "#166534" # Dark Green
    bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%)"
    title = "✅ Positive ROI Strategy"
    conclusion = f"Settling now saves the company <b>${savings:,.0f}</b> and avoids a {int(predicted_months)}-month legal battle."
else:
    strategy_color = "#991B1B" # Dark Red
    bg_grad = "linear-gradient(135deg, #FFFFFF 0%, #FEF2F2 100%)"
    title = "🛡️ Negative ROI Alert"
    conclusion = f"Do not pay. Their demand of <b>${active_demand:,.0f}</b> exceeds the cost to fight (<b>${total_risk:,.0f}</b>). Proceed to litigation."

st.markdown(f"""
<div class="glass-card" style="background: {bg_grad}; border-left: 5px solid {strategy_color};">
    <h3 style="margin-top:0; color: {strategy_color};">{title}</h3>
    <p style="color: #475569; font-size: 1rem; line-height: 1.6;">
    The claimant is asking for <b>${active_demand:,.0f}</b>.
    <br><br>
    <b>Defense Cost Analysis:</b><br>
    Jurisdiction: <span style="color:#2563EB"><b>{state}</b></span> (Est. Legal Fees: <span style="color:#EF4444"><b>${defense_cost:,.0f}</b></span>)
    <br><br>
    <b>Conclusion:</b> {conclusion}
    </p>
</div>
""", unsafe_allow_html=True)