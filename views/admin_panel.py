"""
ADMIN PANEL - System Management and Configuration
User management, Model monitoring, System logs, Settings
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

def show_admin_panel():
    # Simple authentication
    if 'admin_authenticated' not in st.session_state:
        st.session_state.admin_authenticated = False
    
    if not st.session_state.admin_authenticated:
        show_login_screen()
        return
    
    # Admin dashboard
    st.title("⚙️ System Administration Panel")
    st.markdown("*Complete system control and monitoring*")
    
    # System health overview
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("System Uptime", "99.7%", "✅")
    with col2:
        st.metric("Active Users", "1,247", "+89")
    with col3:
        st.metric("API Calls Today", "8,942", "+1.2K")
    with col4:
        st.metric("Storage Used", "45.2 GB", "+2.3 GB")
    with col5:
        st.metric("Model Accuracy", "94.2%", "+0.8%")
    
    st.markdown("---")
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "👥 User Management",
        "🤖 Model Monitoring",
        "📊 System Analytics",
        "📝 Logs & Audit",
        "⚙️ Configuration",
        "🔔 Alerts & Notifications"
    ])
    
    # ====================================
    # TAB 1: USER MANAGEMENT
    # ====================================
    with tab1:
        st.subheader("👥 User Management")
        st.markdown("*Manage user accounts, roles, and permissions*")
        
        # User statistics
        user_col1, user_col2, user_col3, user_col4 = st.columns(4)
        
        with user_col1:
            st.metric("Total Users", "1,247")
        with user_col2:
            st.metric("Active Today", "342")
        with user_col3:
            st.metric("Public Users", "1,089")
        with user_col4:
            st.metric("Gov/Research", "158")
        
        st.markdown("---")
        
        # User table
        st.markdown("### 📋 User Database")
        
        users_data = pd.DataFrame({
            'ID': [f'U{1000+i}' for i in range(10)],
            'Username': [f'user{i}@example.com' for i in range(10)],
            'Role': np.random.choice(['Public', 'Government', 'Researcher', 'Admin'], 10),
            'Status': np.random.choice(['Active', 'Inactive'], 10, p=[0.9, 0.1]),
            'Last Login': [(datetime.now() - timedelta(days=np.random.randint(0, 30))).strftime('%Y-%m-%d') for _ in range(10)],
            'Analyses': np.random.randint(5, 150, 10)
        })
        
        # Filters
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            role_filter = st.selectbox("Filter by Role", ['All', 'Public', 'Government', 'Researcher', 'Admin'])
        with filter_col2:
            status_filter = st.selectbox("Filter by Status", ['All', 'Active', 'Inactive'])
        
        # Apply filters
        filtered_users = users_data.copy()
        if role_filter != 'All':
            filtered_users = filtered_users[filtered_users['Role'] == role_filter]
        if status_filter != 'All':
            filtered_users = filtered_users[filtered_users['Status'] == status_filter]
        
        st.dataframe(filtered_users, use_container_width=True, hide_index=True)
        
        # User actions
        st.markdown("---")
        st.markdown("### ⚡ Quick Actions")
        
        action_col1, action_col2, action_col3, action_col4 = st.columns(4)
        
        with action_col1:
            if st.button("➕ Add New User", use_container_width=True):
                st.info("User creation form would open here")
        
        with action_col2:
            if st.button("📧 Send Notification", use_container_width=True):
                st.info("Bulk notification form would open here")
        
        with action_col3:
            if st.button("🔒 Suspend User", use_container_width=True):
                st.warning("Select user to suspend")
        
        with action_col4:
            if st.button("📊 Export Users", use_container_width=True):
                csv = filtered_users.to_csv(index=False)
                st.download_button(
                    "Download CSV",
                    csv,
                    "users_export.csv",
                    "text/csv",
                    use_container_width=True
                )
        
        # User growth chart
        st.markdown("---")
        st.markdown("### 📈 User Growth Trend")
        
        dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
        user_growth = pd.DataFrame({
            'Date': dates,
            'New Users': np.random.poisson(15, 90),
            'Active Users': 500 + np.cumsum(np.random.randint(0, 20, 90))
        })
        
        fig_growth = go.Figure()
        fig_growth.add_trace(go.Scatter(x=user_growth['Date'], y=user_growth['Active Users'],
                                       mode='lines', name='Active Users', line=dict(width=3)))
        fig_growth.add_trace(go.Bar(x=user_growth['Date'], y=user_growth['New Users'],
                                    name='New Registrations', opacity=0.5))
        
        fig_growth.update_layout(
            title="User Growth (Last 90 Days)",
            xaxis_title="Date",
            yaxis_title="Count",
            height=400,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # ====================================
    # TAB 2: MODEL MONITORING
    # ====================================
    with tab2:
        st.subheader("🤖 Model Performance Monitoring")
        st.markdown("*Real-time model health and performance metrics*")
        
        # Model status cards
        models = [
            {"name": "YOLOv8 Detection", "status": "Online", "accuracy": 94.7, "latency": 45, "calls": 2341},
            {"name": "Raman ML", "status": "Online", "accuracy": 92.3, "latency": 12, "calls": 1842},
            {"name": "WQI Random Forest", "status": "Online", "accuracy": 89.1, "latency": 8, "calls": 3156},
            {"name": "Prophet Forecast", "status": "Online", "accuracy": 85.6, "latency": 150, "calls": 892},
            {"name": "PINN", "status": "Warning", "accuracy": 91.2, "latency": 85, "calls": 1234},
            {"name": "Digital Twin", "status": "Online", "accuracy": 88.7, "latency": 120, "calls": 756}
        ]
        
        for i in range(0, len(models), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(models):
                    model = models[i + j]
                    with col:
                        status_color = "#2ecc71" if model['status'] == "Online" else "#f39c12"
                        st.markdown(f"""
                        <div class="metric-card">
                            <h4>{model['name']}</h4>
                            <p style='color: {status_color}; font-weight: 600;'>● {model['status']}</p>
                            <div style='margin-top: 15px;'>
                                <p><strong>Accuracy:</strong> {model['accuracy']}%</p>
                                <p><strong>Latency:</strong> {model['latency']}ms</p>
                                <p><strong>API Calls:</strong> {model['calls']}</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Model performance comparison
        st.markdown("### 📊 Performance Comparison")
        
        model_df = pd.DataFrame(models)
        
        fig_models = go.Figure()
        
        fig_models.add_trace(go.Bar(
            name='Accuracy',
            x=model_df['name'],
            y=model_df['accuracy'],
            marker_color='#3498db'
        ))
        
        fig_models.update_layout(
            title="Model Accuracy Comparison",
            xaxis_title="Model",
            yaxis_title="Accuracy (%)",
            height=400,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_models, use_container_width=True)
        
        # Model retraining
        st.markdown("---")
        st.markdown("### 🔄 Model Retraining")
        
        retrain_col1, retrain_col2 = st.columns(2)
        
        with retrain_col1:
            selected_model = st.selectbox("Select Model to Retrain", [m['name'] for m in models])
            
            st.markdown("**Training Settings:**")
            epochs = st.slider("Epochs", 10, 200, 50)
            batch_size = st.selectbox("Batch Size", [16, 32, 64, 128])
            learning_rate = st.select_slider("Learning Rate", options=[0.0001, 0.001, 0.01, 0.1])
        
        with retrain_col2:
            st.markdown("**Last Training:**")
            st.info(f"""
            - Date: 2024-12-20
            - Duration: 3.2 hours
            - Final Accuracy: 94.7%
            - Dataset Size: 12,456 samples
            """)
            
            if st.button("🚀 Start Retraining", type="primary", use_container_width=True):
                with st.spinner(f"Retraining {selected_model}..."):
                    progress = st.progress(0)
                    for i in range(100):
                        progress.progress(i + 1)
                    st.success(f"✅ {selected_model} retrained successfully!")
    
    # ====================================
    # TAB 3: SYSTEM ANALYTICS
    # ====================================
    with tab3:
        st.subheader("📊 System Analytics Dashboard")
        st.markdown("*Comprehensive system usage and performance analytics*")
        
        # Time range selector
        time_range = st.selectbox("Time Range", ["Last 24 Hours", "Last 7 Days", "Last 30 Days", "Last 90 Days"])
        
        # API usage statistics
        st.markdown("### 🔌 API Usage Statistics")
        
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        api_data = pd.DataFrame({
            'Date': dates,
            'YOLO': np.random.poisson(300, 30),
            'Raman': np.random.poisson(200, 30),
            'WQI': np.random.poisson(400, 30),
            'Prophet': np.random.poisson(100, 30),
            'PINN': np.random.poisson(150, 30),
            'Digital Twin': np.random.poisson(80, 30)
        })
        
        fig_api = go.Figure()
        
        for col in ['YOLO', 'Raman', 'WQI', 'Prophet', 'PINN', 'Digital Twin']:
            fig_api.add_trace(go.Scatter(
                x=api_data['Date'],
                y=api_data[col],
                mode='lines',
                name=col,
                stackgroup='one'
            ))
        
        fig_api.update_layout(
            title="API Calls by Model (Last 30 Days)",
            xaxis_title="Date",
            yaxis_title="API Calls",
            height=400,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_api, use_container_width=True)
        
        # Geographic distribution
        st.markdown("---")
        st.markdown("### 🌍 Geographic Distribution")
        
        geo_col1, geo_col2 = st.columns(2)
        
        with geo_col1:
            geo_data = pd.DataFrame({
                'State': ['Delhi', 'Maharashtra', 'Karnataka', 'Tamil Nadu', 'Gujarat', 'West Bengal'],
                'Users': [342, 289, 198, 156, 134, 128]
            })
            
            fig_geo = px.bar(geo_data, x='State', y='Users', title="Users by State")
            fig_geo.update_layout(plot_bgcolor='white', height=350)
            st.plotly_chart(fig_geo, use_container_width=True)
        
        with geo_col2:
            fig_pie = px.pie(geo_data, values='Users', names='State', title="User Distribution")
            fig_pie.update_layout(height=350)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        # System resources
        st.markdown("---")
        st.markdown("### 💻 System Resources")
        
        res_col1, res_col2, res_col3, res_col4 = st.columns(4)
        
        with res_col1:
            st.metric("CPU Usage", "42%", "Normal")
        with res_col2:
            st.metric("Memory", "8.2/16 GB", "52%")
        with res_col3:
            st.metric("GPU Usage", "67%", "High")
        with res_col4:
            st.metric("Network", "125 Mbps", "Active")
    
    # ====================================
    # TAB 4: LOGS & AUDIT
    # ====================================
    with tab4:
        st.subheader("📝 System Logs & Audit Trail")
        st.markdown("*Monitor system activities and security events*")
        
        # Log filters
        log_col1, log_col2, log_col3 = st.columns(3)
        
        with log_col1:
            log_level = st.selectbox("Log Level", ["All", "INFO", "WARNING", "ERROR", "CRITICAL"])
        with log_col2:
            log_source = st.selectbox("Source", ["All", "API", "Models", "Authentication", "Database"])
        with log_col3:
            log_time = st.selectbox("Time", ["Last Hour", "Last 24 Hours", "Last 7 Days"])
        
        # Generate sample logs
        st.markdown("---")
        st.markdown("### 📋 Recent Logs")
        
        log_types = ["INFO", "WARNING", "ERROR", "INFO", "INFO"]
        log_messages = [
            "YOLO model inference completed successfully",
            "High API rate detected from IP 192.168.1.100",
            "Database connection timeout - retrying",
            "New user registered: user123@example.com",
            "Model retrained: WQI Random Forest"
        ]
        
        for i, (log_type, message) in enumerate(zip(log_types, log_messages)):
            color = {"INFO": "#3498db", "WARNING": "#f39c12", "ERROR": "#e74c3c"}[log_type]
            timestamp = (datetime.now() - timedelta(minutes=i*15)).strftime('%Y-%m-%d %H:%M:%S')
            
            st.markdown(f"""
            <div style='background: white; padding: 12px; margin: 8px 0; border-left: 4px solid {color}; border-radius: 4px;'>
                <span style='color: {color}; font-weight: 600;'>[{log_type}]</span>
                <span style='color: #7f8c8d; margin-left: 10px;'>{timestamp}</span>
                <p style='margin: 8px 0 0 0; color: #2c3e50;'>{message}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Security events
        st.markdown("---")
        st.markdown("### 🔒 Security Events")
        
        security_events = pd.DataFrame({
            'Timestamp': [(datetime.now() - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M') for i in range(5)],
            'Event': ['Failed login attempt', 'Password reset', 'Admin access', 'API key generated', 'User suspended'],
            'User': ['user123', 'user456', 'admin', 'user789', 'user321'],
            'IP Address': ['192.168.1.' + str(100+i) for i in range(5)],
            'Status': ['Blocked', 'Success', 'Success', 'Success', 'Success']
        })
        
        st.dataframe(security_events, use_container_width=True, hide_index=True)
    
    # ====================================
    # TAB 5: CONFIGURATION
    # ====================================
    with tab5:
        st.subheader("⚙️ System Configuration")
        st.markdown("*Configure system settings and parameters*")
        
        config_tab1, config_tab2, config_tab3 = st.tabs([
            "🔑 API Keys",
            "🚨 Thresholds",
            "📧 Notifications"
        ])
        
        with config_tab1:
            st.markdown("### 🔑 API Key Management")
            
            st.text_input("OpenWeather API Key", type="password", value="**********************")
            st.text_input("Pollution Data API Key", type="password", value="**********************")
            st.text_input("River Flow API Key", type="password", value="**********************")
            st.text_input("Email Service API Key", type="password", value="**********************")
            
            if st.button("💾 Save API Keys", use_container_width=True):
                st.success("✅ API keys saved successfully!")
        
        with config_tab2:
            st.markdown("### 🚨 Alert Thresholds")
            
            wqi_critical = st.slider("WQI Critical Threshold", 0, 100, 40)
            do_critical = st.slider("DO Critical Level (mg/L)", 0.0, 10.0, 4.0, 0.1)
            particle_high = st.slider("Microplastic High Alert", 0, 500, 150)
            particle_critical = st.slider("Microplastic Critical Alert", 0, 500, 250)
            
            if st.button("💾 Update Thresholds", use_container_width=True):
                st.success("✅ Thresholds updated!")
        
        with config_tab3:
            st.markdown("### 📧 Notification Settings")
            
            st.checkbox("Email notifications for critical alerts", value=True)
            st.checkbox("SMS notifications for system errors", value=True)
            st.checkbox("Slack integration for model updates", value=False)
            st.checkbox("Weekly summary reports", value=True)
            
            st.text_area("Email Recipients (comma-separated)", 
                        "admin@example.com, team@example.com")
            
            if st.button("💾 Save Notification Settings", use_container_width=True):
                st.success("✅ Settings saved!")
    
    # ====================================
    # TAB 6: ALERTS & NOTIFICATIONS
    # ====================================
    with tab6:
        st.subheader("🔔 Active Alerts & Notifications")
        st.markdown("*Monitor and manage system alerts*")
        
        # Active alerts
        alerts = [
            {"severity": "Critical", "message": "High contamination detected in Yamuna - Delhi", "time": "2 min ago"},
            {"severity": "Warning", "message": "Model accuracy dropped below 90% - PINN", "time": "15 min ago"},
            {"severity": "Info", "message": "Scheduled maintenance in 24 hours", "time": "1 hour ago"}
        ]
        
        for alert in alerts:
            color = {"Critical": "#e74c3c", "Warning": "#f39c12", "Info": "#3498db"}[alert['severity']]
            st.markdown(f"""
            <div style='background: white; padding: 20px; margin: 15px 0; border-left: 5px solid {color}; border-radius: 8px;'>
                <div style='display: flex; justify-content: space-between;'>
                    <h4 style='color: {color}; margin: 0;'>{alert['severity']}</h4>
                    <span style='color: #7f8c8d;'>{alert['time']}</span>
                </div>
                <p style='margin: 10px 0 0 0; color: #2c3e50;'>{alert['message']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Logout button
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.admin_authenticated = False
        st.rerun()


def show_login_screen():
    """Show admin login screen"""
    st.title("🔐 Admin Login")
    st.markdown("*System Administration Access*")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("🔓 Login", use_container_width=True)
        
        if submitted:
            # Simple authentication (replace with real auth in production)
            if username == "admin" and password == "admin123":
                st.session_state.admin_authenticated = True
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
    
    st.info("💡 **Demo Credentials:** Username: `admin`, Password: `admin123`")