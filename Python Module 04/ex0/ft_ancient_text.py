print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print("Accessing Storage Vault: ancient_fragment.txt")
try:
    file = open('ancient_fragment.txt', 'r')
    print("Connection established...\n")
    print("RECOVERED DATA:")
    content = file.read()
    print(content, end="\n\n")
    print("Data recovery complete. Storage unit disconnected.")
    file.close()

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
