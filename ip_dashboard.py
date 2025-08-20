"""
Leo Electric IP Protection Strategy Dashboard
Interactive Streamlit application for stakeholder presentations
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Import the simulator class
import sys
import os
sys.path.append(os.path.dirname(__file__))
from ip_protection_simulation import IPProtectionSimulator

def main():
    st.set_page_config(
        page_title="Leo Electric IP Strategy Dashboard",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize simulator
    simulator = IPProtectionSimulator()
    
    # Header
    st.title("⚡ Leo Electric IP Protection Strategy")
    st.subheader("Strategic Blueprint for Climate Intelligence Stack")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    view = st.sidebar.selectbox(
        "Select View",
        ["Executive Summary", "Portfolio Overview", "Strategy Matrix", "Risk Assessment", "Timeline", "Individual Assets"]
    )
    
    if view == "Executive Summary":
        show_executive_summary(simulator)
    elif view == "Portfolio Overview":
        show_portfolio_overview(simulator)
    elif view == "Strategy Matrix":
        show_strategy_matrix(simulator)
    elif view == "Risk Assessment":
        show_risk_assessment(simulator)
    elif view == "Timeline":
        show_timeline(simulator)
    elif view == "Individual Assets":
        show_individual_assets(simulator)

def show_executive_summary(simulator):
    st.header("Executive Summary")
    
    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    total_assets = len(simulator.ip_portfolio)
    patent_count = sum(1 for ip in simulator.ip_portfolio.values() if 'Patent' in ip['protection'])
    trade_secret_count = sum(1 for ip in simulator.ip_portfolio.values() if 'Trade Secret' in ip['protection'])
    high_priority = sum(1 for ip in simulator.ip_portfolio.values() if ip['priority'] in ['Critical', 'High'])
    
    with col1:
        st.metric("Total IP Assets", total_assets)
    with col2:
        st.metric("Patent Applications", patent_count)
    with col3:
        st.metric("Trade Secrets", trade_secret_count)
    with col4:
        st.metric("High Priority Assets", f"{high_priority}/{total_assets}")
    
    # Strategic overview
    st.subheader("Strategic Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Key Strategic Pillars
        
        **🔐 Foundation Protection**
        - Core MRV technologies secured through patents
        - Telemetry-attested systems provide market credibility
        
        **💰 Financial Innovation**
        - Blended asset valuation creates new asset class
        - Patent protection prevents replication of algorithms
        
        **🤝 Operational Excellence**
        - Critical algorithms maintained as trade secrets
        - Competitive advantage through proprietary methods
        """)
    
    with col2:
        st.markdown("""
        ### Protection Strategy Rationale
        
        **Patents for Market-Facing Tech**
        - Public credibility with registries
        - Legal defense against competitors
        - Foundation for licensing opportunities
        
        **Trade Secrets for Operational IP**
        - Difficult to reverse-engineer
        - Maintains competitive edge
        - No disclosure requirements
        """)
    
    # Financial impact projection
    st.subheader("Projected Financial Impact")
    
    # Create a simple projection chart
    years = list(range(2025, 2031))
    patent_value = [0, 2, 5, 12, 25, 40]  # Million USD
    trade_secret_value = [1, 3, 6, 10, 15, 22]  # Million USD
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=patent_value, mode='lines+markers', name='Patent Portfolio Value', line=dict(color='#2E86AB')))
    fig.add_trace(go.Scatter(x=years, y=trade_secret_value, mode='lines+markers', name='Trade Secret Value', line=dict(color='#F18F01')))
    
    fig.update_layout(
        title="Projected IP Portfolio Value",
        xaxis_title="Year",
        yaxis_title="Value (Million USD)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_portfolio_overview(simulator):
    st.header("Portfolio Overview")
    
    # Create the portfolio overview visualization
    fig = simulator.create_portfolio_overview()
    st.plotly_chart(fig, use_container_width=True)
    
    # Protection type breakdown
    st.subheader("Protection Strategy Distribution")
    
    protection_counts = {}
    for ip in simulator.ip_portfolio.values():
        prot = ip['protection']
        protection_counts[prot] = protection_counts.get(prot, 0) + 1
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Patents", protection_counts.get('Patent', 0))
        st.caption("Core foundational technologies")
    
    with col2:
        st.metric("Patent/Defensive Pub", protection_counts.get('Patent (or Defensive Pub)', 0))
        st.caption("Standardization considerations")
    
    with col3:
        st.metric("Trade Secrets", protection_counts.get('Trade Secret', 0))
        st.caption("Operational advantages")

def show_strategy_matrix(simulator):
    st.header("Strategy Evaluation Matrix")
    
    fig = simulator.create_protection_strategy_matrix()
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Matrix Interpretation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### High-Impact Assets (Score 8-10)
        - **A**: Telemetry-attested MRV - Foundation technology
        - **B**: Degradation-aware charging - Operational advantage
        - **C**: Swap-station integrity - Market trust
        - **E**: Blended asset valuation - Financial innovation
        """)
    
    with col2:
        st.markdown("""
        ### Protection Strategy Logic
        - **High Market Impact + High Complexity** → Patent
        - **High Defensibility + Lower Complexity** → Trade Secret
        - **Standardization Potential** → Patent or Defensive Publication
        """)

def show_risk_assessment(simulator):
    st.header("Risk Assessment")
    
    fig = simulator.create_risk_assessment()
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Risk Mitigation Strategies")
    
    # Create risk mitigation recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### High-Risk Assets
        - Monitor competitive landscape
        - Accelerate patent filing timelines
        - Implement additional trade secret protections
        """)
    
    with col2:
        st.markdown("""
        ### Mitigation Actions
        1. **Freedom to Operate Analysis** - Before product launch
        2. **IP Monitoring Services** - Track competitor filings
        3. **Employee Training** - Trade secret handling protocols
        """)

def show_timeline(simulator):
    st.header("Implementation Timeline")
    
    fig = simulator.create_timeline_simulation()
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Critical Milestones")
    
    # Timeline details
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Q1 2025
        - File patent applications for A, B, C
        - Implement trade secret protocols
        """)
    
    with col2:
        st.markdown("""
        ### Q2-Q3 2025
        - File remaining patent applications
        - Begin international filing strategy
        """)
    
    with col3:
        st.markdown("""
        ### 2026-2027
        - Patent publications
        - Potential patent grants
        - Licensing opportunities
        """)

def show_individual_assets(simulator):
    st.header("Individual IP Assets")
    
    # Asset selector
    asset_keys = list(simulator.ip_portfolio.keys())
    selected_asset = st.selectbox("Select IP Asset", asset_keys)
    
    if selected_asset:
        ip = simulator.ip_portfolio[selected_asset]
        
        # Asset details
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(f"{selected_asset}. {ip['name']}")
            st.markdown(f"**Protection Strategy:** {ip['protection']}")
            st.markdown(f"**Priority:** {ip['priority']}")
            st.markdown(f"**Rationale:** {ip['rationale']}")
        
        with col2:
            # Metrics
            st.metric("Market Impact", f"{ip['market_impact']}/10")
            st.metric("Technical Complexity", f"{ip['technical_complexity']}/10")
            st.metric("Defensibility", f"{ip['defensibility']}/10")
            st.metric("Revenue Potential", f"{ip['revenue_potential']}/10")
        
        # Radar chart for selected asset
        categories = ['Market Impact', 'Technical Complexity', 'Defensibility', 'Revenue Potential']
        values = [ip['market_impact'], ip['technical_complexity'], ip['defensibility'], ip['revenue_potential']]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],  # Close the polygon
            theta=categories + [categories[0]],
            fill='toself',
            name=ip['name'][:20],
            line=dict(color=simulator.protection_colors[ip['protection']])
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            title=f"Asset Profile: {selected_asset}",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Comparison with portfolio average
        st.subheader("Portfolio Comparison")
        
        avg_market = np.mean([v['market_impact'] for v in simulator.ip_portfolio.values()])
        avg_complexity = np.mean([v['technical_complexity'] for v in simulator.ip_portfolio.values()])
        avg_defensibility = np.mean([v['defensibility'] for v in simulator.ip_portfolio.values()])
        avg_revenue = np.mean([v['revenue_potential'] for v in simulator.ip_portfolio.values()])
        
        comparison_data = {
            'Metric': ['Market Impact', 'Technical Complexity', 'Defensibility', 'Revenue Potential'],
            'Asset Score': [ip['market_impact'], ip['technical_complexity'], ip['defensibility'], ip['revenue_potential']],
            'Portfolio Average': [avg_market, avg_complexity, avg_defensibility, avg_revenue]
        }
        
        df_comparison = pd.DataFrame(comparison_data)
        
        fig_comparison = px.bar(
            df_comparison, 
            x='Metric', 
            y=['Asset Score', 'Portfolio Average'],
            barmode='group',
            title="Asset vs Portfolio Average"
        )
        
        st.plotly_chart(fig_comparison, use_container_width=True)

if __name__ == "__main__":
    main()