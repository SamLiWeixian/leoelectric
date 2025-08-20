"""
Utility functions for parameter explanations and UI helpers
"""

import streamlit as st

def create_parameter_explanation(param_name, description, impact, range_info):
    """Create a styled parameter explanation box"""
    return f"""
    <div class="parameter-explanation">
        <h4>{param_name}</h4>
        <p><strong>Description:</strong> {description}</p>
        <p><strong>Business Impact:</strong> {impact}</p>
        <p><strong>Typical Range:</strong> {range_info}</p>
    </div>
    """

def display_metric_cards(metrics_data):
    """Display a set of metric cards in columns"""
    num_cols = len(metrics_data)
    cols = st.columns(num_cols)
    
    for i, (label, value) in enumerate(metrics_data.items()):
        with cols[i]:
            st.metric(label, value)

def create_success_story_card(title, before, after, result):
    """Create a styled success story card"""
    return f"""
    <div class="simple-explanation">
        <h4>{title}</h4>
        <p><strong>Before:</strong> {before}</p>
        <p><strong>After:</strong> {after}</p>
        <p><strong>Result:</strong> {result}</p>
    </div>
    """

def create_advantage_card(title, description, bg_color="1f4e79"):
    """Create a styled advantage card with custom background color"""
    return f"""
    <div style="background: #{bg_color}; color: white; padding: 1.5rem; border-radius: 10px; margin: 0.5rem; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
        <h4 style="color: white;">{title}</h4>
        <p style="color: white;">{description}</p>
    </div>
    """