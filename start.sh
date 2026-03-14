#!/bin/bash

# Set default port if not provided
PORT=${PORT:-8501}

# Run Streamlit
streamlit run app_streamlit.py --server.port=$PORT --server.address=0.0.0.0
