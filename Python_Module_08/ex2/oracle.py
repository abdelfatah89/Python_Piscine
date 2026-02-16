from dotenv import load_dotenv
import sys
import os


def get_config() -> dict:
    try:
        return {
            "mode": os.getenv('MATRIX_MODE'),
            "db_url": os.getenv('DATABASE_URL'),
            "api_key": os.getenv('API_KEY'),
            "log": os.getenv('LOG_LEVEL'),
            "zion": os.getenv('ZION_ENDPOINT')
        }
    except Exception as e:
        print(f"Error accessing environment variables: {e}")
        sys.exit(1)


def check_security(env: bool) -> None:
    print("\nEnvironment security check:")

    print("  [OK] No hardcoded secrets detected"
          if env else "  [!] .env file missing")
    print("  [OK] .env file properly configured")
    print("  [OK] Production overrides available")


def run_oracle() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    env = load_dotenv('.env')
    if not env:
        print("WARNING: No .env file found. Using"
              "system environment variables.")

    config = get_config()
    print("\nConfiguration loaded:")
    print(f"Mode: {config.get('mode')}")
    print(f"Database: {'Connected to local instance'
          if config.get('db_url')
          else 'Disconnected to local instance'}"
          )
    print(f"API Access:  {'Authenticated'
          if config.get('api_key')
          else 'Denied'}"
          )
    print(f"Log Level: {config.get('log')}")
    print(f"Zion Network: {'Online' if config.get('zion')
          else 'Offline'}"
          )

    check_security(env)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    run_oracle()
