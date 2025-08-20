"""
Leo Climate Intelligence Stack (LCIS) Interactive Business Model Dashboard
Comprehensive Streamlit application for demonstrating all formulas and business concepts
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math
from datetime import datetime
import json

# Import the LCIS business model
import sys
import os
sys.path.append(os.path.dirname(__file__))
from lcis_business_model import LCISBusinessModel

def main():
    st.set_page_config(
        page_title="LCIS Business Model Dashboard",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize LCIS model
    lcis = LCISBusinessModel()
    
    # Header
    st.title("🌱 Leo Climate Intelligence Stack (LCIS)")
    st.subheader("Interactive Business Model & Formula Demonstration")
    
    # Sidebar navigation
    st.sidebar.title("LCIS Components")
    component = st.sidebar.selectbox(
        "Select Component to Explore",
        [
            "🎯 Executive Dashboard", 
            "💰 Carbon Credits (Formula A)",
            "🔋 Degradation-Aware Charging (Formula B)",
            "🔄 Swap Station Integrity (Formula C)",
            "📊 Blended Asset Valuation (Formula E)",
            "🌍 Cross-Border Data (Formula F)",
            "⚗️ Sodium-Ion Optimization (Trade Secret H)",
            "📈 Complete Simulation Results"
        ]
    )
    
    if component == "🎯 Executive Dashboard":
        show_executive_dashboard(lcis)
    elif component == "💰 Carbon Credits (Formula A)":
        show_carbon_credits_calculator(lcis)
    elif component == "🔋 Degradation-Aware Charging (Formula B)":
        show_charging_optimization(lcis)
    elif component == "🔄 Swap Station Integrity (Formula C)":
        show_swap_station_analysis(lcis)
    elif component == "📊 Blended Asset Valuation (Formula E)":
        show_asset_valuation(lcis)
    elif component == "🌍 Cross-Border Data (Formula F)":
        show_cross_border_data(lcis)
    elif component == "⚗️ Sodium-Ion Optimization (Trade Secret H)":
        show_sodium_optimization(lcis)
    elif component == "📈 Complete Simulation Results":
        show_complete_simulation(lcis)

def show_executive_dashboard(lcis):
    st.header("🎯 Executive Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Core Formulas", "6", "Patented IP")
    with col2:
        st.metric("Trade Secrets", "2", "Proprietary")
    with col3:
        st.metric("Market Value", "$25-35M", "NPV 5-year")
    with col4:
        st.metric("ROI Timeline", "18-24 months", "Payback")
    
    # Business model overview
    st.subheader("🚀 Business Model Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💡 Core Value Propositions
        
        **1. Verifiable Carbon Credits**
        - Telemetry-attested MRV system
        - 99% verification confidence
        - Premium pricing for verified credits
        
        **2. Battery Optimization**
        - 20-30% longer battery life
        - Degradation-aware charging
        - Real-time SOH management
        
        **3. Financial Innovation**
        - Securitizable EV asset class
        - Risk-adjusted portfolio yields
        - Cross-border compliance
        """)
    
    with col2:
        st.markdown("""
        ### 📈 Market Opportunity
        
        **Addressable Markets**
        - Carbon Credits: $1B+ annually
        - EV Optimization: $500M+ market
        - Cross-Border Data: $2B+ compliance
        - Battery Management: $10B+ global
        
        **Competitive Advantages**
        - First-mover in telemetry MRV
        - Patented degradation algorithms
        - Proprietary sodium-ion optimization
        """)
    
    # Revenue projections
    st.subheader("💰 Revenue Projections")
    
    years = list(range(2025, 2031))
    carbon_revenue = [0, 2, 8, 20, 35, 50]  # Million USD
    optimization_revenue = [0.5, 3, 8, 15, 22, 30]
    data_revenue = [0.2, 1, 3, 7, 12, 18]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=carbon_revenue, name='Carbon Credits', stackgroup='one'))
    fig.add_trace(go.Scatter(x=years, y=optimization_revenue, name='Battery Optimization', stackgroup='one'))
    fig.add_trace(go.Scatter(x=years, y=data_revenue, name='Data Services', stackgroup='one'))
    
    fig.update_layout(
        title="LCIS Revenue Projection by Business Line",
        xaxis_title="Year",
        yaxis_title="Revenue (Million USD)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_carbon_credits_calculator(lcis):
    st.header("💰 Carbon Credits Calculator")
    st.subheader("Formula A: Telemetry-Attested Micro-Mobility MRV")
    
    # Show the formula
    st.latex(r'''
    Credits = Energy_{delivered} \times Efficiency \times (1 - Carbon_{intensity} \times Clean_{ratio}) \times Rate_{base} \times Quality_{factor}
    ''')
    
    # Input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        energy_delivered = st.slider("Energy Delivered (kWh)", 1.0, 100.0, 25.0, 0.1)
        vehicle_type = st.selectbox("Vehicle Type", ["2W", "3W", "Light"])
        clean_energy_ratio = st.slider("Clean Energy Ratio", 0.0, 1.0, 0.7, 0.01)
    
    with col2:
        carbon_price = st.number_input("Carbon Price ($/tCO2e)", 10.0, 100.0, 25.0, 1.0)
        charging_efficiency = st.slider("Charging Efficiency", 0.8, 0.98, 0.92, 0.01)
        accuracy_threshold = st.slider("Telemetry Accuracy", 0.9, 0.99, 0.95, 0.001)
    
    # Update LCIS parameters
    lcis.carbon_price_per_ton = carbon_price
    lcis.charging_efficiency = charging_efficiency
    lcis.accuracy_threshold = accuracy_threshold
    lcis.clean_energy_ratio = clean_energy_ratio
    
    # Calculate results
    results = lcis.calculate_carbon_credits(energy_delivered, vehicle_type, clean_energy_ratio)
    
    # Display results
    st.subheader("📊 Calculation Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Verified Credits", f"{results['verified_credits']:.3f}")
    with col2:
        st.metric("Carbon Value", f"${results['carbon_value_usd']:.2f}")
    with col3:
        st.metric("Quality Factor", f"{results['quality_factor']:.3f}")
    with col4:
        st.metric("Credit Rate", f"{results['credit_rate']:.4f} credits/kWh")
    
    # Detailed breakdown
    st.subheader("🔍 Detailed Breakdown")
    
    breakdown_data = {
        'Component': ['Energy Delivered', 'Charging Efficiency', 'Clean Energy Factor', 'Base Credit Rate', 'Quality Factor', 'Final Credits'],
        'Value': [
            f"{results['energy_delivered']:.2f} kWh",
            f"{charging_efficiency:.3f}",
            f"{1 - lcis.grid_carbon_intensity * (1 - clean_energy_ratio):.3f}",
            f"{lcis.base_credit_rate:.3f}",
            f"{results['quality_factor']:.3f}",
            f"{results['verified_credits']:.3f}"
        ]
    }
    
    st.table(pd.DataFrame(breakdown_data))
    
    # Sensitivity analysis
    st.subheader("📈 Sensitivity Analysis")
    
    energy_range = np.linspace(1, 100, 50)
    credit_values = []
    
    for energy in energy_range:
        result = lcis.calculate_carbon_credits(energy, vehicle_type, clean_energy_ratio)
        credit_values.append(result['verified_credits'])
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=energy_range, y=credit_values, mode='lines', name='Credits vs Energy'))
    fig.update_layout(
        title="Carbon Credits vs Energy Delivered",
        xaxis_title="Energy Delivered (kWh)",
        yaxis_title="Verified Credits",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_charging_optimization(lcis):
    st.header("🔋 Degradation-Aware Charging Optimization")
    st.subheader("Formula B: SOH-Optimized Charging Orchestration")
    
    # Show the formula
    st.latex(r'''
    Rate_{optimal} = Rate_{base} \times SOH_{factor} \times Temp_{factor} \times DoD_{factor}
    ''')
    
    # Input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        battery_capacity = st.slider("Battery Capacity (kWh)", 2.0, 50.0, 15.0, 0.5)
        current_soh = st.slider("Current SOH", 0.6, 1.0, 0.85, 0.01)
        temperature = st.slider("Temperature (°C)", 0, 50, 25, 1)
    
    with col2:
        target_soc = st.slider("Target SOC (%)", 50, 100, 80, 5)
        cycles_completed = st.number_input("Cycles Completed", 0, 5000, 1000, 50)
    
    # Calculate results
    results = lcis.calculate_degradation_aware_charging(
        battery_capacity, current_soh, temperature, target_soc, cycles_completed
    )
    
    # Display results
    st.subheader("📊 Optimization Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Optimal Rate", f"{results['optimal_charging_rate']:.2f}C")
    with col2:
        st.metric("Credit Multiplier", f"{results['credit_yield_multiplier']:.3f}")
    with col3:
        st.metric("Projected SOH (1yr)", f"{results['projected_soh_1yr']:.3f}")
    with col4:
        st.metric("Degradation Rate", f"{results['degradation_rate']:.4f}/year")
    
    # Impact analysis
    st.subheader("🔍 Impact Analysis")
    
    # Create temperature impact visualization
    temp_range = np.linspace(10, 45, 36)
    optimal_rates = []
    degradation_rates = []
    
    for temp in temp_range:
        result = lcis.calculate_degradation_aware_charging(
            battery_capacity, current_soh, temp, target_soc, cycles_completed
        )
        optimal_rates.append(result['optimal_charging_rate'])
        degradation_rates.append(result['degradation_rate'])
    
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Optimal Rate vs Temperature', 'Degradation vs Temperature'])
    
    fig.add_trace(
        go.Scatter(x=temp_range, y=optimal_rates, mode='lines', name='Optimal Rate'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=temp_range, y=degradation_rates, mode='lines', name='Degradation Rate', line=dict(color='red')),
        row=1, col=2
    )
    
    fig.update_xaxes(title_text="Temperature (°C)", row=1, col=1)
    fig.update_xaxes(title_text="Temperature (°C)", row=1, col=2)
    fig.update_yaxes(title_text="Charging Rate (C)", row=1, col=1)
    fig.update_yaxes(title_text="Degradation Rate", row=1, col=2)
    
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def show_swap_station_analysis(lcis):
    st.header("🔄 Swap Station Integrity Analysis")
    st.subheader("Formula C: Quality-Gate MRV System")
    
    # Show the formula
    st.latex(r'''
    Integrity = (1 - Error_{rate}) \times Confidence_{verification} \times Efficiency_{throughput}
    ''')
    
    # Input parameters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        swaps_per_day = st.slider("Swaps per Day", 10, 500, 150, 10)
        error_rate = st.slider("Error Rate", 0.001, 0.1, 0.02, 0.001)
    
    with col2:
        verification_samples = st.slider("Verification Samples", 5, 100, 25, 1)
        swap_time = st.slider("Swap Time (seconds)", 60, 180, 90, 5)
    
    with col3:
        target_utilization = st.slider("Target Utilization", 0.5, 0.9, 0.7, 0.01)
    
    # Update LCIS parameters
    lcis.swap_time_seconds = swap_time
    lcis.station_utilization_target = target_utilization
    
    # Calculate results
    results = lcis.calculate_swap_station_integrity(swaps_per_day, error_rate, verification_samples)
    
    # Display results
    st.subheader("📊 Integrity Assessment")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Integrity Score", f"{results['integrity_score']:.3f}")
    with col2:
        st.metric("Quality Gate", f"{results['quality_gate_score']:.3f}")
    with col3:
        st.metric("Throughput Efficiency", f"{results['throughput_efficiency']:.3f}")
    with col4:
        st.metric("Capacity Utilization", f"{results['daily_capacity_utilization']:.1%}")
    
    # Confidence interval
    lower, upper = results['confidence_interval']
    st.subheader("🎯 Statistical Confidence")
    st.write(f"Quality Gate Confidence Interval: **{lower:.3f} - {upper:.3f}** (95% confidence)")
    st.write(f"Margin of Error: **±{results['margin_of_error']:.3f}**")
    
    # Operational optimization
    st.subheader("⚙️ Operational Optimization")
    
    # Create heatmap for error rate vs utilization
    error_rates = np.linspace(0.005, 0.05, 20)
    utilizations = np.linspace(0.5, 0.9, 20)
    
    integrity_matrix = []
    for error in error_rates:
        row = []
        for util in utilizations:
            daily_swaps = int(util * (24 * 3600) / swap_time)
            result = lcis.calculate_swap_station_integrity(daily_swaps, error, verification_samples)
            row.append(result['integrity_score'])
        integrity_matrix.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=integrity_matrix,
        x=utilizations,
        y=error_rates,
        colorscale='RdYlGn',
        colorbar=dict(title="Integrity Score")
    ))
    
    fig.update_layout(
        title="Integrity Score vs Error Rate & Utilization",
        xaxis_title="Capacity Utilization",
        yaxis_title="Error Rate",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_asset_valuation(lcis):
    st.header("📊 Blended Asset Valuation")
    st.subheader("Formula E: EV Portfolio Securitization")
    
    # Show the formula
    st.latex(r'''
    Value_{portfolio} = \sum_{i} Asset_i \times Weight_i \times Risk_{adj,i} \times Liquidity_i
    ''')
    
    st.subheader("🏗️ Portfolio Builder")
    
    # Portfolio builder
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = lcis.generate_sample_portfolio_data(5)
    
    # Portfolio editor
    st.write("**Edit Portfolio Assets:**")
    
    for i, asset in enumerate(st.session_state.portfolio):
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            asset['value'] = st.number_input(f"Value {i+1}", 10000, 1000000, int(asset['value']), key=f"val_{i}")
        with col2:
            asset['weight'] = st.number_input(f"Weight {i+1}", 0.05, 0.5, asset['weight'], 0.01, key=f"wgt_{i}")
        with col3:
            asset['risk_score'] = st.slider(f"Risk {i+1}", 0.1, 0.9, asset['risk_score'], 0.01, key=f"risk_{i}")
        with col4:
            asset['liquidity_factor'] = st.slider(f"Liquidity {i+1}", 0.5, 1.0, asset['liquidity_factor'], 0.01, key=f"liq_{i}")
        with col5:
            asset['expected_yield'] = st.slider(f"Yield {i+1}", 0.02, 0.15, asset['expected_yield'], 0.001, key=f"yield_{i}")
    
    # Normalize weights
    total_weight = sum(a['weight'] for a in st.session_state.portfolio)
    for asset in st.session_state.portfolio:
        asset['weight'] = asset['weight'] / total_weight
    
    # Calculate portfolio valuation
    results = lcis.calculate_blended_asset_valuation(st.session_state.portfolio)
    
    # Display results
    st.subheader("📊 Portfolio Valuation Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Value", f"${results['total_portfolio_value']:,.0f}")
    with col2:
        st.metric("Blended Yield", f"{results['blended_yield']:.2%}")
    with col3:
        st.metric("Sharpe Ratio", f"{results['sharpe_ratio']:.3f}")
    with col4:
        st.metric("Diversification Bonus", f"{results['diversification_score']:.1%}")
    
    # Portfolio composition
    st.subheader("🥧 Portfolio Composition")
    
    # Create pie chart
    values = [a['value'] * a['weight'] for a in st.session_state.portfolio]
    labels = [f"Asset {i+1}" for i in range(len(st.session_state.portfolio))]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    fig.update_layout(title="Portfolio Allocation by Value", height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk-return analysis
    risks = [a['risk_score'] for a in st.session_state.portfolio]
    yields = [a['expected_yield'] for a in st.session_state.portfolio]
    sizes = [a['value'] * a['weight'] / 1000 for a in st.session_state.portfolio]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=risks, y=yields, mode='markers+text',
        marker=dict(size=sizes, sizemode='area', sizeref=max(sizes)/50),
        text=labels, textposition="top center",
        name="Assets"
    ))
    
    fig.update_layout(
        title="Risk-Return Profile",
        xaxis_title="Risk Score",
        yaxis_title="Expected Yield",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_cross_border_data(lcis):
    st.header("🌍 Cross-Border Data Stewarding")
    st.subheader("Formula F: Global Data Governance Value")
    
    # Show the formula
    st.latex(r'''
    Value_{data} = Volume \times Jurisdiction_{complexity} \times Compliance_{multiplier} / Time_{penalty}
    ''')
    
    # Input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        data_volume = st.slider("Data Volume (GB)", 1, 1000, 100, 1)
        jurisdictions = st.slider("Number of Jurisdictions", 1, 15, 5, 1)
    
    with col2:
        compliance_score = st.slider("Compliance Score", 0.5, 1.0, 0.9, 0.01)
        processing_time = st.slider("Processing Time (hours)", 0.1, 20.0, 8.0, 0.1)
    
    # Calculate results
    results = lcis.calculate_cross_border_data_value(data_volume, jurisdictions, compliance_score, processing_time)
    
    # Display results
    st.subheader("📊 Data Value Assessment")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Value", f"${results['adjusted_value']:.2f}")
    with col2:
        st.metric("Value per GB", f"${results['value_per_gb']:.2f}")
    with col3:
        st.metric("Governance Score", f"{results['governance_score']:.3f}")
    with col4:
        st.metric("Cost Ratio", f"{results['processing_cost_ratio']:.2f}")
    
    # Detailed breakdown
    st.subheader("🔍 Value Components")
    
    components = {
        'Component': ['Base Value', 'Jurisdiction Factor', 'Compliance Multiplier', 'Time Efficiency', 'Final Value'],
        'Value': [
            f"${results['base_value']:.2f}",
            f"{results['jurisdiction_factor']:.3f}x",
            f"{results['compliance_multiplier']:.3f}x",
            f"{results['time_efficiency']:.3f}x",
            f"${results['adjusted_value']:.2f}"
        ]
    }
    
    st.table(pd.DataFrame(components))
    
    # Jurisdiction analysis
    st.subheader("🗺️ Jurisdiction Impact Analysis")
    
    jurisdiction_range = range(1, 16)
    values_by_jurisdiction = []
    
    for j in jurisdiction_range:
        result = lcis.calculate_cross_border_data_value(data_volume, j, compliance_score, processing_time)
        values_by_jurisdiction.append(result['adjusted_value'])
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(jurisdiction_range), 
        y=values_by_jurisdiction, 
        mode='lines+markers',
        name='Data Value vs Jurisdictions'
    ))
    
    fig.update_layout(
        title="Data Value vs Number of Jurisdictions",
        xaxis_title="Number of Jurisdictions",
        yaxis_title="Data Value (USD)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_sodium_optimization(lcis):
    st.header("⚗️ Sodium-Ion Integration Optimization")
    st.subheader("Trade Secret H: Proprietary Battery Chemistry Blending")
    
    st.warning("⚠️ This contains trade secret information - normally confidential!")
    
    # Show the formula (simplified for demo)
    st.latex(r'''
    Performance = \alpha \times Li_{performance} + \beta \times Na_{performance} + \gamma \times Bonus_{integration}
    ''')
    
    # Input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        total_capacity = st.slider("Total Capacity (kWh)", 50, 200, 100, 5)
        sodium_ratio = st.slider("Sodium-Ion Ratio", 0.0, 0.8, 0.4, 0.01)
        performance_target = st.slider("Performance Target", 0.7, 0.95, 0.85, 0.01)
    
    with col2:
        li_cost = st.slider("Li-ion Cost ($/kWh)", 100, 250, 150, 5)
        na_cost = st.slider("Sodium-ion Cost ($/kWh)", 50, 120, 80, 5)
    
    # Calculate capacities
    sodium_capacity = total_capacity * sodium_ratio
    li_capacity = total_capacity * (1 - sodium_ratio)
    
    # Calculate optimization
    results = lcis.calculate_sodium_ion_optimization(
        li_capacity, sodium_capacity, li_cost, na_cost, performance_target
    )
    
    # Display results
    st.subheader("📊 Optimization Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Blended Performance", f"{results['blended_performance']:.3f}")
    with col2:
        st.metric("Total Cost", f"${results['total_cost']:,.0f}")
    with col3:
        st.metric("Cost per kWh", f"${results['cost_per_kwh']:.0f}")
    with col4:
        st.metric("Optimization Score", f"{results['optimization_score']:.2f}")
    
    # Performance target check
    if results['meets_performance_target']:
        st.success(f"✅ Performance target of {performance_target:.1%} is met!")
    else:
        st.error(f"❌ Performance target of {performance_target:.1%} is not met.")
    
    # Trade secret parameters (normally hidden)
    st.subheader("🔐 Trade Secret Parameters")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Alpha (Li-ion weight)", f"{results['alpha_weight']:.1f}")
    with col2:
        st.metric("Beta (Sodium weight)", f"{results['beta_weight']:.1f}")
    with col3:
        st.metric("Gamma (Integration bonus)", f"{results['gamma_weight']:.1f}")
    
    # Optimization landscape
    st.subheader("🗺️ Optimization Landscape")
    
    ratios = np.linspace(0, 0.8, 41)
    performances = []
    costs = []
    optimization_scores = []
    
    for ratio in ratios:
        na_cap = total_capacity * ratio
        li_cap = total_capacity * (1 - ratio)
        result = lcis.calculate_sodium_ion_optimization(li_cap, na_cap, li_cost, na_cost, performance_target)
        performances.append(result['blended_performance'])
        costs.append(result['cost_per_kwh'])
        optimization_scores.append(result['optimization_score'])
    
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Performance vs Ratio', 'Optimization Score vs Ratio'])
    
    fig.add_trace(
        go.Scatter(x=ratios, y=performances, mode='lines', name='Performance'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=ratios, y=optimization_scores, mode='lines', name='Optimization Score', line=dict(color='red')),
        row=1, col=2
    )
    
    # Add performance target line
    fig.add_hline(y=performance_target, line_dash="dash", line_color="green", row=1, col=1)
    
    fig.update_xaxes(title_text="Sodium-Ion Ratio", row=1, col=1)
    fig.update_xaxes(title_text="Sodium-Ion Ratio", row=1, col=2)
    fig.update_yaxes(title_text="Performance", row=1, col=1)
    fig.update_yaxes(title_text="Optimization Score", row=1, col=2)
    
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def show_complete_simulation(lcis):
    st.header("📈 Complete LCIS Simulation")
    st.subheader("Comprehensive Business Model Results")
    
    # Run simulation button
    if st.button("🚀 Run Complete Simulation", type="primary"):
        with st.spinner("Running comprehensive LCIS simulation..."):
            simulation_results = lcis.run_comprehensive_simulation()
            st.session_state.simulation_results = simulation_results
    
    if 'simulation_results' in st.session_state:
        results = st.session_state.simulation_results
        
        # Summary metrics
        st.subheader("📊 Simulation Summary")
        
        # Calculate summary statistics
        carbon_df = pd.DataFrame(results['carbon_credits'])
        portfolio_df = pd.DataFrame(results['blended_valuation'])
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Scenarios", f"{len(carbon_df) + len(portfolio_df):,}")
        with col2:
            st.metric("Avg Carbon Value", f"${carbon_df['carbon_value_usd'].mean():.2f}")
        with col3:
            st.metric("Avg Portfolio Yield", f"{portfolio_df['blended_yield'].mean():.2%}")
        with col4:
            st.metric("Max Optimization Score", f"{max(s['optimization_score'] for s in results['sodium_optimization']):.2f}")
        
        # Detailed results by category
        st.subheader("🔍 Detailed Results")
        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Carbon Credits", "Charging Optimization", "Swap Integrity", 
            "Asset Valuation", "Cross-Border Data", "Sodium Optimization"
        ])
        
        with tab1:
            st.dataframe(carbon_df.head(20))
            
            # Carbon credits visualization
            fig = px.scatter(carbon_df, x='energy_delivered', y='verified_credits', 
                           color='vehicle_type', size='carbon_value_usd',
                           title="Carbon Credits by Energy Delivered")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            charging_df = pd.DataFrame(results['degradation_charging'])
            st.dataframe(charging_df.head(20))
            
            # 3D visualization
            fig = px.scatter_3d(charging_df, x='soh', y='temperature', z='credit_yield_multiplier',
                              color='optimal_charging_rate', size='cycles',
                              title="Charging Optimization 3D Analysis")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            swap_df = pd.DataFrame(results['swap_integrity'])
            st.dataframe(swap_df.head(20))
            
            # Heatmap - using density_heatmap instead of imshow for NumPy compatibility
            fig = px.density_heatmap(swap_df, x='swaps_per_day', y='error_rate', 
                                   z='integrity_score', title="Swap Station Integrity Heatmap")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.dataframe(portfolio_df)
            
            fig = px.scatter(portfolio_df, x='num_assets', y='blended_yield',
                           size='sharpe_ratio', color='diversification_score',
                           title="Portfolio Performance by Asset Count")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab5:
            data_df = pd.DataFrame(results['cross_border_data'])
            st.dataframe(data_df.head(20))
            
            fig = px.scatter(data_df, x='data_volume_gb', y='adjusted_value',
                           color='governance_score', size='jurisdiction_factor',
                           title="Cross-Border Data Value Analysis")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab6:
            sodium_df = pd.DataFrame(results['sodium_optimization'])
            st.dataframe(sodium_df)
            
            fig = px.line(sodium_df, x='sodium_ion_ratio', y='optimization_score',
                         color='meets_performance_target',
                         title="Sodium-Ion Optimization Curve")
            st.plotly_chart(fig, use_container_width=True)
        
        # Download results
        st.subheader("💾 Export Results")
        
        if st.button("Download Simulation Data"):
            # Convert to JSON for download
            json_data = json.dumps(results, indent=2, default=str)
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name=f"lcis_simulation_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()