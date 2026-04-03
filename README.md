# Automated Threat Intelligence Enrichment Tool

## Overview
This project simulates a real-world Security Operations Center (SOC) workflow by automating threat intelligence enrichment for suspicious IP addresses.

The tool processes event logs, validates indicators of compromise (IOCs), assigns risk scores, and generates investigation-ready reports.

---

## Features
- Parses security event data from CSV input
- Identifies and filters internal/private IP addresses
- Enriches external IPs with threat intelligence data
- Assigns severity levels (High, Medium, Low)
- Generates detailed investigation reports
- Simulates SOC alert triage workflow

---

## Technologies Used
- Python
- CSV processing
- IP address validation
- Basic threat intelligence logic

---

## How It Works
1. Reads event data from `sample_events.csv`
2. Extracts source IP addresses
3. Checks IP reputation (mock threat intelligence)
4. Assigns risk score and severity level
5. Generates a report for SOC investigation

---

## How to Run
bash
python main.py

```bash
python main.py
