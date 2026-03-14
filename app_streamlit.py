import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module=".*sklearn.*")

# Page configuration
st.set_page_config(
    page_title="Gemstone Price Predictor",
    page_icon="💎",
    layout="wide"
)

# Title and description
st.title("💎 Gemstone Price Prediction")
st.markdown("""
This application predicts the price of gemstones based on their physical characteristics.
Enter the details below to get an instant price prediction!
""")

# Create two columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Enter Gemstone Details")
    
    # Numerical inputs
    carat = st.number_input(
        "Carat (weight)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.01,
        help="Weight of the gemstone in carats"
    )
    
    depth = st.number_input(
        "Depth (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.1,
        help="Total depth percentage"
    )
    
    table = st.number_input(
        "Table Width (%)",
        min_value=0.0,
        max_value=100.0,
        value=57.0,
        step=0.1,
        help="Width of the top facet relative to widest diameter"
    )
    
    x = st.number_input(
        "Length (mm)",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        step=0.01,
        help="Length in millimeters"
    )
    
    y = st.number_input(
        "Width (mm)",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        step=0.01,
        help="Width in millimeters"
    )
    
    z = st.number_input(
        "Depth (mm)",
        min_value=0.0,
        max_value=20.0,
        value=3.0,
        step=0.01,
        help="Depth in millimeters"
    )

with col2:
    st.subheader("Select Quality Characteristics")
    
    # Categorical inputs
    cut_options = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
    cut = st.selectbox(
        "Cut Quality",
        options=cut_options,
        index=2,
        help="Quality of the cut (Ideal is best)"
    )
    
    color_options = ["D", "E", "F", "G", "H", "I", "J"]
    color = st.selectbox(
        "Color Grade",
        options=color_options,
        index=3,
        help="Color grade (D is best/colorless)"
    )
    
    clarity_options = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    clarity = st.selectbox(
        "Clarity",
        options=clarity_options,
        index=3,
        help="Clarity grade (IF is best - Internally Flawless)"
    )
    
    # Display sample/reference information
    st.markdown("---")
    st.markdown("**Quick Reference:**")
    st.info("""
    - **Cut**: Fair < Good < Very Good < Premium < Ideal
    - **Color**: D (colorless) to J (light yellow)
    - **Clarity**: I1 (included) to IF (internally flawless)
    """)

# Predict button
st.markdown("---")
if st.button("🔮 Predict Price", type="primary", use_container_width=True):
    try:
        # Create custom data object
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        
        # Get dataframe
        pred_df = data.get_data_as_dataframe()
        
        # Make prediction
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0], 2)
        
        # Display result with formatting
        st.success(f"## 💰 Predicted Price: ${results:,.2f}")
        
        # Display input summary
        st.markdown("### 📊 Input Summary")
        summary_df = pd.DataFrame({
            'Feature': ['Carat', 'Depth', 'Table', 'X', 'Y', 'Z', 'Cut', 'Color', 'Clarity'],
            'Value': [carat, f"{depth}%", f"{table}%", f"{x}mm", f"{y}mm", f"{z}mm", cut, color, clarity]
        })
        st.table(summary_df)
        
    except Exception as e:
        st.error(f"❌ Error occurred during prediction: {str(e)}")
        st.error("Please check your inputs and try again.")

# Add footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Built with Streamlit | Powered by Machine Learning</small>
</div>
""", unsafe_allow_html=True)
