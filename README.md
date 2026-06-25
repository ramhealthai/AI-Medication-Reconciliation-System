# AI Medication Reconciliation System

## Overview

The AI Medication Reconciliation System is a Python-based healthcare application designed to assist healthcare professionals in comparing patient medication records from different sources. The system identifies medication discrepancies, highlights changes in therapy, and supports safer medication management through automated reconciliation.

Medication reconciliation is an important component of patient safety, particularly during transitions of care such as hospital admission, discharge, and outpatient follow-up.

---

## Features

- Compare current and previous medication lists
- Detect newly prescribed medications
- Identify discontinued medications
- Detect duplicate medications
- Generate a medication reconciliation report
- Perform basic medication discrepancy risk assessment
- Demonstrate clinical decision support concepts

---

## Technologies Used

- Python
- Pandas
- CSV Data Processing

---

## Project Structure

```
AI-Medication-Reconciliation-System/
│
├── medication_reconciliation.py
├── sample_current_medications.csv
├── sample_previous_medications.csv
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python medication_reconciliation.py
```

---

## Sample Output

```
AI Medication Reconciliation Report

Current Medications
• Metformin
• Lisinopril
• Atorvastatin
• Aspirin

Previous Medications
• Metformin
• Lisinopril
• Simvastatin

New Medication
• Atorvastatin
• Aspirin

Discontinued Medication
• Simvastatin

Overall Risk Assessment
Moderate Risk
```

---

## Healthcare Applications

This project demonstrates concepts relevant to:

- Medication reconciliation
- Medication safety
- Clinical decision support
- Healthcare informatics
- Patient safety
- Medication management

---

## Future Improvements

- Electronic Health Record (EHR) integration
- FHIR interoperability
- Drug interaction detection
- AI-based medication discrepancy prediction
- Clinical decision support dashboard
- Machine learning risk scoring

---

## Disclaimer

This project is intended for educational and research purposes only. It is not intended for direct clinical use or medical decision-making.

---

## Author

**Ramchandra Pudasaini**

Registered Pharmacist

MS in Information Technology Candidate

Healthcare AI | Clinical Decision Support | Healthcare Informatics
