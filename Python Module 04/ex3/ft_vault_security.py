print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")
with open('classified_data.txt', 'r') as c_data:
    print("SECURE EXTRACTION:")
    print(c_data.read())
    print()

with open('security_protocols.txt', 'w') as s_protocols:
    print("SECURE PRESERVATION:")
    s_protocols.write("[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
