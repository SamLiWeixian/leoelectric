"""
Professional CSS styling for Leo Climate Intelligence Stack Dashboard
All visual styling and theme configurations
"""

DASHBOARD_CSS = """
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f4e79 !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .patent-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #1f4e79;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #333 !important;
    }
    
    .patent-card h3 {
        color: #1f4e79 !important;
        margin-bottom: 1rem;
    }
    
    .patent-card p {
        color: #333 !important;
        margin-bottom: 0.5rem;
    }
    
    .metric-card {
        background: #ffffff !important;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        border: 3px solid #1f4e79;
        margin: 0.5rem 0;
    }
    
    .metric-card h3 {
        color: #1f4e79 !important;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .metric-card p {
        color: #333 !important;
        font-size: 1.1rem !important;
        margin: 0;
        font-weight: 600;
    }
    
    .parameter-explanation {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1976d2;
        margin: 0.5rem 0;
        color: #333 !important;
    }
    
    .parameter-explanation h4 {
        color: #1976d2 !important;
        margin-bottom: 0.5rem;
    }
    
    .parameter-explanation p {
        color: #333 !important;
        margin-bottom: 0.3rem;
    }
    
    .case-study-section {
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        border: 3px solid #1f4e79;
        margin: 1rem 0;
        color: #000000 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .case-study-section h2, .case-study-section h3 {
        color: #1f4e79 !important;
        font-weight: bold;
    }
    
    .case-study-section p, .case-study-section li {
        color: #000000 !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .formula-box {
        background: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #4169e1;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    
    .formula-box h4 {
        color: #4169e1 !important;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    
    .formula-box .formula {
        background: #ffffff;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #4169e1;
        font-size: 1.2rem;
        color: #000000 !important;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .simple-explanation {
        background: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #28a745;
        margin: 1rem 0;
        color: #000000 !important;
    }
    
    .simple-explanation h4 {
        color: #28a745 !important;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .fleet-info {
        background: #1f4e79;
        color: #ffffff !important;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .fleet-info h4 {
        color: #ffffff !important;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .fleet-info p, .fleet-info li {
        color: #ffffff !important;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Override Streamlit's default styles */
    .stMarkdown {
        color: #333 !important;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #1f4e79 !important;
    }
    
    /* Fix metric display */
    [data-testid="metric-container"] {
        background: #ffffff;
        border: 2px solid #1f4e79;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    [data-testid="metric-container"] > div {
        color: #1f4e79 !important;
    }
    
    [data-testid="metric-container"] label {
        color: #666 !important;
    }
</style>
"""

# Theme configurations for different regions
THEME_COLORS = {
    'default': '#1f4e79',
    'philippines': '#007bff',
    'saudi_arabia': '#d4af37', 
    'singapore': '#dc143c',
    'nigeria': '#28a745'
}