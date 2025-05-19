# Recon Scan

#!/usr/bin/env python3
"""
Minimal Nmap wrapper:
    python recon_scan.py target_list.txt
Creates: reports/nmap_report.md
"""

import sys
import subprocess
import pathlib
import os

if len(sys.argv) != 2:
    print("Usage: python recon_scan.py target_list.txt")
    sys.exit(1)

target_file = pathlib.Path(sys.argv[1])
if not target_file.exists():
    print(f"[!] Target file {target_file} not found.")
    sys.exit(1)

targets = target_file.read_text().splitlines()
os.makedirs("reports", exist_ok=True)

with open("reports/nmap_report.md", "w", encoding="utf-8") as report:
    for host in targets:
        print(f"[+] Scanning {host} …")
        # Unprivileged, faster TCP connect scan
        result = subprocess.check_output(
            ["nmap", "--unprivileged", "-sT", "-sV", "-T4", "--top-ports", "100", host],
            text=True,
            encoding="utf-8",
        )
        report.write(f"## {host}\n```\n{result}\n```\n")

print("[✓] Scan complete — see reports/nmap_report.md")

