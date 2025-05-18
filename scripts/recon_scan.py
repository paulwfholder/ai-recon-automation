# Recon Scan

#!/usr/bin/env python3
import sys, subprocess, pathlib, os

targets = pathlib.Path(sys.argv[1]).read_text().splitlines()
os.makedirs("reports", exist_ok=True)
with open("reports/nmap_report.md", "w") as report:
    for host in targets:
        result = subprocess.check_output(["nmap", "-sV", host]).decode()
        report.write(f"## {host}\n```\n{result}\n```\n")
