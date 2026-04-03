import csv
from intel_lookup import lookup_ip
from utils import is_private_ip, classify_severity

INPUT_FILE = "sample_events.csv"
OUTPUT_FILE = "report.txt"

def process_events():
    findings = []

    with open(INPUT_FILE, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            ip = row["source_ip"]

            if is_private_ip(ip):
                continue

            intel = lookup_ip(ip)
            score = intel["risk_score"]
            severity = classify_severity(score)

            findings.append({
                "ip": ip,
                "risk_score": score,
                "severity": severity
            })

    return findings

def main():
    results = process_events()

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
