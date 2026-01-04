
# Pravaah – Microplastic Detection System

🚀 Team Project | Competition Submission

This project was developed by a team of 3 members as part of a competition focused on microplastic detection using Machine Learning and data-driven pipelines.

🔗 Original Repository: https://github.com/Aadrika2106/Pravaah

## My Contributions
-Designed and implemented Digital Twin–based environmental simulation modules to model microplastic impact and water quality dynamics

-Developed and trained Physics-Informed Neural Networks (PINN) for dissolved oxygen prediction by embedding physical constraints into the learning process

-Implemented Explainable AI (XAI) components to interpret model predictions and visualize feature importance through the dashboard

-Trained, validated, and converted models for deployment-ready integration within the Streamlit-based dashboard

# Microplastic Detection & Water Quality Prediction System

An AI-powered system for detecting microplastics, predicting water quality, and simulating environmental impacts using machine learning, deep learning, and physics-informed models.

## Overview

This project provides an end-to-end intelligent framework to:

* Detect and classify microplastics from images
* Identify polymer types using spectroscopic ML models
* Predict and forecast Water Quality Index (WQI)
* Simulate environmental impact using a digital twin
* Support decision-making for researchers and policymakers

The system is deployed as an interactive Streamlit dashboard with role-based access.

## Key Features

### Core Models

* **YOLOv8**
  Microplastic detection and classification (Fragments, Fibers, Pellets)

* **Raman Spectroscopy ML**
  Polymer identification (PET, PE, PP, PS, PVC)

* **Random Forest**
  Water Quality Index prediction with 94% test accuracy

* **Prophet**
  60-day WQI time-series forecasting

* **Physics-Informed Neural Network (PINN)**
  Dissolved oxygen prediction based on physical constraints

* **Digital Twin**
  Environmental impact and scenario simulation


### Advanced Capabilities

* Explainable AI (XAI) dashboard with feature importance
* What-if analysis for policy and environmental scenarios
* Multi-role access (Public, Government, Researcher, Admin)
* Real-time alerts based on threshold violations
* Location-based comparison and benchmarking
* Automated PDF report generation


## Live Demo

Dashboard URL:
[https://pravaah-8ubxbo9e4ssm9okxtagnye.streamlit.app/](https://pravaah-8ubxbo9e4ssm9okxtagnye.streamlit.app/)

Demo Access:
Select any user role from the sidebar (no authentication required for demo).


## Installation & Setup

### Prerequisites

* Python 3.8 or higher
* pip
* Virtual environment (recommended)

### Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/microplastic-detection-system.git
cd microplastic-detection-system

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## Model Performance

| Model         | Metric        | Score    |
| ------------- | ------------- | -------- |
| YOLOv8        | mAP@0.5       | 94.2%    |
| Raman ML      | F1-Score      | 91.8%    |
| Random Forest | Test Accuracy | 94.0%    |
| PINN          | R² Score      | 0.90     |
| Prophet       | MAE           | ±2.5 WQI |


## Project Structure

```
pravaah/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
│
├── views/                # Dashboard UI components
├── models/               # Trained ML/DL models
├── utils/                # Utilities (XAI, simulations, helpers)
├── apis/                 # External API integrations
├── maps/                 # Geographic and spatial mapping
├── pipeline/             # Automated data workflows
├── data/                 # Datasets
├── config/               # Configuration files
└── outputs/              # Generated reports and outputs
```


## User Roles

* **Public**
  Basic detection, visualization, and awareness tools

* **Government**
  Policy-focused insights, XAI explanations, and what-if simulations

* **Researcher**
  Full analytics, model evaluation, and comparative analysis

* **Admin**
  System monitoring and configuration management


## Technology Stack

### Machine Learning & AI

* PyTorch
* scikit-learn
* YOLOv8
* Prophet

### Web & Visualization

* Streamlit
* Plotly
* Folium

### Data Processing

* pandas
* NumPy
* OpenCV


## Team

* **Aadrika Gupta** – Project Lead
* **Sangyan Hari Pushkar** – Team Member
* **Mayur Mundada** – Team Member


## Contact

* Email: [bt24eci032@iiitn.ac.in](mailto:bt24eci032@iiitn.ac.in)
* GitHub: [https://github.com/Aadrika2106](https://github.com/Aadrika2106)


If you find this project useful, consider starring the repository.
\# 🌊 Microplastic Detection \& Water Quality Prediction System



\[!\[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

\[!\[Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)](https://streamlit.io/)

\[!\[License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



> AI-powered system for detecting microplastics, predicting water quality, and simulating environmental impacts.



---



\## ✨ Features



\### 🔬 Core Models

\- \*\*YOLOv8\*\*: Microplastic detection (Fragments, Fibers, Pellets)

\- \*\*Raman ML\*\*: Polymer identification (PET, PE, PP, PS, PVC)

\- \*\*Random Forest\*\*: Water Quality Index prediction (94% accuracy)

\- \*\*Prophet\*\*: 60-day WQI forecasting

\- \*\*PINN\*\*: Physics-informed dissolved oxygen prediction

\- \*\*Digital Twin\*\*: Environmental impact simulation



\### 🎨 Advanced Features

\- \*\*XAI Dashboard\*\*: Explainable AI with feature importance

\- \*\*What-If Simulation\*\*: Interactive scenario testing

\- \*\*Multi-Role Access\*\*: Public, Government, Researcher, Admin

\- \*\*Real-time Alerts\*\*: Automated threshold monitoring

\- \*\*Location Comparison\*\*: Multi-site benchmarking

\- \*\*PDF Reports\*\*: Automated report generation



---



\## 🚀 Quick Start



\### Installation

```bash

\# Clone repository

git clone https://github.com/Sangyab-1234/Pravaah.git

cd Pravaah


\# Create virtual environment

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate



\# Install dependencies

pip install -r requirements.txt



\# Run dashboard

streamlit run app.py

```



\*\*Access at:\*\* (http://localhost:8503)



\*\*Demo Roles:\*\* Select any role on the sidebar (no password needed for demo)



---



\## 📊 Model Performance



| Model | Metric | Score |

|-------|--------|-------|

| YOLOv8 | mAP@0.5 | 94.2% |

| Raman ML | F1-Score | 91.8% |

| Random Forest | Test Accuracy | 94.0% |

| PINN | R² Score | 0.90 |

| Prophet | MAE | ±2.5 WQI |



---



\## 📁 Project Structure
pravaah/

├── app.py                    # Main application

├── requirements.txt          # Dependencies

├── views/                    # Dashboard interfaces

├── models/                   # ML/DL models

├── utils/                    # Utilities (XAI, What-If, etc.)

├── apis/                     # External APIs

├── maps/                     # Geographic mapping

├── pipeline/                 # Automated workflows

├── data/                     # Datasets

├── config/                   # Configuration

└── outputs/                  # Generated reports

---



\## 🎯 User Roles



\- \*\*Public\*\*: Basic detection and awareness

\- \*\*Government\*\*: Policy tools, XAI, What-If simulation

\- \*\*Researcher\*\*: Full analytics, model comparison

\- \*\*Admin\*\*: System management



---



\## 🛠️ Technologies



\- \*\*ML/DL\*\*: PyTorch, scikit-learn, YOLOv8, Prophet

\- \*\*Web\*\*: Streamlit, Plotly, Folium

\- \*\*Data\*\*: pandas, NumPy, OpenCV



---



\## 📄 License



MIT License - see \[LICENSE](LICENSE) file



---



\## 👥 Team



\- Aadrika Gupta - Project Lead

\- Sangyan Hari Pushkar, Mayur Mundada - Team Members



---



\## 📧 Contact



\- Email: bt24ece128@iiitn.ac.in

\- GitHub: \[Sangyan-1234](https://github.com/Sangyan-1234)



---



⭐ \*\*Star this repo if helpful!\*\*

