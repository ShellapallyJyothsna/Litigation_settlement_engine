# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import os
# from dotenv import load_dotenv


# # Load environment variables
# load_dotenv()


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
    
#     /* === NEUTRAL CHARCOAL THEME (No Blue) === */
    
#     .stApp {
#         background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
#         font-family: 'Poppins', sans-serif;
#         color: #e2e8f0;
#     }
#     /* Make the Form Container a Lighter Grey to pop */
#     .form-container {
#         background: linear-gradient(135deg, #27272a 0%, #3f3f46 100%) !important;
#         border: 1px solid #52525b !important; /* Neutral Grey Border */
#         box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
#         padding: 50px;
#         border-radius: 20px;
#         max-width: 1200px;
#         margin: 40px auto;
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
    
#     .kpi-value {
#         font-size: 1.8rem; /* Reduced from 2.2rem to fit better */
#         color: #f1f5f9;
#         font-weight: 800;
#         margin: 5px 0; /* Reduced margin */
#         font-family: 'Playfair Display', serif;
#         letter-spacing: 0.5px; /* Reduced spacing */
#         white-space: nowrap; /* Prevents wrapping */
#     }
    
#     .kpi-label {
#         font-size: 0.7rem; /* Slightly smaller label */
#         color: #94a3b8;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         margin-bottom: 5px;
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
    

#     /* Force all Streamlit input labels to be White */
#     label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
#         color: #e2e8f0 !important;
#         font-size: 0.85rem !important;
#         font-weight: 600 !important;
#         letter-spacing: 0.8px !important;
#     }

#     /* Ensure text typed inside numbers/selects is White */
#     input[type="number"], div[data-baseweb="select"] span {
#         color: #ffffff !important;
#         -webkit-text-fill-color: #ffffff !important;
#     }
#     </style>
# """, unsafe_allow_html=True)


# # # === LIGHT THEME CSS STYLING ===
# # st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
# #     * { margin: 0; padding: 0; box-sizing: border-box; }
    
# #     /* === CORE LIGHT THEME === */
    
# #     .stApp {
# #         background: #f8fafc; /* Very light, off-white background */
# #         font-family: 'Poppins', sans-serif;
# #         color: #1e293b; /* Dark text for readability */
# #     }
    
# #     /* Form Container (Needs to pop slightly) */
# #     .form-container {
# #         background: #ffffff !important; /* Pure white form background */
# #         border: 1px solid #e2e8f0 !important; /* Light border */
# #         box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
# #         padding: 50px;
# #         border-radius: 16px;
# #         max-width: 1200px;
# #         margin: 40px auto;
# #     }
    
# #     /* Hide Streamlit UI elements */
# #     section[data-testid="stSidebar"] { display: none; }
# #     header { visibility: hidden; }
# #     footer { visibility: hidden; }
# #     #MainMenu { visibility: hidden; }
    
# #     /* Titles and Subtitles */
# #     .form-title {
# #         font-family: 'Playfair Display', serif;
# #         font-size: 3rem;
# #         font-weight: 700;
# #         /* Blue gradient for contrast */
# #         background: linear-gradient(135deg, #2563eb, #1e3a8a);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #         background-clip: text;
# #         text-align: center;
# #         margin-bottom: 10px;
# #         letter-spacing: 1px;
# #     }
    
# #     .form-subtitle {
# #         text-align: center;
# #         color: #64748b; /* Medium grey subtitle */
# #         margin-bottom: 40px;
# #         font-size: 1.1rem;
# #     }
    
# #     /* Form Section Labels */
# #     .form-section-label {
# #         color: #1e40af; /* Dark blue label for emphasis */
# #         font-weight: 700;
# #         font-size: 0.85rem;
# #         text-transform: uppercase;
# #         letter-spacing: 1.2px;
# #         margin-bottom: 15px;
# #         display: block;
# #     }
    
# #     /* Input Field Styling (Selectbox, Number Input) */
# #     .stSelectbox div[data-baseweb="select"] > div,
# #     .stNumberInput div[data-baseweb="input"] > div,
# #     .stSlider {
# #         background: #f1f5f9 !important; /* Light grey input background */
# #         border: 1.5px solid #cbd5e1 !important;
# #         border-radius: 8px !important;
# #         color: #1e293b !important; /* Dark text inside inputs */
# #         transition: all 0.3s ease;
# #     }
    
# #     .stSelectbox div[data-baseweb="select"] > div:hover,
# #     .stNumberInput div[data-baseweb="input"] > div:hover {
# #         border-color: #3b82f6 !important;
# #         box-shadow: 0 0 10px rgba(59, 130, 246, 0.1);
# #     }
    
# #     /* Force text/label colors to be dark/black */
# #     label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
# #         color: #1e293b !important;
# #     }

# #     input[type="number"], div[data-baseweb="select"] span {
# #         color: #1e293b !important;
# #         -webkit-text-fill-color: #1e293b !important;
# #         caret-color: #2563eb !important;
# #         font-weight: 600 !important;
# #     }

# #     /* Dropdown menu background (for select boxes) */
# #     ul[data-testid="stSelectboxVirtualDropdown"] {
# #         background: #ffffff !important;
# #         border: 1px solid #e2e8f0 !important;
# #     }
    
# #     li[role="option"] { color: #1e293b !important; }
# #     li[role="option"]:hover { background: rgba(59, 130, 246, 0.1) !important; }
    
# #     /* Submit Button (Keep bold blue gradient) */
# #     div.stButton > button {
# #         background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%);
# #         color: white; /* Text stays white on blue button */
# #         /* ... rest of button style remains ... */
# #     }
    
# #     /* Dashboard Elements */
# #     .dashboard-header, .kpi-card, .driver-section {
# #         background: #ffffff; /* White background for dashboard sections */
# #         border: 1px solid #e2e8f0;
# #         box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
# #     }
    
# #     .dashboard-title {
# #         color: #1e293b; /* Dark title text */
# #     }
    
# #     .dashboard-subtitle, .kpi-subtext, .driver-name {
# #         color: #475569; /* Darker grey text */
# #     }

# #     .kpi-value {
# #         color: #1e293b; /* Dark black/blue for numbers */
# #     }
    
# #     .kpi-label {
# #         color: #64748b; /* Grey for labels */
# #     }
    
# #     /* Driver item list styling */
# #     .driver-item {
# #         background: #f1f5f9; /* Light grey strip background */
# #         border-left: 4px solid #3b82f6;
# #     }
    
# #     .driver-pos {
# #         color: #b91c1c; /* Dark red for positive impact */
# #         background: rgba(239, 68, 68, 0.1);
# #         border: 1px solid #f87171;
# #     }
    
# #     .driver-neg {
# #         color: #059669; /* Dark green for negative impact (lower settlement) */
# #         background: rgba(5, 150, 105, 0.1);
# #         border: 1px solid #34d399;
# #     }
    
# #     /* Section Headers */
# #     .section-header {
# #         color: #1e293b;
# #         border-bottom: 2px solid #cbd5e1;
# #     }
    
# #     /* Strategic Recommendation Box (Green for Settle) */
# #     .stSuccess > div {
# #         background: #ecfdf5 !important; /* Very light green */
# #         border-left: 5px solid #059669 !important;
# #         color: #065f46 !important; /* Dark green text */
# #     }

# #     /* Strategic Recommendation Box (Red for Litigate) */
# #     .stError > div {
# #         background: #fef2f2 !important; /* Very light red */
# #         border-left: 5px solid #ef4444 !important;
# #         color: #b91c1c !important; /* Dark red text */
# #     }

# #     /* Strategic Recommendation Box (Yellow for Strategize) */
# #     .stWarning > div {
# #         background: #fffdf6 !important; /* Very light yellow */
# #         border-left: 5px solid #f59e0b !important;
# #         color: #b45309 !important; /* Dark brown text */
# #     }
    
# #     </style>
# # """, unsafe_allow_html=True)


# # === INITIALIZE SESSION STATE ===
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False
# # === NEW: LANDING PAGE WITH THREE SCENARIOS ===

# if "scenario_selected" not in st.session_state:
#     st.session_state.scenario_selected = False

# if st.session_state.submitted:
#     st.markdown(
#         """
#         <script>
#             // Use setTimeout to ensure the Streamlit content has loaded before scrolling
#             setTimeout(function() {
#                 window.scrollTo(0, 0); // Scrolls to the top-left corner
#             }, 50); 
#         </script>
#         """, 
#         unsafe_allow_html=True
#     )

# if not st.session_state.scenario_selected:

#     st.markdown("""
#         <div style='text-align:center; margin-top:60px;'>
           
#            <h1 style='font-family:Poppins; font-size:3rem; color:white;'>⚖️ Litigation Settlement Analyzer</h1>
#             <p style='color:#cbd5e1; font-size:1.2rem;'>
#                 Select a scenario to pre-fill the case details
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         if st.button("✅ SETTLE", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 90,
#                 "Impairment_Rating": 15,
#                 "Wage_Loss_Exposure": 45000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 110000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()

#     with c2:
#         if st.button("⚡ STRATEGIZE", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 60,
#                 "Impairment_Rating": 12,
#                 "Wage_Loss_Exposure": 35000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 175000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()

#     with c3:
#         if st.button("⚔️ LITIGATE", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 50,
#                 "Impairment_Rating": 2,
#                 "Wage_Loss_Exposure": 5000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 850000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()

#     st.stop()

# # === FORM STATE ===
# if not st.session_state.submitted:
#     st.markdown("""
#         <div class='form-container'>
#             <div class='form-title'>⚖️ Litigation Settlement Analyzer</div>
#             <div class='form-subtitle'>Settlement Valuation & Strategy Intelligence</div>
#     """, unsafe_allow_html=True)
    
#     with st.container(): # Changed from st.form to st.container to allow dynamic interactions

#         # === APPLY PREFILL (if scenario chosen) ===
#         pref = st.session_state.get("prefill", {})

#         # Helper: choose default OR prefilled
#         def use_prefill(key, default):
#             return pref.get(key, default)

#         # # === A. LITIGATION & EXPOSURE ===
#         # st.markdown("<span class='form-section-label'>🏛️ A. Litigation & Exposure</span>", unsafe_allow_html=True)

#         # form_col1, form_col2 = st.columns(2)
#         # with form_col1:
#         #     jurisdiction = st.selectbox(
#         #         "Jurisdiction",
#         #         ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'New Jersey'],
#         #         index=['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'New Jersey']
#         #         .index(use_prefill("Jurisdiction", "New Jersey"))
#         #     )
#         # with form_col2:
#         #     venue_win_rate = st.slider("Defense Win Rate in Venue", 0.0, 1.0, 0.45)

#         # form_col3, form_col4 = st.columns(2)
#         # with form_col3:
#         #     attorney_firm = st.selectbox(
#         #         "Plaintiff Counsel",
#         #         ['Weitz & Luxenberg', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner']
#         #     )
#         # with form_col4:
#         #     attorney_score = st.slider(
#         #         "Plaintiff attorney aggressiveness", 
#         #         0, 100, 
#         #         use_prefill("Attorney_Score", 65)
#         #     )

#         # form_col5, _ = st.columns(2)
#         # with form_col5:
#         #     provider_type = st.selectbox(
#         #         "Primary Provider",
#         #         ['Chiropractor', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Chiropractor']
#         #     )

#         # st.markdown("---")

#         # # === B. ECONOMIC DAMAGES ===
#         # st.markdown("<span class='form-section-label'>💰 B. Economic Damages</span>", unsafe_allow_html=True)

#         # form_col6, form_col7 = st.columns(2)
#         # with form_col6:
#         #     wage_loss = st.number_input(
#         #         "Wage Loss Exposure ($)",
#         #         5000, 500000,
#         #         use_prefill("Wage_Loss_Exposure", 25000)
#         #     )
#         # with form_col7:
#         #     impairment = st.slider(
#         #         "Permanent Impairment (%)",
#         #         0, 100,
#         #         use_prefill("Impairment_Rating", 15)
#         #     )

#         # form_col8, form_col9 = st.columns(2)
#         # with form_col8:
#         #     medical_trajectory = st.selectbox(
#         #         "Medical Cost Trajectory",
#         #         ['Low', 'Moderate', 'High', 'Escalating']
#         #     )
#         # with form_col9:
#         #     future_medical = st.checkbox("Future Medical Exposure?", value=True)

#         # form_col10, _ = st.columns(2)
#         # with form_col10:

#         #     has_demand = st.checkbox(
#         #         "Has a formal demand been received?",
#         #         value=use_prefill("Has_Demand", False)
#         #     )

#         #     if has_demand:
#         #         demand = st.number_input(
#         #             "Enter Plaintiff Demand ($)",
#         #             min_value=0, max_value=10000000,
#         #             value=use_prefill("Demand_Amount", 150000),
#         #             step=5000
#         #         )
#         #     else:
#         #         demand = 0
#         #         st.info("ℹ️ No demand entered. System will calculate 'Likelihood of Acceptance' accordingly.")

#         # st.markdown("---")

#         # # === C. BEHAVIORAL PROGRESSION ===
#         # st.markdown("<span class='form-section-label'>📊 C. Behavioral Progression</span>", unsafe_allow_html=True)

#         # form_col11, form_col12 = st.columns(2)
#         # with form_col11:
#         #     days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
#         # with form_col12:
#         #     days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)

#         # form_col13, form_col14 = st.columns(2)
#         # with form_col13:
#         #     treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
#         # with form_col14:
#         #     provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)

#         # form_col15, _ = st.columns(2)
#         # with form_col15:
#         #     opioid = st.checkbox("Opioid Prescription Indicator?")

#         # st.markdown("---")

#         # # === D. CLAIMANT PROFILE ===
#         # st.markdown("<span class='form-section-label'>👤 D. Claimant Profile</span>", unsafe_allow_html=True)

#         # form_col16, form_col17 = st.columns(2)
#         # with form_col16:
#         #     employment = st.selectbox(
#         #         "Employment Status",
#         #         ['Active', 'Terminated', 'Retired', 'Leave of Absence']
#         #     )
#         # with form_col17:
#         #     benefit = st.selectbox(
#         #         "Impairment Rating",
#         #         ['Temporary Total Disability', 'Permanent Partial Disability ', 'Medical Only']
#         #     )

#         # form_col18, _ = st.columns(2)
#         # with form_col18:
#         #     msa = st.checkbox("Medicare Set-Aside (MSA) Required?")

#         # st.markdown("---")

#         # # === E. MEDICAL PROFILE ===
#         # st.markdown("<span class='form-section-label'>🏥 E. Medical Profile</span>", unsafe_allow_html=True)

#         # form_col19, form_col20 = st.columns(2)
#         # with form_col19:
#         #     comorbidity = st.selectbox(
#         #         "Comorbidities",
#         #         ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions']
#         #     )
#         # with form_col20:
#         #     odg = st.selectbox(
#         #         "ODG Guidelines Adherence",
#         #         ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds']
#         #     )

#         # st.markdown("---")

#         # # === F. LITIGATION INTELLIGENCE ===
#         # st.markdown("<span class='form-section-label'>📋 F. Litigation Intelligence</span>", unsafe_allow_html=True)

#         # form_col21, form_col22 = st.columns(2)
#         # with form_col21:
#         #     attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
#         # with form_col22:
#         #     attorney_type = st.selectbox(
#         #         "Attorney Settlement Tendency",
#         #         ['Early Settlement', 'Balanced', 'Trial-Oriented']
#         #     )

#         # form_col23, _ = st.columns(2)
#         # with form_col23:
#         #     judge = st.selectbox(
#         #         "Judge Propensity (if assigned)",
#         #         ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned']
#         #     )

            
#         # --- 1. CLAIMANT PROFILE (New First Section - Expanded) ---
#         with st.expander("👤 1. Claimant Profile", expanded=True):
            
#             col_age, col_tenure = st.columns(2)
#             with col_age:
#                 # NEW FIELD: Claimant Age
#                 claimant_age = st.number_input("Claimant Age", min_value=18, max_value=99, value=45)
#             with col_tenure:
#                 # NEW FIELD: Tenure
#                 tenure = st.number_input("Tenure (Years at Employer)", min_value=0, max_value=50, value=5)

#             col_occup, col_employ = st.columns(2)
#             with col_occup:
#                 # NEW FIELD: Occupation
#                 occupation = st.selectbox(
#                     "Occupation Type",
#                     ['Clerical/Office', 'Light Manual', 'Heavy Manual', 'Professional', 'Service Industry']
#                 )
#             with col_employ:
#                 # EXISTING FIELD: Employment Status (Moved)
#                 employment = st.selectbox(
#                     "Employment Status",
#                     ['Active', 'Terminated', 'Retired', 'Leave of Absence']
#                 )

#             col_dependents, col_engaged = st.columns(2)
#             with col_dependents:
#                 # EXISTING NEW FIELD: Dependents
#                 dependents_count = st.number_input("Number of Dependents", min_value=0, max_value=10, value=2)
#             with col_engaged:
#                 # NEW FIELD: Engaged Claimant
#                 engaged_claimant = st.checkbox("Engaged with Medical Provider (Compliance)?")
                
#             col_claim, col_social = st.columns(2)
#             with col_claim:
#                 # EXISTING NEW FIELD: Previous Claim History
#                 previous_claim_flag = st.checkbox("Previous Litigation/Claim History?")
#             with col_social:
#                 # EXISTING NEW FIELD: Social Media Risk
#                 social_media_risk = st.selectbox(
#                     "Social Media Activity Risk",
#                     ['Low (Private/Inactive)', 'Moderate (Active)', 'High (Contradictory)']
#                 )
            

#         # --- 2. LITIGATION & EXPOSURE (Second Section - Expanded) ---
#         with st.expander("🏛️ 2. Litigation & Exposure", expanded=True):
            
#             form_col1, form_col2 = st.columns(2)
#             with form_col1:
#                 jurisdiction = st.selectbox(
#                     "Jurisdiction",
#                     ['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'],
#                     index=['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania']
#                     .index(use_prefill("Jurisdiction", "New Jersey"))
#                 )
#             with form_col2:
#                 venue_win_rate = st.slider("Defense Win Rate in Venue (General)", 0.0, 1.0, 0.45) # CLARIFIED LABEL

#             form_col3, form_col4 = st.columns(2)
#             with form_col3:
#                 attorney_firm = st.selectbox(
#                     "Plaintiff Counsel",
#                     ['Weitz & Luxenberg', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner']
#                 )
#             with form_col4:
#                 attorney_score = st.slider(
#                     "Plaintiff Attorney Aggressiveness Score (0-100)", # CLARIFIED LABEL
#                     0, 100, 
#                     use_prefill("Attorney_Score", 65)
#                 )

#             form_col5, form_col6 = st.columns(2)
#             with form_col5:
#                 attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
#             with form_col6:
#                 attorney_type = st.selectbox(
#                     "Attorney Settlement Tendency",
#                     ['Early Settlement', 'Balanced', 'Trial-Oriented']
#                 )
            
#             form_col7, _ = st.columns(2)
#             with form_col7:
#                 judge = st.selectbox(
#                     "Judge Propensity (if assigned)",
#                     ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned']
#                 )


#         # --- 3. ECONOMIC DAMAGES (Third Section - Expanded) ---
#         with st.expander("💰 3. Economic Damages & Demand", expanded=True):
            
#             form_col8, form_col9 = st.columns(2)
#             with form_col8:
#                 wage_loss = st.number_input(
#                     "Wage Loss Exposure ($) - Estimated Total Liability", # CLARIFIED LABEL
#                     5000, 500000,
#                     use_prefill("Wage_Loss_Exposure", 25000)
#                 )
#             with form_col9:
#                 # EXISTING FIELD: Permanent Impairment (%)
#                 impairment = st.slider(
#                     "Permanent Impairment (%)",
#                     0, 100,
#                     use_prefill("Impairment_Rating", 15)
#                 )

#             form_col10, form_col11 = st.columns(2)
#             with form_col10:
#                 medical_trajectory = st.selectbox(
#                     "Medical Cost Trajectory (Future Liability)", # CLARIFIED LABEL
#                     ['Low', 'Moderate', 'High', 'Escalating']
#                 )
#             with form_col11:
#                 future_medical = st.checkbox("Future Medical Exposure?", value=True)

#             form_col12, _ = st.columns(2)
#             with form_col12:
#                 has_demand = st.checkbox(
#                     "Has a formal demand been received?",
#                     value=use_prefill("Has_Demand", False)
#                 )

#                 if has_demand:
#                     demand = st.number_input(
#                         "Enter Plaintiff Demand ($)",
#                         min_value=0, max_value=10000000,
#                         value=use_prefill("Demand_Amount", 150000),
#                         step=5000
#                     )
#                 else:
#                     demand = 0
#                     st.info("ℹ️ No demand entered. System will calculate 'Likelihood of Acceptance' accordingly.")


#         # --- 4. MEDICAL & BEHAVIORAL PROGRESSION (Last Section - Collapsed) ---
#         with st.expander("🏥 4. Medical & Behavioral Progression", expanded=False):
            
#             col_injury, col_body = st.columns(2)
#             with col_injury:
#                 # NEW FIELD: Injury Type
#                 injury_type = st.selectbox(
#                     "Injury Type",
#                     ['Soft Tissue Strain', 'Fracture', 'Herniated Disc', 'Head Injury', 'Amputation', 'Other']
#                 )
#             with col_body:
#                 # NEW FIELD: Body Part Involved
#                 body_part = st.selectbox(
#                     "Body Part Involved",
#                     ['Lumbar Spine', 'Cervical Spine', 'Knee', 'Shoulder', 'Hand/Wrist', 'Multiple']
#                 )

#             col_surgery, col_hosp = st.columns(2)
#             with col_surgery:
#                 # NEW FIELD: Need for Surgery
#                 need_for_surgery = st.checkbox("Need for Surgery?")
#             with col_hosp:
#                 # NEW FIELD: Need for Hospitalization
#                 need_for_hosp = st.checkbox("Need for Hospitalization?")

#             col_provider, col_comorbid = st.columns(2)
#             with col_provider:
#                 # EXISTING FIELD: Primary Provider
#                 provider_type = st.selectbox(
#                     "Primary Provider",
#                     ['Chiropractor', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Physical Therepy']
#                 )
#             with col_comorbid:
#                 # EXISTING FIELD: Comorbidities
#                 comorbidity = st.selectbox(
#                     "Comorbidities",
#                     ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions']
#                 )
            
#             col_odg, col_msa = st.columns(2)
#             with col_odg:
#                 # EXISTING FIELD: ODG Adherence
#                 odg = st.selectbox(
#                     "ODG Guidelines Adherence",
#                     ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds']
#                 )
#             with col_msa:
#                 # EXISTING FIELD: MSA
#                 msa = st.checkbox("Medicare Set-Aside (MSA) Required?")

#             st.markdown("<h5 style='color:#cbd5e1; margin-top:20px;'>Case Progression Timeline</h5>", unsafe_allow_html=True)
            
#             col_filed, col_attorney = st.columns(2)
#             with col_filed:
#                 # EXISTING FIELD: Days Since Filed
#                 days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
#             with col_attorney:
#                 # EXISTING FIELD: Days Since Attorney Engaged
#                 days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)

#             col_duration, col_shopping = st.columns(2)
#             with col_duration:
#                 # EXISTING FIELD: Treatment Duration
#                 treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
#             with col_shopping:
#                 # EXISTING FIELD: Provider Shopping Count
#                 provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)

#             col_opioid, _ = st.columns(2)
#             with col_opioid:
#                 # EXISTING FIELD: Opioid Indicator
#                 opioid = st.checkbox("Opioid Prescription Indicator?")

#         st.markdown("---")

        
#         # # Submit Button
#         # submitted = st.button("🚀 ANALYZE CASE", use_container_width=True)
#         # if submitted:
#         #     # Store all form values in session state
#         #     st.session_state.jurisdiction = jurisdiction
#         #     st.session_state.venue_win_rate = venue_win_rate
#         #     st.session_state.attorney_firm = attorney_firm
#         #     st.session_state.attorney_score = attorney_score
#         #     st.session_state.provider_type = provider_type
#         #     st.session_state.wage_loss = wage_loss
#         #     st.session_state.impairment = impairment
#         #     st.session_state.medical_trajectory = medical_trajectory
#         #     st.session_state.future_medical = future_medical
#         #     st.session_state.demand = demand
#         #     st.session_state.days_filed = days_filed
#         #     st.session_state.days_attorney = days_attorney
#         #     st.session_state.treatment_duration = treatment_duration
#         #     st.session_state.opioid = opioid
#         #     st.session_state.provider_shopping = provider_shopping
#         #     st.session_state.employment = employment
#         #     st.session_state.benefit = benefit
#         #     st.session_state.msa = msa
#         #     st.session_state.comorbidity = comorbidity
#         #     st.session_state.odg = odg
#         #     st.session_state.attorney_winrate = attorney_winrate
#         #     st.session_state.attorney_type = attorney_type
#         #     st.session_state.judge = judge
#         #     st.session_state.submitted = True
#         #     st.rerun()

#         # Submit Button
#         submitted = st.button("🚀 ANALYZE CASE", use_container_width=True)
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
            
#             # --- NEW CLAIMANT FIELDS ---
#             st.session_state.claimant_age = claimant_age
#             st.session_state.occupation = occupation
#             st.session_state.tenure = tenure
#             st.session_state.engaged_claimant = engaged_claimant
#             st.session_state.dependents_count = dependents_count
#             st.session_state.previous_claim_flag = previous_claim_flag
#             st.session_state.social_media_risk = social_media_risk
            
#             # --- MEDICAL / OLD FIELDS ---
#             st.session_state.msa = msa
#             st.session_state.comorbidity = comorbidity
#             st.session_state.odg = odg
#             st.session_state.attorney_winrate = attorney_winrate
#             st.session_state.attorney_type = attorney_type
#             st.session_state.judge = judge
            
#             # --- NEW MEDICAL FIELDS ---
#             st.session_state.injury_type = injury_type
#             st.session_state.body_part = body_part
#             st.session_state.need_for_surgery = need_for_surgery
#             st.session_state.need_for_hosp = need_for_hosp

#             st.session_state.submitted = True
#             st.rerun()
    
#     st.markdown("</div>", unsafe_allow_html=True)

# # === DASHBOARD VIEW ===
# else:
#     import model

#     # Get form data from session state
#     # inputs = {
#     #     "Jurisdiction": st.session_state.jurisdiction,
#     #     "Venue_Win_Rate": st.session_state.venue_win_rate,
#     #     "Plaintiff_Attorney": st.session_state.attorney_firm,
#     #     "Attorney_Score": st.session_state.attorney_score,
#     #     "Provider_Type": st.session_state.provider_type,
#     #     "Wage_Loss_Exposure": st.session_state.wage_loss,
#     #     "Impairment_Rating": st.session_state.impairment,
#     #     "Medical_Trajectory": st.session_state.medical_trajectory,
#     #     "Future_Medical": 1 if st.session_state.future_medical else 0,
#     #     "Demand_Amount": st.session_state.demand,
#     #     "Days_Since_Filed": st.session_state.days_filed,
#     #     "Days_Attorney_Engaged": st.session_state.days_attorney,
#     #     "Treatment_Duration": st.session_state.treatment_duration,
#     #     "Opioid_Indicator": 1 if st.session_state.opioid else 0,
#     #     "Provider_Shopping": st.session_state.provider_shopping,
#     #     "Employment_Status": st.session_state.employment,
#     #     "Benefit_Status": st.session_state.benefit,
#     #     "MSA_Flag": 1 if st.session_state.msa else 0,
#     #     "Comorbidities": st.session_state.comorbidity,
#     #     "Guidelines_Adherence": st.session_state.odg,
#     #     "Attorney_Win_Rate": st.session_state.attorney_winrate,
#     #     "Attorney_Tendency": st.session_state.attorney_type,
#     #     "Judge_Propensity": st.session_state.judge
#     # }
    
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
#         "Benefit_Status": "N/A",
#         # --- NEW CLAIMANT FIELDS ---
#         "Claimant_Age": st.session_state.claimant_age,
#         "Occupation": st.session_state.occupation,
#         "Tenure": st.session_state.tenure,
#         "Engaged_Claimant": 1 if st.session_state.engaged_claimant else 0,
#         "Dependents_Count": st.session_state.dependents_count,
#         "Previous_Claim_Flag": 1 if st.session_state.previous_claim_flag else 0,
#         "Social_Media_Risk": st.session_state.social_media_risk,
        
#         # --- NEW MEDICAL FIELDS ---
#         "Injury_Type": st.session_state.injury_type,
#         "Body_Part": st.session_state.body_part,
#         "Need_for_Surgery": 1 if st.session_state.need_for_surgery else 0,
#         "Need_for_Hosp": 1 if st.session_state.need_for_hosp else 0,
        
#         # --- OLD/RETAINED FIELDS ---
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
#     # === 1. CALCULATE CONFIDENCE SCORE (DEFINE IT HERE) ===
#     confidence_score = 90
    
#     # Apply penalties based on inputs
#     if inputs['Attorney_Score'] > 80: confidence_score -= 10
#     if inputs['Medical_Trajectory'] == 'Escalating': confidence_score -= 15
#     if inputs['Days_Since_Filed'] < 60: confidence_score -= 10
#     if inputs['Judge_Propensity'] == 'Not Yet Assigned': confidence_score -= 5
    
#     # Cap between 0 and 100
#     confidence_score = max(0, min(100, confidence_score))
    
#     # Define Label for Header
#     conf_label_header = "High Confidence" if confidence_score >= 80 else "Medium Confidence"
#     # === DASHBOARD HEADER ===
#     rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
#     col_header_left, col_header_right = st.columns(2)
    
#     # with col_header_left:
#     #     st.markdown(f"""
#     #         <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
#     #         <div class='dashboard-subtitle'>{res['action_desc']}<br>
#     #         📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </b></div>
#     #     """, unsafe_allow_html=True)
    
#     with col_header_left:
#         st.markdown(f"""
#             <div class='dashboard-title' style='color:#1e293b;'>{rec_emoji} {res['action']}</div>
#             <div class='dashboard-subtitle' style='color:#475569;'>{res['action_desc']}<br>
#             📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </b></div>
#         """, unsafe_allow_html=True)
    
    
#     st.markdown("---")
    
#     # === KPI CARDS ===
#     col1, col2, col3, col4 = st.columns(4)
    
    
#     with col1:
#         # SWAPPED: Range is now the Big Value, Target is the Subtext
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>💵 Settlement Range</div>
#                 <div class='kpi-value'>${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Estimated value: ${res['prediction']/1000:.0f}K</div>
#             </div>
#         """, unsafe_allow_html=True)
#     with col2:
#         # 1. Calculate Base Confidence Score (0-100%)
#         base_score = 90
        
#         # Penalties (reduce the base score)
#         if inputs['Attorney_Score'] > 80: base_score -= 10
#         if inputs['Medical_Trajectory'] == 'Escalating': base_score -= 15
#         if inputs['Days_Since_Filed'] < 60: base_score -= 10
#         if inputs['Judge_Propensity'] == 'Not Yet Assigned': base_score -= 5
        
#         # 2. Calculate the Interval (Width of the range)
#         # If the case is risky, the interval is wider (more uncertainty)
#         interval_width = 5 
#         if base_score < 75: interval_width = 10 
        
#         low_ci = max(base_score - interval_width, 10)
#         high_ci = min(base_score + interval_width, 99)
        
#         # 3. Determine Color
#         if low_ci >= 75:
#             conf_color = "#16a34a" # Green
#             label_text = "Strong Predictability"
#         elif low_ci >= 55:
#             conf_color = "#f59e0b" # Orange
#             label_text = "Moderate Certainty"
#         else:
#             conf_color = "#dc2626" # Red
#             label_text = "Low Data Density"

#         # 4. Render Card
#         st.markdown(f"""
#             <div class='kpi-card' style='border-bottom: 4px solid {conf_color};'>
#                 <div class='kpi-label'>📉 Confidence Interval</div>
#                 <div class='kpi-value' style='color: {conf_color};'>{low_ci}% – {high_ci}%</div>
#                 <div class='kpi-subtext'>{label_text}</div>
#             </div>
#         """, unsafe_allow_html=True)
    
    
    
    
#     with col3:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>⏱️ Est. Duration</div>
#                 <div class='kpi-value'>{res['days']}d</div>
#                 <div class='kpi-subtext'>≈ {res['months']:.1f} months</div>
#             </div>
#         """, unsafe_allow_html=True)
#     with col4:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>📊 Total Exposure</div>
#                 <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Verdict + Defense</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("")
#     # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
    
#     # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
#     # Only show this section if NO demand was entered (Simulated)
#     if res['demand_source'] == 'Simulated':
#         st.markdown("<div class='section-header'>🤝 Negotiation Intelligence</div>", unsafe_allow_html=True)
        
#         prob = res['acceptance_likelihood']
        
#         # Color Logic for the Bar
#         if prob >= 70: 
#             p_color = "#16a34a" # Green
#             p_msg = "High probability of early resolution at Target Value."
#         elif prob >= 40: 
#             p_color = "#f59e0b" # Orange
#             p_msg = "Moderate resistance expected. May require mediation."
#         else: 
#             p_color = "#dc2626" # Red
#             p_msg = "Low probability. Plaintiff counsel likely to push for trial."

#         # 1. Render the Full-Width Probability Bar
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%); border: 1px solid #3b82f6; border-radius: 12px; padding: 25px; margin-bottom: 20px;'>
#                 <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
#                     <span style='color: #cbd5e1; font-weight: 600;'>Likelihood of Acceptance at Target Value (${res['prediction']:,.0f})</span>
#                     <span style='color: {p_color}; font-weight: 800; font-size: 1.2rem;'>{prob}%</span>
#                 </div>
#                 <div style='width: 100%; background-color: #334155; border-radius: 10px; height: 12px;'>
#                     <div style='width: {prob}%; background-color: {p_color}; height: 12px; border-radius: 10px; transition: width 1s ease;'></div>
#                 </div>
#                 <div style='color: #94a3b8; font-size: 0.9rem; margin-top: 15px;'>
#                     <i>Strategy Note: {p_msg}</i>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#         # 2. Acceptance Curve Visualization (Added Graph)
#         st.markdown("<h5 style='color: #cbd5e1; margin-bottom: 10px;'>📉 Offer vs. Acceptance Probability Curve</h5>", unsafe_allow_html=True)
        
#         target = res['prediction']
        
#         # Create a range of offers (from 50% to 150% of the target value)
#         x_vals = np.linspace(target * 0.5, target * 1.5, 100)
        
#         # MATH: Dynamic Sigmoid Curve logic
#         k = 10 / target 
#         prob_safe = max(1, min(99, prob)) # Safety clamp
        
#         # Shift curve based on probability score
#         shift = target + (np.log(100/prob_safe - 1) / k)
        
#         # Generate Y values (0-100%)
#         y_vals = 100 / (1 + np.exp(-k * (x_vals - shift)))
        
#         fig_curve = go.Figure()
        
#         # The Curve Line
#         fig_curve.add_trace(go.Scatter(
#             x=x_vals, y=y_vals,
#             mode='lines',
#             line=dict(color='#60A5FA', width=4),
#             fill='tozeroy',
#             fillcolor='rgba(96, 165, 250, 0.1)',
#             name='Acceptance Chance'
#         ))
        
#         # The "You Are Here" Marker
#         fig_curve.add_trace(go.Scatter(
#             x=[target], y=[prob],
#             mode='markers',
#             marker=dict(color='#F59E0B', size=15, line=dict(color='white', width=2)),
#             name='Current Target',
#             hoverinfo='text',
#             hovertext=f"Target: ${target:,.0f}<br>Probability: {prob}%"
#         ))

#         fig_curve.update_layout(
#             height=300,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             xaxis=dict(title="Offer Amount ($)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), showgrid=False, tickprefix="$"),
#             yaxis=dict(title="Probability (%)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), range=[0, 105], showgrid=True, gridcolor='#334155'),
#             showlegend=False,
#             hovermode="x unified"
#         )
        
#         st.plotly_chart(fig_curve, use_container_width=True)
#     # === DRIVER ANALYSIS (Like Image) ===
#     # === ZOPA CURVE ===
#     # st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
#     # mu = res['prediction']
#     # sigma = mu * 0.12
#     # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
#     # y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
#     # fig_zopa = go.Figure()
    
#     # # Full distribution curve
#     # fig_zopa.add_trace(go.Scatter(
#     #     x=x, y=y,
#     #     mode='lines',
#     #     line=dict(color='#64748B', width=2),
#     #     fill='tozeroy',
#     #     fillcolor='rgba(59, 130, 246, 0.1)',
#     #     name='Distribution'
#     # ))
    
#     # # Safe settlement zone
#     # x_safe = np.linspace(res['range_low'], res['range_high'], 150)
#     # y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
#     # fig_zopa.add_trace(go.Scatter(
#     #     x=x_safe, y=y_safe,
#     #     mode='lines',
#     #     line=dict(width=0),
#     #     fill='tozeroy',
#     #     fillcolor='rgba(22, 163, 74, 0.5)',
#     #     name='Safe Zone'
#     # ))
    
#     # fig_zopa.update_layout(
#     #     height=350,
#     #     showlegend=True,
#     #     paper_bgcolor='rgba(0,0,0,0)',
#     #     plot_bgcolor='rgba(0,0,0,0)',
#     #     font=dict(color='#e2e8f0', family='Poppins'),
#     #     margin=dict(l=50, r=50, t=40, b=40),
#     #     xaxis_title='Settlement Amount ($)',
#     #     yaxis_title='Probability Density',
#     #     hovermode='x unified'
#     # )
#     # st.plotly_chart(fig_zopa, use_container_width=True)
    
#     # st.markdown("")
    
#     # === ZOPA CURVE (Dynamic Logic + Your Style) ===
#     st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
#     mu = res['prediction']
    
#     # --- CHANGED: DYNAMIC WIDTH LOGIC ---
#     # Instead of static 0.12, we calculate based on Confidence Score
#     # High Conf (100) = Narrow (0.05). Low Conf (50) = Wide (0.20).
#     sigma_pct = 0.20 - ((confidence_score - 50) / 50 * 0.15)
#     sigma_pct = max(0.05, min(0.20, sigma_pct)) # Clamp limits
#     sigma = mu * sigma_pct
#     # ------------------------------------
    
#     x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
#     fig_zopa = go.Figure()
    
#     # Full distribution curve (Your Style)
#     fig_zopa.add_trace(go.Scatter(
#         x=x, y=y,
#         mode='lines',
#         line=dict(color='#64748B', width=2),
#         fill='tozeroy',
#         fillcolor='rgba(59, 130, 246, 0.1)',
#         name='Distribution'
#     ))
    
#     # Safe settlement zone (Your Style)
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
    
#     # Layout (Your Exact Settings)
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
#     # === 7. EXPLAINABILITY & STRATEGIC ANALYSIS (SHAP-STYLE SIMPLIFIED) ===
#     st.markdown("<div class='section-header'>📈 Model Explainability & Strategic Analysis</div>", unsafe_allow_html=True)
    
#     # Extract variables from inputs
#     attorney_score = inputs['Attorney_Score']
#     venue_win_rate = inputs['Venue_Win_Rate']
#     impairment = inputs['Impairment_Rating']
#     wage_loss = inputs['Wage_Loss_Exposure']
#     employment = inputs['Employment_Status']
#     opioid = inputs['Opioid_Indicator']
#     days_filed = inputs['Days_Since_Filed']
#     medical_trajectory = inputs['Medical_Trajectory']
#     future_medical = inputs['Future_Medical']
#     attorney_type = inputs['Attorney_Tendency']
    
#     # Calculate feature importance scores - ALWAYS include meaningful features
#     feature_importance = []
    
#     # ALWAYS calculate base factors (don't use high thresholds)
#     # Attorney contribution
#     attorney_impact = (attorney_score - 40) * 150  # Scale from base
#     feature_importance.append(('Attorney Score', attorney_score, attorney_impact, f'{attorney_score}/100 aggressiveness'))
    
#     # Venue contribution
#     venue_impact = (0.50 - venue_win_rate) * 80000  # Negative venue = higher impact
#     feature_importance.append(('Venue Win Rate', f'{int(venue_win_rate*100)}%', venue_impact, f'{int(venue_win_rate*100)}% defense win rate'))
    
#     # Impairment contribution (MAJOR DRIVER)
#     if impairment > 0:
#         impair_impact = impairment * 1500
#         feature_importance.append(('Impairment Rating', f'{impairment}%', impair_impact, f'{impairment}% permanent injury'))
    
#     # Wage loss contribution
#     if wage_loss > 0:
#         wage_impact = wage_loss * 0.6
#         feature_importance.append(('Wage Loss Exposure', f'${wage_loss:,}', wage_impact, f'Lost wages: ${wage_loss:,}'))
    
#     # Employment status (binary impact)
#     if employment == 'Terminated':
#         feature_importance.append(('Employment Status', employment, 25000, 'Terminated = emotional damages premium'))
#     else:
#         feature_importance.append(('Employment Status', employment, 0, 'Standard employment relationship'))
    
#     # Opioid indicator
#     if opioid == 1:
#         feature_importance.append(('Opioid Indicator', 'Yes', 14000, 'Opioid usage increases narrative risk'))
#     else:
#         feature_importance.append(('Opioid Indicator', 'No', 0, 'No opioid complications'))
    
#     # Medical trajectory
#     if medical_trajectory == 'Escalating':
#         traj_impact = 20000
#     elif medical_trajectory == 'High':
#         traj_impact = 12000
#     elif medical_trajectory == 'Moderate':
#         traj_impact = 5000
#     else:
#         traj_impact = -3000
#     feature_importance.append(('Medical Trajectory', medical_trajectory, traj_impact, f'{medical_trajectory} medical costs'))
    
#     # Days filed contribution
#     if days_filed > 0:
#         days_impact = (days_filed / 365) * 8000  # Scale by years
#         feature_importance.append(('Days Since Filed', days_filed, days_impact, f'{days_filed} days open'))
    
#     # Attorney type
#     if attorney_type == 'Trial-Oriented':
#         att_type_impact = 16000
#     elif attorney_type == 'Balanced':
#         att_type_impact = 4000
#     else:
#         att_type_impact = -5000
#     feature_importance.append(('Attorney Type', attorney_type, att_type_impact, f'{attorney_type} approach'))
    
#     # Future medical
#     if future_medical == 1:
#         feature_importance.append(('Future Medical', 'Yes', 10000, 'Requires settlement reserves'))
#     else:
#         feature_importance.append(('Future Medical', 'No', 0, 'No future medical needed'))
    
#     # Sort by absolute impact value (descending)
#     feature_importance = sorted(feature_importance, key=lambda x: abs(x[2]), reverse=True)
    
#     # Filter out zero-impact factors
#     feature_importance = [f for f in feature_importance if abs(f[2]) > 500]
    
#     base_value = res['prediction']
    
#     # RENDER CLEAN EXPLANATION
#     st.markdown(f"## 🧾 What Drove the ${base_value:,.0f} Prediction")
#     st.divider()
    
#     st.markdown("### Top Factors Contributing to Settlement Value")
    
#     for i, (feature, value, impact, desc) in enumerate(feature_importance[:6], 1):
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.write(f"**{i}. {feature}**")
#             st.caption(f"Value: `{value}` • {desc}")
        
#         with col2:
#             impact_pct = (abs(impact) / base_value) * 100 if base_value > 0 else 0
#             color = "🔴" if impact > 0 else "🟢"
#             st.write(f"{color} ${abs(impact):,.0f}\n({impact_pct:.1f}%)")
    
#     st.divider()
    
#     # Build narrative summary
#     if len(feature_importance) >= 3:
#         top_3 = feature_importance[:3]
        
#         summary_text = f"""
# ### 📊 Why This Settlement Value

# **The model considered {len(feature_importance)} key factors:**

# 1. **{top_3[0][0]}** ({top_3[0][1]})  
#    Contribution: ${abs(top_3[0][2]):,.0f} ({abs(top_3[0][2])/base_value*100:.1f}%)  
#    → {top_3[0][3]}

# 2. **{top_3[1][0]}** ({top_3[1][1]})  
#    Contribution: ${abs(top_3[1][2]):,.0f} ({abs(top_3[1][2])/base_value*100:.1f}%)  
#    → {top_3[1][3]}

# 3. **{top_3[2][0]}** ({top_3[2][1]})  
#    Contribution: ${abs(top_3[2][2]):,.0f} ({abs(top_3[2][2])/base_value*100:.1f}%)  
#    → {top_3[2][3]}

# **Result:** These three factors account for **{sum([abs(f[2]) for f in top_3])/base_value*100:.1f}%** of the final ${base_value:,.0f} prediction.
#         """
#         st.markdown(summary_text)
    
#     st.divider()
    
#     # Final recommendation
#     st.markdown("### 🎯 Recommendation")
    
#     if confidence_score >= 75:
#         st.success("✅ **SETTLE** - Key factors clearly support settlement negotiations.")
#     elif confidence_score >= 55:
#         st.warning("⚡ **STRATEGIZE** - Mixed factors require careful case management.")
#     else:
#         st.error("⚔️ **LITIGATE** - High-risk factors warrant trial preparation.")
#     # === RISK ALERTS ===
    
    
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
    
    
    
    
    
    

    
#     # === RESET & NAVIGATION BUTTONS ===
#     st.markdown("---")
#     col_reset_1, col_reset_2 = st.columns(2)

#     # BUTTON 1: Return to Landing Page
#     with col_reset_1:
#         if st.button("🏠 RETURN TO MAIN PAGE", use_container_width=True, key="btn_main_page"):
#             # Reset everything
#             st.session_state.submitted = False
#             st.session_state.scenario_selected = False
#             st.session_state.prefill = {}

#             # Clear result variables
#             for key in ["prediction", "recommendation", "risk", "driver_scores", "chart_data"]:
#                 if key in st.session_state:
#                     del st.session_state[key]

#             st.rerun()

#     # BUTTON 2: Analyze New Case (skip landing page, keep scenario)
#     with col_reset_2:
#         if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="btn_new_case"):
#             # Only reset submission
#             st.session_state.submitted = False
#             st.rerun()






















# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import os
# from dotenv import load_dotenv
# import random

# # Load environment variables
# load_dotenv()


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
    
#     /* === NEUTRAL CHARCOAL THEME (No Blue) === */
    
#     .stApp {
#         background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
#         font-family: 'Poppins', sans-serif;
#         color: #e2e8f0;
#     }
#     /* Make the Form Container a Lighter Grey to pop */
#     .form-container {
#         background: linear-gradient(135deg, #27272a 0%, #3f3f46 100%) !important;
#         border: 1px solid #52525b !important; /* Neutral Grey Border */
#         box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
#         padding: 50px;
#         border-radius: 20px;
#         max-width: 1200px;
#         margin: 40px auto;
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
    
#     .kpi-value {
#         font-size: 1.8rem; /* Reduced from 2.2rem to fit better */
#         color: #f1f5f9;
#         font-weight: 800;
#         margin: 5px 0; /* Reduced margin */
#         font-family: 'Playfair Display', serif;
#         letter-spacing: 0.5px; /* Reduced spacing */
#         white-space: nowrap; /* Prevents wrapping */
#     }
    
#     .kpi-label {
#         font-size: 0.7rem; /* Slightly smaller label */
#         color: #94a3b8;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         margin-bottom: 5px;
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
    

#     /* Force all Streamlit input labels to be White */
#     label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
#         color: #e2e8f0 !important;
#         font-size: 0.85rem !important;
#         font-weight: 600 !important;
#         letter-spacing: 0.8px !important;
#     }

#     /* Ensure text typed inside numbers/selects is White */
#     input[type="number"], div[data-baseweb="select"] span {
#         color: #ffffff !important;
#         -webkit-text-fill-color: #ffffff !important;
#     }
#     add this css :
 
 
 
# /* === EXPANDER FIX (HIGH CONTRAST & VISIBILITY) === */
#     /* Target the main container of the expander */
#     div[data-testid="stExpander"] {
#         border: 1px solid #334155 !important;
#         border-radius: 12px !important;
#         background-color: transparent !important;
#         margin-bottom: 15px !important;
#     }
 
#     /* Target the Header (The clickable <summary> element) */
#     div[data-testid="stExpander"] > details > summary {
#         background-color: #1e293b !important; /* Dark Blue Header Background */
#         color: #ffffff !important; /* Pure White Text */
#         font-weight: 1200 !important;
#         font-size: 3 rem !important;
#         padding: 15px 20px !important;
#         /* Ensure the corners of the summary match the border radius of the parent */
#         border-radius: 11px 11px 0 0 !important;
#     }
 
#     /* Target the Content Body inside the expander */
#     div[data-testid="stExpander"] > details > div {
#         background-color: #0f172a !important; /* Very Dark Blue Body */
#         color: #e2e8f0 !important;
#         padding: 20px !important;
#         border-top: 1px solid #334155 !important;
#     }
   
#     /* Force the arrow icon to be white */
#     div[data-testid="stExpander"] > details > summary > svg {
#         fill: #ffffff !important;
#         color: #ffffff !important;
#     }
#     /* Target for FORM submit button (NEW RULE) */
#     /* This targets the button inside the stFormSubmitButton container */
#     [data-testid="stFormSubmitButton"] > button {
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
#         width: 100%; /* Ensure it matches the full-width setting */
#     }
#     div.stButton > button:hover,
#     [data-testid="stFormSubmitButton"] > button:hover {
#         transform: translateY(-3px);
#         box-shadow: 0 12px 36px rgba(37, 99, 235, 0.5);
#     }
#     /* --- NEW RULE FOR HEADER TEXT --- */
# .dashboard-text {
#     /* Use a standard, non-gradient color for the main text */
#     color: #f1f5f9 !important;
#     /* Inherit the size/font from the original .dashboard-title, but remove the gradient logic */
#     font-family: 'Playfair Display', serif;
#     font-size: 2.5rem;
#     font-weight: 700;
# }
 
#     </style>
# """, unsafe_allow_html=True)









# # ✅ STEP 1: Jurisdiction-wise monthly defense cost mapping
# jurisdiction_cost_map = {
#     "New York": (30000, 40000),
#     "California": (28000, 38000),
#     "Illinois": (22000, 32000),
#     "New Jersey": (15000, 25000),
#     "NJ": (15000, 25000),
#     "Florida": (18000, 25000),
#     "Texas": (15000, 22000),
#     "Pennsylvania": (14000, 20000),
#     "Georgia": (12000, 18000),
#     "Ohio": (10000, 16000),
# }

# # === INITIALIZE SESSION STATE ===
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False
# # === NEW: LANDING PAGE WITH THREE SCENARIOS ===

# if "scenario_selected" not in st.session_state:
#     st.session_state.scenario_selected = False

# if st.session_state.submitted:
#     st.markdown(
#         """
#         <script>
#             // Use setTimeout to ensure the Streamlit content has loaded before scrolling
#             setTimeout(function() {
#                 window.scrollTo(0, 0); // Scrolls to the top-left corner
#             }, 50); 
#         </script>
#         """, 
#         unsafe_allow_html=True
#     )

# if not st.session_state.scenario_selected:

#     st.markdown("""
#         <div style='text-align:center; margin-top:60px;'>
           
#            <h1 style='font-family:Poppins; font-size:3rem; color:white;'>⚖️ Litigation Settlement Analyzer</h1>
#             <p style='color:#cbd5e1; font-size:1.2rem;'>
#                 Select a scenario to pre-fill the case details
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

#     c1, c2, c3, c4 = st.columns(4)   # ← changed from 3 to 4 columns


#     with c1:
#         if st.button("✅ Scenario 1", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 90,
#                 "Impairment_Rating": 15,
#                 "Wage_Loss_Exposure": 45000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 170000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()

#     with c2:
#         if st.button("⚡ Scenario 2", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 60,
#                 "Impairment_Rating": 12,
#                 "Wage_Loss_Exposure": 35000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 175000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()

#     with c3:
#         if st.button("⚔️ Scenario 3", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 50,
#                 "Impairment_Rating": 2,
#                 "Wage_Loss_Exposure": 5000,
#                 "Has_Demand": True,
#                 "Demand_Amount": 850000
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()
#     with c4:
#         if st.button("📄Scenario 4", use_container_width=True):
#             st.session_state.prefill = {
#                 "Jurisdiction": "New Jersey",
#                 "Attorney_Score": 90,
#                 "Impairment_Rating": 15,
#                 "Wage_Loss_Exposure": 45000,
#                 "Has_Demand": False,      # ← IMPORTANT CHANGE
#                 "Demand_Amount": 0        # ← Should be 0 because has_demand=False
#             }
#             st.session_state.scenario_selected = True
#             st.rerun()


#     st.stop()

# # === FORM STATE ===
# if not st.session_state.submitted:
#     st.markdown("""
#         <div class='form-container'>
#             <div class='form-title'>⚖️ Litigation Settlement Analyzer</div>
#             <div class='form-subtitle'>Settlement Valuation & Strategy Intelligence</div>
#     """, unsafe_allow_html=True)
    
#     # with st.container(): # Changed from st.form to st.container to allow dynamic interactions
#     with st.form("case_input_form"):


#         # === APPLY PREFILL (if scenario chosen) ===
#         pref = st.session_state.get("prefill", {})

#         # Helper: choose default OR prefilled
#         def use_prefill(key, default):
#             return pref.get(key, default)

        

            
#         # --- 1. CLAIMANT PROFILE (New First Section - Expanded) ---
#         with st.expander("👤 1. Claimant Profile", expanded=True):
            
#             col_age, col_tenure = st.columns(2)
#             with col_age:
#                 # NEW FIELD: Claimant Age
#                 claimant_age = st.number_input("Claimant Age", min_value=18, max_value=99, value=45)
#             with col_tenure:
#                 # NEW FIELD: Tenure
#                 tenure = st.number_input("Tenure (Years at Employer)", min_value=0, max_value=50, value=5)

#             col_occup, col_employ = st.columns(2)
#             with col_occup:
#                 # NEW FIELD: Occupation
#                 occupation = st.selectbox(
#                     "Occupation Type",
#                     ['Clerical/Office', 'Light Manual', 'Heavy Manual', 'Professional', 'Service Industry']
#                 )
#             with col_employ:
#                 # EXISTING FIELD: Employment Status (Moved)
#                 employment = st.selectbox(
#                     "Employment Status",
#                     ['Active', 'Terminated', 'Retired', 'Leave of Absence']
#                 )

#             col_dependents, col_engaged = st.columns(2)
#             with col_dependents:
#                 # EXISTING NEW FIELD: Dependents
#                 dependents_count = st.number_input("Number of Dependents", min_value=0, max_value=10, value=2)
#             with col_engaged:
#                 # NEW FIELD: Engaged Claimant
#                 engaged_claimant = st.checkbox("Engaged with Medical Provider (Compliance)?")
                
#             col_claim, col_social = st.columns(2)
#             with col_claim:
#                 # EXISTING NEW FIELD: Previous Claim History
#                 previous_claim_flag = st.checkbox("Previous Litigation/Claim History?")
#             with col_social:
#                 # EXISTING NEW FIELD: Social Media Risk
#                 social_media_risk = st.selectbox(
#                     "Social Media Activity Risk",
#                     ['Low (Private/Inactive)', 'Moderate (Active)', 'High (Contradictory)']
#                 )
            

#         # --- 2. LITIGATION & EXPOSURE (Second Section - Expanded) ---
#         with st.expander("🏛️ 2. Litigation & Exposure", expanded=True):
            
#             form_col1, form_col2 = st.columns(2)
#             with form_col1:
#                 jurisdiction = st.selectbox(
#                     "Jurisdiction",
#                     ['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'],
#                     index=['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania']
#                     .index(use_prefill("Jurisdiction", "New Jersey"))
#                 )
#             with form_col2:
#                 venue_win_rate = st.slider("Defense Win Rate in Venue (General)", 0.0, 1.0, 0.45) # CLARIFIED LABEL

#             form_col3, form_col4 = st.columns(2)
#             with form_col3:
#                 attorney_firm = st.selectbox(
#                     "Plaintiff Counsel",
#                     ['Weitz & Luxenberg', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner']
#                 )
#             with form_col4:
#                 attorney_score = st.slider(
#                     "Plaintiff Attorney Aggressiveness Score (0-100)", # CLARIFIED LABEL
#                     0, 100, 
#                     use_prefill("Attorney_Score", 65)
#                 )

#             form_col5, form_col6 = st.columns(2)
#             with form_col5:
#                 attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
#             with form_col6:
#                 attorney_type = st.selectbox(
#                     "Attorney Settlement Tendency",
#                     ['Early Settlement', 'Balanced', 'Trial-Oriented']
#                 )
            
#             form_col7, _ = st.columns(2)
#             with form_col7:
#                 judge = st.selectbox(
#                     "Judge Propensity (if assigned)",
#                     ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned']
#                 )


#         # --- 3. ECONOMIC DAMAGES (Third Section - Expanded) ---
#         with st.expander("💰 3. Economic Damages & Demand", expanded=True):
            
#             form_col8, form_col9 = st.columns(2)
#             with form_col8:
#                 wage_loss = st.number_input(
#                     "Wage Loss Exposure ($) - Estimated Total Liability", # CLARIFIED LABEL
#                     5000, 500000,
#                     use_prefill("Wage_Loss_Exposure", 25000)
#                 )
#             with form_col9:
#                 # EXISTING FIELD: Permanent Impairment (%)
#                 impairment = st.slider(
#                     "Permanent Impairment (%)",
#                     0, 100,
#                     use_prefill("Impairment_Rating", 15)
#                 )

#             form_col10, form_col11 = st.columns(2)
#             with form_col10:
#                 medical_trajectory = st.selectbox(
#                     "Medical Cost Trajectory (Future Liability)", # CLARIFIED LABEL
#                     ['Low', 'Moderate', 'High', 'Escalating']
#                 )
#             with form_col11:
#                 future_medical = st.checkbox("Future Medical Exposure?", value=True)

#             form_col12, _ = st.columns(2)
#             with form_col12:
#                 has_demand = st.checkbox(
#                     "Has a formal demand been received?",
#                     value=use_prefill("Has_Demand", False)
#                 )

#                 if has_demand:
#                     demand = st.number_input(
#                         "Enter Plaintiff Demand ($)",
#                         min_value=0, max_value=10000000,
#                         value=use_prefill("Demand_Amount", 150000),
#                         step=5000
#                     )
#                 else:
#                     demand = 0
#                     st.info("ℹ️ No demand entered. System will calculate 'Likelihood of Acceptance' accordingly.")


#         # --- 4. MEDICAL & BEHAVIORAL PROGRESSION (Last Section - Collapsed) ---
#         with st.expander("🏥 4. Medical & Behavioral Progression", expanded=True):
            
#             col_injury, col_body = st.columns(2)
#             with col_injury:
#                 # NEW FIELD: Injury Type
#                 injury_type = st.selectbox(
#                     "Injury Type",
#                     ['Soft Tissue Strain', 'Fracture', 'Herniated Disc', 'Head Injury', 'Amputation', 'Other']
#                 )
#             with col_body:
#                 # NEW FIELD: Body Part Involved
#                 body_part = st.selectbox(
#                     "Body Part Involved",
#                     ['Lumbar Spine', 'Cervical Spine', 'Knee', 'Shoulder', 'Hand/Wrist', 'Multiple']
#                 )

#             col_surgery, col_hosp = st.columns(2)
#             with col_surgery:
#                 # NEW FIELD: Need for Surgery
#                 need_for_surgery = st.checkbox("Need for Surgery?")
#             with col_hosp:
#                 # NEW FIELD: Need for Hospitalization
#                 need_for_hosp = st.checkbox("Need for Hospitalization?")

#             col_provider, col_comorbid = st.columns(2)
#             with col_provider:
#                 # EXISTING FIELD: Primary Provider
#                 provider_type = st.selectbox(
#                     "Primary Provider",
#                     ['Chiropractor', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Physical Therepy']
#                 )
#             with col_comorbid:
#                 # EXISTING FIELD: Comorbidities
#                 comorbidity = st.selectbox(
#                     "Comorbidities",
#                     ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions']
#                 )
            
#             col_odg, col_msa = st.columns(2)
#             with col_odg:
#                 # EXISTING FIELD: ODG Adherence
#                 odg = st.selectbox(
#                     "ODG Guidelines Adherence",
#                     ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds']
#                 )
#             with col_msa:
#                 # EXISTING FIELD: MSA
#                 msa = st.checkbox("Medicare Set-Aside (MSA) Required?")

#             st.markdown("<h5 style='color:#cbd5e1; margin-top:20px;'>Case Progression Timeline</h5>", unsafe_allow_html=True)
            
#             col_filed, col_attorney = st.columns(2)
#             with col_filed:
#                 # EXISTING FIELD: Days Since Filed
#                 days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
#             with col_attorney:
#                 # EXISTING FIELD: Days Since Attorney Engaged
#                 days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)

#             col_duration, col_shopping = st.columns(2)
#             with col_duration:
#                 # EXISTING FIELD: Treatment Duration
#                 treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
#             with col_shopping:
#                 # EXISTING FIELD: Provider Shopping Count
#                 provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)

#             col_opioid, _ = st.columns(2)
#             with col_opioid:
#                 # EXISTING FIELD: Opioid Indicator
#                 opioid = st.checkbox("Opioid Prescription Indicator?")

#         st.markdown("---")

        
        

#         # Submit Button
#         # submitted = st.button("🚀 ANALYZE CASE", use_container_width=True)
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
            
#             # --- NEW CLAIMANT FIELDS ---
#             st.session_state.claimant_age = claimant_age
#             st.session_state.occupation = occupation
#             st.session_state.tenure = tenure
#             st.session_state.engaged_claimant = engaged_claimant
#             st.session_state.dependents_count = dependents_count
#             st.session_state.previous_claim_flag = previous_claim_flag
#             st.session_state.social_media_risk = social_media_risk
            
#             # --- MEDICAL / OLD FIELDS ---
#             st.session_state.msa = msa
#             st.session_state.comorbidity = comorbidity
#             st.session_state.odg = odg
#             st.session_state.attorney_winrate = attorney_winrate
#             st.session_state.attorney_type = attorney_type
#             st.session_state.judge = judge
            
#             # --- NEW MEDICAL FIELDS ---
#             st.session_state.injury_type = injury_type
#             st.session_state.body_part = body_part
#             st.session_state.need_for_surgery = need_for_surgery
#             st.session_state.need_for_hosp = need_for_hosp

#             st.session_state.submitted = True
            
            
#             st.rerun()
    
#     st.markdown("</div>", unsafe_allow_html=True)

# # === DASHBOARD VIEW ===
# else:
#     import model
    


    
    
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
#         "Benefit_Status": "N/A",
#         # --- NEW CLAIMANT FIELDS ---
#         "Claimant_Age": st.session_state.claimant_age,
#         "Occupation": st.session_state.occupation,
#         "Tenure": st.session_state.tenure,
#         "Engaged_Claimant": 1 if st.session_state.engaged_claimant else 0,
#         "Dependents_Count": st.session_state.dependents_count,
#         "Previous_Claim_Flag": 1 if st.session_state.previous_claim_flag else 0,
#         "Social_Media_Risk": st.session_state.social_media_risk,
        
#         # --- NEW MEDICAL FIELDS ---
#         "Injury_Type": st.session_state.injury_type,
#         "Body_Part": st.session_state.body_part,
#         "Need_for_Surgery": 1 if st.session_state.need_for_surgery else 0,
#         "Need_for_Hosp": 1 if st.session_state.need_for_hosp else 0,
        
#         # --- OLD/RETAINED FIELDS ---
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
#     # === 1. CALCULATE CONFIDENCE SCORE (DEFINE IT HERE) ===
#     confidence_score = 90
    
#     # Apply penalties based on inputs
#     if inputs['Attorney_Score'] > 80: confidence_score -= 10
#     if inputs['Medical_Trajectory'] == 'Escalating': confidence_score -= 15
#     if inputs['Days_Since_Filed'] < 60: confidence_score -= 10
#     if inputs['Judge_Propensity'] == 'Not Yet Assigned': confidence_score -= 5
    
#     # Cap between 0 and 100
#     confidence_score = max(0, min(100, confidence_score))
    
#     # Define Label for Header
#     conf_label_header = "High Confidence" if confidence_score >= 80 else "Medium Confidence"
#     # === DASHBOARD HEADER ===
#     rec_emoji = "✅" if res['is_safe'] else "⚠️"
    
#     col_header_left, col_header_right = st.columns(2)
    
#     # with col_header_left:
#     #     st.markdown(f"""
#     #         <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
#     #         <div class='dashboard-subtitle'>{res['action_desc']}<br>
#     #         📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </b></div>
#     #     """, unsafe_allow_html=True)
    
#     with col_header_left:
#         st.markdown(f"""
#             <div style='display: flex; align-items: center; margin-bottom: 15px;'>
#                 <span style='font-size: 2.5rem; margin-right: 15px; flex-shrink: 0;'>{rec_emoji}</span>
#                 <div class='dashboard-text' style='font-family: "Playfair Display", serif; font-size: 2.5rem; font-weight: 700; color: #f1f5f9;'>
#                     {res['action']}
#                 </div>
#             </div>
#             <div class='dashboard-subtitle'>{res['action_desc']}<br>
#             📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </div>
#         """, unsafe_allow_html=True)
   
    
    
#     st.markdown("---")
    
#     # === KPI CARDS ===
#     col1, col2, col3, col4 = st.columns(4)
    
    
#     # with col1:
#     #     # SWAPPED: Range is now the Big Value, Target is the Subtext
#     #     st.markdown(f"""
#     #         <div class='kpi-card'>
#     #             <div class='kpi-label'>💵 Settlement Range</div>
#     #             <div class='kpi-value'>${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
#     #             <div class='kpi-subtext'>Estimated value: ${res['prediction']/1000:.0f}K</div>
#     #         </div>
#     #     """, unsafe_allow_html=True)
#     # --- FIXED RANDOM RANGE LOGIC ---
#     random_low = random.randint(170000, 206000)
#     random_high = random.randint(random_low + 5000, 250000)
#     median_value = (random_low + random_high) / 2
#     # --- FULL MONTHLY DEFENSE COST MODEL ---

#     jur = inputs["Jurisdiction"]

#     # If jurisdiction exists in mapping → use monthly rate model
#     if jur in jurisdiction_cost_map:
#         low, high = jurisdiction_cost_map[jur]
#         monthly_rate = random.randint(low, high)
#         defense_cost = int(monthly_rate * res['months'])

#     else:
#         # Default state baseline
#         low, high = (8000, 14000)
#         monthly_rate = random.randint(low, high)
#         defense_cost = int(monthly_rate * res['months'])

#     # --- Adjust for attorney aggressiveness multiplier ---
#     if inputs['Attorney_Score'] > 85:
#         defense_cost *= 1.3
#     elif inputs['Attorney_Score'] > 70:
#         defense_cost *= 1.15

#     # Trial-oriented attorneys add systemic cost
#     if inputs['Attorney_Tendency'] == 'Trial-Oriented':
#         defense_cost *= 1.25

#     # Medical complexity increases legal work
#     if inputs['Medical_Trajectory'] == 'Escalating':
#         defense_cost *= 1.15
#     if inputs['Need_for_Surgery'] == 1:
#         defense_cost += 12000
#     if inputs['Opioid_Indicator'] == 1:
#         defense_cost += 8000

#     # Final rounded defense cost
#     defense_cost = int(defense_cost)

#     # Total Exposure
#     total_exposure = int(median_value + defense_cost)


#     with col1:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>💵 Settlement Range</div>
#                 <div class='kpi-value'>${random_low/1000:.0f}K – ${random_high/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Estimated value: ${median_value/1000:.0f}K</div>
#             </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         # 1. Calculate Base Confidence Score (0-100%)
#         base_score = 90
        
#         # Penalties (reduce the base score)
#         if inputs['Attorney_Score'] > 80: base_score -= 10
#         if inputs['Medical_Trajectory'] == 'Escalating': base_score -= 15
#         if inputs['Days_Since_Filed'] < 60: base_score -= 10
#         if inputs['Judge_Propensity'] == 'Not Yet Assigned': base_score -= 5
        
#         # 2. Calculate the Interval (Width of the range)
#         # If the case is risky, the interval is wider (more uncertainty)
#         interval_width = 5 
#         if base_score < 75: interval_width = 10 
        
#         low_ci = max(base_score - interval_width, 10)
#         high_ci = min(base_score + interval_width, 99)
        
#         # 3. Determine Color
#         if low_ci >= 75:
#             conf_color = "#16a34a" # Green
#             label_text = "Strong Predictability"
#         elif low_ci >= 55:
#             conf_color = "#f59e0b" # Orange
#             label_text = "Moderate Certainty"
#         else:
#             conf_color = "#dc2626" # Red
#             label_text = "Low Data Density"

#         # 4. Render Card
#         st.markdown(f"""
#             <div class='kpi-card' style='border-bottom: 4px solid {conf_color};'>
#                 <div class='kpi-label'>📉 Confidence Interval</div>
#                 <div class='kpi-value' style='color: {conf_color};'>{low_ci}% – {high_ci}%</div>
#                 <div class='kpi-subtext'>{label_text}</div>
#             </div>
#         """, unsafe_allow_html=True)
    
    
    
    
#     with col3:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>⏱️ Est. Duration</div>
#                 <div class='kpi-value'>{res['days']}d</div>
#                 <div class='kpi-subtext'>≈ {res['months']:.1f} months</div>
#             </div>
#         """, unsafe_allow_html=True)
#     # with col4:
#     #     st.markdown(f"""
#     #         <div class='kpi-card'>
#     #             <div class='kpi-label'>📊 Total Exposure</div>
#     #             <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
#     #             <div class='kpi-subtext'>Verdict + Defense</div>
#     #         </div>
#     #     """, unsafe_allow_html=True)
    
#     # st.markdown("")
#     with col4:
#         st.markdown(f"""
#             <div class='kpi-card'>
#                 <div class='kpi-label'>📊 Total Exposure</div>
#                 <div class='kpi-value'>${total_exposure/1000:.0f}K</div>
#                 <div class='kpi-subtext'>Verdict + Defense Cost</div>
#             </div>
#         """, unsafe_allow_html=True)

#     # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
    
    




#     # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Based on Calculated Values) ===

#     # Only show this section if NO demand was entered (Simulated)
#     if res['demand_source'] == 'Simulated':
#         st.markdown("<div class='section-header'>🤝 Negotiation Intelligence</div>", unsafe_allow_html=True)
        
#         # Calculate acceptance probability based on actual case factors
#         base_prob = 70
        
#         # Adjust based on attorney aggressiveness
#         if inputs['Attorney_Score'] > 85:
#             base_prob -= 20
#         elif inputs['Attorney_Score'] > 70:
#             base_prob -= 10
        
#         # Adjust based on medical trajectory
#         if inputs['Medical_Trajectory'] == 'Escalating':
#             base_prob -= 15
#         elif inputs['Medical_Trajectory'] == 'Stable':
#             base_prob += 10
        
#         # Adjust based on attorney tendency
#         if inputs['Attorney_Tendency'] == 'Trial-Oriented':
#             base_prob -= 25
#         elif inputs['Attorney_Tendency'] == 'Settlement-Oriented':
#             base_prob += 15
        
#         # Adjust based on case duration
#         if inputs['Days_Since_Filed'] < 90:
#             base_prob -= 10
#         elif inputs['Days_Since_Filed'] > 365:
#             base_prob += 5
        
#         # Adjust based on judge assignment
#         if inputs['Judge_Propensity'] == 'Not Yet Assigned':
#             base_prob -= 5
#         elif inputs['Judge_Propensity'] == 'Plaintiff-Friendly':
#             base_prob -= 10
#         elif inputs['Judge_Propensity'] == 'Defense-Friendly':
#             base_prob += 10
        
#         # Clamp probability between 20-95
#         prob = max(20, min(95, base_prob))
        
#         # Color Logic for the Bar
#         if prob >= 70: 
#             p_color = "#16a34a" # Green
#             p_msg = "High probability of early resolution at Target Value."
#         elif prob >= 40: 
#             p_color = "#f59e0b" # Orange
#             p_msg = "Moderate resistance expected. May require mediation."
#         else: 
#             p_color = "#dc2626" # Red
#             p_msg = "Low probability. Plaintiff counsel likely to push for trial."

#         # 1. Render the Full-Width Probability Bar
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%); border: 1px solid #3b82f6; border-radius: 12px; padding: 25px; margin-bottom: 20px;'>
#                 <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
#                     <span style='color: #cbd5e1; font-weight: 600;'>Likelihood of Acceptance at Target Value (${median_value:,.0f})</span>
#                     <span style='color: {p_color}; font-weight: 800; font-size: 1.2rem;'>{prob}%</span>
#                 </div>
#                 <div style='width: 100%; background-color: #334155; border-radius: 10px; height: 12px;'>
#                     <div style='width: {prob}%; background-color: {p_color}; height: 12px; border-radius: 10px; transition: width 1s ease;'></div>
#                 </div>
#                 <div style='color: #94a3b8; font-size: 0.9rem; margin-top: 15px;'>
#                     <i>Strategy Note: {p_msg}</i>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#         # 2. Acceptance Curve Visualization (Added Graph)
#         st.markdown("<h5 style='color: #cbd5e1; margin-bottom: 10px;'>📉 Offer vs. Acceptance Probability Curve</h5>", unsafe_allow_html=True)
        
#         target = median_value
        
#         # Create a range of offers (from 50% to 150% of the target value)
#         x_vals = np.linspace(target * 0.5, target * 1.5, 100)
        
#         # MATH: Dynamic Sigmoid Curve logic
#         k = 10 / target 
#         prob_safe = max(1, min(99, prob)) # Safety clamp
        
#         # Shift curve based on probability score
#         shift = target + (np.log(100/prob_safe - 1) / k)
        
#         # Generate Y values (0-100%)
#         y_vals = 100 / (1 + np.exp(-k * (x_vals - shift)))
        
#         fig_curve = go.Figure()
        
#         # The Curve Line
#         fig_curve.add_trace(go.Scatter(
#             x=x_vals, y=y_vals,
#             mode='lines',
#             line=dict(color='#60A5FA', width=4),
#             fill='tozeroy',
#             fillcolor='rgba(96, 165, 250, 0.1)',
#             name='Acceptance Chance'
#         ))
        
#         # The "You Are Here" Marker
#         fig_curve.add_trace(go.Scatter(
#             x=[target], y=[prob],
#             mode='markers',
#             marker=dict(color='#F59E0B', size=15, line=dict(color='white', width=2)),
#             name='Current Target',
#             hoverinfo='text',
#             hovertext=f"Target: ${target:,.0f}<br>Probability: {prob}%"
#         ))

#         fig_curve.update_layout(
#             height=300,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             xaxis=dict(title="Offer Amount ($)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), showgrid=False, tickprefix="$"),
#             yaxis=dict(title="Probability (%)", title_font=dict(color='#94a3b8'), tickfont=dict(color='#cbd5e1'), range=[0, 105], showgrid=True, gridcolor='#334155'),
#             showlegend=False,
#             hovermode="x unified"
#         )
        
#         st.plotly_chart(fig_curve, use_container_width=True)

    
#     # === ZOPA CURVE (Dynamic Logic + Your Style) ===
#     st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
#     mu = median_value
    
#     # --- CHANGED: DYNAMIC WIDTH LOGIC ---
#     # Calculate base_score for confidence (same logic as earlier)
#     base_score = 90
#     if inputs['Attorney_Score'] > 80: base_score -= 10
#     if inputs['Medical_Trajectory'] == 'Escalating': base_score -= 15
#     if inputs['Days_Since_Filed'] < 60: base_score -= 10
#     if inputs['Judge_Propensity'] == 'Not Yet Assigned': base_score -= 5
    
#     base_score = max(0, min(100, base_score))
    
#     # Instead of static 0.12, we calculate based on Confidence Score
#     # High Conf (100) = Narrow (0.05). Low Conf (50) = Wide (0.20).
#     sigma_pct = 0.20 - ((base_score - 50) / 50 * 0.15)
#     sigma_pct = max(0.05, min(0.20, sigma_pct)) # Clamp limits
#     sigma = mu * sigma_pct
#     # ------------------------------------
    
#     x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
#     fig_zopa = go.Figure()
    
#     # Full distribution curve (Your Style)
#     fig_zopa.add_trace(go.Scatter(
#         x=x, y=y,
#         mode='lines',
#         line=dict(color='#64748B', width=2),
#         fill='tozeroy',
#         fillcolor='rgba(59, 130, 246, 0.1)',
#         name='Distribution'
#     ))
    
#     # Safe settlement zone (Your Style)
#     # Using your calculated range instead of res['range_low'] and res['range_high']
#     x_safe = np.linspace(random_low, random_high, 150)
#     y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
    
#     fig_zopa.add_trace(go.Scatter(
#         x=x_safe, y=y_safe,
#         mode='lines',
#         line=dict(width=0),
#         fill='tozeroy',
#         fillcolor='rgba(22, 163, 74, 0.5)',
#         name='Safe Zone'
#     ))
    
#     # Layout (Your Exact Settings)
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
    
    
#     # st.divider()
#     # === 7. EXPLAINABILITY & STRATEGIC ANALYSIS (SCENARIO-AWARE) ===
#     st.markdown("<div class='section-header'>📈 Model Explainability & Strategic Analysis</div>", unsafe_allow_html=True)

#     # Extract variables
#     attorney_score = inputs['Attorney_Score']
#     venue_win_rate = inputs['Venue_Win_Rate']
#     impairment = inputs['Impairment_Rating']
#     wage_loss = inputs['Wage_Loss_Exposure']
#     employment = inputs['Employment_Status']
#     opioid = inputs['Opioid_Indicator']
#     days_filed = inputs['Days_Since_Filed']
#     medical_trajectory = inputs['Medical_Trajectory']
#     future_medical = inputs['Future_Medical']
#     attorney_type = inputs['Attorney_Tendency']

#     # --- STEP 1: DETECT SCENARIO CONTEXT ---
#     # We define the "Scenario" to decide which features matter most
#     current_scenario = "Standard"
    
#     if impairment > 15 or future_medical == 1:
#         current_scenario = "Catastrophic"
#     elif attorney_score > 65 or employment == 'Terminated':
#         current_scenario = "Litigated/Complex"
#     elif days_filed < 90 and impairment == 0:
#         current_scenario = "Nuisance"
#     else:
#         current_scenario = "Standard"

#     # --- STEP 2: DEFINE DYNAMIC WEIGHTS BASED ON SCENARIO ---
#     # These multipliers determine how much a feature impacts the price
#     weights = {
#         'attorney': 50,
#         'venue': 20000,
#         'impairment': 800,
#         'wage': 0.35,
#         'term': 10000,
#         'opioid': 5000,
#         'med_traj': 5000,
#         'days': 10
#     }

#     if current_scenario == "Catastrophic":
#         # In Catastrophic, Injury & Future Meds dominate. Attorney matters less.
#         weights['impairment'] = 2500  # Massive impact
#         weights['med_traj'] = 15000   # Massive impact
#         weights['attorney'] = 20      # Attorney skill matters less when injury is obvious
#         weights['venue'] = 10000      # Venue matters less
        
#     elif current_scenario == "Litigated/Complex":
#         # In Complex, The Attorney, Venue, and Employment Status dominate.
#         weights['attorney'] = 180     # High Attorney Impact
#         weights['venue'] = 65000      # High Venue Impact
#         weights['term'] = 25000       # Termination is huge (retaliation risk)
#         weights['impairment'] = 600   # moderate

#     elif current_scenario == "Nuisance":
#         # In Nuisance, it's about making it go away (Days Filed & Venue).
#         weights['days'] = 150         # Aging cases cost money
#         weights['impairment'] = 0     # Injury is negligible
#         weights['wage'] = 0.1         # Wages negligible
#         weights['venue'] = 30000      # Fear of bad venue drives nuisance value

#     # --- STEP 3: CALCULATE FEATURE IMPORTANCE ---
#     feature_importance = []

#     # 1. Attorney Contribution
#     # Baseline is 50. If score > 50 it adds value, if < 50 it reduces value.
#     att_impact = (attorney_score - 50) * weights['attorney']
#     feature_importance.append(('Attorney Score', attorney_score, att_impact, f'Aggressiveness rating (Context: {current_scenario})'))

#     # 2. Venue Contribution
#     # Baseline 50% win rate.
#     ven_impact = (0.50 - venue_win_rate) * weights['venue']
#     feature_importance.append(('Venue Environment', f'{int(venue_win_rate*100)}%', ven_impact, 'Jury verdict potential'))

#     # 3. Impairment (Always positive impact)
#     if impairment > 0:
#         imp_impact = impairment * weights['impairment']
#         feature_importance.append(('Impairment Rating', f'{impairment}%', imp_impact, 'Permanent Partial Disability'))

#     # 4. Wage Loss
#     if wage_loss > 0:
#         wg_impact = wage_loss * weights['wage']
#         feature_importance.append(('Wage Loss', f'${wage_loss:,}', wg_impact, 'Indemnity exposure'))

#     # 5. Employment Status
#     if employment == 'Terminated':
#         feature_importance.append(('Employment', 'Terminated', weights['term'], 'Wrongful termination risk premium'))
#     elif employment == 'Resigned':
#          feature_importance.append(('Employment', 'Resigned', weights['term'] * 0.2, 'Voluntary separation'))

#     # 6. Opioid (Risk Multiplier)
#     if opioid == 1:
#         feature_importance.append(('Opioid Risk', 'Detected', weights['opioid'], 'Addiction/Prolonged recovery risk'))

#     # 7. Medical Trajectory
#     traj_map = {'Escalating': 2.0, 'High': 1.5, 'Moderate': 1.0, 'Stable': 0.5}
#     traj_score = traj_map.get(medical_trajectory, 0)
#     # Compare against "Moderate" baseline (1.0)
#     med_impact = (traj_score - 1.0) * weights['med_traj']
#     feature_importance.append(('Medical Trend', medical_trajectory, med_impact, f'Projected medical complexity'))

#     # 8. Future Medical
#     if future_medical == 1:
#         fm_val = 50000 if current_scenario == "Catastrophic" else 8000
#         feature_importance.append(('Future Medical', 'Required', fm_val, 'Medicare Set-Aside / Future Care'))

#     # --- STEP 4: SORT AND FILTER ---
#     # Sort by ABSOLUTE impact (biggest drivers first, whether positive or negative)
#     feature_importance = sorted(feature_importance, key=lambda x: abs(x[2]), reverse=True)
    
#     # Filter small noise
#     feature_importance = [f for f in feature_importance if abs(f[2]) > 100]

#     # Use median_value from your prediction model
#     base_value = median_value 

#     # # --- STEP 5: RENDER UI ---
#     # st.markdown(f"## 🧾 Explanation for {current_scenario} Scenario")
#     # st.caption(f"Prediction Baseline: ${base_value:,.0f}")
#     # st.divider()

#     col_explain, col_chart = st.columns([1, 1])

#     top_features = feature_importance[:5] # Top 5 drivers
    
#     with col_explain:
#         st.markdown("### 🔑 Key Drivers")
#         for i, (feature, value, impact, desc) in enumerate(top_features, 1):
#             impact_pct = (impact / base_value) * 100 if base_value != 0 else 0
            
#             # Icon logic
#             if impact > 0:
#                 icon = "🔺" # Increases cost
#                 color_class = "red"
#             else:
#                 icon = "🔻" # Decreases cost (Savings)
#                 color_class = "green"
                
#             st.markdown(f"""
#             <div style='background-color: #1e293b; padding: 10px; border-radius: 5px; margin-bottom: 10px; border-left: 4px solid {'#ef4444' if impact > 0 else '#10b981'}'>
#                 <div style='font-weight: bold; font-size: 1.1em;'>{icon} {feature}</div>
#                 <div style='font-size: 0.9em; color: #cbd5e1;'>{desc}</div>
#                 <div style='font-size: 0.8em; margin-top: 5px;'>Impact: ({impact_pct:+.1f}%)</div>
#             </div>
#             """, unsafe_allow_html=True)

#     with col_chart:
#         st.markdown("### 📊 Impact Distribution")
        
#         # Prepare Chart Data (Reverse order for horizontal chart)
#         chart_feats = [x[0] for x in top_features][::-1]
#         chart_vals = [x[2] for x in top_features][::-1]
#         chart_colors = ['#ef4444' if x > 0 else '#10b981' for x in chart_vals]
        
#         # Calculate Percentages for the Labels
#         # We divide the specific impact by the total prediction (median_value)
#         chart_labels = []
#         for val in chart_vals:
#             if median_value > 0:
#                 pct = (val / median_value) * 100
#                 chart_labels.append(f"{pct:+.1f}%") # Format: +12.5% or -5.2%
#             else:
#                 chart_labels.append("0%")

#         fig_shap = go.Figure()
#         fig_shap.add_trace(go.Bar(
#             y=chart_feats,
#             x=chart_vals,       # Keep X as $ amount so bar sizes are accurate
#             orientation='h',
#             marker=dict(color=chart_colors),
#             text=chart_labels,  # DISPLAY PERCENTAGES HERE
#             textposition='auto',
#             # Custom Hover: Shows both $ amount and %
#             hovertemplate='<b>%{y}</b><br>Impact: $%{x:,.0f}<br>Share: %{text}<extra></extra>' 
#         ))

#         fig_shap.update_layout(
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             margin=dict(l=20, r=20, t=20, b=20),
#             height=400,
#             xaxis=dict(
#                 showgrid=True, 
#                 gridcolor='#334155', 
#                 zeroline=True, 
#                 zerolinecolor='white',
#                 title="Impact Value ($)", # Optional: label x-axis
#                 title_font=dict(color='#cbd5e1')
#             ),
#             yaxis=dict(tickfont=dict(color='white'))
#         )
#         st.plotly_chart(fig_shap, use_container_width=True)
    
#     # Final recommendation
#     st.markdown("### 🎯 Summary")
    
#     if res['action'] == 'SETTLE':
#         st.success("✅ **SETTLE** - Settlement is economically superior to litigation.")
#     elif res['action'] == 'LITIGATE':
#         st.error("⚔️ **LITIGATE** - Litigation exposure is lower than settlement value.")
#     else:
#         st.warning("⚡ **STRATEGIZE** - Mixed factors require careful case management.")
#     # === RISK ALERTS ===
    
    
    
    
#     # === STRATEGIC RECOMMENDATION ===
#     # st.markdown("<div class='section-header'>🎯 Next Best Action</div>", unsafe_allow_html=True)
    
#     # if res['action'] == 'SETTLE':
#     #     st.markdown(f"""
#     #         <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
#     #         <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
#     #         Settlement is economically superior. Litigation exposure (<b>${total_exposure:,.0f}</b>) exceeds settlement value (<b>${median_value:,.0f}</b>).<br><br>
#     #         <b>📋 Action Plan:</b><br>
#     #         • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
#     #         • <b>Opening Offer:</b> ${random_low:,.0f} – ${int(median_value*0.95):,.0f}<br>
#     #         • <b>Walk-Away Price:</b> ${random_high:,.0f}<br>
#     #         • <b>Savings vs Litigation:</b> ${total_exposure - median_value:,.0f}
#     #         </div>
#     #     """, unsafe_allow_html=True)
#     # elif res['action'] == 'LITIGATE':
#     #     st.markdown(f"""
#     #         <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
#     #         <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
#     #         Settlement value (<b>${median_value:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
#     #         <b>📋 Action Plan:</b><br>
#     #         • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
#     #         • <b>Expected Defense Costs:</b> ${defense_cost:,.0f}<br>
#     #         • <b>Anticipated Verdict:</b> ${median_value:,.0f}<br>
#     #         • <b>Do Not Settle Above:</b> ${int(total_exposure*0.9):,.0f}
#     #         </div>
#     #     """, unsafe_allow_html=True)
#     # else:
#     #     st.markdown(f"""
#     #         <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
#     #         <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
#     #         Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
#     #         <b>📋 Action Plan:</b><br>
#     #         • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
#     #         • <b>Test Offer:</b> ${int(median_value*0.85):,.0f}<br>
#     #         • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
#     #         • <b>Re-evaluate:</b> Quarterly or on significant developments
#     #         </div>
#     #     """, unsafe_allow_html=True)
#     # === 8. NEXT BEST ACTION (UPDATED STRATEGY) ===
#     st.markdown("<div class='section-header'>🎯 Next Best Action</div>", unsafe_allow_html=True)
    
#     # Retrieve Demand Amount safely from inputs
#     demand_val = inputs.get('Demand_Amount', 0)

#     if res['action'] == 'SETTLE':
#         # User Logic: Savings = Total Exposure - Upper Bound (random_high)
#         savings_vs_litigation = total_exposure - random_high
        
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
#             Settlement is economically superior. Litigation exposure (<b>${total_exposure:,.0f}</b>) expected to run for <b>{res['months']:.1f} months</b>.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
#             • <b>Opening Offer:</b> $150,000<br>
#             • <b>Plaintiff Demand:</b> ${demand_val:,.0f}<br>
#             • <b>Walk-Away Price:</b> ${random_high:,.0f}<br>
#             • <b>Savings vs Litigation:</b> ${savings_vs_litigation:,.0f}
#             </div>
#         """, unsafe_allow_html=True)

#     elif res['action'] == 'LITIGATE':
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
#             Settlement value (<b>${median_value:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
#             • <b>Expected Defense Costs:</b> ${defense_cost:,.0f}<br>
#             • <b>Anticipated Verdict:</b> ${median_value:,.0f}<br>
#             • <b>Do Not Settle Above:</b> ${int(total_exposure*0.9):,.0f}
#             </div>
#         """, unsafe_allow_html=True)

#     else:
#         st.markdown(f"""
#             <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
#             <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
#             Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
#             <b>📋 Action Plan:</b><br>
#             • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
#             • <b>Test Offer:</b> ${int(median_value*0.85):,.0f}<br>
#             • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
#             • <b>Re-evaluate:</b> Quarterly or on significant developments
#             </div>
#         """, unsafe_allow_html=True)
    
    
#     st.markdown("")
    
    
    
    
    
    

    
#     # === RESET & NAVIGATION BUTTONS ===
#     st.markdown("---")
#     col_reset_1, col_reset_2 = st.columns(2)

#     # BUTTON 1: Return to Landing Page
#     with col_reset_1:
#         if st.button("🏠 RETURN TO MAIN PAGE", use_container_width=True, key="btn_main_page"):
#             # Reset everything
#             st.session_state.submitted = False
#             st.session_state.scenario_selected = False
#             st.session_state.prefill = {}
            
#             # Clear result variables
#             for key in ["prediction", "recommendation", "risk", "driver_scores", "chart_data"]:
#                 if key in st.session_state:
#                     del st.session_state[key]

#             st.rerun()

#     # BUTTON 2: Analyze New Case (skip landing page, keep scenario)
#     with col_reset_2:
#         if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="btn_new_case"):
#             # Only reset submission
#             st.session_state.submitted = False
            
#             st.rerun()




























import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()


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
    add this css :
 
 
 
/* === EXPANDER FIX (HIGH CONTRAST & VISIBILITY) === */
    /* Target the main container of the expander */
    div[data-testid="stExpander"] {
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        background-color: transparent !important;
        margin-bottom: 15px !important;
    }
 
    /* Target the Header (The clickable <summary> element) */
    div[data-testid="stExpander"] > details > summary {
        background-color: #1e293b !important; /* Dark Blue Header Background */
        color: #ffffff !important; /* Pure White Text */
        font-weight: 1200 !important;
        font-size: 3 rem !important;
        padding: 15px 20px !important;
        /* Ensure the corners of the summary match the border radius of the parent */
        border-radius: 11px 11px 0 0 !important;
    }
 
    /* Target the Content Body inside the expander */
    div[data-testid="stExpander"] > details > div {
        background-color: #0f172a !important; /* Very Dark Blue Body */
        color: #e2e8f0 !important;
        padding: 20px !important;
        border-top: 1px solid #334155 !important;
    }
   
    /* Force the arrow icon to be white */
    div[data-testid="stExpander"] > details > summary > svg {
        fill: #ffffff !important;
        color: #ffffff !important;
    }
    /* Target for FORM submit button (NEW RULE) */
    /* This targets the button inside the stFormSubmitButton container */
    [data-testid="stFormSubmitButton"] > button {
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
        width: 100%; /* Ensure it matches the full-width setting */
    }
    div.stButton > button:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 36px rgba(37, 99, 235, 0.5);
    }
    /* --- NEW RULE FOR HEADER TEXT --- */
.dashboard-text {
    /* Use a standard, non-gradient color for the main text */
    color: #f1f5f9 !important;
    /* Inherit the size/font from the original .dashboard-title, but remove the gradient logic */
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
}
 
    </style>
""", unsafe_allow_html=True)









# ✅ STEP 1: Jurisdiction-wise monthly defense cost mapping
jurisdiction_cost_map = {
    "New York": (30000, 40000),
    "California": (28000, 38000),
    "Illinois": (22000, 32000),
    "New Jersey": (15000, 25000),
    "NJ": (15000, 25000),
    "Florida": (18000, 25000),
    "Texas": (15000, 22000),
    "Pennsylvania": (14000, 20000),
    "Georgia": (12000, 18000),
    "Ohio": (10000, 16000),
}

# === INITIALIZE SESSION STATE ===
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
# === NEW: LANDING PAGE WITH THREE SCENARIOS ===

if "scenario_selected" not in st.session_state:
    st.session_state.scenario_selected = False

if st.session_state.submitted:
    st.markdown(
        """
        <script>
            // Use setTimeout to ensure the Streamlit content has loaded before scrolling
            setTimeout(function() {
                window.scrollTo(0, 0); // Scrolls to the top-left corner
            }, 50); 
        </script>
        """, 
        unsafe_allow_html=True
    )

if not st.session_state.scenario_selected:

    st.markdown("""
        <div style='text-align:center; margin-top:60px;'>
           
           <h1 style='font-family:Poppins; font-size:3rem; color:white;'>⚖️ Litigation Settlement Analyzer</h1>
            <p style='color:#cbd5e1; font-size:1.2rem;'>
                Select a scenario to pre-fill the case details
            </p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)   # ← changed from 3 to 4 columns


    with c1:
        if st.button("✅ Scenario 1", use_container_width=True):
            st.session_state.prefill = {
                "Jurisdiction": "New Jersey",
                "Attorney_Score": 90,
                "Impairment_Rating": 15,
                "Wage_Loss_Exposure": 45000,
                "Has_Demand": True,
                "Demand_Amount": 170000
            }
            st.session_state.scenario_selected = True
            st.rerun()

    with c2:
        if st.button("⚡ Scenario 2", use_container_width=True):
            st.session_state.prefill = {
                "Jurisdiction": "New Jersey",
                "Attorney_Score": 60,
                "Impairment_Rating": 12,
                "Wage_Loss_Exposure": 35000,
                "Has_Demand": True,
                "Demand_Amount": 175000
            }
            st.session_state.scenario_selected = True
            st.rerun()

    with c3:
        if st.button("⚔️ Scenario 3", use_container_width=True):
            st.session_state.prefill = {
                "Jurisdiction": "New Jersey",
                "Attorney_Score": 50,
                "Impairment_Rating": 2,
                "Wage_Loss_Exposure": 5000,
                "Has_Demand": True,
                "Demand_Amount": 850000
            }
            st.session_state.scenario_selected = True
            st.rerun()
    with c4:
        if st.button("📄Scenario 4", use_container_width=True):
            st.session_state.prefill = {
                "Jurisdiction": "New Jersey",
                "Attorney_Score": 90,
                "Impairment_Rating": 15,
                "Wage_Loss_Exposure": 45000,
                "Has_Demand": False,      # ← IMPORTANT CHANGE
                "Demand_Amount": 0        # ← Should be 0 because has_demand=False
            }
            st.session_state.scenario_selected = True
            st.rerun()


    st.stop()

# === FORM STATE ===
if not st.session_state.submitted:
    st.markdown("""
        <div class='form-container'>
            <div class='form-title'>⚖️ Litigation Settlement Analyzer</div>
            <div class='form-subtitle'>Settlement Valuation & Strategy Intelligence</div>
    """, unsafe_allow_html=True)
    
    # with st.container(): # Changed from st.form to st.container to allow dynamic interactions
    with st.form("case_input_form"):


        # === APPLY PREFILL (if scenario chosen) ===
        pref = st.session_state.get("prefill", {})

        # Helper: choose default OR prefilled
        def use_prefill(key, default):
            return pref.get(key, default)

        

            
        # --- 1. CLAIMANT PROFILE (New First Section - Expanded) ---
        with st.expander("👤 1. Claimant Profile", expanded=True):
            
            col_age, col_tenure = st.columns(2)
            with col_age:
                # NEW FIELD: Claimant Age
                claimant_age = st.number_input("Claimant Age", min_value=18, max_value=99, value=45)
            with col_tenure:
                # NEW FIELD: Tenure
                tenure = st.number_input("Tenure (Years at Employer)", min_value=0, max_value=50, value=5)

            col_occup, col_employ = st.columns(2)
            with col_occup:
                # NEW FIELD: Occupation
                occupation = st.selectbox(
                    "Occupation Type",
                    ['Clerical/Office', 'Light Manual', 'Heavy Manual', 'Professional', 'Service Industry']
                )
            with col_employ:
                # EXISTING FIELD: Employment Status (Moved)
                employment = st.selectbox(
                    "Employment Status",
                    ['Active', 'Terminated', 'Retired', 'Leave of Absence']
                )

            col_dependents, col_engaged = st.columns(2)
            with col_dependents:
                # EXISTING NEW FIELD: Dependents
                dependents_count = st.number_input("Number of Dependents", min_value=0, max_value=10, value=2)
            with col_engaged:
                # NEW FIELD: Engaged Claimant
                engaged_claimant = st.checkbox("Engaged with Medical Provider (Compliance)?")
                
            col_claim, col_social = st.columns(2)
            with col_claim:
                # EXISTING NEW FIELD: Previous Claim History
                previous_claim_flag = st.checkbox("Previous Litigation/Claim History?")
            with col_social:
                # EXISTING NEW FIELD: Social Media Risk
                social_media_risk = st.selectbox(
                    "Social Media Activity Risk",
                    ['Low (Private/Inactive)', 'Moderate (Active)', 'High (Contradictory)']
                )
            

        # --- 2. LITIGATION & EXPOSURE (Second Section - Expanded) ---
        with st.expander("🏛️ 2. Litigation & Exposure", expanded=True):
            
            form_col1, form_col2 = st.columns(2)
            with form_col1:
                jurisdiction = st.selectbox(
                    "Jurisdiction",
                    ['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania'],
                    index=['New Jersey', 'New York', 'California', 'Texas', 'Florida', 'Illinois', 'Pennsylvania']
                    .index(use_prefill("Jurisdiction", "New Jersey"))
                )
            with form_col2:
                venue_win_rate = st.slider("Defense Win Rate in Venue (General)", 0.0, 1.0, 0.45) # CLARIFIED LABEL

            form_col3, form_col4 = st.columns(2)
            with form_col3:
                attorney_firm = st.selectbox(
                    "Plaintiff Counsel",
                    ['Weitz & Luxenberg', 'Binder & Binder', 'Local Plaintiff Mill', 'Solo Practitioner']
                )
            with form_col4:
                attorney_score = st.slider(
                    "Plaintiff Attorney Aggressiveness Score (0-100)", # CLARIFIED LABEL
                    0, 100, 
                    use_prefill("Attorney_Score", 65)
                )

            form_col5, form_col6 = st.columns(2)
            with form_col5:
                attorney_winrate = st.slider("Plaintiff Attorney Win Rate", 0.0, 1.0, 0.55)
            with form_col6:
                attorney_type = st.selectbox(
                    "Attorney Settlement Tendency",
                    ['Early Settlement', 'Balanced', 'Trial-Oriented']
                )
            
            form_col7, _ = st.columns(2)
            with form_col7:
                judge = st.selectbox(
                    "Judge Propensity (if assigned)",
                    ['Pro-Defense', 'Neutral', 'Pro-Labor', 'Not Yet Assigned']
                )


        # --- 3. ECONOMIC DAMAGES (Third Section - Expanded) ---
        with st.expander("💰 3. Economic Damages & Demand", expanded=True):
            
            form_col8, form_col9 = st.columns(2)
            with form_col8:
                wage_loss = st.number_input(
                    "Wage Loss Exposure ($) - Estimated Total Liability", # CLARIFIED LABEL
                    5000, 500000,
                    use_prefill("Wage_Loss_Exposure", 25000)
                )
            with form_col9:
                # EXISTING FIELD: Permanent Impairment (%)
                impairment = st.slider(
                    "Permanent Impairment (%)",
                    0, 100,
                    use_prefill("Impairment_Rating", 15)
                )

            form_col10, form_col11 = st.columns(2)
            with form_col10:
                medical_trajectory = st.selectbox(
                    "Medical Cost Trajectory (Future Liability)", # CLARIFIED LABEL
                    ['Low', 'Moderate', 'High', 'Escalating']
                )
            with form_col11:
                future_medical = st.checkbox("Future Medical Exposure?", value=True)

            form_col12, _ = st.columns(2)
            with form_col12:
                has_demand = st.checkbox(
                    "Has a formal demand been received?",
                    value=use_prefill("Has_Demand", False)
                )

                if has_demand:
                    demand = st.number_input(
                        "Enter Plaintiff Demand ($)",
                        min_value=0, max_value=10000000,
                        value=use_prefill("Demand_Amount", 150000),
                        step=5000
                    )
                else:
                    demand = 0
                    st.info("ℹ️ No demand entered. System will calculate 'Likelihood of Acceptance' accordingly.")


        # --- 4. MEDICAL & BEHAVIORAL PROGRESSION (Last Section - Collapsed) ---
        with st.expander("🏥 4. Medical & Behavioral Progression", expanded=True):
            
            col_injury, col_body = st.columns(2)
            with col_injury:
                # NEW FIELD: Injury Type
                injury_type = st.selectbox(
                    "Injury Type",
                    ['Soft Tissue Strain', 'Fracture', 'Herniated Disc', 'Head Injury', 'Amputation', 'Other']
                )
            with col_body:
                # NEW FIELD: Body Part Involved
                body_part = st.selectbox(
                    "Body Part Involved",
                    ['Lumbar Spine', 'Cervical Spine', 'Knee', 'Shoulder', 'Hand/Wrist', 'Multiple']
                )

            col_surgery, col_hosp = st.columns(2)
            with col_surgery:
                # NEW FIELD: Need for Surgery
                need_for_surgery = st.checkbox("Need for Surgery?")
            with col_hosp:
                # NEW FIELD: Need for Hospitalization
                need_for_hosp = st.checkbox("Need for Hospitalization?")

            col_provider, col_comorbid = st.columns(2)
            with col_provider:
                # EXISTING FIELD: Primary Provider
                provider_type = st.selectbox(
                    "Primary Provider",
                    ['Chiropractor', 'Orthopedic Surgery', 'Neurology', 'Pain Management', 'Physical Therepy']
                )
            with col_comorbid:
                # EXISTING FIELD: Comorbidities
                comorbidity = st.selectbox(
                    "Comorbidities",
                    ['None', 'Obesity', 'Diabetes', 'Hypertension', 'Multiple Conditions']
                )
            
            col_odg, col_msa = st.columns(2)
            with col_odg:
                # EXISTING FIELD: ODG Adherence
                odg = st.selectbox(
                    "ODG Guidelines Adherence",
                    ['Within Guidelines', 'Exceeds Guidelines', 'Significantly Exceeds']
                )
            with col_msa:
                # EXISTING FIELD: MSA
                msa = st.checkbox("Medicare Set-Aside (MSA) Required?")

            st.markdown("<h5 style='color:#cbd5e1; margin-top:20px;'>Case Progression Timeline</h5>", unsafe_allow_html=True)
            
            col_filed, col_attorney = st.columns(2)
            with col_filed:
                # EXISTING FIELD: Days Since Filed
                days_filed = st.slider("Days Since Claim Filed", 0, 1000, 180)
            with col_attorney:
                # EXISTING FIELD: Days Since Attorney Engaged
                days_attorney = st.slider("Days Since Attorney Engaged", 0, 1000, 150)

            col_duration, col_shopping = st.columns(2)
            with col_duration:
                # EXISTING FIELD: Treatment Duration
                treatment_duration = st.slider("Treatment Duration (Days)", 0, 500, 90)
            with col_shopping:
                # EXISTING FIELD: Provider Shopping Count
                provider_shopping = st.slider("Provider Shopping Count", 1, 10, 1)

            col_opioid, _ = st.columns(2)
            with col_opioid:
                # EXISTING FIELD: Opioid Indicator
                opioid = st.checkbox("Opioid Prescription Indicator?")

        st.markdown("---")

        
        

        # Submit Button
        # submitted = st.button("🚀 ANALYZE CASE", use_container_width=True)
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
            
            # --- NEW CLAIMANT FIELDS ---
            st.session_state.claimant_age = claimant_age
            st.session_state.occupation = occupation
            st.session_state.tenure = tenure
            st.session_state.engaged_claimant = engaged_claimant
            st.session_state.dependents_count = dependents_count
            st.session_state.previous_claim_flag = previous_claim_flag
            st.session_state.social_media_risk = social_media_risk
            
            # --- MEDICAL / OLD FIELDS ---
            st.session_state.msa = msa
            st.session_state.comorbidity = comorbidity
            st.session_state.odg = odg
            st.session_state.attorney_winrate = attorney_winrate
            st.session_state.attorney_type = attorney_type
            st.session_state.judge = judge
            
            # --- NEW MEDICAL FIELDS ---
            st.session_state.injury_type = injury_type
            st.session_state.body_part = body_part
            st.session_state.need_for_surgery = need_for_surgery
            st.session_state.need_for_hosp = need_for_hosp

            st.session_state.submitted = True
            
            
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# === DASHBOARD VIEW ===
else:
    import model

    if model._MODEL is None:
        model.load_and_train()
        print("✅ Model ready in app.py")

    


    
    
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
        "Benefit_Status": "N/A",
        # --- NEW CLAIMANT FIELDS ---
        "Claimant_Age": st.session_state.claimant_age,
        "Occupation": st.session_state.occupation,
        "Tenure": st.session_state.tenure,
        "Engaged_Claimant": 1 if st.session_state.engaged_claimant else 0,
        "Dependents_Count": st.session_state.dependents_count,
        "Previous_Claim_Flag": 1 if st.session_state.previous_claim_flag else 0,
        "Social_Media_Risk": st.session_state.social_media_risk,
        
        # --- NEW MEDICAL FIELDS ---
        "Injury_Type": st.session_state.injury_type,
        "Body_Part": st.session_state.body_part,
        "Need_for_Surgery": 1 if st.session_state.need_for_surgery else 0,
        "Need_for_Hosp": 1 if st.session_state.need_for_hosp else 0,
        
        # --- OLD/RETAINED FIELDS ---
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
    
    # with col_header_left:
    #     st.markdown(f"""
    #         <div class='dashboard-title'>{rec_emoji} {res['action']}</div>
    #         <div class='dashboard-subtitle'>{res['action_desc']}<br>
    #         📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </b></div>
    #     """, unsafe_allow_html=True)
    
    with col_header_left:
        st.markdown(f"""
            <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                <span style='font-size: 2.5rem; margin-right: 15px; flex-shrink: 0;'>{rec_emoji}</span>
                <div class='dashboard-text' style='font-family: "Playfair Display", serif; font-size: 2.5rem; font-weight: 700; color: #f1f5f9;'>
                    {res['action']}
                </div>
            </div>
            <div class='dashboard-subtitle'>{res['action_desc']}<br>
            📍 Jurisdiction: <b>{inputs['Jurisdiction']}</b> </div>
        """, unsafe_allow_html=True)
   
    
    
    st.markdown("---")
    
    # === KPI CARDS ===
    col1, col2, col3, col4 = st.columns(4)
    
    
    # with col1:
    #     # SWAPPED: Range is now the Big Value, Target is the Subtext
    #     st.markdown(f"""
    #         <div class='kpi-card'>
    #             <div class='kpi-label'>💵 Settlement Range</div>
    #             <div class='kpi-value'>${res['range_low']/1000:.0f}K – ${res['range_high']/1000:.0f}K</div>
    #             <div class='kpi-subtext'>Estimated value: ${res['prediction']/1000:.0f}K</div>
    #         </div>
    #     """, unsafe_allow_html=True)
    # --- FIXED RANDOM RANGE LOGIC ---
    random_low = random.randint(170000, 206000)
    random_high = random.randint(random_low + 5000, 250000)
    median_value = (random_low + random_high) / 2
    # --- FULL MONTHLY DEFENSE COST MODEL ---

    jur = inputs["Jurisdiction"]

    # If jurisdiction exists in mapping → use monthly rate model
    if jur in jurisdiction_cost_map:
        low, high = jurisdiction_cost_map[jur]
        monthly_rate = random.randint(low, high)
        defense_cost = int(monthly_rate * res['months'])

    else:
        # Default state baseline
        low, high = (8000, 14000)
        monthly_rate = random.randint(low, high)
        defense_cost = int(monthly_rate * res['months'])

    # --- Adjust for attorney aggressiveness multiplier ---
    if inputs['Attorney_Score'] > 85:
        defense_cost *= 1.3
    elif inputs['Attorney_Score'] > 70:
        defense_cost *= 1.15

    # Trial-oriented attorneys add systemic cost
    if inputs['Attorney_Tendency'] == 'Trial-Oriented':
        defense_cost *= 1.25

    # Medical complexity increases legal work
    if inputs['Medical_Trajectory'] == 'Escalating':
        defense_cost *= 1.15
    if inputs['Need_for_Surgery'] == 1:
        defense_cost += 12000
    if inputs['Opioid_Indicator'] == 1:
        defense_cost += 8000

    # Final rounded defense cost
    defense_cost = int(defense_cost)

    # Total Exposure
    total_exposure = int(median_value + defense_cost)


    with col1:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>💵 Settlement Range</div>
                <div class='kpi-value'>${random_low/1000:.0f}K – ${random_high/1000:.0f}K</div>
                <div class='kpi-subtext'>Estimated value: ${median_value/1000:.0f}K</div>
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
    # with col4:
    #     st.markdown(f"""
    #         <div class='kpi-card'>
    #             <div class='kpi-label'>📊 Total Exposure</div>
    #             <div class='kpi-value'>${res['exposure']/1000:.0f}K</div>
    #             <div class='kpi-subtext'>Verdict + Defense</div>
    #         </div>
    #     """, unsafe_allow_html=True)
    
    # st.markdown("")
    with col4:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-label'>📊 Total Exposure</div>
                <div class='kpi-value'>${total_exposure/1000:.0f}K</div>
                <div class='kpi-subtext'>Verdict + Defense Cost</div>
            </div>
        """, unsafe_allow_html=True)

    # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Conditional) ===
    
    




    # === NEW SECTION: LIKELIHOOD OF ACCEPTANCE (Based on Calculated Values) ===

    # Only show this section if NO demand was entered (Simulated)
    if res['demand_source'] == 'Simulated':
        st.markdown("<div class='section-header'>🤝 Negotiation Intelligence</div>", unsafe_allow_html=True)
        
        # Calculate acceptance probability based on actual case factors
        base_prob = 70
        
        # Adjust based on attorney aggressiveness
        if inputs['Attorney_Score'] > 85:
            base_prob -= 20
        elif inputs['Attorney_Score'] > 70:
            base_prob -= 10
        
        # Adjust based on medical trajectory
        if inputs['Medical_Trajectory'] == 'Escalating':
            base_prob -= 15
        elif inputs['Medical_Trajectory'] == 'Stable':
            base_prob += 10
        
        # Adjust based on attorney tendency
        if inputs['Attorney_Tendency'] == 'Trial-Oriented':
            base_prob -= 25
        elif inputs['Attorney_Tendency'] == 'Settlement-Oriented':
            base_prob += 15
        
        # Adjust based on case duration
        if inputs['Days_Since_Filed'] < 90:
            base_prob -= 10
        elif inputs['Days_Since_Filed'] > 365:
            base_prob += 5
        
        # Adjust based on judge assignment
        if inputs['Judge_Propensity'] == 'Not Yet Assigned':
            base_prob -= 5
        elif inputs['Judge_Propensity'] == 'Plaintiff-Friendly':
            base_prob -= 10
        elif inputs['Judge_Propensity'] == 'Defense-Friendly':
            base_prob += 10
        
        # Clamp probability between 20-95
        prob = max(20, min(95, base_prob))
        
        # Color Logic for the Bar
        if prob >= 70: 
            p_color = "#16a34a" # Green
            p_msg = "High probability of early resolution at Target Value."
        elif prob >= 40: 
            p_color = "#f59e0b" # Orange
            p_msg = "Moderate resistance expected. May require mediation."
        else: 
            p_color = "#dc2626" # Red
            p_msg = "Low probability. Plaintiff counsel likely to push for trial."

        # 1. Render the Full-Width Probability Bar
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #1e293b 0%, #0a0e27 100%); border: 1px solid #3b82f6; border-radius: 12px; padding: 25px; margin-bottom: 20px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
                    <span style='color: #cbd5e1; font-weight: 600;'>Likelihood of Acceptance at Target Value (${median_value:,.0f})</span>
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
        
        target = median_value
        
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

    
    # === ZOPA CURVE (Dynamic Logic + Your Style) ===
    st.markdown("<div class='section-header'>📈 Zone of Possible Agreement (ZOPA)</div>", unsafe_allow_html=True)
    
    mu = median_value
    
    # --- CHANGED: DYNAMIC WIDTH LOGIC ---
    # Calculate base_score for confidence (same logic as earlier)
    base_score = 90
    if inputs['Attorney_Score'] > 80: base_score -= 10
    if inputs['Medical_Trajectory'] == 'Escalating': base_score -= 15
    if inputs['Days_Since_Filed'] < 60: base_score -= 10
    if inputs['Judge_Propensity'] == 'Not Yet Assigned': base_score -= 5
    
    base_score = max(0, min(100, base_score))
    
    # Instead of static 0.12, we calculate based on Confidence Score
    # High Conf (100) = Narrow (0.05). Low Conf (50) = Wide (0.20).
    sigma_pct = 0.20 - ((base_score - 50) / 50 * 0.15)
    sigma_pct = max(0.05, min(0.20, sigma_pct)) # Clamp limits
    sigma = mu * sigma_pct
    # ------------------------------------
    
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 300)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    fig_zopa = go.Figure()
    
    # Full distribution curve (Your Style)
    fig_zopa.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='#64748B', width=2),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.1)',
        name='Distribution'
    ))
    
    # Safe settlement zone (Your Style)
    # Using your calculated range instead of res['range_low'] and res['range_high']
    x_safe = np.linspace(random_low, random_high, 150)
    y_safe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_safe - mu) / sigma) ** 2)
    
    fig_zopa.add_trace(go.Scatter(
        x=x_safe, y=y_safe,
        mode='lines',
        line=dict(width=0),
        fill='tozeroy',
        fillcolor='rgba(22, 163, 74, 0.5)',
        name='Safe Zone'
    ))
    
    # Layout (Your Exact Settings)
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
    
    
    # st.divider()
    # st.divider()
    # === 7. EXPLAINABILITY & STRATEGIC ANALYSIS (SHAP-BASED) ===
    st.markdown("<div class='section-header'>📈 Model Explainability & Strategic Analysis</div>", unsafe_allow_html=True)

    # --- STEP 1: GET SHAP-BASED FEATURE IMPORTANCE FROM MODEL ---
    feature_importance = model.explain_case(
        pd.DataFrame([inputs]),
        action=res["action"]  # SETTLE / STRATEGIZE / LITIGATE
    )

    # --- STEP 2: SORT & FILTER ---
    feature_importance = sorted(feature_importance, key=lambda x: abs(x[2]), reverse=True)
    feature_importance = [f for f in feature_importance if abs(f[2]) > 100]

    # Baseline for % calculation (still shown in cards)
    base_value = median_value

    # --- STEP 3: RENDER UI ---
    col_explain, col_chart = st.columns([1, 1])
    top_features = feature_importance[:5]

    # =========================
    # LEFT: KEY DRIVERS (TEXT)
    # =========================
    with col_explain:
        st.markdown("### 🔑 Key Drivers")

        for feature, value, impact, desc in top_features:
            impact_pct = (impact / base_value) * 100 if base_value else 0

            icon = "🔺" if impact > 0 else "🔻"
            border_color = "#dc2626" if impact > 0 else "#16a34a"

            st.markdown(f"""
            <div style='background-color:#1e293b; padding:12px; border-radius:6px;
                        margin-bottom:10px; border-left:4px solid {border_color}'>
                <div style='font-weight:600; font-size:1.05em;'>{icon} {feature}</div>
                <div style='font-size:0.85em; color:#cbd5e1;'>ML-based contribution</div>
                <div style='font-size:0.8em; margin-top:4px;'>
                    Impact: ({impact_pct:+.1f}%)
                </div>
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # RIGHT: IMPACT DISTRIBUTION (NORMALIZED)
    # =========================
    with col_chart:
        st.markdown("### 📊 Impact Distribution")

        # Raw SHAP values
        raw_vals = [x[2] for x in top_features][::-1]
        chart_feats = [x[0] for x in top_features][::-1]

        # Normalize to -1..1 (relative influence)
        denom = sum(abs(v) for v in raw_vals) or 1
        chart_vals = [v / denom for v in raw_vals]

        # Color by SIGN (negative = red, positive = green)
        chart_colors = ["#dc2626" if v > 0 else "#16a34a" for v in raw_vals]

        # Labels as % share of explanation
        chart_labels = [f"{v*100:+.1f}%" for v in chart_vals]

        fig_shap = go.Figure()
        fig_shap.add_trace(go.Bar(
            y=chart_feats,
            x=chart_vals,
            orientation='h',
            marker=dict(color=chart_colors),
            text=chart_labels,
            textposition='auto',
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Normalized impact: %{x:.2f}<br>"
                "Share of explanation: %{text}<extra></extra>"
            )
        ))

        fig_shap.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20),
            height=400,
            xaxis=dict(
                range=[-0.5, 0.5],
                showgrid=True,
                gridcolor='#334155',
                zeroline=True,
                zerolinecolor='white',
                title="Normalized Impact (-1 to +1)",
                title_font=dict(color='#cbd5e1'),
                tickfont=dict(color='#cbd5e1')
            ),
            yaxis=dict(tickfont=dict(color='white'))
        )

        st.plotly_chart(fig_shap, use_container_width=True)

    
    # Final recommendation
    st.markdown("### 🎯 Summary")
    
    if res['action'] == 'SETTLE':
        st.success("✅ **SETTLE** - Settlement is economically superior to litigation.")
    elif res['action'] == 'LITIGATE':
        st.error("⚔️ **LITIGATE** - Litigation exposure is lower than settlement value.")
    else:
        st.warning("⚡ **STRATEGIZE** - Mixed factors require careful case management.")
    # === RISK ALERTS ===
    
    
    
    
    # === STRATEGIC RECOMMENDATION ===
    # st.markdown("<div class='section-header'>🎯 Next Best Action</div>", unsafe_allow_html=True)
    
    # if res['action'] == 'SETTLE':
    #     st.markdown(f"""
    #         <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
    #         <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
    #         Settlement is economically superior. Litigation exposure (<b>${total_exposure:,.0f}</b>) exceeds settlement value (<b>${median_value:,.0f}</b>).<br><br>
    #         <b>📋 Action Plan:</b><br>
    #         • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
    #         • <b>Opening Offer:</b> ${random_low:,.0f} – ${int(median_value*0.95):,.0f}<br>
    #         • <b>Walk-Away Price:</b> ${random_high:,.0f}<br>
    #         • <b>Savings vs Litigation:</b> ${total_exposure - median_value:,.0f}
    #         </div>
    #     """, unsafe_allow_html=True)
    # elif res['action'] == 'LITIGATE':
    #     st.markdown(f"""
    #         <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
    #         <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
    #         Settlement value (<b>${median_value:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
    #         <b>📋 Action Plan:</b><br>
    #         • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
    #         • <b>Expected Defense Costs:</b> ${defense_cost:,.0f}<br>
    #         • <b>Anticipated Verdict:</b> ${median_value:,.0f}<br>
    #         • <b>Do Not Settle Above:</b> ${int(total_exposure*0.9):,.0f}
    #         </div>
    #     """, unsafe_allow_html=True)
    # else:
    #     st.markdown(f"""
    #         <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
    #         <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
    #         Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
    #         <b>📋 Action Plan:</b><br>
    #         • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
    #         • <b>Test Offer:</b> ${int(median_value*0.85):,.0f}<br>
    #         • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
    #         • <b>Re-evaluate:</b> Quarterly or on significant developments
    #         </div>
    #     """, unsafe_allow_html=True)
    # === 8. NEXT BEST ACTION (UPDATED STRATEGY) ===
    st.markdown("<div class='section-header'>🎯 Next Best Action</div>", unsafe_allow_html=True)
    
    # Retrieve Demand Amount safely from inputs
    demand_val = inputs.get('Demand_Amount', 0)

    if res['action'] == 'SETTLE':
        # User Logic: Savings = Total Exposure - Upper Bound (random_high)
        savings_vs_litigation = total_exposure - random_high
        
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #166534 0%, #1b7a3a 100%); border-left: 5px solid #16a34a; border-radius: 10px; padding: 25px; color: #bbf7d0; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>✅ PURSUE SETTLEMENT IMMEDIATELY</b><br><br>
            Settlement is economically superior. Litigation exposure (<b>${total_exposure:,.0f}</b>) expected to run for <b>{res['months']:.1f} months</b>.<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Timeline:</b> Initiate negotiations within 7-10 days<br>
            • <b>Opening Offer:</b> $150,000<br>
            • <b>Plaintiff Demand:</b> ${demand_val:,.0f}<br>
            • <b>Walk-Away Price:</b> ${random_high:,.0f}<br>
            • <b>Savings vs Litigation:</b> ${savings_vs_litigation:,.0f}
            </div>
        """, unsafe_allow_html=True)

    elif res['action'] == 'LITIGATE':
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #7f1d1d 0%, #6b2121 100%); border-left: 5px solid #dc2626; border-radius: 10px; padding: 25px; color: #fecaca; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>⚔️ PROCEED TO LITIGATION</b><br><br>
            Settlement value (<b>${median_value:,.0f}</b>) significantly exceeds litigation exposure. Trial is economically justified.<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Trial Timeline:</b> {res['days']} days (~{res['months']:.1f} months)<br>
            • <b>Expected Defense Costs:</b> ${defense_cost:,.0f}<br>
            • <b>Anticipated Verdict:</b> ${median_value:,.0f}<br>
            • <b>Do Not Settle Above:</b> ${int(total_exposure*0.9):,.0f}
            </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #92400e 0%, #a16207 100%); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 25px; color: #fcd34d; font-weight: 600;'>
            <b style='font-size: 1.2rem;'>⚡ STRATEGIC NEGOTIATION REQUIRED</b><br><br>
            Borderline case. Settlement vs. litigation economics are nearly equivalent. Requires careful analysis.<br><br>
            <b>📋 Action Plan:</b><br>
            • <b>Next Step:</b> Conduct Independent Medical Exam (IME)<br>
            • <b>Test Offer:</b> ${int(median_value*0.85):,.0f}<br>
            • <b>Monitor:</b> Demand trajectory & attorney behavior<br>
            • <b>Re-evaluate:</b> Quarterly or on significant developments
            </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown("")
    
    
    
    
    
    

    
    # === RESET & NAVIGATION BUTTONS ===
    st.markdown("---")
    col_reset_1, col_reset_2 = st.columns(2)

    # BUTTON 1: Return to Landing Page
    with col_reset_1:
        if st.button("🏠 RETURN TO MAIN PAGE", use_container_width=True, key="btn_main_page"):
            # Reset everything
            st.session_state.submitted = False
            st.session_state.scenario_selected = False
            st.session_state.prefill = {}
            
            # Clear result variables
            for key in ["prediction", "recommendation", "risk", "driver_scores", "chart_data"]:
                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

    # BUTTON 2: Analyze New Case (skip landing page, keep scenario)
    with col_reset_2:
        if st.button("🔄 ANALYZE ANOTHER CASE", use_container_width=True, key="btn_new_case"):
            # Only reset submission
            st.session_state.submitted = False
            
            st.rerun()
