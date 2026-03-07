# Logistics AI Dashboard - Streamlit Application
import streamlit as st
import pandas as pd
import numpy as np
from modules.delay_prediction import DelayPredictor
from modules.sustainability_engine import SustainabilityEngine
from modules.route_optimizer import RouteOptimizer
import joblib
import os

# Custom CSS for modern AI theme with green + teal palette
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #F2F9F0 0%, #D1EACA 100%);
        min-height: 100vh;
        color: #000000;
    }
    
    /* Primary buttons with teal green */
    .stButton>button {
        background-color: #1F8268;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(31, 130, 104, 0.2);
    }
    
    .stButton>button:hover {
        background-color: #1a6b55;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(31, 130, 104, 0.3);
    }
    
    /* Cards and containers with soft mint */
    .css-1rddmyn, .stDataFrame, .stJson, .stAlert {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        color: #000000;
    }
    
    /* Metric cards with pale green */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        color: #000000;
    }
    
    /* Headers with black text */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, span, div {
        color: #000000 !important;
        font-weight: 700;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMarkdown {
        color: #000000;
    }
    
    /* Sidebar select dropdown styling */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: #FFFFFF !important;
        border: 2px solid #4DB8B8;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div > select {
        background-color: #FFFFFF !important;
        color: #000000;
    }
    
    /* Dropdown options */
    [data-testid="stSidebar"] .stSelectbox option {
        background-color: #FFFFFF !important;
        color: #000000;
    }
    
    /* All dropdown/select elements - force white background */
    .stSelectbox > div > div,
    .stSelectbox > div > div > select,
    .stSelectbox option {
        background-color: #FFFFFF !important;
        color: #000000;
    }
    
    /* Input fields */
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select,
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
        border: 2px solid #4DB8B8;
        color: #000000;
        border-radius: 8px;
    }
    
    /* Success messages */
    .stSuccess {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        color: #000000;
        border-left: 5px solid #000000;
    }
    
    /* Info messages */
    .stInfo {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        color: #000000;
        border-left: 5px solid #000000;
    }
    
    /* Warning messages */
    .stWarning {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        color: #000000;
        border-left: 5px solid #000000;
    }
    
    /* Error messages */
    .stError {
        background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%);
        color: #000000;
        border-left: 5px solid #000000;
    }
    
    /* Progress bar customization */
    .stProgress > div > div > div > div {
        background-color: #1F8268;
    }
    
    /* Form containers */
    .stForm {
        background: linear-gradient(135deg, rgba(77, 184, 184, 0.3) 0%, rgba(47, 168, 138, 0.3) 100%);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #4DB8B8;
    }
    
    /* General text color */
    body, .stApp * {
        color: #000000 !important;
    }
    
    /* Divider lines */
    hr {
        border-color: #1F8268;
        opacity: 0.3;
    }
</style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Logistics AI Dashboard",
    page_icon="🚚",
    layout="wide"
)

# Title and header with gradient background
st.markdown("""
<div style='background: linear-gradient(90deg, #FFFFFF 0%, #F2F9F0 100%); 
            padding: 30px; 
            border-radius: 15px; 
            margin-bottom: 30px;
            box-shadow: 0 6px 12px rgba(31, 130, 104, 0.3);'>
    <h1 style='color: #000000; margin: 0; font-size: 2.5em;'>🚚 Logistics AI Dashboard</h1>
    <p style='color: #000000; margin: 10px 0 0 0; font-size: 1.1em;'>
        Intelligent logistics optimization powered by Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard Overview Grid - TE Layout
st.markdown("""
<div style='margin-bottom: 30px;'>
    <h2 style='color: #000000; margin-bottom: 20px;'>Dashboard Overview</h2>
</div>
""", unsafe_allow_html=True)

# First Row - Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 10px 0; font-size: 1.1em;'>Active Trips</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 10px 0; font-size: 1.1em;'>At Risk</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 10px 0; font-size: 1.1em;'>Delayed</h3>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 10px 0; font-size: 1.1em;'>Carbon Emission</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Second Row - Agentic Feed and Tables
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 15px 0;'>Agentic Feed</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 15px 0;'>Risk Table</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Third Row - Map and Decision Layer
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 15px 0;'>MAP</h3>
    </div>
    """, unsafe_allow_html=True)

# Bot symbol between MAP and Decision Layer
st.markdown("""
<div style='text-align: center; margin: -10px 0 20px 0;'>
    <h1 style='color: #000000; font-size: 3em; margin: 0;'>🤖</h1>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 15px 0;'>Decision Layer</h3>
    </div>
    """, unsafe_allow_html=True)

# Fourth Row - Counter Factual and Screen Auton
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4DB8B8 0%, #2FA88A 100%); 
                padding: 25px; 
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(31,130,104,0.3);
                margin-bottom: 20px;'>
        <h3 style='color: #000000; margin: 0 0 15px 0;'>Counter Factual</h3>
    </div>
    """, unsafe_allow_html=True)

# Initialize models
@st.cache_resource
def load_models():
    """Load ML models and initialize engines"""
    delay_predictor = None
    model_path = 'models/delay_model.pkl'
    
    if os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            delay_predictor = {'model': model, 'loaded': True}
        except Exception as e:
            st.error(f"Error loading model: {e}")
            delay_predictor = {'model': None, 'loaded': False}
    else:
        delay_predictor = {'model': None, 'loaded': False}
    
    sustainability_engine = SustainabilityEngine()
    route_optimizer = RouteOptimizer()
    
    return delay_predictor, sustainability_engine, route_optimizer

delay_predictor, sustainability_engine, route_optimizer = load_models()

# Sidebar navigation with custom styling
st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Choose a module",
    ["📊 Dashboard Overview", 
     "⏱️ Delay Prediction", 
     "🌱 Carbon Footprint Calculator", 
     "🗺️ Route Optimizer",
     "📁 Data Viewer"],
    index=0
)

# Delay Prediction Module
if page == "⏱️ Delay Prediction":
    st.header("⏱️ Delivery Delay Prediction")
    
    with st.form("delay_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            distance = st.number_input("Distance (km)", min_value=0.0, value=100.0, step=1.0)
            traffic = st.selectbox("Traffic Level", ["low", "medium", "high"])
            weather = st.selectbox("Weather Condition", ["clear", "rain", "snow", "storm", "fog"])
        
        with col2:
            time_of_day = st.selectbox("Time of Day", ["day", "night", "peak"])
            vehicle_type = st.selectbox("Vehicle Type", ["truck", "van", "bike"])
        
        submitted = st.form_submit_button("🔮 Predict Delay", use_container_width=True)
        
        if submitted:
            input_data = {
                'distance': distance,
                'traffic': traffic,
                'weather': weather,
                'time_of_day': time_of_day,
                'vehicle_type': vehicle_type
            }
            
            predictor = DelayPredictor('models/delay_model.pkl') if delay_predictor['loaded'] else DelayPredictor()
            prediction = predictor.predict(input_data)
            
            # Display result in styled card
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #1F8268 0%, #2FA88A 100%); 
                        padding: 30px; 
                        border-radius: 15px; 
                        margin: 20px 0;
                        box-shadow: 0 6px 12px rgba(31, 130, 104, 0.3);
                        text-align: center;'>
                <h2 style='color: white; margin: 0;'>Predicted Delay</h2>
                <h1 style='color: white; font-size: 3em; margin: 10px 0;'>{prediction['delay']:.2f} minutes</h1>
                <p style='color: #F2F9F0; font-size: 1.2em;'>Confidence Level: {prediction['confidence']*100:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Show factors
            st.subheader("Input Parameters:")
            st.json(input_data)

# Carbon Footprint Calculator
elif page == "🌱 Carbon Footprint Calculator":
    st.header("🌱 Carbon Footprint Calculator")
    
    with st.form("carbon_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            distance = st.number_input("Distance (km)", min_value=0.0, value=100.0, step=1.0)
            vehicle_type = st.selectbox("Vehicle Type", 
                                      ["truck", "van", "bike", "electric_van", "train", "ship"])
            weight = st.number_input("Weight (kg)", min_value=0.0, value=1000.0, step=50.0)
        
        with col2:
            packaging = st.selectbox("Packaging Type", 
                                   ["standard", "eco_friendly", "minimal", "excessive"])
        
        submitted = st.form_submit_button("🌍 Calculate Carbon Footprint", use_container_width=True)
        
        if submitted:
            input_data = {
                'distance': distance,
                'vehicle_type': vehicle_type,
                'weight': weight,
                'packaging': packaging
            }
            
            result = sustainability_engine.calculate(input_data)
            
            # Display results in styled cards
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div style='background-color: #1F8268; padding: 20px; border-radius: 12px; 
                            text-align: center; box-shadow: 0 4px 8px rgba(31,130,104,0.3);'>
                    <h3 style='color: white; margin: 0;'>Carbon Footprint</h3>
                    <h2 style='color: white; font-size: 2em; margin: 10px 0;'>{result['carbon']:.3f}</h2>
                    <p style='color: #F2F9F0;'>kg CO2e</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #1F8268 0%, #2FA88A 100%); 
                            padding: 20px; border-radius: 12px; text-align: center;
                            box-shadow: 0 4px 8px rgba(31,130,104,0.3);'>
                    <h3 style='color: white; margin: 0;'>Sustainability Score</h3>
                    <h2 style='color: white; font-size: 2em; margin: 10px 0;'>{result['score']:.1f}</h2>
                    <p style='color: #F2F9F0;'>out of 100</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div style='background-color: #C4E4BB; padding: 20px; border-radius: 12px; 
                            text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
                    <h3 style='color: #190A28; margin: 0;'>Emission Factor</h3>
                    <h2 style='color: #190A28; font-size: 1.8em; margin: 10px 0;'>{result['vehicle_emission_factor']:.3f}</h2>
                    <p style='color: #190A28;'>kg/km</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Progress bar for sustainability score
            st.subheader("Sustainability Rating")
            st.progress(result['score'] / 100)
            
            if result['score'] >= 80:
                st.success("Excellent! Very eco-friendly shipment 🌟")
            elif result['score'] >= 60:
                st.info("Good sustainability practices 👍")
            elif result['score'] >= 40:
                st.warning("Fair - room for improvement ⚠️")
            else:
                st.error("Poor - consider eco-friendly alternatives 🚨")

# Route Optimizer
elif page == "🗺️ Route Optimizer":
    st.header("🗺️ Delivery Route Optimization")
    
    with st.form("route_form"):
        st.write("Enter delivery stops (one per line or comma-separated):")
        stops_input = st.text_area("Delivery Stops", 
                                  placeholder="Stop A\nStop B\nStop C\nStop D",
                                  height=100)
        start_location = st.text_input("Starting Location", "Warehouse")
        
        submitted = st.form_submit_button("🚀 Optimize Route", use_container_width=True)
        
        if submitted:
            # Parse stops
            if '\n' in stops_input:
                stops = [s.strip() for s in stops_input.split('\n') if s.strip()]
            else:
                stops = [s.strip() for s in stops_input.split(',') if s.strip()]
            
            if not stops:
                st.warning("Please enter at least one delivery stop")
            else:
                input_data = {
                    'stops': stops,
                    'start': start_location
                }
                
                result = route_optimizer.optimize(input_data)
                
                # Display optimized route in styled box
                st.subheader("Optimized Route:")
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #1F8268 0%, #2FA88A 100%); 
                            padding: 25px; 
                            border-radius: 12px; 
                            margin: 20px 0;
                            box-shadow: 0 4px 8px rgba(31,130,104,0.3);'>
                    <h3 style='color: white; margin: 0 0 15px 0;'>🛣️ Route Path</h3>
                    <p style='color: white; font-size: 1.3em; font-weight: 600;'>{route_display}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Total Distance", f"{result['distance']:.1f} km")
                with col2:
                    st.metric("Estimated Time", f"{result['time']:.1f} min")
                with col3:
                    st.metric("Fuel Savings", f"{result['savings']:.1f}%")
                
                if result['savings'] > 0:
                    st.success("Route optimization successful! Fuel saved! 💰")
                else:
                    st.info("Route calculated ✓")

# Data Viewer
elif page == "📁 Data Viewer":
    st.header("📁 Logistics Data Viewer")
    
    data_path = 'data/logistics_data.csv'
    
    if os.path.exists(data_path):
        try:
            df = pd.read_csv(data_path)
            
            # Show basic info
            st.subheader("Dataset Overview")
            st.write(f"**Records:** {len(df)} | **Columns:** {len(df.columns)}")
            
            # Show dataframe with custom styling
            st.dataframe(df, use_container_width=True)
            
            # Statistics
            st.subheader("Statistics")
            st.write(df.describe())
            
            # Quick visualizations
            st.subheader("Quick Insights")
            col1, col2 = st.columns(2)
            
            with col1:
                if 'distance_km' in df.columns:
                    st.bar_chart(df['distance_km'].head(10))
                    st.caption("Top 10 Distances")
            
            with col2:
                if 'vehicle_type' in df.columns:
                    vehicle_counts = df['vehicle_type'].value_counts()
                    st.bar_chart(vehicle_counts)
                    st.caption("Vehicle Distribution")
        
        except Exception as e:
            st.error(f"Error loading data: {e}")
    else:
        st.warning("Data file not found. Please upload logistics_data.csv to the data/ folder.")

# Footer with gradient
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(90deg, #1F8268 0%, #2FA88A 100%); 
            padding: 20px; 
            border-radius: 15px; 
            text-align: center;
            margin-top: 30px;
            box-shadow: 0 4px 8px rgba(31, 130, 104, 0.2);'>
    <p style='color: white; margin: 0; font-size: 0.9em;'>
        Logistics AI Dashboard © 2026 | Powered by Streamlit, Flask, and Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)
