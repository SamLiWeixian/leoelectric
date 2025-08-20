"""
Leo Climate Intelligence Stack (LCIS) - Professional Interactive Dashboard
A comprehensive IP portfolio demonstration system with organized, modular architecture
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import organized modules
try:
    from models.lcis_model import LEOClimateStack
    from config.styles import DASHBOARD_CSS, THEME_COLORS
    imports_successful = True
except ImportError as e:
    imports_successful = False
    # Define LCIS model locally if imports fail
    class LEOClimateStack:
        """Leo Climate Intelligence Stack Business Model - Local Definition"""
        
        def __init__(self):
            self.patents = {
                "carbon_credits": {
                    "title": "Automated Carbon Credit Generation from EV Charging",
                    "description": "Patent-pending system that automatically calculates, validates, and monetizes carbon credits from electric vehicle charging sessions",
                    "technical_details": "Uses real-time energy source tracking, emission factor calculations, and blockchain verification",
                    "business_impact": "Creates new revenue stream worth $50-200 per vehicle annually",
                    "patent_status": "Provisional filed, full application pending"
                },
                "degradation_aware": {
                    "title": "AI-Driven Battery Degradation Prediction and Optimization",
                    "description": "Machine learning system that predicts battery degradation and optimizes charging patterns for maximum lifespan",
                    "technical_details": "Combines battery chemistry models, usage patterns, and environmental factors for predictive analytics",
                    "business_impact": "Extends battery life by 15-25%, reducing replacement costs",
                    "patent_status": "Core algorithms protected, hardware integration pending"
                },
                "swap_integrity": {
                    "title": "Real-Time Battery Swap Station Integrity Monitoring",
                    "description": "IoT-enabled system for monitoring battery health, safety, and performance in swap stations",
                    "technical_details": "Multi-sensor fusion with predictive maintenance algorithms",
                    "business_impact": "Reduces downtime by 40%, ensures 99.9% station reliability",
                    "patent_status": "Hardware and software patents filed"
                },
                "asset_valuation": {
                    "title": "Dynamic Blended Asset Valuation for EV Ecosystems",
                    "description": "Novel valuation methodology treating EV, battery, and software as integrated financial instruments",
                    "technical_details": "Real-time asset tracking with depreciation models and market value algorithms",
                    "business_impact": "Enables new financing models and insurance products",
                    "patent_status": "Business method patent application submitted"
                },
                "cross_border": {
                    "title": "Cross-Border EV Data Intelligence Platform",
                    "description": "Secure, privacy-compliant system for aggregating and monetizing international EV usage data",
                    "technical_details": "Federated learning with differential privacy and regulatory compliance automation",
                    "business_impact": "Creates global data marketplace worth $10-50M annually",
                    "patent_status": "Multiple jurisdictions, privacy-tech focus"
                },
                "sodium_ion": {
                    "title": "Next-Generation Sodium-Ion Battery Optimization",
                    "description": "Advanced control algorithms specifically designed for sodium-ion battery characteristics",
                    "technical_details": "Adaptive charging protocols accounting for sodium-ion chemistry differences",
                    "business_impact": "Enables cost-effective alternative to lithium with 30% cost reduction",
                    "patent_status": "Chemistry and control system patents pending"
                }
            }
        
        def carbon_credit_revenue(self, num_vehicles, avg_kwh_per_charge, charges_per_month, carbon_price_per_ton):
            """Calculate carbon credit revenue from EV charging"""
            monthly_kwh = num_vehicles * avg_kwh_per_charge * charges_per_month
            annual_kwh = monthly_kwh * 12
            
            # Grid emission factor (kg CO2/kWh) - varies by region
            grid_emission_factor = 0.4  # US average
            avoided_emissions_kg = annual_kwh * grid_emission_factor
            avoided_emissions_tons = avoided_emissions_kg / 1000
            
            annual_revenue = avoided_emissions_tons * carbon_price_per_ton
            return {
                'annual_kwh': annual_kwh,
                'avoided_emissions_tons': avoided_emissions_tons,
                'annual_revenue': annual_revenue,
                'revenue_per_vehicle': annual_revenue / num_vehicles
            }
        
        def degradation_aware_charging(self, battery_capacity, current_soh, target_charge_time, temperature):
            """Calculate optimal charging parameters considering degradation"""
            # State of Health factor
            soh_factor = current_soh / 100
            
            # Temperature derating
            if temperature < 0:
                temp_factor = 0.7
            elif temperature > 35:
                temp_factor = 0.8
            else:
                temp_factor = 1.0
            
            # Optimal charging rate (C-rate)
            base_c_rate = 0.8
            optimal_c_rate = base_c_rate * soh_factor * temp_factor
            
            # Calculate charging parameters
            max_charging_power = battery_capacity * optimal_c_rate
            actual_charge_time = (battery_capacity * 0.8) / max_charging_power
            
            # Degradation impact
            if optimal_c_rate > 1.0:
                degradation_factor = 1.2
            elif optimal_c_rate < 0.5:
                degradation_factor = 0.8
            else:
                degradation_factor = 1.0
            
            # Life extension calculation
            base_cycles = 2000
            extended_cycles = base_cycles * (2 - degradation_factor) * soh_factor
            life_extension_percent = ((extended_cycles - base_cycles) / base_cycles) * 100
            
            # Cost savings (battery replacement cost)
            battery_replacement_cost = battery_capacity * 200  # $200/kWh
            cost_savings = battery_replacement_cost * (life_extension_percent / 100) * 0.5
            
            return {
                'soh_factor': soh_factor,
                'temp_factor': temp_factor,
                'optimal_c_rate': optimal_c_rate,
                'max_charging_power': max_charging_power,
                'actual_charge_time': actual_charge_time,
                'degradation_factor': degradation_factor,
                'extended_cycles': extended_cycles,
                'life_extension_percent': life_extension_percent,
                'cost_savings': cost_savings
            }
        
        def swap_station_monitoring(self, num_stations, swaps_per_day, swap_fee, target_uptime):
            """Calculate swap station revenue and reliability metrics"""
            # Basic revenue calculation
            daily_swaps_total = num_stations * swaps_per_day
            daily_revenue = daily_swaps_total * swap_fee
            annual_revenue = daily_revenue * 365
            
            # Uptime bonus calculation
            if target_uptime > 99:
                uptime_multiplier = 1.0 + (target_uptime - 99) * 0.1
            else:
                uptime_multiplier = target_uptime / 99
            
            uptime_bonus = daily_revenue * (uptime_multiplier - 1) * 365
            
            # Reliability scoring
            reliability_score = min(10, target_uptime / 10)
            
            # Downtime cost avoidance
            industry_average_uptime = 96.0
            downtime_cost_per_hour = swap_fee * (swaps_per_day / 24) * num_stations
            hours_saved = ((target_uptime - industry_average_uptime) / 100) * 24 * 365
            downtime_savings = hours_saved * downtime_cost_per_hour
            
            return {
                'daily_swaps_total': daily_swaps_total,
                'daily_revenue': daily_revenue,
                'annual_revenue': annual_revenue,
                'uptime_bonus': uptime_bonus,
                'reliability_score': reliability_score,
                'downtime_savings': downtime_savings,
                'total_annual_value': annual_revenue + uptime_bonus + downtime_savings
            }
        
        def blended_asset_valuation(self, base_vehicle_value, battery_health, software_level, data_value_multiplier):
            """Calculate dynamic blended asset valuation"""
            # Battery value calculation
            battery_health_factor = battery_health / 100
            battery_value = (base_vehicle_value * 0.3) * battery_health_factor
            
            # Software value mapping
            software_values = {
                "Basic": 1000,
                "Advanced": 5000,
                "Premium": 12000,
                "Autonomous": 20000
            }
            software_value = software_values.get(software_level, 1000)
            
            # Data value calculation
            base_data_value = 2000  # Base annual data value
            data_value = base_data_value * data_value_multiplier
            monthly_data_revenue = data_value / 12
            
            # Brand premium calculation
            brand_premium = base_vehicle_value * 0.15  # 15% brand premium
            
            # Total valuation
            vehicle_value = base_vehicle_value
            total_value = vehicle_value + battery_value + software_value + data_value + brand_premium
            
            # Calculate metrics
            value_premium_percent = ((total_value - base_vehicle_value) / base_vehicle_value) * 100
            three_year_data_value = data_value * 3
            three_year_value = total_value + three_year_data_value
            
            return {
                'vehicle_value': vehicle_value,
                'battery_value': battery_value,
                'software_value': software_value,
                'data_value': data_value,
                'brand_premium': brand_premium,
                'total_value': total_value,
                'value_premium_percent': value_premium_percent,
                'monthly_data_revenue': monthly_data_revenue,
                'three_year_value': three_year_value
            }
        
        def cross_border_data_intelligence(self, total_vehicles, countries_covered, premium_clients, data_quality_score):
            """Calculate cross-border data intelligence revenue"""
            # Basic data revenue
            base_revenue_per_vehicle_per_month = 2.0  # $2 per vehicle per month
            quality_multiplier = data_quality_score / 10
            basic_revenue = total_vehicles * base_revenue_per_vehicle_per_month * 12 * quality_multiplier
            
            # Premium analytics revenue
            premium_fee_per_client = 50000  # $50K per premium client annually
            premium_revenue = premium_clients * premium_fee_per_client
            
            # Cross-border premium
            if countries_covered > 5:
                cross_border_multiplier = 1 + (countries_covered - 5) * 0.1
            else:
                cross_border_multiplier = 1.0
            
            cross_border_premium = basic_revenue * (cross_border_multiplier - 1)
            
            # Regulatory compliance value
            regulatory_value_per_country = 25000  # $25K per country for compliance
            regulatory_compliance_value = countries_covered * regulatory_value_per_country
            
            # Total calculations
            total_revenue = basic_revenue + premium_revenue + cross_border_premium + regulatory_compliance_value
            total_data_points = total_vehicles * 365 * 24  # Hourly data points
            
            return {
                'total_data_points': total_data_points,
                'basic_revenue': basic_revenue,
                'premium_revenue': premium_revenue,
                'cross_border_premium': cross_border_premium,
                'regulatory_value': regulatory_compliance_value,
                'total_annual_revenue': total_revenue,
                'revenue_per_vehicle': total_revenue / total_vehicles
            }
        
        def sodium_ion_optimization(self, battery_capacity, cycle_target, cost_per_kwh_lithium):
            """Optimize sodium-ion battery performance and economics"""
            # Sodium-ion characteristics
            cost_reduction = 0.30  # 30% cheaper than lithium
            energy_density_ratio = 0.85  # 85% of lithium density
            cycle_life_advantage = 1.25  # 25% more cycles
            
            # Economic calculations
            sodium_cost_per_kwh = cost_per_kwh_lithium * (1 - cost_reduction)
            battery_cost_sodium = battery_capacity * sodium_cost_per_kwh
            battery_cost_lithium = battery_capacity * cost_per_kwh_lithium
            
            # Performance optimization
            effective_capacity = battery_capacity * energy_density_ratio
            extended_cycle_life = cycle_target * cycle_life_advantage
            
            # Total cost of ownership
            cost_per_cycle_sodium = battery_cost_sodium / extended_cycle_life
            cost_per_cycle_lithium = battery_cost_lithium / cycle_target
            
            # Payback calculation
            cost_savings = battery_cost_lithium - battery_cost_sodium
            annual_savings = cost_savings + (cost_per_cycle_lithium - cost_per_cycle_sodium) * 365
            
            return {
                'battery_cost_sodium': battery_cost_sodium,
                'battery_cost_lithium': battery_cost_lithium,
                'cost_savings': cost_savings,
                'effective_capacity': effective_capacity,
                'extended_cycle_life': extended_cycle_life,
                'cost_per_cycle_sodium': cost_per_cycle_sodium,
                'cost_per_cycle_lithium': cost_per_cycle_lithium,
                'annual_savings': annual_savings,
                'payback_period': cost_savings / max(annual_savings, 1) if annual_savings > 0 else float('inf')
            }
    
    # Define CSS locally if imports fail
    DASHBOARD_CSS = """
    <style>
    [data-testid="stMetricValue"] {
        color: #1f4e79 !important;
    }
    
    [data-testid="metric-container"] label {
        color: #666 !important;
    }
    </style>
    """
    THEME_COLORS = {"primary": "#1f4e79"}
# from utils.ui_helpers import create_parameter_explanation, display_metric_cards, create_success_story_card
# from utils.chart_utils import create_revenue_breakdown_chart, create_comparison_bar_chart, create_timeline_chart
# from utils.export_utils import (
#     create_export_button, 
#     create_green_city_export_data,
#     create_nigerian_farmers_export_data,
#     create_philippines_export_data,
#     create_saudi_arabia_export_data,
#     create_singapore_export_data
# )

# Configure Streamlit page
st.set_page_config(
    page_title="Leo Climate Intelligence Stack",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS styling
st.markdown(DASHBOARD_CSS, unsafe_allow_html=True)

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
    """Display metrics in a card layout"""
    cols = st.columns(len(metrics_data))
    for i, (label, value) in enumerate(metrics_data.items()):
        with cols[i]:
            st.metric(label=label, value=value)

def create_success_story_card(title, story):
    """Create a success story card"""
    return f"""
    <div class="simple-explanation">
        <h4>{title}</h4>
        <p>{story}</p>
    </div>
    """

def create_revenue_breakdown_chart(breakdown_data, title="Monthly Revenue"):
    """Create a bar chart with cumulative line for revenue breakdown"""
    fig = px.bar(breakdown_data, x='Month', y='Revenue', title=title)
    fig.add_scatter(x=breakdown_data['Month'], y=breakdown_data['Cumulative'], 
                   mode='lines+markers', name='Cumulative', yaxis='y2')
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'))
    return fig

def create_comparison_bar_chart(data, x_col, y_col, title, color_scale='Blues'):
    """Create a standard comparison bar chart"""
    fig = px.bar(data, x=x_col, y=y_col, title=title, 
                color=y_col, color_continuous_scale=color_scale)
    return fig

def create_timeline_chart(data, x_col, y_col, title, line_color='#1f4e79'):
    """Create a timeline chart with markers"""
    fig = px.line(data, x=x_col, y=y_col, title=title, markers=True)
    fig.update_traces(line=dict(width=3, color=line_color))
    return fig

def create_export_button(case_data, filename, button_text):
    """Create an export button for case study data"""
    if st.button(button_text):
        import json
        with open(filename, 'w') as f:
            json.dump(case_data, f, indent=2)
        st.success(f"✅ Case study exported to '{filename}'")

def create_green_city_export_data(total_value):
    """Create export data for Green City case study"""
    return {
        'scenario': 'Green City Electric Fleet',
        'total_vehicles': 5000,
        'annual_value': total_value,
        'key_innovations': [
            'Carbon credit generation',
            'Battery optimization',
            'Data intelligence',
            'Swap stations',
            'Asset valuation',
            'Sodium-ion technology'
        ]
    }

def create_nigerian_farmers_export_data(total_impact):
    """Create export data for Nigerian farmers case study"""
    return {
        'scenario': 'Nigerian Electric Agriculture',
        'participants': '500 farmers',
        'annual_impact': total_impact,
        'key_innovations': [
            'Electric farming equipment',
            'Solar charging infrastructure',
            'Carbon credit programs',
            'Agricultural data monetization'
        ]
    }

def create_philippines_export_data(total_impact):
    """Create export data for Philippines case study"""
    return {
        'scenario': 'Philippines Rural Microgrids',
        'communities': 50,
        'annual_impact': total_impact,
        'key_innovations': [
            'Island microgrids',
            'Electric marine fleet',
            'DLSU research partnership',
            'Marine carbon credits'
        ]
    }

def create_saudi_arabia_export_data(annual_value, total_value):
    """Create export data for Saudi Arabia case study"""
    return {
        'scenario': 'Saudi Arabia Jeeny Acquisition',
        'annual_value': annual_value,
        'total_enterprise_value': total_value,
        'key_innovations': [
            'Ride-sharing electrification',
            'Middle East expansion',
            'Climate tech integration',
            'Regional transportation hub'
        ]
    }

def create_singapore_export_data(total_impact):
    """Create export data for Singapore case study"""
    return {
        'scenario': 'Singapore Smart City Carbon-to-Wealth',
        'annual_impact': total_impact,
        'key_innovations': [
            'Carbon-negative urban systems',
            'Smart city integration',
            'Sovereign wealth building',
            'Technology export leadership'
        ]
    }

def main():
    """Main dashboard application"""
    
    # Sidebar navigation
    st.sidebar.markdown("## 🧭 Quick Navigation")
    
    st.sidebar.write("🔬 TECHNOLOGY TABS:")
    st.sidebar.text("📊 IP - Patent portfolio")
    st.sidebar.text("🌱 CO₂ - Carbon credits")
    st.sidebar.text("🔋 Tech - Battery optimization")
    st.sidebar.text("🔄 Swap - Station monitoring")
    st.sidebar.text("💰 Value - Asset pricing")
    st.sidebar.text("🌍 Data - Global intelligence")
    st.sidebar.text("⚡ Na-Ion - Sodium chemistry")
    
    st.sidebar.write("")
    st.sidebar.write("💼 CASE STUDY TABS:")
    st.sidebar.text("📈 City - Green City ($32.4M)")
    st.sidebar.text("🚜 Farm - Nigeria ($3.6M)")
    st.sidebar.text("🏝️ Island - Philippines ($12.6M)")
    st.sidebar.text("🏜️ Saudi - Jeeny ($712M)")
    st.sidebar.text("🦁 SG - Singapore ($11.4B)")
    
    # Header
    st.markdown('<h1 style="color: #1f4e79; text-align: center; font-size: 3rem; margin-bottom: 1rem;">⚡ Leo Climate Intelligence Stack</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #666; margin-bottom: 2rem;">Professional IP Portfolio & Business Model Demonstration</h3>', unsafe_allow_html=True)
    
    # Initialize LCIS
    lcis = LEOClimateStack()
    
    # Quick Dashboard Summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%); padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
        <h4 style="color: white; margin: 0;">🎯 Dashboard Overview: 12 Interactive Tabs | 6 Patent Technologies | 5 Global Case Studies</h4>
        <p style="color: #e0f2fe; margin: 5px 0 0 0;">Demonstrating how Leo Electric's IP creates measurable wealth across different markets</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs with very short names for better navigation
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs([
        "📊 IP", "🌱 CO₂", "🔋 Tech", 
        "🔄 Swap", "💰 Value", "🌍 Data", 
        "⚡ Na-Ion", "📈 City", "🚜 Farm",
        "🏝️ Island", "🏜️ Saudi", "🦁 SG"
    ])
    
    # Tab 1: Portfolio Overview
    with tab1:
        render_portfolio_overview(lcis)
    
    # Tab 2: Carbon Credits
    with tab2:
        render_carbon_credits_tab(lcis)
    
    # Tab 3: Battery Optimization  
    with tab3:
        try:
            render_battery_optimization_tab(lcis)
        except Exception as e:
            st.error(f"Error in Battery Optimization tab: {str(e)}")
            st.info("This tab is being updated. Please use other tabs for now.")
    
    # Tab 4: Swap Stations
    with tab4:
        try:
            render_swap_stations_tab(lcis)
        except Exception as e:
            st.error(f"Error in Swap Stations tab: {str(e)}")
            st.info("This tab is being updated. Please use other tabs for now.")
    
    # Tab 5: Asset Valuation
    with tab5:
        try:
            render_asset_valuation_tab(lcis)
        except Exception as e:
            st.error(f"Error in Asset Valuation tab: {str(e)}")
            st.info("This tab is being updated. Please use other tabs for now.")
    
    # Tab 6: Global Data
    with tab6:
        try:
            render_global_data_tab(lcis)
        except Exception as e:
            st.error(f"Error in Global Data tab: {str(e)}")
            st.info("This tab is being updated. Please use other tabs for now.")
    
    # Tab 7: Sodium-Ion Tech
    with tab7:
        try:
            render_sodium_ion_tab(lcis)
        except Exception as e:
            st.error(f"Error in Sodium-Ion tab: {str(e)}")
            st.info("This tab is being updated. Please use other tabs for now.")
    
    # Tab 8: Green City Case Study
    with tab8:
        render_green_city_case_study(lcis)
    
    # Tab 9: Nigerian Farmers Case Study
    with tab9:
        render_nigerian_farmers_case_study(lcis)
    
    # Tab 10: Philippines Microgrids
    with tab10:
        render_philippines_case_study(lcis)
    
    # Tab 11: Saudi Arabia Jeeny
    with tab11:
        render_saudi_arabia_case_study(lcis)
    
    # Tab 12: Singapore Smart City
    with tab12:
        render_singapore_case_study(lcis)


def render_portfolio_overview(lcis):
    """Render the portfolio overview tab"""
    st.header("Leo Climate Intelligence Stack - Patent Portfolio Overview")
    
    # Metrics row
    metrics_data = {
        "Core Patents": "6",
        "Est. NPV": "$25M+", 
        "Countries": "15+",
        "Tech Readiness": "95%"
    }
    display_metric_cards(metrics_data)
    
    st.markdown("---")
    
    # Patent cards
    for patent_key, patent_info in lcis.patents.items():
        st.markdown(f"""
        <div class="patent-card">
            <h3>{patent_info['title']}</h3>
            <p><strong>Description:</strong> {patent_info['description']}</p>
            <p><strong>Technical Details:</strong> {patent_info['technical_details']}</p>
            <p><strong>Business Impact:</strong> {patent_info['business_impact']}</p>
            <p><strong>Patent Status:</strong> {patent_info['patent_status']}</p>
        </div>
        """, unsafe_allow_html=True)


def render_carbon_credits_tab(lcis):
    """Render the carbon credits analysis tab"""
    st.header("🌱 Automated Carbon Credit Generation System")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['carbon_credits']['title']}</h3>
        <p>{lcis.patents['carbon_credits']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Carbon Credit Formula</h4>
        <div class="formula">
            Annual Revenue = (Vehicles × kWh/Charge × Charges/Month × 12) × Grid_Emission_Factor × Carbon_Price
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> Every time an electric car charges, it prevents pollution that would come from burning gas. We calculate how much pollution was prevented and sell "carbon credits" to companies that want to offset their pollution.</p>
        <p><strong>Why it makes money:</strong> Companies pay $50+ per ton of CO₂ avoided. A single electric car can prevent 5-10 tons of CO₂ per year, earning $250-500 annually just from charging!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 System Parameters")
        
        # Parameter inputs with explanations
        num_vehicles = st.slider("Number of Vehicles", 100, 10000, 1000, 100)
        st.markdown(create_parameter_explanation(
            "Fleet Size", 
            "Total number of electric vehicles in the carbon credit generation program",
            "Directly scales revenue potential - larger fleets generate more credits",
            "Small fleet: 100-500, Medium: 500-2000, Large: 2000+ vehicles"
        ), unsafe_allow_html=True)
        
        avg_kwh = st.slider("Average kWh per Charge", 10, 100, 45, 5)
        st.markdown(create_parameter_explanation(
            "Energy per Charge", 
            "Average kilowatt-hours consumed per charging session",
            "Higher energy consumption = more carbon credits per session",
            "Compact EV: 30-40 kWh, Mid-size: 40-60 kWh, Large: 60-100 kWh"
        ), unsafe_allow_html=True)
        
        charges_per_month = st.slider("Charges per Month per Vehicle", 4, 30, 12, 2)
        st.markdown(create_parameter_explanation(
            "Charging Frequency", 
            "How often each vehicle charges per month",
            "More frequent charging increases total carbon credit volume",
            "Light use: 4-8, Normal: 8-15, Heavy: 15+ charges/month"
        ), unsafe_allow_html=True)
        
        carbon_price = st.slider("Carbon Price ($/ton CO₂)", 10, 150, 50, 5)
        st.markdown(create_parameter_explanation(
            "Carbon Credit Price", 
            "Market price per metric ton of CO₂ equivalent avoided",
            "Higher prices directly increase revenue from same emissions reduction",
            "Current: $10-50, California: $30-80, EU: $50-100+ per ton"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Revenue Analysis")
        
        # Calculate results
        results = lcis.carbon_credit_revenue(num_vehicles, avg_kwh, charges_per_month, carbon_price)
        
        # Display metrics
        metrics_data = {
            "Annual Revenue": f"${results['annual_revenue']:,.0f}",
            "Revenue per Vehicle": f"${results['revenue_per_vehicle']:.0f}",
            "CO₂ Avoided (tons/year)": f"{results['avoided_emissions_tons']:,.0f}",
            "Total Energy (MWh/year)": f"{results['annual_kwh']/1000:,.0f}"
        }
        display_metric_cards(metrics_data)
        
        # Revenue breakdown chart
        breakdown_data = pd.DataFrame({
            'Month': range(1, 13),
            'Revenue': [results['annual_revenue']/12] * 12,
            'Cumulative': [results['annual_revenue']/12 * i for i in range(1, 13)]
        })
        
        fig = create_revenue_breakdown_chart(breakdown_data, "Monthly Carbon Credit Revenue")
        st.plotly_chart(fig, use_container_width=True)


def render_battery_optimization_tab(lcis):
    """Render the battery optimization tab"""
    st.header("🔋 AI-Driven Battery Degradation Prediction & Optimization")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['degradation_aware']['title']}</h3>
        <p>{lcis.patents['degradation_aware']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Degradation-Aware Charging Formula</h4>
        <div class="formula">
            Optimal_Charge_Rate = Base_Rate × SOH_Factor × Temperature_Factor × Degradation_Multiplier
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> Our AI watches how batteries age and adjusts charging speed to keep them healthy longer. Like a smart trainer that knows when to push hard and when to take it easy.</p>
        <p><strong>Why it makes money:</strong> Batteries cost $10,000-20,000 to replace. By extending battery life 15-25%, we save $2,500-5,000 per vehicle while keeping performance high!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("� Battery Parameters")
        
        battery_capacity = st.slider("Battery Capacity (kWh)", 20, 150, 75, 5)
        st.markdown(create_parameter_explanation(
            "Battery Size", 
            "Total energy storage capacity of the battery pack",
            "Larger batteries have different degradation patterns and optimization needs",
            "Small: 20-40 kWh, Medium: 40-80 kWh, Large: 80-150 kWh"
        ), unsafe_allow_html=True)
        
        current_soh = st.slider("Current State of Health (%)", 60, 100, 90, 5)
        st.markdown(create_parameter_explanation(
            "Battery Health", 
            "Current condition compared to new battery (100% = like new)",
            "Lower health requires gentler charging to prevent rapid degradation",
            "Excellent: 90-100%, Good: 80-90%, Fair: 70-80%, Poor: <70%"
        ), unsafe_allow_html=True)
        
        temperature = st.slider("Operating Temperature (°C)", -10, 50, 25, 5)
        st.markdown(create_parameter_explanation(
            "Temperature Impact", 
            "Ambient temperature affects battery chemistry and safe charging rates",
            "Extreme temperatures reduce efficiency and require protective measures",
            "Cold: <0°C, Optimal: 15-25°C, Hot: 25-35°C, Extreme: >35°C"
        ), unsafe_allow_html=True)
        
        target_charge_time = st.slider("Target Charge Time (hours)", 0.5, 12.0, 2.0, 0.5)
        st.markdown(create_parameter_explanation(
            "Charging Speed", 
            "How fast the customer wants to charge (faster = more stress)",
            "Balances convenience with battery longevity",
            "Ultra-fast: 0.5-1h, Fast: 1-3h, Normal: 3-8h, Slow: 8-12h"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Optimization Results")
        
        # Calculate results
        results = lcis.degradation_aware_charging(battery_capacity, current_soh, target_charge_time, temperature)
        
        # Debug: Check if results is None
        if results is None:
            st.error("Error: degradation_aware_charging returned None")
            return
        
        # Display metrics
        metrics_data = {
            "Optimal Charging Power": f"{results['max_charging_power']:.1f} kW",
            "Recommended Time": f"{results['actual_charge_time']:.1f} hours",
            "Life Extension": f"+{results['life_extension_percent']:.1f}%",
            "Cost Savings": f"${results['cost_savings']:.0f}"
        }
        display_metric_cards(metrics_data)
        
        # Create optimization chart
        optimization_data = pd.DataFrame({
            'Metric': ['Power (kW)', 'Time (h)', 'Life Ext (%)', 'Savings ($)'],
            'Value': [results['max_charging_power'], results['actual_charge_time'], 
                     results['life_extension_percent'], results['cost_savings']/100],
            'Optimal': [50, 2, 20, 30]  # Baseline comparisons
        })
        
        fig = create_comparison_bar_chart(optimization_data, 'Metric', 'Value', 
                                        "Battery Optimization Impact", 'RdYlGn')
        st.plotly_chart(fig, use_container_width=True)


def render_swap_stations_tab(lcis):
    """Render the swap stations tab"""
    st.header("🔄 Real-Time Battery Swap Station Integrity Monitoring")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['swap_integrity']['title']}</h3>
        <p>{lcis.patents['swap_integrity']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Swap Station Revenue Formula</h4>
        <div class="formula">
            Daily Revenue = (Swaps/Day × Swap_Fee) + (Uptime_% × Premium_Multiplier × Base_Revenue)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> Think of it like a smart gas station that never breaks down. Our sensors watch every battery swap in real-time, predicting problems before they happen.</p>
        <p><strong>Why it makes money:</strong> Each hour of downtime costs $500-2,000 in lost swaps. Our system achieves 99.9% uptime vs industry average of 96%, earning massive reliability premiums!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("� Station Parameters")
        
        num_stations = st.slider("Number of Swap Stations", 1, 100, 10, 1)
        st.markdown(create_parameter_explanation(
            "Station Network", 
            "Total number of battery swap stations in the network",
            "More stations create network effects and economies of scale",
            "Pilot: 1-5, City: 5-20, Regional: 20-50, National: 50+"
        ), unsafe_allow_html=True)
        
        swaps_per_day = st.slider("Swaps per Day per Station", 50, 500, 200, 25)
        st.markdown(create_parameter_explanation(
            "Daily Throughput", 
            "Number of battery swaps completed per station per day",
            "Higher throughput increases revenue but stresses equipment more",
            "Low: 50-100, Medium: 100-250, High: 250-400, Peak: 400+"
        ), unsafe_allow_html=True)
        
        swap_fee = st.slider("Fee per Swap ($)", 5, 50, 20, 2.5)
        st.markdown(create_parameter_explanation(
            "Swap Pricing", 
            "Revenue earned per battery swap transaction",
            "Competitive pricing balances profitability with market adoption",
            "Budget: $5-15, Standard: $15-25, Premium: $25-35, Luxury: $35+"
        ), unsafe_allow_html=True)
        
        target_uptime = st.slider("Target Uptime (%)", 90, 99.9, 99.5, 0.1)
        st.markdown(create_parameter_explanation(
            "Reliability Target", 
            "Percentage of time stations are operational and available",
            "Higher uptime requires better monitoring but commands premium pricing",
            "Basic: 90-95%, Good: 95-98%, Excellent: 98-99.5%, World-class: 99.5%+"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Performance Analysis")
        
        # Calculate results
        results = lcis.swap_station_monitoring(num_stations, swaps_per_day, swap_fee, target_uptime)
        
        # Display metrics
        metrics_data = {
            "Daily Revenue": f"${results['daily_revenue']:,.0f}",
            "Annual Revenue": f"${results['annual_revenue']:,.0f}",
            "Uptime Bonus": f"${results['uptime_bonus']:,.0f}",
            "Reliability Score": f"{results['reliability_score']:.1f}/10"
        }
        display_metric_cards(metrics_data)
        
        # Create performance timeline
        days = list(range(1, 31))
        daily_revenues = [results['daily_revenue'] + np.random.normal(0, results['daily_revenue']*0.1) for _ in days]
        
        timeline_data = pd.DataFrame({
            'Day': days,
            'Revenue': daily_revenues,
            'Uptime': [target_uptime + np.random.normal(0, 0.5) for _ in days]
        })
        
        fig = create_timeline_chart(timeline_data, 'Day', 'Revenue', 
                                  "30-Day Station Performance")
        st.plotly_chart(fig, use_container_width=True)


def render_asset_valuation_tab(lcis):
    """Render the asset valuation tab"""
    st.header("💰 Dynamic Blended Asset Valuation System")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['asset_valuation']['title']}</h3>
        <p>{lcis.patents['asset_valuation']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Blended Asset Valuation Formula</h4>
        <div class="formula">
            Total_Value = Vehicle_Value + Battery_Value + Software_Value + Data_Value + Brand_Premium
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> Instead of just selling cars, we create "smart assets" that are part vehicle, part computer, part data generator. Each component has separate value that we can optimize and monetize.</p>
        <p><strong>Why it makes money:</strong> A $30,000 car becomes a $45,000 smart asset. Plus we earn ongoing revenue from data, software updates, and services - turning one-time sales into recurring income streams!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("� Asset Components")
        
        base_vehicle_value = st.slider("Base Vehicle Value ($)", 15000, 100000, 35000, 2500)
        st.markdown(create_parameter_explanation(
            "Vehicle Platform", 
            "Core value of the physical vehicle without smart features",
            "Foundation value that all other components build upon",
            "Economy: $15-25K, Mid-range: $25-50K, Premium: $50-75K, Luxury: $75K+"
        ), unsafe_allow_html=True)
        
        battery_health = st.slider("Battery Health (%)", 70, 100, 90, 5)
        st.markdown(create_parameter_explanation(
            "Battery Condition", 
            "Current battery capacity compared to new condition",
            "Heavily impacts resale value and financing options",
            "Excellent: 90-100%, Good: 80-90%, Fair: 70-80%, Replace: <70%"
        ), unsafe_allow_html=True)
        
        software_level = st.selectbox("Software Package", 
                                    ["Basic", "Advanced", "Premium", "Autonomous"],
                                    index=1)
        st.markdown(create_parameter_explanation(
            "Software Features", 
            "Level of AI, connectivity, and autonomous capabilities installed",
            "Software can be upgraded over-the-air, adding value post-purchase",
            "Basic: $0-2K, Advanced: $2-8K, Premium: $8-15K, Autonomous: $15K+"
        ), unsafe_allow_html=True)
        
        data_value_multiplier = st.slider("Data Value Multiplier", 0.5, 3.0, 1.2, 0.1)
        st.markdown(create_parameter_explanation(
            "Data Monetization", 
            "How effectively the vehicle generates valuable data",
            "Higher multipliers mean better routes, more valuable insights",
            "Low: 0.5-0.8, Average: 0.8-1.2, High: 1.2-2.0, Exceptional: 2.0+"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Valuation Breakdown")
        
        # Calculate results
        results = lcis.blended_asset_valuation(base_vehicle_value, battery_health, software_level, data_value_multiplier)
        
        # Display metrics
        metrics_data = {
            "Total Asset Value": f"${results['total_value']:,.0f}",
            "Value Premium": f"+{results['value_premium_percent']:.1f}%",
            "Monthly Data Revenue": f"${results['monthly_data_revenue']:.0f}",
            "3-Year Total Value": f"${results['three_year_value']:,.0f}"
        }
        display_metric_cards(metrics_data)
        
        # Create value breakdown pie chart
        value_breakdown = {
            'Vehicle': results['vehicle_value'],
            'Battery': results['battery_value'],
            'Software': results['software_value'],
            'Data': results['data_value'],
            'Brand': results['brand_premium']
        }
        
        breakdown_df = pd.DataFrame(list(value_breakdown.items()), columns=['Component', 'Value'])
        fig = px.pie(breakdown_df, values='Value', names='Component', 
                    title="Asset Value Breakdown")
        st.plotly_chart(fig, use_container_width=True)


def render_global_data_tab(lcis):
    """Render the global data tab"""
    st.header("🌍 Cross-Border EV Data Intelligence Platform")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['cross_border']['title']}</h3>
        <p>{lcis.patents['cross_border']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Global Data Revenue Formula</h4>
        <div class="formula">
            Total Revenue = (Basic_Data × Vehicles) + (Premium_Analytics × Premium_Clients) + (Cross_Border_Premium × International_Partnerships)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> We collect anonymized data from millions of electric vehicles across different countries and turn it into valuable insights. Like Google Maps, but for energy and transportation patterns.</p>
        <p><strong>Why it makes money:</strong> Governments pay $100K+ for traffic studies. Energy companies pay millions for grid planning data. We provide real-time insights from actual vehicle usage across borders!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("� Data Platform Parameters")
        
        total_vehicles = st.slider("Total Vehicles in Network", 10000, 10000000, 500000, 50000)
        st.markdown(create_parameter_explanation(
            "Network Scale", 
            "Total number of vehicles contributing data across all regions",
            "Larger networks provide more valuable and comprehensive insights",
            "Regional: 10K-100K, National: 100K-1M, Continental: 1M-5M, Global: 5M+"
        ), unsafe_allow_html=True)
        
        countries_covered = st.slider("Countries Covered", 1, 50, 12, 1)
        st.markdown(create_parameter_explanation(
            "Geographic Coverage", 
            "Number of countries participating in data sharing program",
            "More countries enable cross-border insights and higher premium pricing",
            "Regional: 1-5, Multi-regional: 5-15, Continental: 15-30, Global: 30+"
        ), unsafe_allow_html=True)
        
        premium_clients = st.slider("Premium Analytics Clients", 5, 500, 50, 5)
        st.markdown(create_parameter_explanation(
            "Premium Subscribers", 
            "Number of organizations paying for advanced analytics and insights",
            "Premium clients pay 10-100x more than basic data access",
            "Startup: 5-20, Growth: 20-100, Enterprise: 100-300, Global: 300+"
        ), unsafe_allow_html=True)
        
        data_quality_score = st.slider("Data Quality Score", 1, 10, 8, 1)
        st.markdown(create_parameter_explanation(
            "Data Quality", 
            "Accuracy, completeness, and timeliness of collected data",
            "Higher quality data commands premium pricing and client retention",
            "Basic: 1-4, Good: 4-7, Excellent: 7-9, World-class: 9-10"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Revenue Analysis")
        
        # Calculate results
        results = lcis.cross_border_data_intelligence(total_vehicles, countries_covered, premium_clients, data_quality_score)
        
        # Display metrics
        metrics_data = {
            "Annual Revenue": f"${results['total_annual_revenue']:,.0f}",
            "Revenue per Vehicle": f"${results['revenue_per_vehicle']:.2f}",
            "Premium Revenue": f"${results['premium_revenue']:,.0f}",
            "Cross-Border Bonus": f"${results['cross_border_premium']:,.0f}"
        }
        display_metric_cards(metrics_data)
        
        # Create revenue streams chart
        revenue_streams = {
            'Basic Data': results['basic_revenue'],
            'Premium Analytics': results['premium_revenue'],
            'Cross-Border Premium': results['cross_border_premium'],
            'Regulatory Compliance': results['regulatory_value']
        }
        
        streams_df = pd.DataFrame(list(revenue_streams.items()), columns=['Stream', 'Revenue'])
        fig = px.bar(streams_df, x='Stream', y='Revenue', 
                    title="Annual Revenue by Stream",
                    color='Revenue', color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)


def render_sodium_ion_tab(lcis):
    """Render the sodium ion tab"""
    st.header("⚡ Next-Generation Sodium-Ion Battery Optimization")
    
    st.markdown(f"""
    <div class="patent-card">
        <h3>{lcis.patents['sodium_ion']['title']}</h3>
        <p>{lcis.patents['sodium_ion']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula explanation
    st.markdown("""
    <div class="formula-box">
        <h4>💡 Sodium-Ion Economic Formula</h4>
        <div class="formula">
            Total Savings = (Lithium_Cost - Sodium_Cost) + (Extended_Cycles × Cost_per_Cycle_Difference)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-explanation">
        <h4>🧠 Simple Explanation</h4>
        <p><strong>What it does:</strong> Sodium is everywhere (salt water!) while lithium is rare and expensive. Our algorithms make sodium-ion batteries work as well as lithium but cost 30% less.</p>
        <p><strong>Why it makes money:</strong> Battery packs cost $10,000-20,000. Saving 30% means $3,000-6,000 per vehicle! Plus sodium lasts longer, saving even more on replacements.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("� Battery Comparison")
        
        battery_capacity = st.slider("Battery Pack Size (kWh)", 30, 200, 75, 5)
        st.markdown(create_parameter_explanation(
            "Battery Capacity", 
            "Total energy storage capacity of the battery pack",
            "Larger packs show bigger absolute savings with sodium-ion technology",
            "Small: 30-50 kWh, Medium: 50-100 kWh, Large: 100-150 kWh, Massive: 150+ kWh"
        ), unsafe_allow_html=True)
        
        cycle_target = st.slider("Target Cycle Life", 1000, 5000, 2500, 250)
        st.markdown(create_parameter_explanation(
            "Battery Longevity", 
            "Expected number of charge-discharge cycles before replacement",
            "Sodium-ion typically lasts 25% longer than lithium-ion",
            "Basic: 1000-2000, Standard: 2000-3000, Premium: 3000-4000, Advanced: 4000+"
        ), unsafe_allow_html=True)
        
        cost_per_kwh_lithium = st.slider("Lithium Cost ($/kWh)", 100, 300, 150, 10)
        st.markdown(create_parameter_explanation(
            "Lithium Battery Cost", 
            "Current market price per kWh for lithium-ion battery packs",
            "Lithium prices are volatile and generally trending upward",
            "Low: $100-130, Current: $130-180, High: $180-250, Crisis: $250+"
        ), unsafe_allow_html=True)
        
        production_volume = st.slider("Annual Production Volume", 1000, 100000, 10000, 1000)
        st.markdown(create_parameter_explanation(
            "Manufacturing Scale", 
            "Number of battery packs produced annually",
            "Higher volumes increase cost savings through economies of scale",
            "Startup: 1K-5K, Small: 5K-20K, Medium: 20K-50K, Large: 50K+"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Economic Analysis")
        
        # Calculate results
        results = lcis.sodium_ion_optimization(battery_capacity, cycle_target, cost_per_kwh_lithium)
        
        # Display metrics
        metrics_data = {
            "Cost Savings per Pack": f"${results['cost_savings']:,.0f}",
            "Annual Savings": f"${results['annual_savings']:,.0f}",
            "Payback Period": f"{results['payback_period']:.1f} years",
            "Extended Cycle Life": f"{results['extended_cycle_life']:,.0f}"
        }
        display_metric_cards(metrics_data)
        
        # Create cost comparison chart
        comparison_data = pd.DataFrame({
            'Technology': ['Lithium-Ion', 'Sodium-Ion'],
            'Battery Cost ($)': [results['battery_cost_lithium'], results['battery_cost_sodium']],
            'Cost per Cycle ($)': [results['cost_per_cycle_lithium'], results['cost_per_cycle_sodium']],
            'Effective Capacity (kWh)': [battery_capacity, results['effective_capacity']]
        })
        
        fig = px.bar(comparison_data, x='Technology', y='Battery Cost ($)', 
                    title="Lithium vs Sodium-Ion Cost Comparison",
                    color='Technology', color_discrete_sequence=['#ff6b6b', '#4ecdc4'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Annual savings projection
        years = list(range(1, 11))
        cumulative_savings = [results['annual_savings'] * year for year in years]
        
        timeline_data = pd.DataFrame({
            'Year': years,
            'Cumulative Savings': cumulative_savings
        })
        
        fig2 = create_timeline_chart(timeline_data, 'Year', 'Cumulative Savings', 
                                   "10-Year Cumulative Savings Projection")
        st.plotly_chart(fig2, use_container_width=True)


def render_green_city_case_study(lcis):
    """Render Green City case study"""
    st.header("📈 Real-World Case Study: How Leo Makes Money")
    
    st.markdown("""
    <div class="case-study-section">
        <h2>🏢 The Story: "Green City" Goes Electric</h2>
        <p><strong>Meet Green City:</strong> A modern city that wants to go 100% electric for deliveries, taxis, and buses. They have 5,000 vehicles and want to see how Leo's technology will make them money.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fleet breakdown
    st.subheader("🚗 Green City's Electric Fleet:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚛 Delivery Vehicles: 3,000</h4>
            <p>• Amazon-style delivery vans</p>
            <p>• 60 kWh batteries each</p>
            <p>• 2 charges per day average</p>
            <p>• High carbon credit potential</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚕 Electric Taxis: 1,500</h4>
            <p>• Uber/Lyft style vehicles</p>
            <p>• 75 kWh batteries each</p>
            <p>• 3 charges per day average</p>
            <p>• Premium data value</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚌 Electric Buses: 500</h4>
            <p>• Public transportation</p>
            <p>• 400 kWh batteries each</p>
            <p>• 1 charge per day</p>
            <p>• Maximum visibility impact</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💰 How Leo Makes Money from Green City:")
    
    # Calculate results for each patent
    delivery_carbon = lcis.carbon_credit_revenue(3000, 60, 60, 45)  # 2 charges/day = 60/month
    taxi_carbon = lcis.carbon_credit_revenue(1500, 75, 90, 45)     # 3 charges/day = 90/month
    bus_carbon = lcis.carbon_credit_revenue(500, 400, 30, 45)      # 1 charge/day = 30/month
    
    # Patent 1: Carbon Credits
    total_carbon_revenue = delivery_carbon['annual_revenue'] + taxi_carbon['annual_revenue'] + bus_carbon['annual_revenue']
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🌱 Patent #1: Carbon Credits = ${total_carbon_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Every time a vehicle charges, we calculate exactly how much pollution was prevented and sell those "carbon credits" to companies.</p>
        <p><strong>The math:</strong> 5,000 vehicles × 45 kWh average × charges per month × CO₂ factor = {delivery_carbon['avoided_emissions_tons'] + taxi_carbon['avoided_emissions_tons'] + bus_carbon['avoided_emissions_tons']:,.0f} tons CO₂ avoided!</p>
        <p><strong>Revenue breakdown:</strong> Deliveries: ${delivery_carbon['annual_revenue']:,.0f}, Taxis: ${taxi_carbon['annual_revenue']:,.0f}, Buses: ${bus_carbon['annual_revenue']:,.0f}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 2: Battery Optimization
    battery_savings = 5000 * 2500  # Average savings per vehicle
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🔋 Patent #2: Battery Life Extension = ${battery_savings:,.0f} savings per year</h4>
        <p><strong>What happens:</strong> Our AI watches each battery's health and adjusts charging to make them last 25% longer.</p>
        <p><strong>Why it matters:</strong> New batteries cost $15,000-25,000 each. Extending life by 25% saves Green City millions!</p>
        <p><strong>Per vehicle savings:</strong> ${battery_savings/5000:,.0f} average per vehicle annually</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 3: Data Intelligence
    data_revenue = 5000 * 120  # $120 per vehicle per year
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>📊 Patent #3: City Data Intelligence = ${data_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> 5,000 vehicles become mobile sensors collecting traffic, air quality, and route optimization data.</p>
        <p><strong>Who pays:</strong> City planning departments, Google Maps, insurance companies, and logistics firms pay premium prices for real-time urban data.</p>
        <p><strong>Value creation:</strong> Anonymous, privacy-protected insights help optimize the entire city!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 4: Swap Station Revenue
    swap_revenue = 50 * 365 * 200 * 25  # 50 stations, daily swaps, fee
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🔄 Patent #4: Battery Swap Stations = ${swap_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> 50 strategically placed swap stations across Green City provide 3-minute battery changes instead of 30-minute charging.</p>
        <p><strong>Premium pricing:</strong> Drivers pay $25 per swap for convenience. Stations average 200 swaps per day.</p>
        <p><strong>Reliability bonus:</strong> 99.9% uptime creates premium pricing and customer loyalty!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 5: Asset Valuation
    asset_premium = 5000 * 5000  # $5,000 premium per vehicle
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>💎 Patent #5: Smart Asset Valuation = ${asset_premium:,.0f} portfolio value</h4>
        <p><strong>What happens:</strong> Each vehicle becomes a "smart asset" worth more than a regular car because it generates data and carbon credits.</p>
        <p><strong>Investment attraction:</strong> Green City can get better financing and insurance rates because Leo tracks real-time asset values.</p>
        <p><strong>Resale value:</strong> Vehicles hold value better because buyers know exact battery health and earning potential!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 6: Sodium-Ion Advantage
    sodium_savings = 1000 * 8000  # Future sodium-ion savings
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>⚡ Patent #6: Sodium-Ion Technology = ${sodium_savings:,.0f} future savings</h4>
        <p><strong>What happens:</strong> Next-generation vehicles use Leo's sodium-ion batteries: 30% cheaper, longer-lasting, better for hot climates.</p>
        <p><strong>Competitive advantage:</strong> While others depend on expensive lithium, Leo makes EVs affordable for everyone!</p>
        <p><strong>Market expansion:</strong> Lower costs mean Green City can electrify more vehicles faster!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Total impact summary
    total_annual_value = total_carbon_revenue + battery_savings + data_revenue + swap_revenue
    total_asset_value = asset_premium + sodium_savings
    grand_total = total_annual_value + (total_asset_value / 10)  # Amortize asset value
    
    st.subheader("🎯 Green City Total Annual Impact:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌱 Carbon Credits", f"${total_carbon_revenue:,.0f}")
    
    with col2:
        st.metric("🔋 Battery Optimization", f"${battery_savings:,.0f}")
    
    with col3:
        st.metric("� Data + Swaps", f"${data_revenue + swap_revenue:,.0f}")
    
    with col4:
        st.metric("🎉 Total Annual Value", f"${total_annual_value:,.0f}")
    
    # Success story
    st.markdown("""
    <div class="case-study-section">
        <h3>🚀 Why This Is a Game-Changer:</h3>
        <ul>
            <li><strong>Multiple Revenue Streams:</strong> Instead of just selling vehicles, Leo creates 6 different ways to make money from the same fleet</li>
            <li><strong>Recurring Income:</strong> Carbon credits, data, and services provide ongoing revenue, not just one-time sales</li>
            <li><strong>Environmental Impact:</strong> {delivery_carbon['avoided_emissions_tons'] + taxi_carbon['avoided_emissions_tons'] + bus_carbon['avoided_emissions_tons']:,.0f} tons of CO₂ prevented annually</li>
            <li><strong>Economic Development:</strong> Lower transportation costs boost entire city economy</li>
            <li><strong>Technology Leadership:</strong> Green City becomes showcase for sustainable urban transportation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Export functionality
    case_data = create_green_city_export_data(grand_total)
    create_export_button(case_data, 'green_city_case_study.json', "📁 Export Green City Case Study")


def render_nigerian_farmers_case_study(lcis):
    """Render Nigerian farmers case study"""
    st.header("🚜 Nigerian Farmers: From Diesel to Electric - Building Generational Wealth")
    
    st.markdown("""
    <div class="case-study-section">
        <h2>🌾 The Story: "Transforming Nigerian Agriculture with Electric Farming"</h2>
        <p><strong>Meet the Cooperative:</strong> 500 small-scale farmers in Kaduna State, Nigeria, who traditionally used expensive diesel tractors and generators. They're switching to electric farming equipment powered by solar energy and Leo's technology.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fleet breakdown
    st.subheader("🚜 Electric Farming Fleet:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚜 Electric Tractors: 150</h4>
            <p>• 50 kWh battery each</p>
            <p>• Solar charging stations</p>
            <p>• Replace diesel tractors</p>
            <p>• 8-hour work capacity</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fleet-info">
            <h4>⚡ Processing Equipment: 200</h4>
            <p>• Electric mills and pumps</p>
            <p>• 25 kWh battery packs</p>
            <p>• Community charging hubs</p>
            <p>• Increase processing speed 3x</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fleet-info">
            <h4>🌞 Solar Infrastructure: 50</h4>
            <p>• Community charging stations</p>
            <p>• 100 kW solar + storage</p>
            <p>• Village energy centers</p>
            <p>• Surplus energy sales</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💰 How Nigerian Farmers Build Generational Wealth:")
    
    # Patent 1: Carbon Credits for Agriculture
    st.markdown("""
    <div class="simple-explanation">
        <h4>🌱 Patent #1: Agricultural Carbon Credits = $238,000 per year</h4>
        <p><strong>What happens:</strong> Every electric tractor and solar panel prevents CO₂ emissions. African agricultural carbon credits sell for premium prices to international buyers who want to support sustainable farming.</p>
        <p><strong>The opportunity:</strong> 350 electric vehicles × 8 tons CO₂ saved × $85/ton (premium African ag credits) = $238,000 annually</p>
        <p><strong>Family legacy fund:</strong> Each farming family earns $476 yearly just from carbon credits!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 2: Diesel Cost Elimination
    st.markdown("""
    <div class="simple-explanation">
        <h4>⛽ Patent #2: Eliminate Diesel Costs = $430,000 annual savings</h4>
        <p><strong>What happens:</strong> Nigerian farmers spend $860 per year on diesel fuel. Electric equipment powered by free solar energy eliminates this cost forever.</p>
        <p><strong>The math:</strong> 500 farmers × $860 diesel savings = $430,000 total</p>
        <p><strong>Family wealth building:</strong> That's $8,600 saved per family over 10 years - enough to buy land and send children to university!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 3: Productivity Revolution
    st.markdown("""
    <div class="simple-explanation">
        <h4>📈 Patent #3: Triple Productivity = $2,400,000 additional income</h4>
        <p><strong>What happens:</strong> Electric equipment is more precise, reliable, and efficient. Farmers can plant more crops, process faster, and work longer hours with solar-powered LED lighting.</p>
        <p><strong>Real results:</strong> Average farm income increases from $4,300 to $12,900 per year (300% increase)</p>
        <p><strong>Community impact:</strong> 500 families earn $2.4M additional income annually!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 4: Agricultural Data Monetization
    st.markdown("""
    <div class="simple-explanation">
        <h4>📊 Patent #4: Agricultural Data Intelligence = $300,000 per year</h4>
        <p><strong>What happens:</strong> Electric tractors collect valuable data on soil conditions, crop yields, weather patterns, and farming efficiency. This data is gold for agricultural research and food security planning.</p>
        <p><strong>Revenue streams:</strong> Government pays $600 per farmer annually for agricultural planning data</p>
        <p><strong>Global opportunity:</strong> International organizations pay premium for African farming insights to improve food security worldwide!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 5: Community Energy Business
    st.markdown("""
    <div class="simple-explanation">
        <h4>🔋 Patent #5: Energy Sales to Grid = $120,000 additional income</h4>
        <p><strong>What happens:</strong> Solar charging stations generate excess energy during sunny days. Farmers sell surplus electricity back to the national grid and neighboring communities.</p>
        <p><strong>Energy entrepreneurs:</strong> Each charging station earns $2,400 annually from energy sales</p>
        <p><strong>Community transformation:</strong> Farmers become energy producers, not just food producers!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 6: Rural Banking & Financial Inclusion
    st.markdown("""
    <div class="simple-explanation">
        <h4>💳 Patent #6: Digital Carbon Banking = $75,000 annual value</h4>
        <p><strong>What happens:</strong> Carbon credit payments create Nigeria's first rural digital banking system. Farmers get mobile money accounts, digital payments, and access to microloans for equipment upgrades.</p>
        <p><strong>Financial inclusion:</strong> 500 farming families gain access to modern banking for the first time</p>
        <p><strong>Economic multiplier:</strong> Digital payments reduce transaction costs and enable new business opportunities!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Total impact summary
    total_carbon_value = 238000
    total_savings = 430000
    total_productivity = 2400000
    total_data_value = 300000
    total_energy_income = 120000
    total_banking_value = 75000
    total_annual_impact = total_carbon_value + total_savings + total_productivity + total_data_value + total_energy_income + total_banking_value
    
    st.subheader("🎯 Total Impact for 500 Nigerian Farming Families:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌱 Carbon Legacy Fund", f"${total_carbon_value:,.0f}")
    
    with col2:
        st.metric("⛽ Diesel Elimination", f"${total_savings:,.0f}")
    
    with col3:
        st.metric("📈 Productivity Boost", f"${total_productivity:,.0f}")
    
    with col4:
        st.metric("🎉 Total Annual Impact", f"${total_annual_impact:,.0f}")
    
    # Family wealth building timeline
    st.subheader("👨‍👩‍👧‍👦 Family Wealth Building Timeline:")
    
    wealth_data = pd.DataFrame({
        'Year': [1, 3, 5, 7, 10],
        'Family Wealth ($)': [1380, 7200, 16500, 29300, 48400],
        'Milestone': ['Start', 'Buy Land', 'New House', 'Children University', 'Generational Wealth']
    })
    
    fig = px.line(wealth_data, x='Year', y='Family Wealth ($)', 
                 title="Average Family Wealth Growth Over 10 Years",
                 markers=True, text='Milestone')
    fig.update_traces(line=dict(width=4, color='#28a745'))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Success stories
    st.subheader("🌟 Real Family Impact Stories:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="simple-explanation">
            <h4>👨‍🌾 Farmer Adamu's Story:</h4>
            <p><strong>Before:</strong> Spent $70/month on diesel, earned $350/month farming</p>
            <p><strong>After:</strong> Zero fuel costs, $1,050/month farming income, $140/month carbon credits</p>
            <p><strong>Legacy Fund:</strong> $14,700 saved in first year for children's education and land expansion</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="simple-explanation">
            <h4>👩‍🌾 Farmer Khadija's Cooperative:</h4>
            <p><strong>Before:</strong> 20 women sharing 2 diesel generators</p>
            <p><strong>After:</strong> Each has electric processing equipment, solar charging station</p>
            <p><strong>Result:</strong> Cooperative income increased 300%, now processing for neighboring villages</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Export functionality
    case_data = create_nigerian_farmers_export_data(total_annual_impact)
    create_export_button(case_data, 'nigerian_farmers_case_study.json', "📁 Export Nigerian Farmers Case Study")


def render_philippines_case_study(lcis):
    """Render Philippines case study"""
    st.header("🏝️ Philippines: Rural Microgrids Partnership with DLSU")
    
    st.markdown("""
    <div class="case-study-section">
        <h2>🏫 The Partnership: "Leo + De La Salle University = Rural Energy Revolution"</h2>
        <p><strong>The Challenge:</strong> 2.1 million Filipino families lack reliable electricity. Rural island communities depend on expensive diesel generators, preventing economic development and trapping families in poverty.</p>
        <p><strong>The Solution:</strong> Leo partners with DLSU to deploy intelligent microgrids across 50 remote island communities, transforming energy poverty into sustainable wealth generation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fleet breakdown
    st.subheader("🏝️ What Philippine Island Communities Get:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fleet-info">
            <h4>⚡ Smart Microgrids: 50</h4>
            <p>• Island community microgrids</p>
            <p>• Solar + battery storage systems</p>
            <p>• AI-managed energy distribution</p>
            <p>• 24/7 reliable electricity</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚤 Electric Marine Fleet: 350</h4>
            <p>• 200 electric fishing boats</p>
            <p>• 150 inter-island transport boats</p>
            <p>• Battery swap stations at ports</p>
            <p>• Reduced fuel costs by 80%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fleet-info">
            <h4>🏫 DLSU Research Centers: 5</h4>
            <p>• Energy research stations</p>
            <p>• Real-time data monitoring</p>
            <p>• Student innovation labs</p>
            <p>• Community training programs</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💰 How Leo Transforms Island Communities into Wealth Generators:")
    
    # Patent 1: Marine Carbon Credits
    ph_carbon_revenue = 350 * 12 * 75  # 350 boats × 12 tons CO₂ × $75/ton premium marine credits
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🌊 Patent #1: Marine Carbon Credits = ${ph_carbon_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Every electric fishing boat and transport vessel prevents marine diesel pollution. Island communities earn premium "Blue Carbon" credits for protecting marine ecosystems.</p>
        <p><strong>The ocean opportunity:</strong> 350 boats × 12 tons CO₂ saved × $75/ton (premium marine credits) = ${ph_carbon_revenue:,.0f} annually</p>
        <p><strong>Community wealth fund:</strong> 80% goes to families ($210 per boat annually), 20% to community development projects!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 2: Energy Independence
    ph_energy_savings = 50 * 76000  # 50 communities × $76K savings each
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>⚡ Patent #2: Microgrid Energy Independence = ${ph_energy_savings:,.0f} annual savings</h4>
        <p><strong>What happens:</strong> Intelligent microgrids eliminate expensive diesel generators ($0.45/kWh) with free solar power managed by Leo's AI.</p>
        <p><strong>The math:</strong> 50 communities save $76,000 each on diesel costs = ${ph_energy_savings:,.0f} total</p>
        <p><strong>Economic multiplier:</strong> Families spend savings on education, small businesses, and fishing equipment!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 3: Fishing Productivity Revolution
    ph_fishing_income = 200 * 4500  # 200 fishing boats × $4,500 additional income
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🎣 Patent #3: Electric Fishing Fleet Productivity = ${ph_fishing_income:,.0f} income boost</h4>
        <p><strong>What happens:</strong> Electric boats are quieter (don't scare fish), more precise positioning, LED fishing lights powered all night, and GPS fish-finding systems.</p>
        <p><strong>Real results:</strong> Average fishing income increases 140% from $3,200 to $7,700 per year per boat</p>
        <p><strong>Community impact:</strong> 200 fishing families see ${ph_fishing_income:,.0f} additional annual income!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 4: DLSU Research Revenue
    ph_research_revenue = 1200000  # Research grants and consulting
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🏫 Patent #4: Academic Research Data Monetization = ${ph_research_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> DLSU and Leo jointly publish valuable research on tropical microgrid optimization, marine electrification, and island sustainability.</p>
        <p><strong>Revenue streams:</strong> Research grants ($600K), consulting fees ($300K), patent licensing ($300K)</p>
        <p><strong>Knowledge sharing:</strong> Philippines becomes the global leader in island electrification technology!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 5: Tourism & Commerce Boom
    ph_tourism_revenue = 4100000  # New business revenue
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🏨 Patent #5: Sustainable Tourism Economy = ${ph_tourism_revenue:,.0f} new business revenue</h4>
        <p><strong>What happens:</strong> Reliable electricity enables eco-tourism, internet connectivity, refrigeration for food businesses, and electric vehicle rentals.</p>
        <p><strong>New businesses:</strong> Beach resorts, dive shops, seafood restaurants, handicraft centers, and marine sanctuaries</p>
        <p><strong>Community transformation:</strong> Islands become sustainable tourism destinations instead of struggling fishing villages!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 6: Inter-Island Energy Trading
    ph_energy_trading = 800000  # Energy trading income
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🔄 Patent #6: Energy Trading Network = ${ph_energy_trading:,.0f} annual income</h4>
        <p><strong>What happens:</strong> Sunny islands sell excess solar power to cloudy islands through Leo's smart grid network and battery-powered transport boats.</p>
        <p><strong>Island entrepreneurs:</strong> Communities with better solar become "energy exporters" earning $16,000 annually per excess-energy island</p>
        <p><strong>Regional cooperation:</strong> Islands work together instead of competing, creating inter-island prosperity networks!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Total impact summary
    ph_total_impact = ph_carbon_revenue + ph_energy_savings + ph_fishing_income + ph_research_revenue + ph_tourism_revenue + ph_energy_trading
    
    st.subheader("🎯 Total Community Transformation (50 Philippine Island Communities):")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌊 Marine Carbon Credits", f"${ph_carbon_revenue:,.0f}")
    
    with col2:
        st.metric("⚡ Energy Independence", f"${ph_energy_savings:,.0f}")
    
    with col3:
        st.metric("🎣 Fishing + Tourism Boom", f"${ph_fishing_income + ph_tourism_revenue:,.0f}")
    
    with col4:
        st.metric("🎉 Total Annual Impact", f"${ph_total_impact:,.0f}")
    
    # Community wealth building timeline
    st.subheader("�‍👩‍👧‍👦 Island Family Wealth Building Timeline:")
    
    wealth_data = pd.DataFrame({
        'Year': [1, 3, 5, 7, 10],
        'Family Wealth ($)': [1200, 8500, 18000, 32000, 52000],
        'Milestone': ['Start Electric', 'New Boat', 'House Upgrade', 'Children University', 'Generational Wealth']
    })
    
    fig = px.line(wealth_data, x='Year', y='Family Wealth ($)', 
                 title="Average Island Family Wealth Growth Over 10 Years",
                 markers=True, text='Milestone')
    fig.update_traces(line=dict(width=4, color='#1f77b4'))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Success stories
    st.subheader("🌟 Real Island Impact Stories:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="simple-explanation">
            <h4>🚤 Fisherman Mario's Story:</h4>
            <p><strong>Before:</strong> Spent $150/month on diesel, earned $270/month fishing</p>
            <p><strong>After:</strong> Zero fuel costs, $640/month fishing income, plus marine carbon credits</p>
            <p><strong>Island transformation:</strong> His community now has 24/7 electricity and internet connectivity</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="simple-explanation">
            <h4>🏨 Tourism Entrepreneur Rosa:</h4>
            <p><strong>Before:</strong> Could only offer basic accommodation with unreliable generator power</p>
            <p><strong>After:</strong> Runs successful eco-resort with electric boat tours and sustainable energy showcase</p>
            <p><strong>Result:</strong> Island income increased 400%, now training other communities in sustainable tourism</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Export functionality
    case_data = create_philippines_export_data(ph_total_impact)
    create_export_button(case_data, 'philippines_microgrids_case_study.json', "📁 Export Philippines Case Study")


def render_saudi_arabia_case_study(lcis):
    """Render Saudi Arabia case study"""
    st.header("🏜️ Saudi Arabia: Jeeny Acquisition - From Ride-Sharing to Wealth Empire")
    
    st.markdown("""
    <div class="case-study-section">
        <h2>🚗 The Opportunity: "Leo + Jeeny = Middle East Transportation Revolution"</h2>
        <p><strong>The Vision:</strong> Leo acquires majority stake in profitable, pre-IPO Jeeny (Saudi Arabia's Uber). Transform from simple ride-sharing into the Middle East's first climate-tech transportation empire worth $5+ billion.</p>
        <p><strong>Strategic Advantage:</strong> Jeeny already has government approval, local partnerships, and 2M+ active users across Saudi Arabia, UAE, and Kuwait.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Current Jeeny Overview
    st.subheader("📊 Jeeny's Current Market Position:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚗 Current Fleet: 45,000</h4>
            <p>• Active drivers across 3 countries</p>
            <p>• 2M+ monthly active users</p>
            <p>• $180M annual gross revenue</p>
            <p>• $25M net profit (2024)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fleet-info">
            <h4>🌍 Market Coverage:</h4>
            <p>• Saudi Arabia: 25 cities</p>
            <p>• UAE: 7 emirates</p>
            <p>• Kuwait: Full coverage</p>
            <p>• Pre-approved for Oman & Bahrain</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fleet-info">
            <h4>💰 Acquisition Opportunity:</h4>
            <p>• Pre-IPO valuation: $800M</p>
            <p>• Leo investment: $400M (51%)</p>
            <p>• Government backing: Confirmed</p>
            <p>• Path to IPO: 18-24 months</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💰 How Leo Transforms Jeeny into Climate-Tech Empire:")
    
    # Patent 1: Fleet Electrification Revenue
    jeeny_carbon_revenue = 45000 * 850  # 45,000 vehicles × $850 annual carbon credits
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🌱 Patent #1: Fleet Electrification & Carbon Credits = ${jeeny_carbon_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Convert Jeeny's 45,000 vehicles to electric. In the Middle East, carbon credits from transportation earn premium prices due to extreme heat and air quality concerns.</p>
        <p><strong>The opportunity:</strong> 45,000 EVs × 15 tons CO₂ saved × $57/ton (Middle East premium) = ${jeeny_carbon_revenue:,.0f} annually</p>
        <p><strong>Government incentives:</strong> Saudi Vision 2030 pays additional $200/vehicle annually for electric conversion!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 2: Charging Infrastructure Empire
    charging_revenue = 2500 * 95000  # 2,500 charging stations × $95K annual revenue
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>⚡ Patent #2: Charging Infrastructure Network = ${charging_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Build 2,500 fast-charging stations across the Gulf. Leo's battery optimization technology works perfectly in extreme heat conditions.</p>
        <p><strong>Revenue streams:</strong> Charging fees ($65M), maintenance contracts ($85M), energy storage services ($87M)</p>
        <p><strong>Strategic moat:</strong> First-mover advantage in Gulf charging infrastructure with government partnerships!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 3: Data Intelligence Goldmine
    data_revenue = 45000 * 2400  # 45,000 vehicles × $2,400 annual data value
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>📊 Patent #3: Middle East Transportation Data = ${data_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> 45,000 vehicles become mobile sensors collecting traffic, weather, air quality, and consumer behavior data across the world's wealthiest region.</p>
        <p><strong>Premium buyers:</strong> Government planning agencies, international logistics companies, real estate developers, and retail chains pay top dollar for Gulf insights</p>
        <p><strong>Unique value:</strong> Only comprehensive real-time dataset covering Saudi Arabia, UAE, and Kuwait transportation patterns!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 4: Regional Expansion Acceleration
    expansion_revenue = 125000 * 2200  # 125,000 additional vehicles × $2,200 revenue each
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🌍 Patent #4: Gulf Region Domination = ${expansion_revenue:,.0f} additional revenue</h4>
        <p><strong>What happens:</strong> Use Jeeny's government relationships to expand rapidly across Oman, Bahrain, Qatar, and Jordan with Leo's electric fleet model.</p>
        <p><strong>Market opportunity:</strong> 125,000 additional vehicles across 4 new countries within 3 years</p>
        <p><strong>Competitive advantage:</strong> Established brand + proven electric technology + government backing = unstoppable expansion!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 5: Luxury Electric Services
    luxury_revenue = 8500000  # Premium services
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>💎 Patent #5: Luxury Electric Transportation = ${luxury_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Launch premium electric vehicle services: luxury airport transfers, private electric yacht connections, and VIP shopping transport in Dubai, Riyadh, and Kuwait City.</p>
        <p><strong>Target market:</strong> Ultra-wealthy individuals who pay $200-500 per ride for luxury electric experiences</p>
        <p><strong>Brand positioning:</strong> "The world's most sustainable luxury transportation" - perfect for ESG-conscious wealthy clients!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 6: Energy Trading & Storage
    energy_trading_revenue = 45000000  # Energy services
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>� Patent #6: Vehicle-to-Grid Energy Empire = ${energy_trading_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> 170,000 electric vehicles become a massive distributed battery network. During peak demand, vehicles sell energy back to the grid at premium prices.</p>
        <p><strong>Middle East advantage:</strong> Extreme temperature swings create huge energy price variations - perfect for battery arbitrage</p>
        <p><strong>Scale opportunity:</strong> Largest vehicle-to-grid network in the Middle East, earning $265 per vehicle annually from energy trading!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Total impact and valuation
    total_annual_revenue = jeeny_carbon_revenue + charging_revenue + data_revenue + expansion_revenue + luxury_revenue + energy_trading_revenue
    original_jeeny_revenue = 180000000  # Original $180M
    combined_annual_revenue = total_annual_revenue + original_jeeny_revenue
    enterprise_value = combined_annual_revenue * 12  # 12x revenue multiple for high-growth tech
    
    st.subheader("🎯 Jeeny Transformation - Annual Revenue Breakdown:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌱 Carbon + Charging", f"${jeeny_carbon_revenue + charging_revenue:,.0f}")
    
    with col2:
        st.metric("📊 Data + Expansion", f"${data_revenue + expansion_revenue:,.0f}")
    
    with col3:
        st.metric("💎 Luxury + Energy", f"${luxury_revenue + energy_trading_revenue:,.0f}")
    
    with col4:
        st.metric("🎉 Total New Revenue", f"${total_annual_revenue:,.0f}")
    
    # Enterprise valuation
    st.subheader("� Enterprise Valuation Timeline:")
    
    valuation_data = pd.DataFrame({
        'Stage': ['Current Jeeny', 'Leo Integration (Year 1)', 'Full Transformation (Year 3)', 'IPO (Year 5)'],
        'Enterprise Value ($B)': [0.8, 2.1, 4.8, 8.5],
        'Leo Stake Value ($B)': [0.4, 1.1, 2.4, 4.3]
    })
    
    fig = px.bar(valuation_data, x='Stage', y='Enterprise Value ($B)',
                title="Jeeny-Leo Enterprise Value Growth",
                color='Enterprise Value ($B)', color_continuous_scale='YlOrRd')
    fig.update_layout(xaxis_tickangle=-20, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Success story
    st.subheader("🌟 Strategic Impact:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="simple-explanation">
            <h4>🚗 Driver Success Story:</h4>
            <p><strong>Ahmed's Transformation:</strong> Jeeny driver in Riyadh</p>
            <p><strong>Before:</strong> $800/month income, $400/month gas costs</p>
            <p><strong>After Leo:</strong> $1,200/month income, zero fuel costs, carbon credit bonuses</p>
            <p><strong>Result:</strong> Net income increased from $400 to $1,200 monthly!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="simple-explanation">
            <h4>🌍 Regional Impact:</h4>
            <p><strong>Market Leadership:</strong> Largest electric vehicle fleet in Middle East</p>
            <p><strong>Government Partnership:</strong> Key contributor to Saudi Vision 2030</p>
            <p><strong>Economic Impact:</strong> 170,000 jobs created across 7 countries</p>
            <p><strong>Environmental:</strong> 2.5 million tons CO₂ avoided annually</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Export functionality
    case_data = create_saudi_arabia_export_data(total_annual_revenue, enterprise_value)
    create_export_button(case_data, 'saudi_arabia_jeeny_case_study.json', "📁 Export Saudi Arabia Case Study")


def render_singapore_case_study(lcis):
    """Render Singapore case study"""
    st.header("🦁 Singapore: Smart Nation Carbon-to-Wealth Ecosystem")
    
    st.markdown("""
    <div class="case-study-section">
        <h2>🏙️ The Vision: "Singapore = World's First Carbon-Negative Smart City"</h2>
        <p><strong>The Opportunity:</strong> Singapore's Smart Nation initiative meets Leo's climate intelligence. Transform the city-state into a living laboratory for carbon-negative urban living while building massive sovereign wealth through environmental technology exports.</p>
        <p><strong>Strategic Partnership:</strong> Singapore government + Leo + local universities create the world's most advanced urban sustainability ecosystem worth $10+ billion annually.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Singapore Smart City Infrastructure
    st.subheader("🏙️ Singapore Smart Nation Integration:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fleet-info">
            <h4>🚗 Complete Vehicle Electrification:</h4>
            <p>• 150,000 electric vehicles</p>
            <p>• All taxis, buses, delivery vehicles</p>
            <p>• Private vehicle transition program</p>
            <p>• 5,000 smart charging stations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fleet-info">
            <h4>🏢 Smart Building Integration:</h4>
            <p>• 25,000 buildings with smart energy</p>
            <p>• Vehicle-to-building power sharing</p>
            <p>• AI-optimized energy distribution</p>
            <p>• Real-time carbon tracking</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fleet-info">
            <h4>🌊 Marine & Port Electrification:</h4>
            <p>• World's first electric port</p>
            <p>• 2,000 electric harbor vessels</p>
            <p>• Shore power for all ships</p>
            <p>• Maritime carbon credit leader</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💰 How Singapore Becomes Global Carbon-Tech Export Leader:")
    
    # Patent 1: Urban Carbon Credits at Scale
    sg_carbon_revenue = 150000 * 1200  # 150,000 vehicles × $1,200 annual carbon credits
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🌱 Patent #1: Urban Carbon Credit System = ${sg_carbon_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Singapore becomes the world's first carbon-negative city. Every vehicle, building, and device contributes to massive carbon credit generation that's sold globally.</p>
        <p><strong>The opportunity:</strong> 150,000 EVs + 25,000 smart buildings + 2,000 marine vessels = 3.2 million tons CO₂ avoided annually</p>
        <p><strong>Premium pricing:</strong> Singapore carbon credits sell for $56/ton premium due to verified urban sustainability leadership!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 2: Smart City Technology Exports
    tech_export_revenue = 2400000000  # Technology licensing and exports
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🚀 Patent #2: Smart City Technology Exports = ${tech_export_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Singapore packages its complete smart city solution and sells it to 50+ cities worldwide. Every major city wants "Singapore's carbon-negative model."</p>
        <p><strong>Export products:</strong> AI energy management ($800M), integrated EV systems ($600M), smart building tech ($500M), carbon tracking platforms ($500M)</p>
        <p><strong>Competitive advantage:</strong> Only proven, real-world tested smart city ecosystem available for global deployment!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 3: Financial Services Innovation
    fintech_revenue = 850000000  # Green fintech services
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>💳 Patent #3: Green Financial Services Hub = ${fintech_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Singapore becomes the global center for carbon finance, green bonds, and sustainability investing. Leo's real-time carbon tracking enables new financial products.</p>
        <p><strong>Services offered:</strong> Carbon-backed loans, green insurance products, sustainability derivatives, climate risk analytics</p>
        <p><strong>Market capture:</strong> 25% of Asia-Pacific's $3.4 trillion green finance market flows through Singapore!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 4: Urban Data Intelligence
    data_intelligence_revenue = 650000000  # Urban data monetization
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>📊 Patent #4: Urban Intelligence Platform = ${data_intelligence_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> 150,000 vehicles + smart buildings + IoT sensors create the world's most comprehensive urban dataset. Cities, corporations, and governments pay premium for Singapore's insights.</p>
        <p><strong>Data products:</strong> Traffic optimization ($200M), energy management ($150M), urban planning ($150M), consumer behavior ($150M)</p>
        <p><strong>Unique value:</strong> Only complete real-time dataset of a fully integrated smart city ecosystem!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 5: Maritime Decarbonization Leadership
    maritime_revenue = 1200000000  # Maritime solutions
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>⚓ Patent #5: Maritime Decarbonization Hub = ${maritime_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Singapore's port becomes the global model for sustainable shipping. Every major port wants Singapore's electric maritime technology.</p>
        <p><strong>Revenue streams:</strong> Electric port technology exports ($400M), maritime carbon credits ($300M), ship electrification services ($300M), green shipping certification ($200M)</p>
        <p><strong>Strategic position:</strong> Controls 20% of global shipping traffic - perfect platform for maritime sustainability leadership!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patent 6: Research & Education Excellence
    education_revenue = 350000000  # Education and research exports
    st.markdown(f"""
    <div class="simple-explanation">
        <h4>🎓 Patent #6: Sustainability Education Exports = ${education_revenue:,.0f} per year</h4>
        <p><strong>What happens:</strong> Singapore universities become the global center for sustainability education. Students worldwide pay premium to study in the world's only carbon-negative city.</p>
        <p><strong>Programs offered:</strong> Smart city engineering ($100M), carbon finance degrees ($75M), urban sustainability research ($75M), corporate training ($100M)</p>
        <p><strong>Brand value:</strong> "Educated in Singapore" becomes the gold standard for sustainability professionals globally!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Total impact and economic multiplier
    total_direct_revenue = sg_carbon_revenue + tech_export_revenue + fintech_revenue + data_intelligence_revenue + maritime_revenue + education_revenue
    economic_multiplier = 1.8  # Each dollar generates additional economic activity
    total_economic_impact = total_direct_revenue * economic_multiplier
    
    st.subheader("🎯 Singapore's Global Economic Impact:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌱 Carbon + Tech Exports", f"${(sg_carbon_revenue + tech_export_revenue)/1000000:.1f}B")
    
    with col2:
        st.metric("💳 Finance + Data", f"${(fintech_revenue + data_intelligence_revenue)/1000000:.1f}B")
    
    with col3:
        st.metric("⚓ Maritime + Education", f"${(maritime_revenue + education_revenue)/1000000:.1f}B")
    
    with col4:
        st.metric("🎉 Total Economic Impact", f"${total_economic_impact/1000000:.1f}B")
    
    # Sovereign wealth growth
    st.subheader("� Singapore Sovereign Wealth Growth:")
    
    wealth_data = pd.DataFrame({
        'Year': [1, 3, 5, 7, 10],
        'Sovereign Wealth Fund ($B)': [650, 720, 850, 1100, 1500],
        'Climate Tech Revenue ($B)': [2.1, 4.8, 8.5, 12.2, 18.7]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wealth_data['Year'], y=wealth_data['Sovereign Wealth Fund ($B)'],
                            mode='lines+markers', name='Total Sovereign Wealth',
                            line=dict(width=4, color='#1f77b4')))
    fig.add_trace(go.Scatter(x=wealth_data['Year'], y=wealth_data['Climate Tech Revenue ($B)'],
                            mode='lines+markers', name='Annual Climate Tech Revenue',
                            line=dict(width=4, color='#ff7f0e')))
    fig.update_layout(title="Singapore's Climate-Tech Driven Wealth Growth",
                     xaxis_title="Year", yaxis_title="Value ($B)",
                     height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Global leadership metrics
    st.subheader("🌍 Global Leadership Impact:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="simple-explanation">
            <h4>🏆 Singapore's Global Firsts:</h4>
            <p><strong>World's First:</strong> Carbon-negative smart city</p>
            <p><strong>Technology Leader:</strong> #1 smart city technology exporter</p>
            <p><strong>Financial Hub:</strong> Global center for green finance</p>
            <p><strong>Education Excellence:</strong> Top sustainability education destination</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="simple-explanation">
            <h4>📈 Economic Transformation:</h4>
            <p><strong>GDP Contribution:</strong> Climate tech becomes 15% of GDP</p>
            <p><strong>Job Creation:</strong> 180,000 high-skilled green jobs</p>
            <p><strong>Export Growth:</strong> $5.8B annual technology exports</p>
            <p><strong>Investment Attraction:</strong> $50B in climate tech FDI</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Export functionality
    case_data = create_singapore_export_data(total_economic_impact)
    create_export_button(case_data, 'singapore_smart_city_case_study.json', "📁 Export Singapore Case Study")


if __name__ == "__main__":
    main()