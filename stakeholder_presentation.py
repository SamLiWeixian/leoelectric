"""
Leo Electric IP Protection Strategy - Stakeholder Presentation Generator
Creates comprehensive visualizations and reports for stakeholder meetings
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Rectangle, FancyBboxPatch
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import json

class StakeholderPresentation:
    def __init__(self):
        self.ip_portfolio = {
            'A': {
                'name': 'Telemetry-attested micro-mobility MRV',
                'protection': 'Patent',
                'rationale': 'Foundational technology for verifiable credits. Patenting provides public credibility and legal defense against competitors seeking to build a similar system.',
                'priority': 'High',
                'market_impact': 9,
                'technical_complexity': 8,
                'defensibility': 9,
                'revenue_potential': 10,
                'timeline_months': 6,
                'estimated_cost': 50000,
                'competitive_advantage': 'High'
            },
            'B': {
                'name': 'Degradation-aware charging orchestration',
                'protection': 'Patent',
                'rationale': 'Novel method of optimizing charging for SOH and credit yield. Secures a key operational and financial advantage.',
                'priority': 'High',
                'market_impact': 8,
                'technical_complexity': 9,
                'defensibility': 8,
                'revenue_potential': 9,
                'timeline_months': 8,
                'estimated_cost': 45000,
                'competitive_advantage': 'High'
            },
            'C': {
                'name': 'Swap-station integrity & quality-gate MRV',
                'protection': 'Patent',
                'rationale': 'Addresses a core market integrity problem (data veracity). This non-obvious method provides a strong basis for a patentable claim that builds trust with registries and auditors.',
                'priority': 'High',
                'market_impact': 9,
                'technical_complexity': 7,
                'defensibility': 9,
                'revenue_potential': 8,
                'timeline_months': 6,
                'estimated_cost': 40000,
                'competitive_advantage': 'High'
            },
            'E': {
                'name': 'Blended asset valuation for EV portfolios',
                'protection': 'Patent',
                'rationale': 'The specific, technically-implemented algorithm that creates a securitizable asset class. Patenting protects this financial innovation from replication.',
                'priority': 'Critical',
                'market_impact': 10,
                'technical_complexity': 8,
                'defensibility': 8,
                'revenue_potential': 10,
                'timeline_months': 12,
                'estimated_cost': 60000,
                'competitive_advantage': 'Critical'
            },
            'F': {
                'name': 'Cross-border data stewarding for climate credits',
                'protection': 'Patent',
                'rationale': 'Novel method for handling complex, cross-jurisdictional data flows. Essential for global operations and provides a legal framework for data governance.',
                'priority': 'High',
                'market_impact': 8,
                'technical_complexity': 9,
                'defensibility': 7,
                'revenue_potential': 8,
                'timeline_months': 10,
                'estimated_cost': 55000,
                'competitive_advantage': 'Medium'
            },
            'G': {
                'name': 'Swap-aware OCPP/OCPI gateway for 2W/3W',
                'protection': 'Patent (or Defensive Pub)',
                'rationale': 'A protocol extension that provides a clear technical advancement. Patenting is preferred, but a defensive publication could be used if standardization is prioritized.',
                'priority': 'Medium',
                'market_impact': 7,
                'technical_complexity': 8,
                'defensibility': 6,
                'revenue_potential': 7,
                'timeline_months': 4,
                'estimated_cost': 25000,
                'competitive_advantage': 'Medium'
            },
            'H': {
                'name': 'Sodium-ion integration policy',
                'protection': 'Trade Secret',
                'rationale': 'The specific, proprietary policies and algorithms for optimizing sodium-ion with Li-ion are performance-enhancing and difficult to reverse-engineer. Secrecy is key.',
                'priority': 'Medium',
                'market_impact': 6,
                'technical_complexity': 7,
                'defensibility': 8,
                'revenue_potential': 6,
                'timeline_months': 2,
                'estimated_cost': 5000,
                'competitive_advantage': 'Medium'
            },
            'I': {
                'name': 'Calibration tables for losses & swap queue heuristics',
                'protection': 'Trade Secret',
                'rationale': 'These are operational "recipes" that provide a competitive edge. They are highly specific, easy to keep internal, and provide a marginal but critical performance advantage.',
                'priority': 'Medium',
                'market_impact': 5,
                'technical_complexity': 6,
                'defensibility': 9,
                'revenue_potential': 5,
                'timeline_months': 1,
                'estimated_cost': 2000,
                'competitive_advantage': 'Low'
            }
        }
        
        # Professional color scheme
        self.colors = {
            'primary': '#1f4e79',      # Deep blue
            'secondary': '#2e8b57',    # Sea green
            'accent': '#ff6b35',       # Orange red
            'neutral': '#6c757d',      # Gray
            'success': '#28a745',      # Green
            'warning': '#ffc107',      # Yellow
            'danger': '#dc3545'        # Red
        }

    def create_executive_summary_visual(self):
        """Create a comprehensive executive summary visualization"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Leo Electric IP Portfolio: Executive Summary', fontsize=20, fontweight='bold')
        
        # 1. Protection Strategy Distribution (Pie Chart)
        protection_counts = {}
        for ip in self.ip_portfolio.values():
            prot = ip['protection']
            protection_counts[prot] = protection_counts.get(prot, 0) + 1
        
        colors = [self.colors['primary'], self.colors['secondary'], self.colors['accent']]
        wedges, texts, autotexts = ax1.pie(
            protection_counts.values(), 
            labels=protection_counts.keys(),
            autopct='%1.0f%%',
            colors=colors,
            explode=(0.05, 0.05, 0.05)
        )
        ax1.set_title('Protection Strategy Distribution', fontweight='bold')
        
        # 2. Priority vs Market Impact Scatter
        priorities = {'Critical': 3, 'High': 2, 'Medium': 1}
        x_vals = [priorities[ip['priority']] for ip in self.ip_portfolio.values()]
        y_vals = [ip['market_impact'] for ip in self.ip_portfolio.values()]
        sizes = [ip['revenue_potential'] * 20 for ip in self.ip_portfolio.values()]
        
        scatter = ax2.scatter(x_vals, y_vals, s=sizes, alpha=0.6, c=range(len(x_vals)), cmap='viridis')
        
        for i, key in enumerate(self.ip_portfolio.keys()):
            ax2.annotate(key, (x_vals[i], y_vals[i]), xytext=(5, 5), textcoords='offset points')
        
        ax2.set_xlabel('Priority Level')
        ax2.set_ylabel('Market Impact Score')
        ax2.set_title('Priority vs Market Impact\n(Bubble size = Revenue Potential)', fontweight='bold')
        ax2.set_xticks([1, 2, 3])
        ax2.set_xticklabels(['Medium', 'High', 'Critical'])
        ax2.grid(True, alpha=0.3)
        
        # 3. Cost vs Revenue Potential
        costs = [ip['estimated_cost'] for ip in self.ip_portfolio.values()]
        revenues = [ip['revenue_potential'] for ip in self.ip_portfolio.values()]
        
        bars = ax3.barh(list(self.ip_portfolio.keys()), costs, alpha=0.7, color=self.colors['accent'])
        ax3_twin = ax3.twinx()
        line = ax3_twin.plot(revenues, list(self.ip_portfolio.keys()), 'o-', color=self.colors['primary'], linewidth=2, markersize=8)
        
        ax3.set_xlabel('Estimated Cost (USD)')
        ax3.set_title('Cost vs Revenue Potential Analysis', fontweight='bold')
        ax3_twin.set_ylabel('Revenue Potential Score')
        
        # 4. Implementation Timeline
        timeline_data = []
        labels = []
        for key, ip in self.ip_portfolio.items():
            timeline_data.append(ip['timeline_months'])
            labels.append(f"{key}: {ip['name'][:20]}...")
        
        bars = ax4.barh(labels, timeline_data, color=self.colors['secondary'], alpha=0.7)
        ax4.set_xlabel('Implementation Timeline (Months)')
        ax4.set_title('Implementation Timeline by Asset', fontweight='bold')
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax4.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                    f'{timeline_data[i]}m', ha='left', va='center')
        
        plt.tight_layout()
        plt.savefig('executive_summary.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

    def create_detailed_comparison_matrix(self):
        """Create a detailed comparison matrix for all IP assets"""
        # Prepare data for heatmap
        metrics = ['Market\nImpact', 'Technical\nComplexity', 'Defensibility', 'Revenue\nPotential']
        ip_names = [f"{k}: {v['name'][:15]}..." for k, v in self.ip_portfolio.items()]
        
        data_matrix = []
        for metric in ['market_impact', 'technical_complexity', 'defensibility', 'revenue_potential']:
            row = [ip[metric] for ip in self.ip_portfolio.values()]
            data_matrix.append(row)
        
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Create heatmap
        im = ax.imshow(data_matrix, cmap='RdYlBu_r', aspect='auto', vmin=0, vmax=10)
        
        # Set labels
        ax.set_xticks(range(len(ip_names)))
        ax.set_yticks(range(len(metrics)))
        ax.set_xticklabels(ip_names, rotation=45, ha='right')
        ax.set_yticklabels(metrics)
        
        # Add text annotations
        for i in range(len(metrics)):
            for j in range(len(ip_names)):
                text = ax.text(j, i, f'{data_matrix[i][j]}', 
                             ha="center", va="center", color="black", fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Score (1-10)', rotation=270, labelpad=15)
        
        ax.set_title('IP Asset Evaluation Matrix', fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig('comparison_matrix.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

    def create_risk_assessment_dashboard(self):
        """Create a comprehensive risk assessment dashboard"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('IP Risk Assessment Dashboard', fontsize=20, fontweight='bold')
        
        # Calculate risk metrics
        infringement_risks = []
        competitive_threats = []
        replication_risks = []
        protection_effectiveness = []
        
        for ip in self.ip_portfolio.values():
            infringement_risks.append(10 - ip['defensibility'])
            competitive_threats.append(ip['market_impact'])
            replication_risks.append(10 - ip['technical_complexity'])
            
            if ip['protection'] == 'Patent':
                protection_effectiveness.append(8)
            elif ip['protection'] == 'Patent (or Defensive Pub)':
                protection_effectiveness.append(6)
            else:  # Trade Secret
                protection_effectiveness.append(7)
        
        # 1. Risk Components Stacked Bar Chart
        x_pos = np.arange(len(self.ip_portfolio))
        width = 0.6
        
        bars1 = ax1.bar(x_pos, infringement_risks, width, label='Infringement Risk', 
                       color=self.colors['danger'], alpha=0.8)
        bars2 = ax1.bar(x_pos, competitive_threats, width, bottom=infringement_risks,
                       label='Competitive Threat', color=self.colors['warning'], alpha=0.8)
        bars3 = ax1.bar(x_pos, replication_risks, width, 
                       bottom=np.array(infringement_risks) + np.array(competitive_threats),
                       label='Replication Risk', color=self.colors['accent'], alpha=0.8)
        
        ax1.set_xlabel('IP Assets')
        ax1.set_ylabel('Risk Score')
        ax1.set_title('Risk Components by Asset')
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(list(self.ip_portfolio.keys()))
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Protection Effectiveness
        bars = ax2.bar(list(self.ip_portfolio.keys()), protection_effectiveness, 
                      color=self.colors['success'], alpha=0.7)
        ax2.set_ylabel('Protection Effectiveness Score')
        ax2.set_title('Protection Effectiveness by Asset')
        ax2.set_ylim(0, 10)
        ax2.grid(True, alpha=0.3)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height}', ha='center', va='bottom')
        
        # 3. Overall Risk Assessment
        overall_risks = []
        for i in range(len(self.ip_portfolio)):
            risk = (infringement_risks[i] + competitive_threats[i] + replication_risks[i])/3 - protection_effectiveness[i]/2
            overall_risks.append(max(0, risk))
        
        risk_colors = []
        for risk in overall_risks:
            if risk > 5:
                risk_colors.append(self.colors['danger'])
            elif risk > 3:
                risk_colors.append(self.colors['warning'])
            else:
                risk_colors.append(self.colors['success'])
        
        bars = ax3.bar(list(self.ip_portfolio.keys()), overall_risks, color=risk_colors, alpha=0.8)
        ax3.set_ylabel('Overall Risk Score')
        ax3.set_title('Overall Risk Assessment')
        ax3.axhline(y=3, color='red', linestyle='--', alpha=0.5, label='High Risk Threshold')
        ax3.axhline(y=5, color='darkred', linestyle='--', alpha=0.5, label='Critical Risk Threshold')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Risk vs Revenue Matrix
        revenues = [ip['revenue_potential'] for ip in self.ip_portfolio.values()]
        scatter = ax4.scatter(overall_risks, revenues, s=200, alpha=0.6, c=range(len(overall_risks)), cmap='viridis')
        
        for i, key in enumerate(self.ip_portfolio.keys()):
            ax4.annotate(key, (overall_risks[i], revenues[i]), xytext=(5, 5), textcoords='offset points')
        
        ax4.set_xlabel('Overall Risk Score')
        ax4.set_ylabel('Revenue Potential')
        ax4.set_title('Risk vs Revenue Potential Matrix')
        ax4.grid(True, alpha=0.3)
        
        # Add quadrant labels
        ax4.axvline(x=3, color='red', linestyle='--', alpha=0.3)
        ax4.axhline(y=7, color='red', linestyle='--', alpha=0.3)
        ax4.text(1, 9, 'Low Risk\nHigh Revenue', ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor=self.colors['success'], alpha=0.3))
        ax4.text(6, 9, 'High Risk\nHigh Revenue', ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=self.colors['warning'], alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('risk_assessment.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

    def create_financial_projection(self):
        """Create financial projections for IP portfolio"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        fig.suptitle('IP Portfolio Financial Projections', fontsize=18, fontweight='bold')
        
        # 1. Investment Timeline
        years = list(range(2025, 2031))
        
        # Patent costs (front-loaded)
        patent_costs = [200000, 150000, 100000, 80000, 60000, 40000]
        
        # Trade secret costs (ongoing)
        trade_secret_costs = [10000, 15000, 20000, 25000, 30000, 35000]
        
        # Revenue projections
        patent_revenue = [0, 500000, 2000000, 5000000, 12000000, 20000000]
        trade_secret_revenue = [100000, 300000, 600000, 1000000, 1500000, 2200000]
        
        ax1.bar(years, patent_costs, alpha=0.7, label='Patent Costs', color=self.colors['accent'])
        ax1.bar(years, trade_secret_costs, bottom=patent_costs, alpha=0.7, 
               label='Trade Secret Costs', color=self.colors['warning'])
        
        ax1_twin = ax1.twinx()
        ax1_twin.plot(years, patent_revenue, 'o-', linewidth=3, markersize=8, 
                     label='Patent Revenue', color=self.colors['primary'])
        ax1_twin.plot(years, trade_secret_revenue, 's-', linewidth=3, markersize=8,
                     label='Trade Secret Revenue', color=self.colors['secondary'])
        
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Costs (USD)')
        ax1_twin.set_ylabel('Revenue (USD)')
        ax1.set_title('Investment vs Revenue Timeline')
        ax1.legend(loc='upper left')
        ax1_twin.legend(loc='upper right')
        ax1.grid(True, alpha=0.3)
        
        # 2. ROI Analysis
        total_costs = np.array(patent_costs) + np.array(trade_secret_costs)
        total_revenue = np.array(patent_revenue) + np.array(trade_secret_revenue)
        cumulative_costs = np.cumsum(total_costs)
        cumulative_revenue = np.cumsum(total_revenue)
        roi = ((cumulative_revenue - cumulative_costs) / cumulative_costs) * 100
        
        bars = ax2.bar(years, roi, color=[self.colors['success'] if r > 0 else self.colors['danger'] for r in roi], alpha=0.8)
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Cumulative ROI (%)')
        ax2.set_title('Return on Investment Timeline')
        ax2.grid(True, alpha=0.3)
        
        # Add value labels
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + (5 if height > 0 else -15),
                    f'{roi[i]:.0f}%', ha='center', va='bottom' if height > 0 else 'top')
        
        plt.tight_layout()
        plt.savefig('financial_projections.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

    def generate_stakeholder_report(self):
        """Generate a comprehensive stakeholder report"""
        report = f"""
# Leo Electric IP Protection Strategy
## Stakeholder Executive Brief
### Generated: {datetime.now().strftime('%B %d, %Y')}

---

## Executive Summary

Leo Electric's intellectual property portfolio represents a strategic foundation for establishing market leadership in the climate intelligence and micro-mobility sectors. Our comprehensive IP strategy encompasses **{len(self.ip_portfolio)} critical assets** across foundational technologies, operational innovations, and financial instruments.

### Key Strategic Metrics

- **Total IP Assets**: {len(self.ip_portfolio)}
- **Patent Applications**: {sum(1 for ip in self.ip_portfolio.values() if 'Patent' in ip['protection'])}
- **Trade Secrets**: {sum(1 for ip in self.ip_portfolio.values() if 'Trade Secret' in ip['protection'])}
- **High Priority Assets**: {sum(1 for ip in self.ip_portfolio.values() if ip['priority'] in ['Critical', 'High'])}
- **Estimated Total Investment**: ${sum(ip['estimated_cost'] for ip in self.ip_portfolio.values()):,}

### Strategic Protection Framework

Our IP protection strategy is built on three pillars:

**1. Foundation Protection (Patents)**
- Core MRV technologies for market credibility
- Charging optimization algorithms for operational advantage
- Data integrity systems for registry trust

**2. Financial Innovation (Patents)**
- Blended asset valuation creating new securitizable asset class
- Cross-border data governance for global operations

**3. Operational Excellence (Trade Secrets)**
- Proprietary optimization algorithms
- Performance-enhancing calibration systems

---

## Individual Asset Analysis

"""
        
        for key, ip in self.ip_portfolio.items():
            report += f"""
### {key}. {ip['name']}

**Protection Strategy**: {ip['protection']}  
**Priority**: {ip['priority']}  
**Timeline**: {ip['timeline_months']} months  
**Estimated Cost**: ${ip['estimated_cost']:,}  

**Strategic Rationale**: {ip['rationale']}

**Key Metrics**:
- Market Impact: {ip['market_impact']}/10
- Technical Complexity: {ip['technical_complexity']}/10  
- Defensibility: {ip['defensibility']}/10
- Revenue Potential: {ip['revenue_potential']}/10

---
"""
        
        report += f"""
## Risk Assessment & Mitigation

### High-Priority Risks
1. **Competitive Replication**: Patents provide legal protection for foundational technologies
2. **Trade Secret Exposure**: Robust internal protocols and employee training required
3. **Global IP Enforcement**: International filing strategy needed for key markets

### Mitigation Strategies
- **Freedom to Operate Analysis**: Comprehensive landscape review before product launch
- **IP Monitoring Services**: Automated tracking of competitive patent filings
- **Employee Education**: Trade secret handling and confidentiality protocols
- **Portfolio Insurance**: Professional liability coverage for IP assets

## Financial Projections

### Investment Timeline
- **Year 1**: ${sum(ip['estimated_cost'] for ip in self.ip_portfolio.values() if ip['timeline_months'] <= 12):,} (Initial patent filings)
- **Years 2-3**: Ongoing prosecution and international expansion
- **Years 4-6**: Patent grants and licensing opportunities

### Revenue Projections
- **Patent Licensing**: Potential $20M+ annual revenue by 2030
- **Trade Secret Advantage**: $2M+ annual operational savings
- **Total ROI**: Estimated 400%+ over 6-year horizon

## Recommended Actions

### Immediate (Next 90 Days)
1. File patent applications for assets A, B, C, E
2. Implement trade secret protection protocols
3. Conduct freedom-to-operate analysis

### Medium-term (6-12 Months)
1. Complete remaining patent filings
2. Initiate international filing strategy
3. Establish IP monitoring systems

### Long-term (1-3 Years)
1. Pursue patent grants and enforcement
2. Explore licensing opportunities
3. Expand international portfolio

---

**This report demonstrates Leo Electric's commitment to building a defensible, valuable intellectual property portfolio that will secure our competitive position and create significant stakeholder value.**
"""
        
        # Save report to file
        with open('stakeholder_report.md', 'w') as f:
            f.write(report)
        
        print("Stakeholder report generated: stakeholder_report.md")
        return report

def main():
    """Generate all visualizations and reports for stakeholder presentation"""
    print("Leo Electric IP Protection Strategy - Stakeholder Presentation Generator")
    print("=" * 70)
    
    presentation = StakeholderPresentation()
    
    print("\nGenerating visualizations...")
    
    # Create all visualizations
    print("1. Creating executive summary visual...")
    presentation.create_executive_summary_visual()
    
    print("2. Creating comparison matrix...")
    presentation.create_detailed_comparison_matrix()
    
    print("3. Creating risk assessment dashboard...")
    presentation.create_risk_assessment_dashboard()
    
    print("4. Creating financial projections...")
    presentation.create_financial_projection()
    
    print("5. Generating stakeholder report...")
    presentation.generate_stakeholder_report()
    
    print("\n" + "=" * 70)
    print("PRESENTATION MATERIALS GENERATED:")
    print("=" * 70)
    print("📊 executive_summary.png - High-level portfolio overview")
    print("📈 comparison_matrix.png - Detailed asset evaluation matrix") 
    print("⚠️  risk_assessment.png - Comprehensive risk analysis")
    print("💰 financial_projections.png - Investment and ROI timeline")
    print("📄 stakeholder_report.md - Complete executive brief")
    print("\nAll materials are ready for stakeholder presentations!")

if __name__ == "__main__":
    main()