import pandas as pd

print("=" * 60)
print("AI Medication Reconciliation System")
print("=" * 60)

current = pd.read_csv("sample_current_medications.csv")
previous = pd.read_csv("sample_previous_medications.csv")

print("\nCurrent Medication List")
print(current)

print("\nPrevious Medication List")
print(previous)

current_set = set(current["Medication"])
previous_set = set(previous["Medication"])

new_meds = current_set - previous_set
missing_meds = previous_set - current_set

print("\nMedication Reconciliation Report")
print("-" * 50)

if new_meds:
    print("\nNew Medications:")
    for med in new_meds:
        print(f"+ {med}")

if missing_meds:
    print("\nDiscontinued / Missing Medications:")
    for med in missing_meds:
        print(f"- {med}")

duplicates = current[current.duplicated("Medication")]

if not duplicates.empty:
    print("\nDuplicate Medications Detected:")
    print(duplicates)

risk_score = len(new_meds) + len(missing_meds)

print("\nOverall Risk Assessment")

if risk_score == 0:
    print("Low Risk")
elif risk_score <= 2:
    print("Moderate Risk")
else:
    print("High Risk")

print("\nMedication reconciliation completed successfully.")
