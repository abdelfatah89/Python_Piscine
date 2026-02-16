def ft_crisis_response(path: str) -> None:

    try:
        with open(path) as file:
            print(f"\nROUTINE ACCESS: Attempting access to '{path}'...")
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{path}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{path}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    normal_file = "standard_archive.txt"
    deny_file = "classified_vault.txt"
    lost_file = "lost_archive.txt"

    ft_crisis_response(lost_file)
    ft_crisis_response(deny_file)
    ft_crisis_response(normal_file)

    print("\nAll crisis scenarios handled successfully. Archives secure.")
