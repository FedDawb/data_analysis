
# Surgical Site Infection (SSI) Risk Assessment Project

This project is a dual-interface tool for assessing and visualizing surgical site infection (SSI) risk based on patient data. It includes:

- A **Flask web application** that allows users to input patient details and receive a risk assessment.
- A **Dash dashboard** for visualizing aggregated dummy patient data using charts and statistics.

---
<img src="Screenshot 2025-04-13 164606.png">

<img src="Screenshot 2025-04-13 164634.png">

## 🚀 Getting Started

These instructions will help you clone the project and run it locally. Basic familiarity with Git and Python is recommended.

### ✅ Prerequisites

Make sure you have the following installed:

- **Git**  
  Check:  
  ```bash
  git --version
  ```  
  [Download Git](https://git-scm.com/downloads)

- **Python 3.7+**  
  Check:  
  ```bash
  python --version
  ```  
  or  
  ```bash
  python3 --version
  ```  
  [Download Python](https://www.python.org/downloads/)

- **pip (Python Package Installer)**  
  Check:  
  ```bash
  pip --version
  ```

---

## 📁 Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the folder where you want to save the project. Example:

   ```bash
   cd Documents
   ```

3. Clone the repository (replace the URL below with your actual GitHub repo):

   ```bash
   git clone https://github.com/your-username/ssi-risk-assessment.git
   ```

4. Navigate into the project folder:

   ```bash
   cd ssi-risk-assessment
   ```

---

## 📦 Install Dependencies

Make sure you’re inside the project folder. Then run:

```bash
pip install -r requirements.txt
```

This installs all required libraries, including:

- `Flask` for the web app
- `pandas` for data handling
- `dash` and `plotly` for interactive visualizations

---

## 🧠 Run the Web Application (Flask)

The Flask app provides an interactive risk assessment form. Start the app with:

```bash
python app.py
```

Once running, visit:

```
http://127.0.0.1:5000/
```

### What You'll See:

#### 🩺 Antenatal Risk Assessment Form
- Input: BMI, checkboxes for diabetes, smoking, and prior C-section
- Navigation: Click **Next** to proceed

#### 🧪 Intrapartum Risk Assessment Form
- Input: Duration of PROM (in hours), checkboxes for conditions like prolonged labor, chorioamnionitis, emergency C-section
- Action: Click **Calculate Risk** to view the results

#### 📊 Risk Assessment Results
- Final Score & Risk Level (Low / Medium / High)
- List of contributing risk factors
- Option to assess another patient

---

## 📊 Run the Data Visualization Dashboard (Dash)

To explore visual insights from the dummy dataset, run:

```bash
python dashboard.py
```

Once running, visit:

```
http://127.0.0.1:8050/
```

### Dashboard Features

#### 📋 Header:
**Surgical Site Infection Risk Assessment Results**  
Displays total number of patients from the `dummy_patient_data.csv` file.

#### 📈 Bar Chart:
**"Distribution of Calculated Risk Levels"**  
- X-axis: Risk Levels (Low, Medium, High)  
- Y-axis: Number of Patients  
- Each bar color-coded for clarity

#### 📊 Pie Chart:
**"Proportion of Risk Levels"**  
- Each slice represents the percentage of patients in each category

#### 🔢 Risk Level Percentages:
- Low: XX%
- Medium: XX%
- High: XX%

---

## 🧪 Example Use Case

This tool is ideal for:

- Clinical teams assessing surgical risks in real-time
- Data scientists prototyping medical risk models
- Students demonstrating full-stack Python projects (Flask + Dash)

---


