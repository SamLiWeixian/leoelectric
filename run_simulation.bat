@echo off
echo Leo Electric IP Protection Strategy Simulation
echo =============================================

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Running IP Protection Simulation...
python ip_protection_simulation.py

echo.
echo Starting Interactive Dashboard...
echo Open your browser to http://localhost:8501
echo Press Ctrl+C to stop the dashboard
streamlit run ip_dashboard.py

pause