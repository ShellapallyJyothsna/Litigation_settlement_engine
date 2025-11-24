# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# # --- 0. PAGE CONFIGURATION (Must be first) ---
# st.set_page_config(
#     page_title="Settlement Intelligence AI",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 1. CUSTOM CSS (The "Makeup") ---
# # This injects custom HTML/CSS to make the app look like a SaaS product
# # st.markdown("""
# #     <style>
# #     /* Main Background */
# #     .stApp {
# #         background-color: #F5F7F9;
# #     }
    
# #     /* Top Header Style */
# #     .main-header {
# #         font-family: 'Helvetica Neue', sans-serif;
# #         font-weight: 700;
# #         color: #1E3A8A; /* Navy Blue */
# #         font-size: 2.5rem;
# #         margin-bottom: 0px;
# #     }
# #     .sub-header {
# #         font-family: 'Helvetica Neue', sans-serif;
# #         color: #64748B;
# #         font-size: 1.1rem;
# #         margin-bottom: 30px;
# #     }
    
# #     /* Custom Card for Metrics */
# #     .metric-card {
# #         background-color: white;
# #         padding: 20px;
# #         border-radius: 10px;
# #         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #         text-align: center;
# #         border-left: 5px solid #3B82F6;
# #     }
# #     .metric-value {
# #         font-size: 2rem;
# #         font-weight: bold;
# #         color: #1F2937;
# #     }
# #     .metric-label {
# #         color: #6B7280;
# #         font-size: 0.9rem;
# #         text-transform: uppercase;
# #         letter-spacing: 1px;
# #     }
    
# #     /* Recommendation Box */
# #     .rec-box-settle {
# #         background-color: #D1FAE5;
# #         border: 1px solid #34D399;
# #         padding: 15px;
# #         border-radius: 8px;
# #         color: #065F46;
# #     }
# #     .rec-box-fight {
# #         background-color: #FEE2E2;
# #         border: 1px solid #F87171;
# #         padding: 15px;
# #         border-radius: 8px;
# #         color: #991B1B;
# #     }
    
# #     /* Sidebar Styling */
# #     [data-testid="stSidebar"] {
# #         background-color: #1E293B;
# #     }
# #     [data-testid="stSidebar"] .css-17lntkn {
# #         color: white;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# # --- 1. CUSTOM CSS (The "Makeup") ---
# st.markdown("""
#     <style>
#     /* Main Background */
#     .stApp {
#         background-color: #F5F7F9;
#     }
    
#     /* Top Header Style */
#     .main-header {
#         font-family: 'Helvetica Neue', sans-serif;
#         font-weight: 700;
#         color: #1E3A8A; /* Navy Blue */
#         font-size: 2.5rem;
#         margin-bottom: 0px;
#     }
#     .sub-header {
#         font-family: 'Helvetica Neue', sans-serif;
#         color: #64748B;
#         font-size: 1.1rem;
#         margin-bottom: 30px;
#     }
    
#     /* Custom Card for Metrics */
#     .metric-card {
#         background-color: white;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         text-align: center;
#         border-left: 5px solid #3B82F6;
#     }
#     .metric-value {
#         font-size: 2rem;
#         font-weight: bold;
#         color: #1F2937;
#     }
#     .metric-label {
#         color: #6B7280;
#         font-size: 0.9rem;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#     }
    
#     /* Recommendation Box */
#     .rec-box-settle {
#         background-color: #D1FAE5;
#         border: 1px solid #34D399;
#         padding: 15px;
#         border-radius: 8px;
#         color: #065F46;
#     }
#     .rec-box-fight {
#         background-color: #FEE2E2;
#         border: 1px solid #F87171;
#         padding: 15px;
#         border-radius: 8px;
#         color: #991B1B;
#     }
    
#     /* --- SIDEBAR FIX (CORRECTED) --- */
    
#     /* 1. Sidebar Background */
#     [data-testid="stSidebar"] {
#         background-color: #1E293B;
#     }
    
#     /* 2. Make Labels and Headers WHITE */
#     [data-testid="stSidebar"] .stMarkdown, 
#     [data-testid="stSidebar"] h1, 
#     [data-testid="stSidebar"] h2, 
#     [data-testid="stSidebar"] h3, 
#     [data-testid="stSidebar"] label, 
#     [data-testid="stSidebar"] .stCaption {
#         color: #FFFFFF !important;
#     }
    
#     /* 3. Make Input Text (inside the boxes) DARK */
#     /* This targets the text inside selectboxes and number inputs */
#     [data-testid="stSidebar"] div[data-baseweb="select"] > div,
#     [data-testid="stSidebar"] input {
#         color: #1E293B !important; /* Dark Navy Text */
#         -webkit-text-fill-color: #1E293B !important;
#     }
    
#     /* 4. Fix Dropdown Menu Items (The list that pops up) */
#     ul[data-testid="stSelectboxVirtualDropdown"] li {
#         color: #1E293B !important;
#     }

#     /* 5. Fix Expander Header (Background Dark, Text White) */
#     .streamlit-expanderHeader {
#         background-color: #334155 !important;
#         color: #FFFFFF !important;
#         border-radius: 5px;
#     }
    
#     /* --- END SIDEBAR FIX --- */
    
#     </style>
#     """, unsafe_allow_html=True)

# # --- 2. LOAD & TRAIN MODEL (Cached) ---
# @st.cache_resource
# def load_engine():
#     # Load Data (Ensure this CSV exists in the same folder)
#     df = pd.read_csv("synthetic_workers_comp_data.csv")
    
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

# try:
#     engine = load_engine()
# except FileNotFoundError:
#     st.error("🚨 Data file not found! Please run the data generation script first to create 'synthetic_workers_comp_data.csv'.")
#     st.stop()

# # --- 3. SIDEBAR (The Control Panel) ---
# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/2704/2704022.png", width=50) # Placeholder Logo
#     st.markdown("<h2 style='color: white;'>Case Parameters</h2>", unsafe_allow_html=True)
#     st.markdown("<hr style='margin-top:0; border-top: 1px solid #334155;'>", unsafe_allow_html=True)

#     # Grouping inputs for better UX
#     with st.expander("📍 Jurisdiction & Injury", expanded=True):
#         state = st.selectbox("State", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
#         body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#         injury_nature = st.selectbox("Injury Nature", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
#         cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])
    
#     with st.expander("💰 Financials & Medical", expanded=True):
#         wage = st.number_input("Avg Weekly Wage ($)", value=900, step=50)
#         medical_cat = st.radio("Medical Path", ['PT/Conservative', 'Surgery'])
    
#     with st.expander("⚖️ Litigation Intelligence", expanded=True):
#         attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#         st.caption("Attorney Aggressiveness Index")
#         aggressiveness = st.slider("", 1, 10, 5)
#         if aggressiveness > 7:
#             st.warning("⚠️ High Litigation Risk Detected")

# # --- 4. MAIN DASHBOARD CONTENT ---

# # Header
# st.markdown('<div class="main-header">Settlement Intelligence Engine</div>', unsafe_allow_html=True)
# st.markdown('<div class="sub-header">AI-Powered Litigation Risk & Valuation Analysis</div>', unsafe_allow_html=True)

# # PREDICTION LOGIC
# input_data = pd.DataFrame({
#     'State': [state],
#     'Body Part': [body_part],
#     'Injury Nature': [injury_nature],
#     'Cause of Injury': [cause],
#     'Wage Information': [wage],
#     'Attorney Firm': [attorney_firm],
#     'Attorney Aggressiveness': [aggressiveness],
#     'Medical Bill Categories': [medical_cat],
#     'Comorbidity': [False]
# })

# predicted_val = engine.predict(input_data)[0]
# lower_bound = predicted_val * 0.88
# upper_bound = predicted_val * 1.12

# # CONFIDENCE LOGIC
# confidence_level = "HIGH"
# conf_color = "#10B981" # Green
# if aggressiveness > 8 or wage > 2000:
#     confidence_level = "MODERATE"
#     conf_color = "#F59E0B" # Orange

# # --- ROW 1: KPI CARDS (Using HTML for custom look) ---
# c1, c2, c3 = st.columns(3)

# with c1:
#     st.markdown(f"""
#     <div class="metric-card">
#         <div class="metric-label">Predicted Settlement</div>
#         <div class="metric-value">${predicted_val:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown(f"""
#     <div class="metric-card" style="border-left: 5px solid #8B5CF6;">
#         <div class="metric-label">Recommended Range</div>
#         <div class="metric-value">${lower_bound:,.0f} - ${upper_bound:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown(f"""
#     <div class="metric-card" style="border-left: 5px solid {conf_color};">
#         <div class="metric-label">AI Confidence Score</div>
#         <div class="metric-value" style="color: {conf_color};">{confidence_level}</div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# # --- ROW 2: CHARTS & STRATEGY ---

# col_chart, col_strat = st.columns([2, 1])

# with col_chart:
#     st.subheader("📈 Probability of Acceptance Curve")
    
#     # Data for Curve
#     x_vals = np.linspace(predicted_val * 0.6, predicted_val * 1.4, 100)
#     y_vals = 1 / (1 + np.exp(-0.00005 * (x_vals - predicted_val * 0.95))) * 100
    
#     # PLOTLY CHART (Interactive)
#     fig = go.Figure()
    
#     # The Area Curve
#     fig.add_trace(go.Scatter(
#         x=x_vals, y=y_vals,
#         fill='tozeroy',
#         mode='lines',
#         line=dict(color='#3B82F6', width=3),
#         name='Acceptance %'
#     ))
    
#     # The Predicted Line Marker
#     fig.add_vline(x=predicted_val, line_width=2, line_dash="dash", line_color="red", annotation_text="Predicted Value")
    
#     fig.update_layout(
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         xaxis_title="Offer Amount ($)",
#         yaxis_title="Likelihood of Acceptance (%)",
#         hovermode="x unified",
#         margin=dict(l=20, r=20, t=30, b=20),
#         height=350
#     )
#     st.plotly_chart(fig, use_container_width=True)

# with col_strat:
#     st.subheader("🧠 Decision Support")
    
#     # Defense Cost Calculation
#     defense_cost_base = 45000 if state in ['New York', 'California'] else 15000
#     defense_cost = defense_cost_base * (1.5 if aggressiveness > 7 else 1.0)
    
#     total_risk = predicted_val + defense_cost
#     savings = total_risk - predicted_val
    
#     # Recommendation Card
#     if savings > 0:
#         st.markdown(f"""
#         <div class="rec-box-settle">
#             <h3>✅ SETTLE NOW</h3>
#             <p><b>Strategy:</b> Settle near <b>${predicted_val:,.0f}</b>.</p>
#             <p>Fighting this case exposes you to <b>${total_risk:,.0f}</b> in total liability.</p>
#             <p style="font-size: 0.9rem; margin-top: 10px;">📉 Avoided Defense Costs: <b>${defense_cost:,.0f}</b></p>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div class="rec-box-fight">
#             <h3>🛡️ LITIGATE / FIGHT</h3>
#             <p><b>Strategy:</b> The demand is likely inflated.</p>
#             <p>Defense costs (${defense_cost:,.0f}) are lower than the premium requested by plaintiff.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("#### Key Drivers")
#     st.progress(aggressiveness / 10, text=f"Attorney Aggression ({aggressiveness}/10)")
#     impact = "High" if injury_nature in ['Fracture', 'Back'] else "Medium"
#     st.progress(0.8 if impact == "High" else 0.4, text=f"Injury Severity: {impact}")

# # --- FOOTER ---
# st.markdown("""
#     <div style='text-align: center; margin-top: 50px; color: #94A3B8; font-size: 0.8rem;'>
#         Powered by Enterprise Litigation Engine v2.1 | Internal Use Only
#     </div>
#     """, unsafe_allow_html=True)














###########3ok somewhat
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# # --- 1. APP CONFIGURATION ---
# st.set_page_config(
#     page_title="ClaimSight | AI Settlement Engine",
#     page_icon="⚖️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- 2. ENTERPRISE CSS STYLING ---
# st.markdown("""
#     <style>
#     /* Global Font & Background */
#     .stApp {
#         background-color: #f8f9fa;
#         font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
#     }
    
#     /* Header Styling */
#     .header-title {
#         color: #0f172a;
#         font-size: 2.2rem;
#         font-weight: 700;
#         margin-bottom: 0.2rem;
#     }
#     .header-subtitle {
#         color: #64748b;
#         font-size: 1rem;
#         margin-bottom: 2rem;
#     }
    
#     /* METRIC CARDS - The "Banking" Look */
#     .kpi-card {
#         background-color: white;
#         border: 1px solid #e2e8f0;
#         border-radius: 8px;
#         padding: 20px;
#         box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
#         text-align: center;
#     }
#     .kpi-label {
#         color: #64748b;
#         font-size: 0.85rem;
#         text-transform: uppercase;
#         letter-spacing: 0.05em;
#         font-weight: 600;
#     }
#     .kpi-value {
#         color: #0f172a;
#         font-size: 1.8rem;
#         font-weight: 700;
#         margin-top: 5px;
#     }
#     .kpi-sub {
#         font-size: 0.8rem;
#         margin-top: 5px;
#     }
    
#     /* Sidebar Tweaks (Your previous fix) */
#     [data-testid="stSidebar"] { background-color: #1e293b; }
#     [data-testid="stSidebar"] * { color: #ffffff !important; }
#     [data-testid="stSidebar"] input, [data-testid="stSidebar"] div[data-baseweb="select"] > div {
#         color: #1e293b !important;
#     }
#     .streamlit-expanderHeader {
#         background-color: #334155 !important;
#         color: white !important;
#     }
    
#     /* Tab Styling */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 24px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         height: 50px;
#         white-space: pre-wrap;
#         background-color: white;
#         border-radius: 4px 4px 0px 0px;
#         gap: 1px;
#         padding-top: 10px;
#         padding-bottom: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- 3. LOAD ENGINE (Cached) ---
# @st.cache_resource
# def load_engine():
#     try:
#         df = pd.read_csv("synthetic_workers_comp_data.csv")
#     except:
#         return None # Handle missing file gracefully
    
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

# if engine is None:
#     st.error("⚠️ Data File Missing. Please run the data generator script first.")
#     st.stop()

# # --- 4. SIDEBAR INPUTS ---
# with st.sidebar:
#     st.markdown("### ⚙️ Case Parameters")
    
#     with st.expander("1. Claimant Profile", expanded=True):
#         state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
#         wage = st.number_input("Avg Weekly Wage ($)", value=900, step=50)
    
#     with st.expander("2. Clinical Factors", expanded=True):
#         body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
#         injury_nature = st.selectbox("Injury Nature", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
#         cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])
#         medical_cat = st.radio("Treatment Path", ['PT/Conservative', 'Surgery'])

#     with st.expander("3. Litigation Environment", expanded=True):
#         attorney_firm = st.selectbox("Plaintiff Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
#         aggressiveness = st.slider("Attorney Aggression Score", 1, 10, 5)

# # --- 5. PREDICTION LOGIC ---
# input_data = pd.DataFrame({
#     'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
#     'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
#     'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
# })

# predicted_val = engine.predict(input_data)[0]
# lower_bound = predicted_val * 0.88
# upper_bound = predicted_val * 1.12

# # Defense Cost Logic
# defense_cost_base = 45000 if state in ['New York', 'California'] else 15000
# defense_cost = defense_cost_base * (1.5 if aggressiveness > 7 else 1.0)
# total_risk = predicted_val + defense_cost
# savings = total_risk - predicted_val
# risk_level = "HIGH" if aggressiveness > 8 else "MODERATE" if aggressiveness > 5 else "LOW"

# # --- 6. MAIN DASHBOARD ---
# st.markdown('<div class="header-title">ClaimSight AI</div>', unsafe_allow_html=True)
# st.markdown(f'<div class="header-subtitle">Litigation Settlement Analysis • Case ID: {np.random.randint(10000,99999)}</div>', unsafe_allow_html=True)

# # TABS FOR CLEAN ORGANIZATION
# tab1, tab2 = st.tabs(["📊 Executive Summary", "💰 Financial Breakdown"])

# with tab1:
#     # --- TOP KPI ROW ---
#     c1, c2, c3, c4 = st.columns(4)
    
#     with c1:
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">Target Settlement</div>
#             <div class="kpi-value">${predicted_val:,.0f}</div>
#             <div class="kpi-sub" style="color: #64748b;">± 12% Margin</div>
#         </div>""", unsafe_allow_html=True)
        
#     with c2:
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">Total Exposure Risk</div>
#             <div class="kpi-value">${total_risk:,.0f}</div>
#             <div class="kpi-sub" style="color: #ef4444;">(Verdict + Defense)</div>
#         </div>""", unsafe_allow_html=True)
        
#     with c3:
#         rec_color = "#22c55e" if savings > 0 else "#ef4444"
#         rec_text = "SETTLE NOW" if savings > 0 else "LITIGATE"
#         st.markdown(f"""
#         <div class="kpi-card" style="border-bottom: 4px solid {rec_color};">
#             <div class="kpi-label">AI Recommendation</div>
#             <div class="kpi-value" style="color: {rec_color}; font-size: 1.5rem;">{rec_text}</div>
#             <div class="kpi-sub">Avoided Cost: ${abs(savings):,.0f}</div>
#         </div>""", unsafe_allow_html=True)
        
#     with c4:
#         conf_color = "#f59e0b" if risk_level == "HIGH" else "#22c55e"
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">Litigation Difficulty</div>
#             <div class="kpi-value" style="color: {conf_color}; font-size: 1.5rem;">{risk_level}</div>
#             <div class="kpi-sub">Based on Attorney Profile</div>
#         </div>""", unsafe_allow_html=True)

#     st.markdown("---")
    
#     # --- MAIN VISUALS ---
#     col_left, col_right = st.columns([2, 1])
    
#     with col_left:
#         st.markdown("##### 📉 Acceptance Probability Curve")
#         # Interactive S-Curve
#         x_vals = np.linspace(predicted_val * 0.6, predicted_val * 1.4, 100)
#         y_vals = 1 / (1 + np.exp(-0.00005 * (x_vals - predicted_val * 0.95))) * 100
        
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=x_vals, y=y_vals, fill='tozeroy', line=dict(color='#3b82f6', width=3), name='Acceptance %'))
#         fig.add_vline(x=predicted_val, line_dash="dash", line_color="#64748b")
#         fig.update_layout(
#             height=350, margin=dict(l=20, r=20, t=10, b=20),
#             xaxis_title="Settlement Offer ($)", yaxis_title="Probability (%)",
#             plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col_right:
#         st.markdown("##### 🧠 Strategy Note")
#         if savings > 0:
#             st.info(f"""
#             **Opportunity Identified:**
#             The model predicts that settling at **${predicted_val:,.0f}** is statistically cheaper than proceeding to trial.
            
#             * **Why?** Defense costs in {state} are high (${defense_cost:,.0f}).
#             * **Action:** Make an opening offer of **${predicted_val*0.85:,.0f}** (85%).
#             """)
#         else:
#             st.error(f"""
#             **Risk Warning:**
#             The plaintiff's likely demand exceeds the cost of litigation.
            
#             * **Strategy:** Depose the claimant.
#             * **Action:** Do not offer above **${total_risk:,.0f}**.
#             """)

# with tab2:
#     st.markdown("### 🏗️ Cost Component Waterfall")
#     st.caption("Estimated contribution of each factor to the total predicted settlement.")
    
#     # Simulate Cost Breakdown for Visualization (Approximation)
#     base_med = predicted_val * 0.40
#     indemnity = predicted_val * 0.30
#     geo_impact = predicted_val * 0.15 if state in ['New York', 'California'] else 0
#     attorney_prem = predicted_val * 0.15 if aggressiveness > 5 else 0
#     remainder = predicted_val - (base_med + indemnity + geo_impact + attorney_prem)
    
#     fig_waterfall = go.Figure(go.Waterfall(
#         name = "20", orientation = "v", measure = ["relative", "relative", "relative", "relative", "relative", "total"],
#         x = ["Base Medical", "Indemnity (Wages)", "Jurisdiction Load", "Attorney Premium", "Misc Factors", "Total Settlement"],
#         y = [base_med, indemnity, geo_impact, attorney_prem, remainder, predicted_val],
#         connector = {"line":{"color":"rgb(63, 63, 63)"}},
#         decreasing = {"marker":{"color":"Maroon"}},
#         increasing = {"marker":{"color":"#3b82f6"}},
#         totals = {"marker":{"color":"#0f172a"}}
#     ))
    
#     fig_waterfall.update_layout(title = "Why is the cost this high?", showlegend = False, plot_bgcolor='rgba(0,0,0,0)')
#     st.plotly_chart(fig_waterfall, use_container_width=True)




















import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# --- 1. PAGE CONFIGURATION ---
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

    /* A. REMOVE DEFAULT PADDING */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }
    header {visibility: hidden;}

    /* B. MAIN BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 228, 255) 90%);
        font-family: 'Inter', sans-serif;
    }

    /* C. SIDEBAR STYLING (Dark Mode) */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B;
    }

    /* --- INPUT TEXT VISIBILITY FIX --- */
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput div[data-baseweb="input"] > div {
        background-color: #1E293B !important;
        border: 1px solid #475569 !important;
        color: white !important;
    }
    input[type="number"], 
    div[data-baseweb="select"] span, 
    div[data-baseweb="select"] div {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        caret-color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    ul[data-testid="stSelectboxVirtualDropdown"] {
        background-color: #0F172A !important;
    }
    li[role="option"] div {
        color: white !important;
    }
    
    /* Expander Headers (Dark) */
    .streamlit-expanderHeader {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid #334155;
        border-radius: 8px;
    }
    .streamlit-expanderHeader p, .streamlit-expanderHeader span, .streamlit-expanderHeader svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }
    
    /* Sidebar Labels */
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] p {
        color: #94A3B8 !important;
    }

    /* D. NAVBAR STYLING */
    .navbar {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.3);
        padding: 15px 30px;
        border-radius: 12px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    }
    .navbar-brand {
        font-size: 1.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #2563EB, #1D4ED8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .navbar-status {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #10B981;
    }

    /* E. GLASS CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
        margin-bottom: 15px;
        transition: transform 0.3s ease;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
    }
    .metric-label {
        color: #64748B;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .metric-value {
        color: #0F172A;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 5px 0;
        white-space: nowrap;
    }

    /* F. CUSTOM TABS */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(255,255,255,0.5);
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        color: #2563EB !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOAD ENGINE ---
@st.cache_resource
def load_engine():
    try:
        df = pd.read_csv("synthetic_workers_comp_data.csv")
    except FileNotFoundError:
        return None
    
    X = df.drop(columns=['Settlement Payout', 'Legal Fees', 'Claim Number', 'DOI', 'Indemnity Paid', 'Medical Cost'])
    y = df['Settlement Payout']
    
    categorical_features = ['State', 'Body Part', 'Injury Nature', 'Cause of Injury', 'Attorney Firm', 'Medical Bill Categories']
    numeric_features = ['Wage Information', 'Attorney Aggressiveness']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
    ])
    model.fit(X, y)
    return model

engine = load_engine()

# --- 4. SIDEBAR (EXPANDERS CLOSED BY DEFAULT) ---
with st.sidebar:
    st.markdown("## ⚖️ Litigation Settlement")
    st.markdown("<div style='color: #94A3B8; margin-bottom: 20px;'>Litigation Intelligence Suite v1.0</div>", unsafe_allow_html=True)
    
    # CHANGED: expanded=False
    with st.expander("👤 CLAIMANT PROFILE", expanded=False):
        state = st.selectbox("Jurisdiction", ['New York', 'California', 'Texas', 'Florida', 'Georgia'])
        wage = st.number_input("Weekly Wage ($)", value=900, step=50)

    # CHANGED: expanded=False
    with st.expander("🏥 MEDICAL PROFILE", expanded=False):
        body_part = st.selectbox("Body Part", ['Back', 'Neck', 'Shoulder', 'Knee', 'Wrist'])
        injury_nature = st.selectbox("Injury Type", ['Fracture', 'Strain', 'Sprain', 'Contusion', 'Laceration'])
        medical_cat = st.radio("Treatment", ['PT/Conservative', 'Surgery'])
        cause = st.selectbox("Cause", ['Lifting', 'Slip/Fall', 'Repetitive Motion', 'Struck By'])

    # CHANGED: expanded=False
    with st.expander("⚖️ LITIGATION PROFILE", expanded=False):
        attorney_firm = st.selectbox("Opposing Counsel", ['Firm A', 'Firm B', 'Firm C', 'Solo Practitioner'])
        aggressiveness = st.slider("Aggression Index", 1, 10, 5)

# --- 5. LOGIC ---
# if engine:
#     input_data = pd.DataFrame({
#         'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
#         'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
#         'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
#     })
#     predicted_val = engine.predict(input_data)[0]
#     lower = predicted_val * 0.88
#     upper = predicted_val * 1.12
#     defense_cost = (45000 if state in ['New York', 'California'] else 15000) * (1.5 if aggressiveness > 7 else 1.0)
#     total_risk = predicted_val + defense_cost
#     savings = total_risk - predicted_val
#     is_settle = savings > 0
# --- 5. LOGIC (UPDATED WITH ROI CALCULATOR) ---
if engine:
    # 1. Create Input Data
    input_data = pd.DataFrame({
        'State': [state], 'Body Part': [body_part], 'Injury Nature': [injury_nature],
        'Cause of Injury': [cause], 'Wage Information': [wage], 'Attorney Firm': [attorney_firm],
        'Attorney Aggressiveness': [aggressiveness], 'Medical Bill Categories': [medical_cat]
    })

    # 2. Get AI Prediction
    predicted_val = engine.predict(input_data)[0]
    lower = predicted_val * 0.88
    upper = predicted_val * 1.12

    # 3. Calculate Defense Costs (Cost to Fight)
    # Base cost is higher in NY/CA. Aggressive attorneys increase cost by 50%.
    defense_base = 45000 if state in ['New York', 'California'] else 15000
    defense_multiplier = 1.5 if aggressiveness > 7 else 1.0
    defense_cost = defense_base * defense_multiplier

    # 4. Calculate Total Exposure (The "Walk Away" Cost)
    # If we lose in court, we pay the Verdict + Our Lawyers
    total_risk = predicted_val + defense_cost

    # 5. Simulate Plaintiff Demand (The "Greedy Attorney" Logic)
    # If Aggressiveness is High (8-10), they demand WAY more than the claim is worth.
    # If Aggressiveness is Low, they demand near the fair value.
    demand_multiplier = 1.0
    if aggressiveness >= 8:
        demand_multiplier = 2.5  # They want 2.5x value (Unreasonable)
    elif aggressiveness >= 6:
        demand_multiplier = 1.5  # They want 1.5x value (Pushy)
    elif aggressiveness >= 4:
        demand_multiplier = 1.1  # They want 10% extra (Standard)
    
    plaintiff_demand = predicted_val * demand_multiplier

    # 6. Calculate ROI / Savings
    # Formula: (Cost to Fight) - (Cost to Pay Demand)
    # If Savings is NEGATIVE, it means fighting is cheaper than paying their crazy demand.
    savings = total_risk - plaintiff_demand
    is_settle = savings > 0

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

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-label">Target Settlement</div>
        <div class="metric-value">${predicted_val:,.0f}</div>
        <div style="color: #64748B; font-size: 0.8rem;">Range: ${lower:,.0f} - ${upper:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-label">Total Exposure</div>
        <div class="metric-value">${total_risk:,.0f}</div>
        <div style="color: #EF4444; font-size: 0.8rem;">Verdict + Defense Fees</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    rec_color = "#10B981" if is_settle else "#EF4444"
    rec_text = "SETTLE NOW" if is_settle else "LITIGATE"
    st.markdown(f"""
    <div class="glass-card" style="border-bottom: 4px solid {rec_color}">
        <div class="metric-label">AI Recommendation</div>
        <div class="metric-value" style="color: {rec_color}">{rec_text}</div>
        <div style="color: #64748B; font-size: 0.8rem;">ROI Positive</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    risk_color = "#F59E0B" if aggressiveness > 7 else "#10B981"
    risk_txt = "HIGH RISK" if aggressiveness > 7 else "STANDARD"
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-label">Litigation Score</div>
        <div class="metric-value" style="color: {risk_color}">{risk_txt}</div>
        <div style="color: #64748B; font-size: 0.8rem;">Attorney Profile</div>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📈 STRATEGY & PROBABILITY", "💰 FINANCIAL WATERFALL"])

with tab1:
    col_L, col_R = st.columns([2, 1])
    with col_L:
        x_vals = np.linspace(predicted_val * 0.6, predicted_val * 1.4, 100)
        y_vals = 1 / (1 + np.exp(-0.00005 * (x_vals - predicted_val * 0.95))) * 100
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, fill='tozeroy', line=dict(color='#2563EB', width=4), name='Acceptance'))
        fig.add_vline(x=predicted_val, line_dash="dash", line_color="#64748B")
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_title="Offer Amount ($)", yaxis_title="Probability (%)", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
    with col_R:
        st.markdown(f"""
        <div class="glass-card" style="background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%); min-height: 350px;">
            <h4 style="margin-top:0; color: #1E293B;">💡 Strategic Insight</h4>
            <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
            The model has identified a <b>{int(savings/predicted_val*100) if predicted_val else 0}% savings opportunity</b> by settling early.
            <br><br>
            <b>Defense Cost Analysis:</b><br>
            Jurisdiction: <span style="color:#2563EB"><b>{state}</b></span><br>
            Est. Legal Fees: <span style="color:#EF4444"><b>${defense_cost:,.0f}</b></span>
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    base = predicted_val * 0.35
    indemnity = predicted_val * 0.25
    geo = predicted_val * 0.15 if state in ['New York', 'California'] else 0
    att_premium = predicted_val * 0.20 if aggressiveness > 6 else 0
    misc = predicted_val - (base + indemnity + geo + att_premium)
    fig_waterfall = go.Figure(go.Waterfall(
        orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "total"],
        x = ["Base Medical", "Indemnity", "Jurisdiction", "Attorney Risk", "Misc", "Total"],
        y = [base, indemnity, geo, att_premium, misc, predicted_val],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
        decreasing = {"marker":{"color":"#EF4444"}},
        increasing = {"marker":{"color":"#2563EB"}},
        totals = {"marker":{"color":"#1E293B"}}
    ))
    fig_waterfall.update_layout(height=450, title="Cost Driver Analysis", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_waterfall, use_container_width=True)