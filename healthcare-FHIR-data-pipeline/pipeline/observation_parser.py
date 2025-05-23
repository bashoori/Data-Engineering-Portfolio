"""
📄 observation_parser.py

This script extracts Observation resources from FHIR Bundles generated by Synthea.

Author: Bita Ashoori
"""

import os
import json
import pandas as pd

INPUT_DIR = "../data/fhir"
OUTPUT_FILE = "../data/output/parsed_observations.csv"
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

observation_records = []

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".json"):
        with open(os.path.join(INPUT_DIR, filename), "r") as f:
            bundle = json.load(f)

        if bundle.get("resourceType") != "Bundle":
            continue

        for entry in bundle.get("entry", []):
            resource = entry.get("resource", {})
            if resource.get("resourceType") == "Observation":
                observation_id = resource.get("id", "")
                subject_ref = resource.get("subject", {}).get("reference", "")
                status = resource.get("status", "")
                code_text = resource.get("code", {}).get("text", "")
                value = resource.get("valueQuantity", {}).get("value", "")
                unit = resource.get("valueQuantity", {}).get("unit", "")
                effective_datetime = resource.get("effectiveDateTime", "")

                observation_records.append([
                    observation_id, subject_ref, status, code_text,
                    value, unit, effective_datetime
                ])

columns = [
    "Observation ID", "Subject Reference", "Status",
    "Observation", "Value", "Unit", "Effective Date"
]

df = pd.DataFrame(observation_records, columns=columns)
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Extracted {len(df)} observations to: {OUTPUT_FILE}")
