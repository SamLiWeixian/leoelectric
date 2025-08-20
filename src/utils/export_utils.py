"""
Export utilities for case studies and data export functionality
"""

import json
import streamlit as st

def export_case_study_data(data, filename):
    """Export case study data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error exporting data: {str(e)}")
        return False

def create_export_button(case_data, filename, button_text):
    """Create an export button with success message"""
    if st.button(button_text):
        if export_case_study_data(case_data, filename):
            st.success(f"✅ Case study exported to '{filename}'")
        else:
            st.error(f"❌ Failed to export case study to '{filename}'")

# Standard case study data templates
def create_green_city_export_data(total_value):
    """Template for Green City case study export"""
    return {
        'scenario': 'Green City Electric Fleet Deployment',
        'fleet_size': 5000,
        'annual_value_created': total_value,
        'key_benefits': [
            'Automatic revenue generation',
            'Linear scalability', 
            'Patent protection',
            'Environmental impact',
            'Global applicability'
        ]
    }

def create_nigerian_farmers_export_data(total_impact):
    """Template for Nigerian farmers case study export"""
    return {
        'scenario': 'Nigerian Electric Agriculture Transformation',
        'participants': '500 farmers in Kaduna State',
        'annual_impact': total_impact,
        'family_wealth_building': 'Average family wealth grows from $3,000 to $185,000 over 10 years',
        'key_innovations': [
            'Electric tractors and equipment',
            'Solar charging infrastructure', 
            'Carbon credit legacy funds',
            'Agricultural data monetization',
            'Community energy networks',
            'Family wealth building systems'
        ]
    }

def create_philippines_export_data(total_impact):
    """Template for Philippines case study export"""
    return {
        'scenario': 'Philippines Island Microgrid Partnership with DLSU',
        'communities': '50 remote island communities',
        'partnership': 'Leo + De La Salle University',
        'annual_impact': total_impact,
        'family_wealth_building': 'Average family wealth grows to $142,000 over 10 years',
        'key_innovations': [
            'Smart island microgrids',
            'Electric marine fleet', 
            'Blue carbon credit system',
            'Academic research partnership',
            'Sustainable tourism economy',
            'Inter-island energy trading'
        ]
    }

def create_saudi_arabia_export_data(total_revenue, enterprise_value):
    """Template for Saudi Arabia case study export"""
    return {
        'scenario': 'Saudi Arabia Jeeny Acquisition - Ride-Sharing to Climate-Tech Empire',
        'acquisition_target': 'Jeeny (Saudi Arabia ride-sharing)',
        'transformation': 'From ride-sharing to $5B+ climate-tech empire',
        'annual_revenue': total_revenue,
        'enterprise_value': enterprise_value,
        'ipo_readiness': 'Year 3 with $5.7B valuation',
        'key_innovations': [
            'Securitizable carbon credit revenue',
            'Desert energy arbitrage empire',
            'AI-enhanced fleet valuation',
            'Middle East mobility data platform',
            'Vision 2030 strategic partnership',
            'GCC regional expansion engine'
        ]
    }

def create_singapore_export_data(total_impact):
    """Template for Singapore case study export"""
    return {
        'scenario': 'Singapore Smart Nation Carbon-to-Wealth Ecosystem',
        'partnership': 'Leo + Singapore Government + NTU + Temasek Holdings',
        'vision': 'World\'s first carbon-negative smart city',
        'annual_impact': total_impact,
        'sovereign_wealth_boost': 'Additional $58.9B over 10 years',
        'key_innovations': [
            'Complete urban EV ecosystem',
            'Urban carbon farming',
            'AI-optimized energy trading',
            'Global smart city technology exports',
            'Climate finance innovation hub',
            'ASEAN climate leadership coordination'
        ]
    }