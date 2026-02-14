import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
arch_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")
print(f"\n[STANDARD] Archive status from {arch_id}: {status_report}")
print("[ALERT] System diagnostic: "
      "Communication channels verified", file=sys.stderr)
print("[STANDARD] Data transmission complete\n")
print("Three-channel communication test successful.")
