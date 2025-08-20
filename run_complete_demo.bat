@echo off
echo.
echo ==================================================================================
echo                    LEO CLIMATE INTELLIGENCE STACK (LCIS) 
echo                      Complete Business Model Demonstration
echo ==================================================================================
echo.

echo 🚀 This demonstration includes:
echo    • Complete mathematical formulas for all 6 core IP assets
echo    • Comprehensive business model simulations 
echo    • Interactive dashboards for stakeholder presentations
echo    • Quantitative proof of all business concepts
echo.

echo 📦 Installing required packages...
pip install -r requirements.txt >nul 2>&1

echo.
echo 🔬 Running IP Protection Strategy Simulation...
python stakeholder_presentation.py

echo.
echo 🌱 Running Complete LCIS Business Model Simulation...
python lcis_business_model.py

echo.
echo ==================================================================================
echo                                DEMONSTRATION COMPLETE
echo ==================================================================================
echo.
echo 📊 Generated Files:
echo    📈 executive_summary.png          - IP portfolio overview
echo    📊 comparison_matrix.png          - Detailed asset evaluation  
echo    ⚠️  risk_assessment.png           - Risk analysis dashboard
echo    💰 financial_projections.png     - Investment timeline
echo    📄 stakeholder_report.md         - IP strategy executive brief
echo.
echo 🌱 LCIS Business Model Files:
echo    🔬 lcis_complete_business_model.html - Interactive visualization
echo    📋 lcis_business_case_report.md     - Complete business analysis
echo    💾 lcis_simulation_data.json       - All simulation results
echo.
echo 🎪 Interactive Dashboards Available:
echo    💼 IP Strategy Dashboard:     streamlit run ip_dashboard.py
echo    🌱 LCIS Business Dashboard:   streamlit run lcis_dashboard.py
echo.
echo 🎯 Key Achievements:
echo    ✅ 6 Core formulas implemented with real calculations
echo    ✅ Complete business model with ROI analysis
echo    ✅ Visual proof of all IP protection strategies  
echo    ✅ Interactive tools for stakeholder engagement
echo    ✅ Quantitative validation of business concepts
echo.

choice /c YN /m "Would you like to start the interactive LCIS dashboard now"
if errorlevel 2 goto end
if errorlevel 1 goto dashboard

:dashboard
echo.
echo 🌱 Starting Leo Climate Intelligence Stack Dashboard...
echo    🌐 Open your browser to: http://localhost:8501
echo    🛑 Press Ctrl+C to stop the dashboard
echo.
streamlit run lcis_dashboard.py
goto end

:end
echo.
echo 🎉 Leo Electric LCIS Demonstration Complete!
echo    Ready for stakeholder presentations and business development.
pause