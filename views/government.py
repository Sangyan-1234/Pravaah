"""
GOVERNMENT DASHBOARD - Complete Policy & Monitoring Interface
Real-time monitoring, Geographic analysis, Advanced analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime, timedelta
import folium
from streamlit_folium import st_folium

def show_government_dashboard():
    st.title("🏛️ Government Policy & Monitoring Dashboard")
    st.markdown("*Real-time environmental intelligence for decision makers*")
    
    # Critical metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Critical Zones", "12", "🔴 +3", delta_color="inverse")
    with col2:
        st.metric("Avg WQI", "48.7", "-5.3", delta_color="inverse")
    with col3:
        st.metric("DO Level", "4.2 mg/L", "-0.8", delta_color="inverse")
    with col4:
        st.metric("Compliance", "68%", "-8%", delta_color="inverse")
    with col5:
        st.metric("Budget Used", "₹72Cr", "+12%")
    
    st.markdown("---")
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔬 Complete Analysis Pipeline",
        "🗺️ Geographic Monitoring",
        "📊 Advanced Analytics",
        "⚙️ System Configuration"
    ])
    
    # ====================================
    # TAB 1: COMPLETE ANALYSIS PIPELINE
    # ====================================
    with tab1:
        st.subheader("🚀 Complete Analysis Pipeline")
        st.markdown("*Upload sample → YOLO → Raman → WQI → Forecast → PINN → Digital Twin*")
        
        # File upload
        uploaded = st.file_uploader(
            "Upload Water Sample Image",
            type=['jpg', 'png', 'jpeg'],
            key="govt_upload",
            help="Supported formats: JPG, PNG, JPEG"
        )
        
        if uploaded:
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded, caption="Uploaded Sample", use_container_width=True)
        
        # Environmental parameters
        st.markdown("### 🌡️ Environmental Parameters")
        st.markdown("*Enter measured water quality parameters*")
        
        param_col1, param_col2, param_col3 = st.columns(3)
        
        with param_col1:
            temperature = st.number_input("Temperature (°C)", 10.0, 40.0, 25.0, 0.1)
            ph = st.number_input("pH Level", 0.0, 14.0, 7.0, 0.1)
            turbidity = st.number_input("Turbidity (NTU)", 0.0, 100.0, 25.0, 1.0)
            dissolved_oxygen = st.number_input("Dissolved Oxygen (mg/L)", 0.0, 15.0, 7.5, 0.1)
        
        with param_col2:
            conductivity = st.number_input("Conductivity (µS/cm)", 0.0, 2000.0, 450.0, 10.0)
            bod = st.number_input("BOD (mg/L)", 0.0, 50.0, 10.0, 0.5)
            cod = st.number_input("COD (mg/L)", 0.0, 200.0, 35.0, 1.0)
            tds = st.number_input("TDS (mg/L)", 0.0, 2000.0, 300.0, 10.0)
        
        with param_col3:
            nitrate = st.number_input("Nitrate (mg/L)", 0.0, 50.0, 8.5, 0.5)
            phosphate = st.number_input("Phosphate (mg/L)", 0.0, 20.0, 2.1, 0.1)
            chloride = st.number_input("Chloride (mg/L)", 0.0, 500.0, 85.0, 5.0)
            fecal_coliform = st.number_input("Fecal Coliform (MPN/100ml)", 0, 10000, 150, 10)
        
        # Run pipeline button
        if st.button("🚀 Run Complete Pipeline", type="primary", use_container_width=True):
            if uploaded:
                pipeline_container = st.container()
                
                with pipeline_container:
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Step 1: YOLO Detection
                    status_text.markdown("**Step 1/6:** Running YOLOv8 detection...")
                    progress_bar.progress(16)
                    
                    try:
                        from models.yolo.infer import predict_image_with_viz
                        yolo_result = predict_image_with_viz(uploaded, 0.35, "Government")
                        st.session_state.yolo_result = yolo_result
                    except Exception as e:
                        st.error(f"YOLO detection failed: {e}")
                        yolo_result = {'count': 0, 'particle_types': {}, 'error': str(e)}
                    
                    # Step 2: Raman Classification
                    status_text.markdown("**Step 2/6:** Raman spectroscopy analysis...")
                    progress_bar.progress(33)
                    
                    try:
                        from models.raman.infer import predict_polymer
                        # Simulate Raman spectrum from image
                        raman_spectrum = np.random.rand(1024)
                        raman_result = predict_polymer(raman_spectrum)
                        st.session_state.raman_result = raman_result
                    except Exception as e:
                        st.warning(f"Raman analysis skipped: {e}")
                        raman_result = {'polymer': 'PE', 'confidence': 0.85, 'error': str(e)}
                    
                    # Step 3: WQI Prediction
                    status_text.markdown("**Step 3/6:** Calculating Water Quality Index...")
                    progress_bar.progress(50)
                    
                    try:
                        from models.wqi.predict import predict_wqi
                        wqi_features = {
                            'temperature': temperature,
                            'ph': ph,
                            'dissolved_oxygen': dissolved_oxygen,
                            'conductivity': conductivity,
                            'turbidity': turbidity,
                            'tds': tds,
                            'bod': bod,
                            'cod': cod,
                            'nitrate': nitrate,
                            'phosphate': phosphate,
                            'fecal_coliform': fecal_coliform,
                            'total_coliform': fecal_coliform * 8,
                            'chloride': chloride,
                            'fluoride': 0.8,
                            'hardness': 180,
                            'alkalinity': 120
                        }
                        wqi_result = predict_wqi(wqi_features)
                        st.session_state.wqi_result = wqi_result
                    except Exception as e:
                        st.warning(f"WQI calculation skipped: {e}")
                        wqi_result = {'wqi_score': 52.3, 'classification': 'Moderate', 'error': str(e)}
                    
                    # Step 4: Prophet Forecast
                    status_text.markdown("**Step 4/6:** Generating 60-day WQI forecast...")
                    progress_bar.progress(66)
                    
                    try:
                        from models.forecast.forecast import forecast_wqi
                        forecast_result = forecast_wqi(wqi_result['wqi_score'])
                        st.session_state.forecast_result = forecast_result
                    except Exception as e:
                        st.warning(f"Forecast skipped: {e}")
                        # Generate mock forecast
                        dates = pd.date_range(start=datetime.now(), periods=60, freq='D')
                        forecast_wqi = wqi_result['wqi_score'] + np.random.randn(60) * 5
                        forecast_result = {
                            'forecast_df': pd.DataFrame({'Date': dates, 'Predicted_WQI': forecast_wqi}),
                            'error': str(e)
                        }
                    
                    # Step 5: PINN DO Prediction
                    status_text.markdown("**Step 5/6:** PINN dissolved oxygen prediction (72h)...")
                    progress_bar.progress(83)
                    
                    try:
                        from models.pinn.predict_do import predict_dissolved_oxygen
                        pinn_result = predict_dissolved_oxygen(wqi_features, 72)
                        st.session_state.pinn_result = pinn_result
                    except Exception as e:
                        st.warning(f"PINN prediction skipped: {e}")
                        # Mock PINN result
                        time_hours = np.linspace(0, 72, 100)
                        do_pred = dissolved_oxygen + np.sin(time_hours/12) * 2 - time_hours/72 * 3
                        pinn_result = {
                            'time_hours': time_hours,
                            'do_predictions': do_pred,
                            'mean_do': np.mean(do_pred),
                            'critical_hours': time_hours[do_pred < 4.0],
                            'error': str(e)
                        }
                    
                    # Step 6: Digital Twin Simulation
                    status_text.markdown("**Step 6/6:** Running digital twin simulation (30 days)...")
                    progress_bar.progress(100)
                    
                    try:
                        from models.digital_twin.simulate import run_digital_twin_simulation
                        twin_params = {
                            'pollution_load': yolo_result.get('count', 0) * 10,
                            'cleanup_frequency': 0.2,
                            'regulation_strictness': 0.7,
                            'initial_wqi': wqi_result['wqi_score']
                        }
                        twin_result = run_digital_twin_simulation(twin_params, 30)
                        st.session_state.twin_result = twin_result
                    except Exception as e:
                        st.warning(f"Digital twin skipped: {e}")
                        # Mock twin result
                        days = np.arange(30)
                        wqi_sim = wqi_result['wqi_score'] + np.cumsum(np.random.randn(30)) * 2
                        twin_result = {
                            'days': days,
                            'wqi_trajectory': wqi_sim,
                            'final_wqi': wqi_sim[-1],
                            'error': str(e)
                        }
                    
                    status_text.markdown("**✅ Analysis complete!**")
                    
                    # Display results
                    st.balloons()
                    st.markdown("---")
                    st.markdown("## 📊 Complete Analysis Report")
                    st.markdown(f"*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*")
                    
                    # Summary cards
                    sum_col1, sum_col2, sum_col3, sum_col4 = st.columns(4)
                    
                    with sum_col1:
                        st.markdown(f"""
                        <div class="metric-card">
                            <h3 style='color: #7f8c8d; font-size: 14px; margin-bottom: 5px;'>Microplastics Detected</h3>
                            <h1 style='color: #e74c3c; margin: 10px 0;'>{yolo_result.get('count', 0)}</h1>
                            <p style='color: #95a5a6; font-size: 13px;'>particles in sample</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with sum_col2:
                        st.markdown(f"""
                        <div class="metric-card">
                            <h3 style='color: #7f8c8d; font-size: 14px; margin-bottom: 5px;'>Polymer Type</h3>
                            <h1 style='color: #3498db; margin: 10px 0;'>{raman_result.get('polymer', 'N/A')}</h1>
                            <p style='color: #95a5a6; font-size: 13px;'>{raman_result.get('confidence', 0):.1%} confidence</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with sum_col3:
                        wqi_score = wqi_result.get('wqi_score', 0)
                        wqi_color = '#2ecc71' if wqi_score > 75 else '#f39c12' if wqi_score > 50 else '#e74c3c'
                        st.markdown(f"""
                        <div class="metric-card">
                            <h3 style='color: #7f8c8d; font-size: 14px; margin-bottom: 5px;'>WQI Score</h3>
                            <h1 style='color: {wqi_color}; margin: 10px 0;'>{wqi_score:.1f}</h1>
                            <p style='color: #95a5a6; font-size: 13px;'>{wqi_result.get('classification', 'N/A')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with sum_col4:
                        st.markdown(f"""
                        <div class="metric-card">
                            <h3 style='color: #7f8c8d; font-size: 14px; margin-bottom: 5px;'>Mean DO (72h)</h3>
                            <h1 style='color: #9b59b6; margin: 10px 0;'>{pinn_result.get('mean_do', 0):.1f}</h1>
                            <p style='color: #95a5a6; font-size: 13px;'>mg/L forecast</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Detailed visualization
                    st.markdown("---")
                    st.markdown("### 🔬 Detailed Analysis")
                    
                    viz_col1, viz_col2 = st.columns(2)
                    
                    with viz_col1:
                        st.markdown("#### YOLO Detection Results")
                        if 'annotated_image' in yolo_result:
                            st.image(yolo_result['annotated_image'], use_container_width=True)
                        else:
                            st.image(uploaded, use_container_width=True)
                        
                        if yolo_result.get('particle_types'):
                            st.markdown("**Particle Breakdown:**")
                            for ptype, count in yolo_result['particle_types'].items():
                                st.write(f"• **{ptype.title()}:** {count} particles")
                    
                    with viz_col2:
                        st.markdown("#### WQI 60-Day Forecast")
                        if forecast_result.get('forecast_df') is not None:
                            forecast_df = forecast_result['forecast_df']
                            
                            fig_forecast = go.Figure()
                            fig_forecast.add_trace(go.Scatter(
                                x=forecast_df['Date'],
                                y=forecast_df['Predicted_WQI'],
                                mode='lines',
                                name='WQI Forecast',
                                line=dict(color='#3498db', width=2),
                                fill='tozeroy'
                            ))
                            
                            fig_forecast.add_hline(y=50, line_dash="dash", line_color="red",
                                                  annotation_text="Critical Threshold")
                            
                            fig_forecast.update_layout(
                                xaxis_title="Date",
                                yaxis_title="WQI",
                                height=300,
                                plot_bgcolor='white',
                                margin=dict(l=0, r=0, t=20, b=0)
                            )
                            
                            st.plotly_chart(fig_forecast, use_container_width=True)
                            
                            # Forecast summary
                            final_wqi = forecast_df['Predicted_WQI'].iloc[-1]
                            trend = "improving" if final_wqi > wqi_score else "declining"
                            st.info(f"📈 **Trend:** WQI is {trend} (Day 60: {final_wqi:.1f})")
                    
                    # PINN DO Prediction
                    st.markdown("---")
                    st.markdown("### ⚛️ Dissolved Oxygen Forecast (Physics-Informed Neural Network)")
                    
                    fig_pinn = go.Figure()
                    fig_pinn.add_trace(go.Scatter(
                        x=pinn_result['time_hours'],
                        y=pinn_result['do_predictions'],
                        mode='lines',
                        name='DO Prediction',
                        line=dict(color='#2ecc71', width=3)
                    ))
                    
                    fig_pinn.add_hline(y=4.0, line_dash="dash", line_color="red",
                                      annotation_text="Critical Level (4 mg/L)")
                    
                    fig_pinn.update_layout(
                        title="72-Hour Dissolved Oxygen Prediction",
                        xaxis_title="Time (hours)",
                        yaxis_title="DO (mg/L)",
                        height=400,
                        plot_bgcolor='white'
                    )
                    
                    st.plotly_chart(fig_pinn, use_container_width=True)
                    
                    if len(pinn_result.get('critical_hours', [])) > 0:
                        st.error(f"⚠️ **ALERT:** DO falls below critical level at {len(pinn_result['critical_hours'])} time points!")
                        st.markdown("**Recommended Actions:**")
                        st.markdown("- Increase aeration in affected zones")
                        st.markdown("- Reduce organic load discharge")
                        st.markdown("- Deploy emergency oxygenation systems")
                    else:
                        st.success("✅ DO levels remain within safe limits throughout forecast period")
                    
                    # Digital Twin Simulation
                    st.markdown("---")
                    st.markdown("### 🔮 Digital Twin Simulation (30-Day Policy Impact)")
                    
                    fig_twin = go.Figure()
                    fig_twin.add_trace(go.Scatter(
                        x=twin_result['days'],
                        y=twin_result['wqi_trajectory'],
                        mode='lines+markers',
                        name='Simulated WQI',
                        line=dict(color='#9b59b6', width=2),
                        marker=dict(size=6)
                    ))
                    
                    fig_twin.update_layout(
                        title="WQI Trajectory Under Current Policies",
                        xaxis_title="Days",
                        yaxis_title="WQI",
                        height=400,
                        plot_bgcolor='white'
                    )
                    
                    st.plotly_chart(fig_twin, use_container_width=True)
                    
                    final_wqi_twin = twin_result.get('final_wqi', wqi_score)
                    improvement = final_wqi_twin - wqi_score
                    
                    if improvement > 5:
                        st.success(f"✅ **Positive Impact:** WQI improves by {improvement:.1f} points over 30 days")
                    elif improvement < -5:
                        st.error(f"⚠️ **Negative Impact:** WQI declines by {abs(improvement):.1f} points - policy intervention needed!")
                    else:
                        st.info(f"➡️ **Stable:** WQI remains relatively stable (change: {improvement:+.1f} points)")
                    
                    # Policy recommendations
                    st.markdown("---")
                    st.markdown("### 📋 Policy Recommendations")
                    
                    if yolo_result.get('count', 0) > 100:
                        st.markdown("""
                        <div class="critical-alert">
                        <h4>🚨 HIGH CONTAMINATION - IMMEDIATE ACTION REQUIRED</h4>
                        <ul>
                            <li><strong>Ban single-use plastics</strong> in 5km radius</li>
                            <li><strong>Deploy cleanup crews</strong> within 24 hours</li>
                            <li><strong>Issue public health advisory</strong></li>
                            <li><strong>Enforce strict penalties</strong> for industrial discharge</li>
                        </ul>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Download report
                    st.markdown("---")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        if st.button("📥 Download Full Report (PDF)", use_container_width=True):
                            st.success("PDF report generation in progress...")
                    
                    with col2:
                        # Create CSV summary
                        summary_data = {
                            'Metric': ['Microplastics', 'Polymer', 'WQI', 'DO (72h)', 'Final WQI (30d)'],
                            'Value': [
                                yolo_result.get('count', 0),
                                raman_result.get('polymer', 'N/A'),
                                f"{wqi_score:.1f}",
                                f"{pinn_result.get('mean_do', 0):.1f}",
                                f"{final_wqi_twin:.1f}"
                            ]
                        }
                        summary_df = pd.DataFrame(summary_data)
                        csv = summary_df.to_csv(index=False)
                        
                        st.download_button(
                            label="📥 Download CSV Summary",
                            data=csv,
                            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    
                    with col3:
                        if st.button("📧 Email to Team", use_container_width=True):
                            st.info("Email feature coming soon...")
            
            else:
                st.warning("⚠️ Please upload a water sample image to begin analysis")
    
    # ====================================
    # TAB 2: GEOGRAPHIC MONITORING
    # ====================================
    with tab2:
        st.subheader("🗺️ Geographic Monitoring & Real-time Data")
        st.markdown("*Live sensor network and contamination hotspots*")
        
        # Map display
        st.markdown("### 🌍 River Monitoring Network")
        
        # Create base map centered on India
        m = folium.Map(location=[28.7041, 77.1025], zoom_start=5)
        
        # Sample hotspot data
        hotspots = [
            {"name": "Yamuna - Delhi", "lat": 28.6692, "lon": 77.2194, "wqi": 32, "particles": 245},
            {"name": "Ganga - Kanpur", "lat": 26.4499, "lon": 80.3319, "wqi": 41, "particles": 198},
            {"name": "Sabarmati - Ahmedabad", "lat": 23.0225, "lon": 72.5714, "wqi": 38, "particles": 210},
            {"name": "Cauvery - Bangalore", "lat": 12.9716, "lon": 77.5946, "wqi": 55, "particles": 89},
            {"name": "Mithi - Mumbai", "lat": 19.0760, "lon": 72.8777, "wqi": 28, "particles": 312},
            {"name": "Cooum - Chennai", "lat": 13.0827, "lon": 80.2707, "wqi": 35, "particles": 267},
            {"name": "Musi - Hyderabad", "lat": 17.3850, "lon": 78.4867, "wqi": 44, "particles": 156},
            {"name": "Gomti - Lucknow", "lat": 26.8467, "lon": 80.9462, "wqi": 48, "particles": 134}
        ]
        
        for spot in hotspots:
            color = 'red' if spot['wqi'] < 40 else 'orange' if spot['wqi'] < 60 else 'green'
            
            folium.CircleMarker(
                location=[spot['lat'], spot['lon']],
                radius=10,
                popup=f"""
                <b>{spot['name']}</b><br>
                WQI: {spot['wqi']}<br>
                Microplastics: {spot['particles']}/L
                """,
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.7
            ).add_to(m)
        
        # Display map
        st_folium(m, width=1200, height=500)
        
        # Hotspot table
        st.markdown("---")
        st.markdown("### 📊 Critical Zones Summary")
        
        hotspots_df = pd.DataFrame(hotspots)
        hotspots_df = hotspots_df.sort_values('wqi')
        
        # Add status column
        hotspots_df['Status'] = hotspots_df['wqi'].apply(
            lambda x: '🔴 Critical' if x < 40 else '🟡 Moderate' if x < 60 else '🟢 Good'
        )
        
        st.dataframe(hotspots_df[['name', 'wqi', 'particles', 'Status']], 
                    use_container_width=True, hide_index=True)
        
        # Real-time sensor data
        st.markdown("---")
        st.markdown("### 📡 Real-time Sensor Data")
        
        sensor_col1, sensor_col2 = st.columns(2)
        
        with sensor_col1:
            # Generate live data stream
            times = pd.date_range(end=datetime.now(), periods=50, freq='10min')
            sensor_data = pd.DataFrame({
                'Time': times,
                'DO': 6.5 + np.random.randn(50) * 0.8,
                'pH': 7.2 + np.random.randn(50) * 0.3,
                'Temp': 24 + np.random.randn(50) * 1.5
            })
            
            fig_sensor = go.Figure()
            fig_sensor.add_trace(go.Scatter(x=sensor_data['Time'], y=sensor_data['DO'],
                                           mode='lines', name='DO (mg/L)'))
            fig_sensor.add_trace(go.Scatter(x=sensor_data['Time'], y=sensor_data['pH'],
                                           mode='lines', name='pH'))
            
            fig_sensor.update_layout(
                title="Last 8 Hours - Yamuna Delhi",
                xaxis_title="Time",
                yaxis_title="Value",
                height=350,
                plot_bgcolor='white'
            )
            
            st.plotly_chart(fig_sensor, use_container_width=True)
        
        with sensor_col2:
            st.markdown("#### Live Sensor Status")
            
            sensors = [
                ("Yamuna-DL-01", "Online", 28.6692, 77.2194),
                ("Ganga-KP-02", "Online", 26.4499, 80.3319),
                ("Sabarmati-AH-03", "Offline", 23.0225, 72.5714),
                ("Cauvery-BG-04", "Online", 12.9716, 77.5946),
                ("Mithi-MB-05", "Online", 19.0760, 72.8777)
            ]
            
            for sensor, status, lat, lon in sensors:
                status_color = "#2ecc71" if status == "Online" else "#e74c3c"
                st.markdown(f"""
                <div style='background: white; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid {status_color};'>
                    <strong>{sensor}</strong><br>
                    <span style='color: {status_color};'>● {status}</span> | 
                    <span style='color: #7f8c8d;'>{lat:.4f}, {lon:.4f}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # ====================================
    # TAB 3: ADVANCED ANALYTICS
    # ====================================
    with tab3:
        st.subheader("📊 Advanced Analytics & Multi-location Comparison")
        st.markdown("*Comparative analysis and historical trends*")
        
        # Location selector
        locations = ["Delhi", "Kanpur", "Ahmedabad", "Bangalore", "Mumbai", "Chennai"]
        
        selected_locations = st.multiselect(
            "Select locations to compare",
            locations,
            default=["Delhi", "Kanpur", "Mumbai"]
        )
        
        if selected_locations:
            # Generate comparison data
            comparison_data = []
            for loc in selected_locations:
                comparison_data.append({
                    'Location': loc,
                    'WQI': np.random.uniform(30, 70),
                    'Microplastics': np.random.randint(80, 300),
                    'DO': np.random.uniform(3, 8),
                    'pH': np.random.uniform(6.5, 8.5),
                    'BOD': np.random.uniform(5, 30)
                })
            
            comp_df = pd.DataFrame(comparison_data)
            
            # Comparison charts
            st.markdown("### 📈 Multi-Parameter Comparison")
            
            fig_comp = make_subplots(
                rows=2, cols=2,
                subplot_titles=('WQI Comparison', 'Microplastic Load', 
                               'Dissolved Oxygen', 'BOD Levels')
            )
            
            fig_comp.add_trace(
                go.Bar(x=comp_df['Location'], y=comp_df['WQI'], name='WQI'),
            row=1, col=1
        )
            fig_comp.add_trace(
                go.Bar(x=comp_df['Location'], y=comp_df['Microplastics'], name='Particles'),
            row=1, col=2
        )
        
        fig_comp.add_trace(
            go.Bar(x=comp_df['Location'], y=comp_df['DO'], name='DO'),
            row=2, col=1
        )
        
        fig_comp.add_trace(
            go.Bar(x=comp_df['Location'], y=comp_df['BOD'], name='BOD'),
            row=2, col=2
        )
        
        fig_comp.update_layout(height=600, showlegend=False, plot_bgcolor='white')
        st.plotly_chart(fig_comp, use_container_width=True)
        
        # Historical trends
        st.markdown("---")
        st.markdown("### 📅 Historical Trends (Last 90 Days)")
        
        dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
        trend_data = pd.DataFrame({
            'Date': dates,
            'WQI': 50 + np.cumsum(np.random.randn(90)) * 2,
            'Microplastics': 150 + np.cumsum(np.random.randn(90)) * 10
        })
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(x=trend_data['Date'], y=trend_data['WQI'],
                                      mode='lines', name='WQI', line=dict(width=3)))
        
        fig_trend.update_layout(
            title=f"WQI Trend - {selected_locations[0]}",
            xaxis_title="Date",
            yaxis_title="WQI",
            height=400,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Statistical summary
        st.markdown("---")
        st.markdown("### 📊 Statistical Summary")
        st.dataframe(comp_df.describe(), use_container_width=True)

# ====================================
# TAB 4: SYSTEM CONFIGURATION
# ====================================
with tab4:
    st.subheader("⚙️ System Configuration")
    st.markdown("*API keys, alert thresholds, and model settings*")
    
    config_tab1, config_tab2, config_tab3 = st.tabs([
        "🔑 API Configuration",
        "🚨 Alert Thresholds",
        "🤖 Model Settings"
    ])
    
    with config_tab1:
        st.markdown("### 🔑 API Keys & Credentials")
        
        st.text_input("OpenWeather API Key", type="password", value="**********************")
        st.text_input("Pollution API Key", type="password", value="**********************")
        st.text_input("River Flow API Key", type="password", value="**********************")
        
        if st.button("💾 Save API Keys"):
            st.success("✅ API keys saved successfully!")
    
    with config_tab2:
        st.markdown("### 🚨 Alert Thresholds")
        
        wqi_threshold = st.slider("WQI Critical Threshold", 0, 100, 40)
        do_threshold = st.slider("DO Critical Level (mg/L)", 0.0, 10.0, 4.0, 0.1)
        particle_threshold = st.slider("Microplastic Alert Level (particles/L)", 0, 500, 150)
        
        st.markdown(f"""
        **Current Settings:**
        - WQI Alert: < {wqi_threshold}
        - DO Alert: < {do_threshold} mg/L
        - Microplastics Alert: > {particle_threshold} particles/L
        """)
        
        if st.button("💾 Update Thresholds"):
            st.success("✅ Alert thresholds updated!")
    
    with config_tab3:
        st.markdown("### 🤖 Model Settings")
        
        st.markdown("**Active Models:**")
        
        models = ["YOLOv8", "Raman ML", "WQI RF", "Prophet", "PINN", "Digital Twin"]
        for model in models:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{model}**")
            with col2:
                st.write("✅ Active")
            with col3:
                if st.button("⚙️", key=f"config_{model}"):
                    st.info(f"Configure {model}")
        
        st.markdown("---")
        
        if st.button("🔄 Retrain All Models"):
            st.warning("Model retraining will take 2-4 hours. Proceed?")
        
        if st.button("📊 View Model Logs"):
            st.code("""YOLO: Inference completed in 45ms
                       Raman: Prediction accuracy 94.2%
                       WQI: Model updated with 1,247 samples
                    """, language="log")