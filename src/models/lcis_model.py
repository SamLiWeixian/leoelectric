"""
Leo Climate Intelligence Stack (LCIS) - Core Business Model
Contains all the mathematical formulas and business logic for the patent portfolio
"""

class LEOClimateStack:
    """Leo Climate Intelligence Stack Business Model"""
    
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
        
        lifespan_extension = (1 / degradation_factor - 1) * 100
        
        return {
            'optimal_c_rate': optimal_c_rate,
            'max_charging_power': max_charging_power,
            'actual_charge_time': actual_charge_time,
            'lifespan_extension': lifespan_extension,
            'degradation_factor': degradation_factor
        }
    
    def swap_station_integrity(self, num_batteries, avg_swaps_per_day, maintenance_cost_per_battery):
        """Monitor swap station integrity and predict maintenance needs"""
        days = 365
        total_swaps = num_batteries * avg_swaps_per_day * days
        
        # Integrity scoring
        base_integrity = 95
        wear_factor = total_swaps / (num_batteries * 1000)  # degradation per 1000 swaps
        current_integrity = max(base_integrity - wear_factor, 70)
        
        # Maintenance prediction
        if current_integrity < 80:
            maintenance_urgency = "High"
            predicted_downtime = 24  # hours
        elif current_integrity < 90:
            maintenance_urgency = "Medium"
            predicted_downtime = 8
        else:
            maintenance_urgency = "Low"
            predicted_downtime = 2
        
        annual_maintenance_cost = num_batteries * maintenance_cost_per_battery
        downtime_cost = predicted_downtime * 1000  # $1000 per hour downtime
        
        return {
            'total_swaps': total_swaps,
            'current_integrity': current_integrity,
            'maintenance_urgency': maintenance_urgency,
            'predicted_downtime': predicted_downtime,
            'annual_maintenance_cost': annual_maintenance_cost,
            'total_cost': annual_maintenance_cost + downtime_cost
        }
    
    def blended_asset_valuation(self, vehicle_price, battery_value, software_value, age_months):
        """Calculate dynamic blended asset valuation"""
        # Depreciation curves
        vehicle_depreciation = 0.15 * (age_months / 12) + 0.05 * ((age_months / 12) ** 2)
        battery_depreciation = 0.08 * (age_months / 12)  # Slower depreciation
        software_appreciation = 0.05 * (age_months / 12)  # Software gains value with updates
        
        # Current values
        current_vehicle_value = vehicle_price * (1 - vehicle_depreciation)
        current_battery_value = battery_value * (1 - battery_depreciation)
        current_software_value = software_value * (1 + software_appreciation)
        
        # Blended valuation with synergy factor
        synergy_factor = 1.15  # 15% premium for integrated system
        blended_value = (current_vehicle_value + current_battery_value + current_software_value) * synergy_factor
        
        # Market comparables
        traditional_value = vehicle_price * (1 - 0.20 * (age_months / 12))
        
        return {
            'current_vehicle_value': current_vehicle_value,
            'current_battery_value': current_battery_value,
            'current_software_value': current_software_value,
            'blended_value': blended_value,
            'traditional_value': traditional_value,
            'premium': blended_value - traditional_value,
            'premium_percentage': ((blended_value - traditional_value) / traditional_value) * 100
        }
    
    def cross_border_data_value(self, num_countries, vehicles_per_country, data_points_per_vehicle_day):
        """Calculate cross-border data monetization value"""
        days = 365
        total_vehicles = num_countries * vehicles_per_country
        total_data_points = total_vehicles * data_points_per_vehicle_day * days
        
        # Data value tiers
        basic_data_value = 0.001  # $0.001 per data point
        premium_insights_multiplier = 5
        regulatory_compliance_value = 10000 * num_countries  # Regulatory value per country
        
        # Revenue calculations
        basic_revenue = total_data_points * basic_data_value
        premium_revenue = basic_revenue * premium_insights_multiplier * 0.2  # 20% premium clients
        
        # Cross-border insights premium
        network_effect = min(num_countries * 0.1, 1.0)  # Max 100% bonus
        cross_border_premium = basic_revenue * network_effect
        
        total_revenue = basic_revenue + premium_revenue + cross_border_premium + regulatory_compliance_value
        
        return {
            'total_vehicles': total_vehicles,
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