def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        path: str = "ancient_fragment.txt"
        with open(path, 'r') as file:
            print(f"Accessing Storage Vault: {path}")
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(f"{file.read()}")
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first. ")


if __name__ == "__main__":
    ft_ancient_text()
