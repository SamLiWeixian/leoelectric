"""
Leo Electric IP Protection Strategy Visualization
A comprehensive simulation tool for demonstrating intellectual property protection strategies to stakeholders
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Rectangle, FancyBboxPatch
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from datetime import datetime, timedelta

class IPProtectionSimulator:
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
                'revenue_potential': 10
            },
            'B': {
                'name': 'Degradation-aware charging orchestration',
                'protection': 'Patent',
                'rationale': 'Novel method of optimizing charging for SOH and credit yield. Secures a key operational and financial advantage.',
                'priority': 'High',
                'market_impact': 8,
                'technical_complexity': 9,
                'defensibility': 8,
                'revenue_potential': 9
            },
            'C': {
                'name': 'Swap-station integrity & quality-gate MRV',
                'protection': 'Patent',
                'rationale': 'Addresses a core market integrity problem (data veracity). This non-obvious method provides a strong basis for a patentable claim that builds trust with registries and auditors.',
                'priority': 'High',
                'market_impact': 9,
                'technical_complexity': 7,
                'defensibility': 9,
                'revenue_potential': 8
            },
            'E': {
                'name': 'Blended asset valuation for EV portfolios',
                'protection': 'Patent',
                'rationale': 'The specific, technically-implemented algorithm that creates a securitizable asset class. Patenting protects this financial innovation from replication.',
                'priority': 'Critical',
                'market_impact': 10,
                'technical_complexity': 8,
                'defensibility': 8,
                'revenue_potential': 10
            },
            'F': {
                'name': 'Cross-border data stewarding for climate credits',
                'protection': 'Patent',
                'rationale': 'Novel method for handling complex, cross-jurisdictional data flows. Essential for global operations and provides a legal framework for data governance.',
                'priority': 'High',
                'market_impact': 8,
                'technical_complexity': 9,
                'defensibility': 7,
                'revenue_potential': 8
            },
            'G': {
                'name': 'Swap-aware OCPP/OCPI gateway for 2W/3W',
                'protection': 'Patent (or Defensive Pub)',
                'rationale': 'A protocol extension that provides a clear technical advancement. Patenting is preferred, but a defensive publication could be used if standardization is prioritized.',
                'priority': 'Medium',
                'market_impact': 7,
                'technical_complexity': 8,
                'defensibility': 6,
                'revenue_potential': 7
            },
            'H': {
                'name': 'Sodium-ion integration policy',
                'protection': 'Trade Secret',
                'rationale': 'The specific, proprietary policies and algorithms for optimizing sodium-ion with Li-ion are performance-enhancing and difficult to reverse-engineer. Secrecy is key.',
                'priority': 'Medium',
                'market_impact': 6,
                'technical_complexity': 7,
                'defensibility': 8,
                'revenue_potential': 6
            },
            'I': {
                'name': 'Calibration tables for losses & swap queue heuristics',
                'protection': 'Trade Secret',
                'rationale': 'These are operational "recipes" that provide a competitive edge. They are highly specific, easy to keep internal, and provide a marginal but critical performance advantage.',
                'priority': 'Medium',
                'market_impact': 5,
                'technical_complexity': 6,
                'defensibility': 9,
                'revenue_potential': 5
            }
        }
        
        # Color scheme for different protection types
        self.protection_colors = {
            'Patent': '#2E86AB',
            'Patent (or Defensive Pub)': '#A23B72',
            'Trade Secret': '#F18F01'
        }
        
        # Priority colors
        self.priority_colors = {
            'Critical': '#D32F2F',
            'High': '#F57C00',
            'Medium': '#388E3C'
        }

    def create_portfolio_overview(self):
        """Create a comprehensive portfolio overview visualization"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Protection Strategy Distribution', 'Priority vs Market Impact', 
                          'Technical Complexity vs Defensibility', 'Revenue Potential Analysis'),
            specs=[[{"type": "pie"}, {"type": "scatter"}],
                   [{"type": "scatter"}, {"type": "bar"}]]
        )
        
        # Protection strategy distribution (pie chart)
        protection_counts = {}
        for ip in self.ip_portfolio.values():
            prot = ip['protection']
            protection_counts[prot] = protection_counts.get(prot, 0) + 1
        
        fig.add_trace(
            go.Pie(
                labels=list(protection_counts.keys()),
                values=list(protection_counts.values()),
                marker_colors=[self.protection_colors[p] for p in protection_counts.keys()],
                name="Protection Types"
            ),
            row=1, col=1
        )
        
        # Priority vs Market Impact scatter
        for key, ip in self.ip_portfolio.items():
            priority_value = {'Critical': 3, 'High': 2, 'Medium': 1}[ip['priority']]
            fig.add_trace(
                go.Scatter(
                    x=[priority_value],
                    y=[ip['market_impact']],
                    mode='markers+text',
                    text=[key],
                    textposition="middle center",
                    marker=dict(
                        size=15,
                        color=self.protection_colors[ip['protection']],
                        line=dict(width=2, color='white')
                    ),
                    name=ip['name'][:20] + "...",
                    showlegend=False
                ),
                row=1, col=2
            )
        
        # Technical Complexity vs Defensibility
        for key, ip in self.ip_portfolio.items():
            fig.add_trace(
                go.Scatter(
                    x=[ip['technical_complexity']],
                    y=[ip['defensibility']],
                    mode='markers+text',
                    text=[key],
                    textposition="middle center",
                    marker=dict(
                        size=ip['revenue_potential'] * 2,
                        color=self.protection_colors[ip['protection']],
                        line=dict(width=2, color='white'),
                        opacity=0.7
                    ),
                    name=ip['name'][:20] + "...",
                    showlegend=False
                ),
                row=2, col=1
            )
        
        # Revenue Potential Analysis
        ip_names = [f"{k}: {v['name'][:15]}..." for k, v in self.ip_portfolio.items()]
        revenue_potentials = [v['revenue_potential'] for v in self.ip_portfolio.values()]
        colors = [self.protection_colors[v['protection']] for v in self.ip_portfolio.values()]
        
        fig.add_trace(
            go.Bar(
                x=list(self.ip_portfolio.keys()),
                y=revenue_potentials,
                marker_color=colors,
                name="Revenue Potential",
                showlegend=False
            ),
            row=2, col=2
        )
        
        # Update layout
        fig.update_layout(
            title_text="Leo Electric IP Portfolio Strategic Overview",
            title_x=0.5,
            height=800,
            showlegend=True
        )
        
        # Update axis labels
        fig.update_xaxes(title_text="Priority Level", row=1, col=2)
        fig.update_yaxes(title_text="Market Impact", row=1, col=2)
        fig.update_xaxes(title_text="Technical Complexity", row=2, col=1)
        fig.update_yaxes(title_text="Defensibility", row=2, col=1)
        fig.update_xaxes(title_text="IP Asset", row=2, col=2)
        fig.update_yaxes(title_text="Revenue Potential", row=2, col=2)
        
        return fig

    def create_protection_strategy_matrix(self):
        """Create a detailed protection strategy matrix"""
        # Create data for heatmap
        metrics = ['Market Impact', 'Technical Complexity', 'Defensibility', 'Revenue Potential']
        ip_keys = list(self.ip_portfolio.keys())
        
        matrix_data = []
        for metric in metrics:
            row = []
            for key in ip_keys:
                if metric == 'Market Impact':
                    row.append(self.ip_portfolio[key]['market_impact'])
                elif metric == 'Technical Complexity':
                    row.append(self.ip_portfolio[key]['technical_complexity'])
                elif metric == 'Defensibility':
                    row.append(self.ip_portfolio[key]['defensibility'])
                elif metric == 'Revenue Potential':
                    row.append(self.ip_portfolio[key]['revenue_potential'])
            matrix_data.append(row)
        
        fig = go.Figure(data=go.Heatmap(
            z=matrix_data,
            x=ip_keys,
            y=metrics,
            colorscale='RdYlBu_r',
            text=matrix_data,
            texttemplate="%{text}",
            textfont={"size": 12},
            colorbar=dict(title="Score (1-10)")
        ))
        
        fig.update_layout(
            title="IP Protection Strategy Evaluation Matrix",
            xaxis_title="IP Assets",
            yaxis_title="Evaluation Metrics",
            height=400
        )
        
        return fig

    def create_risk_assessment(self):
        """Create risk assessment visualization"""
        # Calculate risk scores based on protection type and other factors
        risk_data = []
        
        for key, ip in self.ip_portfolio.items():
            # Risk factors
            infringement_risk = 10 - ip['defensibility']  # Higher defensibility = lower risk
            competitive_threat = ip['market_impact']  # Higher impact = higher threat
            replication_risk = 10 - ip['technical_complexity']  # More complex = harder to replicate
            
            # Protection effectiveness
            if ip['protection'] == 'Patent':
                protection_effectiveness = 8
            elif ip['protection'] == 'Patent (or Defensive Pub)':
                protection_effectiveness = 6
            else:  # Trade Secret
                protection_effectiveness = 7
            
            overall_risk = (infringement_risk + competitive_threat + replication_risk) / 3 - protection_effectiveness/2
            
            risk_data.append({
                'IP': key,
                'Name': ip['name'][:30] + "...",
                'Infringement Risk': infringement_risk,
                'Competitive Threat': competitive_threat,
                'Replication Risk': replication_risk,
                'Protection Effectiveness': protection_effectiveness,
                'Overall Risk': max(0, overall_risk),
                'Protection Type': ip['protection']
            })
        
        df = pd.DataFrame(risk_data)
        
        fig = go.Figure()
        
        # Add bars for each risk component
        fig.add_trace(go.Bar(
            name='Infringement Risk',
            x=df['IP'],
            y=df['Infringement Risk'],
            marker_color='rgba(255, 99, 132, 0.7)'
        ))
        
        fig.add_trace(go.Bar(
            name='Competitive Threat',
            x=df['IP'],
            y=df['Competitive Threat'],
            marker_color='rgba(54, 162, 235, 0.7)'
        ))
        
        fig.add_trace(go.Bar(
            name='Replication Risk',
            x=df['IP'],
            y=df['Replication Risk'],
            marker_color='rgba(255, 206, 86, 0.7)'
        ))
        
        # Add line for protection effectiveness
        fig.add_trace(go.Scatter(
            name='Protection Effectiveness',
            x=df['IP'],
            y=df['Protection Effectiveness'],
            mode='lines+markers',
            line=dict(color='green', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title='IP Risk Assessment Dashboard',
            xaxis_title='IP Assets',
            yaxis_title='Risk Score',
            barmode='group',
            height=500
        )
        
        return fig

    def create_timeline_simulation(self):
        """Create a timeline showing patent filing and protection strategy"""
        # Simulate filing dates and milestones
        base_date = datetime.now()
        timeline_data = []
        
        for i, (key, ip) in enumerate(self.ip_portfolio.items()):
            if 'Patent' in ip['protection']:
                # Patent timeline
                filing_date = base_date + timedelta(days=i*30)
                publication_date = filing_date + timedelta(days=540)  # 18 months
                grant_date = filing_date + timedelta(days=1095)  # ~3 years
                
                timeline_data.extend([
                    {'IP': key, 'Event': 'Filing', 'Date': filing_date, 'Status': 'Planned'},
                    {'IP': key, 'Event': 'Publication', 'Date': publication_date, 'Status': 'Future'},
                    {'IP': key, 'Event': 'Grant', 'Date': grant_date, 'Status': 'Future'}
                ])
            else:
                # Trade secret implementation
                impl_date = base_date + timedelta(days=i*15)
                timeline_data.append({
                    'IP': key, 'Event': 'Implementation', 'Date': impl_date, 'Status': 'Planned'
                })
        
        df_timeline = pd.DataFrame(timeline_data)
        
        fig = px.timeline(
            df_timeline,
            x_start="Date",
            x_end="Date",
            y="IP",
            color="Event",
            title="IP Protection Implementation Timeline"
        )
        
        fig.update_yaxes(autorange="reversed")
        
        return fig

    def generate_executive_summary(self):
        """Generate an executive summary of the IP strategy"""
        total_assets = len(self.ip_portfolio)
        patent_count = sum(1 for ip in self.ip_portfolio.values() if 'Patent' in ip['protection'])
        trade_secret_count = sum(1 for ip in self.ip_portfolio.values() if 'Trade Secret' in ip['protection'])
        
        avg_market_impact = np.mean([ip['market_impact'] for ip in self.ip_portfolio.values()])
        avg_revenue_potential = np.mean([ip['revenue_potential'] for ip in self.ip_portfolio.values()])
        
        high_priority_count = sum(1 for ip in self.ip_portfolio.values() if ip['priority'] in ['Critical', 'High'])
        
        summary = f"""
        ## Leo Electric IP Portfolio Executive Summary
        
        **Total IP Assets:** {total_assets}
        - Patents/Patent Applications: {patent_count}
        - Trade Secrets: {trade_secret_count}
        
        **Strategic Metrics:**
        - Average Market Impact Score: {avg_market_impact:.1f}/10
        - Average Revenue Potential: {avg_revenue_potential:.1f}/10
        - High Priority Assets: {high_priority_count}/{total_assets}
        
        **Key Strategic Insights:**
        1. **Foundation Protection**: Core MRV and charging technologies secured through patents
        2. **Financial Innovation**: Blended asset valuation provides competitive moat
        3. **Operational Secrets**: Critical algorithms maintained as trade secrets
        4. **Global Readiness**: Cross-border data handling capabilities protected
        
        **Recommended Actions:**
        - Prioritize patent filings for foundational technologies (A, B, C, E)
        - Implement robust trade secret protection protocols
        - Monitor competitive landscape for potential infringement
        - Consider international patent filing strategy for global markets
        """
        
        return summary

def main():
    """Main function to run the IP protection simulation"""
    simulator = IPProtectionSimulator()
    
    print("Leo Electric IP Protection Strategy Simulation")
    print("=" * 50)
    
    # Generate executive summary
    print(simulator.generate_executive_summary())
    
    # Create visualizations
    portfolio_fig = simulator.create_portfolio_overview()
    matrix_fig = simulator.create_protection_strategy_matrix()
    risk_fig = simulator.create_risk_assessment()
    timeline_fig = simulator.create_timeline_simulation()
    
    # Save visualizations
    portfolio_fig.write_html("ip_portfolio_overview.html")
    matrix_fig.write_html("ip_strategy_matrix.html")
    risk_fig.write_html("ip_risk_assessment.html")
    timeline_fig.write_html("ip_timeline.html")
    
    print("\nVisualizations saved:")
    print("- ip_portfolio_overview.html")
    print("- ip_strategy_matrix.html") 
    print("- ip_risk_assessment.html")
    print("- ip_timeline.html")
    
    # Display individual asset details
    print("\n" + "="*50)
    print("DETAILED IP ASSET ANALYSIS")
    print("="*50)
    
    for key, ip in simulator.ip_portfolio.items():
        print(f"\n{key}. {ip['name']}")
        print(f"   Protection: {ip['protection']}")
        print(f"   Priority: {ip['priority']}")
        print(f"   Rationale: {ip['rationale']}")
        print(f"   Scores - Market Impact: {ip['market_impact']}, Revenue Potential: {ip['revenue_potential']}")

if __name__ == "__main__":
    main()