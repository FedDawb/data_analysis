import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

# Assume your risk assessment functions are defined here or imported
def assess_antenatal_risk(bmi, diabetes, smoking, previous_cs):
    score = 0
    if bmi > 30:
        score += 3
    if diabetes:
        score += 2
    if smoking:
        score += 1
    if previous_cs:
        score += 1

    if score <= 3:
        risk_level = "Low"
    elif score <= 6:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return score, risk_level, []

def assess_intrapartum_risk(prolonged_labor, prom_duration, chorioamnionitis, emergency_cs):
    score = 0
    if prolonged_labor:
        score += 2
    if prom_duration > 12:
        score += 2
    elif prom_duration > 6:
        score += 1
    if chorioamnionitis:
        return "High", []
    if emergency_cs:
        score += 1

    return score, []

def update_risk_with_intrapartum(antenatal_score, antenatal_risk_factors, intrapartum_score, intrapartum_risk_factors):
    total_score = antenatal_score + intrapartum_score
    if total_score <= 5:
        risk_level = "Low"
    elif total_score <= 9:
        risk_level = "Medium"
    else:
        risk_level = "High"
    return total_score, risk_level, []

# Load the dummy data
try:
    dummy_data_df = pd.read_csv('data/dummy_patient_data.csv')
except FileNotFoundError:
    print("Error: dummy_patient_data.csv not found in the data folder.")
    exit()

# Calculate the final risk level for each patient
risk_levels = []
for index, row in dummy_data_df.iterrows():
    bmi = row['BMI']
    diabetes = row['Diabetes'] == 'Yes'
    smoking = row['Smoking'] == 'Yes'
    previous_cs = row['Previous_CS'] == 'Yes'
    prolonged_labor = row['Prolonged_Labor'] == 'Yes'
    prom_duration = row['PROM_Duration_Hours']
    chorioamnionitis = row['Chorioamnionitis'] == 'Yes'
    emergency_cs = row['Emergency_CS'] == 'Yes'

    antenatal_score, antenatal_risk, _ = assess_antenatal_risk(bmi, diabetes, smoking, previous_cs)
    intrapartum_score_or_risk, _ = assess_intrapartum_risk(prolonged_labor, prom_duration, chorioamnionitis, emergency_cs)

    if chorioamnionitis:
        final_risk = "High"
    else:
        final_score, final_risk, _ = update_risk_with_intrapartum(antenatal_score, [], intrapartum_score_or_risk, [])
    risk_levels.append(final_risk)

dummy_data_df['Calculated_Risk_Level'] = risk_levels

# Calculate risk level counts and percentages
risk_counts = dummy_data_df['Calculated_Risk_Level'].value_counts().to_dict()
total_patients = len(dummy_data_df)
risk_percentages = {level: (count / total_patients) * 100 for level, count in risk_counts.items()}

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Surgical Site Infection Risk Assessment Results'),

    html.Div(children=f'Total Patients: {total_patients}'),

    # Bar chart of risk levels
    dcc.Graph(
        id='risk-level-bar-chart',
        figure=px.bar(
            dummy_data_df,
            x='Calculated_Risk_Level',
            color='Calculated_Risk_Level',
            category_orders={"Calculated_Risk_Level": ["Low", "Medium", "High"]},
            title='Distribution of Calculated Risk Levels'
        )
    ),

    html.Div(children=[
        html.H2("Risk Level Percentages:"),
        html.Ul(children=[
            html.Li(f"{level}: {percentage:.2f}%") for level, percentage in risk_percentages.items()
        ])
    ]),

    # Pie chart of risk levels (ADDED THIS SECTION)
    dcc.Graph(
        id='risk-level-pie-chart',
        figure=px.pie(
            dummy_data_df,
            names='Calculated_Risk_Level',
            color='Calculated_Risk_Level',
            category_orders={"Calculated_Risk_Level": ["Low", "Medium", "High"]},
            title='Proportion of Calculated Risk Levels'
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)