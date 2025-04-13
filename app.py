import pandas as pd


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

    return score, risk_level, [] # Returning empty list for risk factors for this example

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

    return score, [] # Returning empty list for risk factors for this example

def update_risk_with_intrapartum(antenatal_score, antenatal_risk_factors, intrapartum_score, intrapartum_risk_factors):
    total_score = antenatal_score + intrapartum_score
    if total_score <= 5:
        risk_level = "Low"
    elif total_score <= 9:
        risk_level = "Medium"
    else:
        risk_level = "High"
    return total_score, risk_level, [] # Returning empty list for risk factors for this example

if __name__ == '__main__':
    # ... (your Flask app.run() line might still be here) ...

    # --- Code to test with dummy data ---
    try:
        dummy_data_df = pd.read_csv('data/dummy_patient_data.csv')
        print("\n--- Running Analysis of Dummy Data ---")
        for index, row in dummy_data_df.iterrows():
            patient_id = row['PatientID']
            bmi = row['BMI']
            diabetes = row['Diabetes'] == 'Yes'
            smoking = row['Smoking'] == 'Yes'
            previous_cs = row['Previous_CS'] == 'Yes'
            prolonged_labor = row['Prolonged_Labor'] == 'Yes'
            prom_duration = row['PROM_Duration_Hours']
            chorioamnionitis = row['Chorioamnionitis'] == 'Yes'
            emergency_cs = row['Emergency_CS'] == 'Yes'
            expected_risk_level = row['Final_Risk_Level']

            antenatal_score, antenatal_risk, _ = assess_antenatal_risk(bmi, diabetes, smoking, previous_cs)
            intrapartum_score_or_risk, _ = assess_intrapartum_risk(prolonged_labor, prom_duration, chorioamnionitis, emergency_cs)

            if chorioamnionitis:
                final_risk = "High (due to chorioamnionitis)"
            else:
                final_score, final_risk, _ = update_risk_with_intrapartum(antenatal_score, [], intrapartum_score_or_risk, [])

            print(f"Patient {patient_id}: Expected Risk - {expected_risk_level}, Calculated Risk - {final_risk}")

    except FileNotFoundError:
        print("Error: dummy_patient_data.csv not found in the data folder.")