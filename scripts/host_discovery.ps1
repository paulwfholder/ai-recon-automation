# Host Discovery

param(
    [string]$Targets = "target_list.txt"
)

if (-not (Test-Path reports)) { New-Item -ItemType Directory -Path reports | Out-Null }

Get-Content $Targets | ForEach-Object {
    if (Test-Connection $_ -Count 1 -Quiet) {
        "$_ : Alive"  | Tee-Object -FilePath reports/host_discovery.md -Append
    } else {
        "$_ : Down"   | Tee-Object -FilePath reports/host_discovery.md -Append
    }
}
