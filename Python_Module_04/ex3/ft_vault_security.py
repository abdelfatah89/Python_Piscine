def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with open("classified_data.txt", "r") as file:
            print("\nSECURE EXTRACTION:")
            content = file.read().strip()
            print(content)
    except FileNotFoundError:
        print("\n[CRISIS] Access failed: Vault missing from matrix.")
        print("SAFE EXIT: Protocol 'with' ensured no resources were leaked.")

    with open("security_protocols.txt", "w") as file:
        print("\nSECURE PRESERVATION:")
        file.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
