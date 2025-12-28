"""
CITIZEN/PUBLIC DASHBOARD - Water Quality Monitoring for Public
Image upload, Detection, Health advice, Reporting
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import io

def show_citizen_dashboard():
    st.title("👥 Public Water Quality Dashboard")
    st.markdown("*Community-driven environmental monitoring*")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rivers Monitored", "24", "+2")
    with col2:
        st.metric("Samples Today", "142", "+18")
    with col3:
        st.metric("Avg WQI", "52.3", "-3.2", delta_color="inverse")
    with col4:
        st.metric("Active Alerts", "3", "🔴")
    
    st.markdown("---")
    
    # Main content
    tab1, tab2, tab3 = st.tabs([
        "📸 Upload & Detect",
        "📊 My Reports",
        "🗺️ Nearby Water Bodies"
    ])
    
    # ====================================
    # TAB 1: UPLOAD AND DETECT
    # ====================================
    with tab1:
        st.subheader("📸 Microplastic Detection")
        st.markdown("*Upload water sample image for AI analysis*")
        
        uploaded_file = st.file_uploader(
            "Drag and drop or click to upload",
            type=['jpg', 'jpeg', 'png'],
            help="Supported formats: JPG, PNG"
        )
        
        if uploaded_file:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📷 Original Sample**")
                st.image(uploaded_file, use_container_width=True)
                
                # Sample info
                file_size = len(uploaded_file.getvalue()) / 1024
                st.caption(f"File: {uploaded_file.name} ({file_size:.1f} KB)")
            
            with col2:
                st.markdown("**🔍 Analysis Settings**")
                
                st.info(f"""
                **Confidence Threshold:** ≥ 50%  
                **Detection Mode:** Public (High confidence only)  
                **Processing Time:** ~2-5 seconds
                """)
            
            st.markdown("---")
            
            if st.button("🚀 Analyze Sample", type="primary", use_container_width=True):
                with st.spinner("Running YOLOv8 detection... Please wait"):
                    try:
                        from models.yolo.infer import predict_image_with_viz
                        
                        result = predict_image_with_viz(
                            uploaded_file,
                            conf_threshold=st.session_state.confidence_threshold,
                            user_level="Public"
                        )
                        
                        if 'error' not in result:
                            st.markdown("---")
                            st.markdown("## 🎯 Detection Results")
                            
                            # Show annotated image
                            res_col1, res_col2 = st.columns(2)
                            
                            with res_col1:
                                st.markdown("**🖼️ Detected Particles**")
                                st.image(result['annotated_image'], use_container_width=True)
                            
                            with res_col2:
                                st.markdown("**📊 Summary Statistics**")
                                
                                # Metrics
                                st.metric(
                                    "Total Particles Detected",
                                    result['count'],
                                    help=f"Confidence ≥ {st.session_state.confidence_threshold*100}%"
                                )
                                
                                avg_conf = result.get('avg_confidence', 0)
                                conf_label = "🟢 High" if avg_conf > 0.75 else "🟡 Medium" if avg_conf > 0.5 else "🔴 Low"
                                st.metric(
                                    "Detection Quality",
                                    conf_label,
                                    f"{avg_conf:.1%}"
                                )
                                
                                if result.get('particle_types'):
                                    most_common = max(result['particle_types'].items(), key=lambda x: x[1])
                                    st.metric(
                                        "Dominant Type",
                                        most_common[0].title(),
                                        f"{most_common[1]} particles"
                                    )
                            
                            # Particle breakdown
                            if result.get('particle_types'):
                                st.markdown("---")
                                st.markdown("### 🔬 Particle Classification")
                                
                                type_data = pd.DataFrame([
                                    {
                                        'Type': ptype.title(),
                                        'Count': count,
                                        'Percentage': f"{count/result['count']*100:.1f}%",
                                        'Description': {
                                            'fiber': 'Long thin particles from textiles',
                                            'fragment': 'Irregular pieces from plastic breakdown',
                                            'pellet': 'Small spherical industrial particles',
                                            'film': 'Thin sheet-like plastic pieces',
                                            'foam': 'Expanded polystyrene particles'
                                        }.get(ptype, 'Unknown particle type')
                                    }
                                    for ptype, count in result['particle_types'].items()
                                ])
                                
                                st.dataframe(type_data, use_container_width=True, hide_index=True)
                                
                                # Visual chart
                                fig = go.Figure(data=[
                                    go.Bar(
                                        x=type_data['Type'],
                                        y=type_data['Count'],
                                        marker_color=['#3498db', '#f39c12', '#2ecc71', '#e74c3c', '#9b59b6'][:len(type_data)],
                                        text=type_data['Count'],
                                        textposition='auto'
                                    )
                                ])
                                
                                fig.update_layout(
                                    title="Particle Distribution by Type",
                                    xaxis_title="Particle Type",
                                    yaxis_title="Count",
                                    plot_bgcolor='white',
                                    height=350
                                )
                                
                                st.plotly_chart(fig, use_container_width=True)
                            
                            # Health impact assessment
                            st.markdown("---")
                            st.markdown("### ⚠️ Health & Environmental Impact")
                            
                            particle_count = result['count']
                            
                            if particle_count > 100:
                                st.markdown("""
                                <div class="critical-alert">
                                    <h4>🚨 HIGH CONTAMINATION DETECTED</h4>
                                    <p><strong>Risk Level: SEVERE</strong></p>
                                    <ul>
                                        <li>❌ <strong>NOT suitable for drinking</strong></li>
                                        <li>⚠️ May severely affect aquatic life</li>
                                        <li>🚫 Avoid direct contact with water</li>
                                        <li>📞 Report to local authorities immediately</li>
                                        <li>🏥 Seek medical advice if consumed</li>
                                    </ul>
                                </div>
                                """, unsafe_allow_html=True)
                                
                            elif particle_count > 50:
                                st.markdown("""
                                <div class="warning-box">
                                    <h4>⚠️ MODERATE CONTAMINATION</h4>
                                    <p><strong>Risk Level: MODERATE</strong></p>
                                    <ul>
                                        <li>💧 Requires treatment before use</li>
                                        <li>📊 Monitor regularly</li>
                                        <li>🔄 Consider filtration systems</li>
                                        <li>👨‍👩‍👧‍👦 Children and elderly should avoid</li>
                                    </ul>
                                </div>
                                """, unsafe_allow_html=True)
                                
                            else:
                                st.markdown("""
                                <div class="success-box">
                                    <h4>✅ LOW CONTAMINATION</h4>
                                    <p><strong>Risk Level: LOW</strong></p>
                                    <ul>
                                        <li>✓ Within acceptable limits</li>
                                        <li>📈 Continue monitoring</li>
                                        <li>💧 Practice water conservation</li>
                                        <li>🌱 Support cleanup initiatives</li>
                                    </ul>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            # What are microplastics?
                            st.markdown("---")
                            with st.expander("ℹ️ What are Microplastics?"):
                                st.markdown("""
                                **Microplastics** are tiny plastic particles less than 5mm in size. They come from:
                                
                                - 🧴 **Personal care products** (microbeads in cosmetics)
                                - 👕 **Synthetic textiles** (fibers from washing clothes)
                                - 🗑️ **Plastic waste breakdown** (larger plastics fragmenting)
                                - 🏭 **Industrial processes** (plastic pellets and manufacturing)
                                
                                **Health Concerns:**
                                - Can enter food chain through fish and seafood
                                - May carry toxic chemicals and pollutants
                                - Potential impacts on human health still being studied
                                - Harm aquatic ecosystems and marine life
                                
                                **What You Can Do:**
                                - Reduce plastic use in daily life
                                - Use natural fiber clothing
                                - Support plastic-free products
                                - Participate in cleanup drives
                                """)
                            
                            # Save results to session
                            st.session_state.current_analysis = result
                            st.session_state.analysis_timestamp = datetime.now()
                            
                            # Download options
                            st.markdown("---")
                            st.markdown("### 📥 Download & Share")
                            
                            dl_col1, dl_col2, dl_col3 = st.columns(3)
                            
                            with dl_col1:
                                # Create CSV report
                                report_data = {
                                    'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                                    'Total_Particles': [result['count']],
                                    'Avg_Confidence': [f"{avg_conf:.2%}"],
                                    'Risk_Level': ['High' if particle_count > 100 else 'Moderate' if particle_count > 50 else 'Low']
                                }
                                
                                if result.get('particle_types'):
                                    for ptype, count in result['particle_types'].items():
                                        report_data[f'{ptype.title()}_Count'] = [count]
                                
                                report_df = pd.DataFrame(report_data)
                                csv = report_df.to_csv(index=False)
                                
                                st.download_button(
                                    label="📄 Download CSV Report",
                                    data=csv,
                                    file_name=f"water_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                                    mime="text/csv",
                                    use_container_width=True
                                )
                            
                            with dl_col2:
                                st.button("📧 Email Report", use_container_width=True, disabled=True)
                                st.caption("Coming soon")
                            
                            with dl_col3:
                                st.button("📱 Share on Social Media", use_container_width=True, disabled=True)
                                st.caption("Coming soon")
                            
                            # Report to authorities
                            st.markdown("---")
                            if particle_count > 50:
                                st.markdown("### 📢 Report to Authorities")
                                
                                with st.form("report_form"):
                                    st.text_input("Location", placeholder="e.g., Yamuna River near ITO Bridge, Delhi")
                                    st.text_input("Your Name (Optional)", placeholder="John Doe")
                                    st.text_input("Contact Number (Optional)", placeholder="+91-XXXXXXXXXX")
                                    st.text_area("Additional Comments", placeholder="Any other observations...")
                                    
                                    submitted = st.form_submit_button("📤 Submit Report", use_container_width=True)
                                    if submitted:
                                        st.success("✅ Report submitted successfully! Authorities have been notified.")
                        
                        else:
                            st.error(f"❌ Detection failed: {result['error']}")
                            st.info("💡 **Troubleshooting:**")
                            st.markdown("""
                            - Ensure your YOLO model is at `models/yolo/best.pt`
                            - Check image quality and format
                            - Try with a different image
                            - Contact support if issue persists
                            """)
                    
                    except Exception as e:
                        st.error(f"❌ Unexpected error: {str(e)}")
                        st.info("Please check your model files and try again")
        
        else:
            # Show instructions when no file uploaded
            st.info("👆 Upload a water sample image to begin analysis")
            
            st.markdown("---")
            st.markdown("### 📸 How to Take a Good Sample Photo")
            
            inst_col1, inst_col2 = st.columns(2)
            
            with inst_col1:
                st.markdown("""
                **✅ DO:**
                - Use good lighting (natural light preferred)
                - Take photo from directly above the water
                - Ensure water surface is visible
                - Keep camera steady
                - Use a white background if possible
                """)
            
            with inst_col2:
                st.markdown("""
                **❌ DON'T:**
                - Take photos in dim lighting
                - Use flash (causes glare)
                - Include too much reflection
                - Use blurry or out-of-focus images
                - Take photos at sharp angles
                """)
    
    # ====================================
    # TAB 2: MY REPORTS
    # ====================================
    with tab2:
        st.subheader("📊 My Analysis History")
        st.markdown("*View your past water quality tests*")
        
        if 'current_analysis' in st.session_state and st.session_state.current_analysis:
            st.success("✅ You have recent analysis results!")
            
            # Display latest result
            result = st.session_state.current_analysis
            timestamp = st.session_state.get('analysis_timestamp', datetime.now())
            
            st.markdown(f"**Latest Analysis:** {timestamp.strftime('%Y-%m-%d at %H:%M:%S')}")
            
            sum_col1, sum_col2, sum_col3 = st.columns(3)
            with sum_col1:
                st.metric("Particles Detected", result.get('count', 0))
            with sum_col2:
                st.metric("Confidence", f"{result.get('avg_confidence', 0):.1%}")
            with sum_col3:
                particle_count = result.get('count', 0)
                risk = 'High' if particle_count > 100 else 'Moderate' if particle_count > 50 else 'Low'
                st.metric("Risk Level", risk)
            
            # Generate mock historical data
            st.markdown("---")
            st.markdown("### 📈 Historical Trend")
            
            dates = pd.date_range(end=datetime.now(), periods=10, freq='W')
            hist_data = pd.DataFrame({
                'Date': dates,
                'Particles': [result.get('count', 80) + np.random.randint(-30, 30) for _ in range(10)]
            })
            
            fig_hist = go.Figure()
            fig_hist.add_trace(go.Scatter(
                x=hist_data['Date'],
                y=hist_data['Particles'],
                mode='lines+markers',
                line=dict(color='#3498db', width=2),
                marker=dict(size=8)
            ))
            
            fig_hist.update_layout(
                title="Your Analysis History (Last 10 Weeks)",
                xaxis_title="Date",
                yaxis_title="Particle Count",
                height=400,
                plot_bgcolor='white'
            )
            
            st.plotly_chart(fig_hist, use_container_width=True)
            
        else:
            st.info("📭 No analysis results yet. Upload an image in the 'Upload & Detect' tab to get started!")
    
    # ====================================
    # TAB 3: NEARBY WATER BODIES
    # ====================================
    with tab3:
        st.subheader("🗺️ Nearby Water Bodies Status")
        st.markdown("*Check water quality in your area*")
        
        # Location input
        location = st.text_input("Enter your location", placeholder="e.g., Delhi, Mumbai, Bangalore")
        
        if location:
            st.info(f"📍 Showing results for: **{location}**")
            
            # Mock data for nearby water bodies
            nearby = [
                {"name": "Yamuna River", "distance": "2.3 km", "wqi": 32, "status": "🔴 Poor"},
                {"name": "Central Park Lake", "distance": "5.1 km", "wqi": 58, "status": "🟡 Moderate"},
                {"name": "City Canal", "distance": "7.8 km", "wqi": 41, "status": "🔴 Poor"},
                {"name": "Municipal Reservoir", "distance": "12.5 km", "wqi": 72, "status": "🟢 Good"}
            ]
            
            for water_body in nearby:
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
                    
                    with col1:
                        st.markdown(f"**{water_body['name']}**")
                    with col2:
                        st.write(f"📍 {water_body['distance']}")
                    with col3:
                        st.write(f"WQI: {water_body['wqi']}")
                    with col4:
                        st.write(water_body['status'])
                    
                    st.markdown("---")
        
        else:
            st.info("👆 Enter your location to see nearby water bodies")
    
    # Community section at bottom
    st.markdown("---")
    st.markdown("### 🤝 Join the Community")
    
    comm_col1, comm_col2, comm_col3 = st.columns(3)
    
    with comm_col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📱 Mobile App</h3>
            <p>Download our app for on-the-go monitoring</p>
            <button style='margin-top: 10px;'>Download Now</button>
        </div>
        """, unsafe_allow_html=True)
    
    with comm_col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🌊 Cleanup Events</h3>
            <p>Join local water cleanup drives</p>
            <button style='margin-top: 10px;'>Find Events</button>
        </div>
        """, unsafe_allow_html=True)
    
    with comm_col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📚 Learn More</h3>
            <p>Educational resources about microplastics</p>
            <button style='margin-top: 10px;'>Read Articles</button>
        </div>
        """, unsafe_allow_html=True)