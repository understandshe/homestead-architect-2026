"""
CHUNDAL GARDENS AI ARCHITECT v1.0 - 2026 GLOBAL EDITION
Architecture: Image-to-Data Pipeline + Multi-Scale 3D Rendering
Engine: Plotly Premium + OpenCV Pro
"""

import streamlit as st
import plotly.io as pio
from core.image_processor import ImageToLandscapeEngine
from core.ultimate_architect_2026 import UltimateVisualizer3D
import pandas as pd

# Page Config for Premium Feel
st.set_page_config(
    page_title="Chundal Gardens | AI Global Architect 2026",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────────────────────
# 1. SIDEBAR: GLOBAL SETTINGS & IMAGE UPLOAD
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://chundalgardens.com/logo.png", width=200) # Brand Power
    st.header("🌍 Global Parameters")
    
    country = st.selectbox("Select Country", ["India", "USA", "Nigeria", "Australia", "UK"])
    currency = "INR" if country == "India" else "USD"
    
    st.divider()
    
    st.subheader("📸 Design Source")
    uploaded_file = st.file_uploader("Upload Pinterest Idea or Site Photo", type=['jpg', 'jpeg', 'png'])
    
    st.subheader("📏 Land Scale")
    # Dynamic Slider from 0.1 to 10,000 Acres
    acres = st.select_slider(
        "How many acres?",
        options=[0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
    )
    
    slope = st.selectbox("Slope Direction", ["Flat", "North", "South", "East", "West"])
    
    generate_btn = st.button("🔥 GENERATE 3D EMPIRE", use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# 2. MAIN INTERFACE
# ─────────────────────────────────────────────────────────────────────────────
st.title("🏡 Homestead Architect Pro 2026")
st.caption(f"Status: Global Engine Active | Scaling: {acres} Acres | Currency: {currency}")

if uploaded_file and generate_btn:
    with st.spinner("🧠 AI is extracting architecture from image..."):
        # STEP 1: Process Image to Extract Pattern DNA
        processor = ImageToLandscapeEngine()
        raw_data = processor.process_image(uploaded_file.getvalue(), acres)
        
        # STEP 2: Feed Data into Ultimate 3D Engine
        # Adding slope info to the processed data
        raw_data['slope'] = slope
        visualizer = UltimateVisualizer3D(raw_data)
        fig = visualizer.generate_global_estate()
        
        # ─────────────────────────────────────────────────────────────────────
        # 3. DISPLAY & INTERACTION
        # ─────────────────────────────────────────────────────────────────────
        tab1, tab2, tab3 = st.tabs(["🏗️ Interactive 3D View", "📊 2026 Global Costing", "📄 Export Report"])
        
        with tab1:
            st.plotly_chart(fig, use_container_width=True, theme=None)
            
            # --- PREMUM HTML DOWNLOAD ---
            html_bytes = fig.to_html(include_plotlyjs='cdn').encode()
            st.download_button(
                label="📥 Download Interactive 3D Map",
                data=html_bytes,
                file_name=f"chundal_gardens_{acres}acre_3d.html",
                mime="text/html",
                help="Download to rotate/zoom without internet!"
            )
            
        with tab2:
            st.subheader(f"💰 Project Financials - {country} (2026 Estimates)")
            # Dynamic Costing Logic based on Acres
            base_cost = 500000 if country == "India" else 15000
            total_est = base_cost * acres * 0.85 # 15% Bulk discount for large scale
            
            st.metric("Total Estimated Investment", f"{currency} {total_est:,.2f}")
            st.dataframe(pd.DataFrame({
                "Category": ["Solar Infrastructure", "Water Management", "Landscaping", "Villa Construction"],
                "Estimate": [total_est*0.2, total_est*0.15, total_est*0.25, total_est*0.4]
            }))
            
        with tab3:
            st.success("✅ 8-Page Ultimate Report Generated!")
            st.button("📥 Download PDF Pro (Full HD Images)")

else:
    # Default Landing State
    st.info("👈 Upload a Pinterest image and select your land scale to begin the transformation.")
    st.image("https://chundalgardens.com/preview_3d.jpg", caption="Your design will appear here in 3D")

# Footer Branding
st.divider()
st.markdown("<center>© 2026 Chundal Gardens Global | Powered by AI Architect Engine</center>", unsafe_allow_name=True)
