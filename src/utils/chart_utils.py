"""
Chart utilities for creating consistent visualizations across the dashboard
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

def create_pie_chart(data, values_col, names_col, title):
    """Create a pie chart for revenue streams"""
    fig = px.pie(data, values=values_col, names=names_col, title=title)
    return fig

def create_scatter_plot(data, x_col, y_col, size_col=None, color_col=None, title="Scatter Plot"):
    """Create a scatter plot with optional size and color coding"""
    fig = px.scatter(data, x=x_col, y=y_col, size=size_col, 
                    color=color_col, title=title)
    return fig

def create_valuation_timeline_chart(timeline_data, title, color_scale='YlOrRd'):
    """Create specialized chart for valuation timelines"""
    fig = px.bar(timeline_data, x='Stage', y='Enterprise Value ($B)',
                title=title, color='Enterprise Value ($B)',
                color_continuous_scale=color_scale)
    fig.update_layout(xaxis_tickangle=-20)
    return fig