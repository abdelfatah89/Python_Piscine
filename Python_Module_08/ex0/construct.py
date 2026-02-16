import sys
import os
import site


def check_env_status() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("\nMATRIX STATUS: You're still plugged in"
                  f"\nCurrent Python: {sys.executable}"
                  "\nVirtual Environment: None detected"
                  "\n\nWARNING: You're in the global environment!"
                  "\nThe machines can see everything you install."
                  "\nTo enter the construct, run:"
                  "\npython -m venv matrix_env"
                  "\nsource matrix_env/bin/activate # On Unix"
                  "\nmatrix_env"
                  "\nScripts"
                  "\nactivate # On Windows"
                  "\n\nThen run this program again.")
        else:
            venv_path: str = sys.prefix
            venv_name: str = os.path.basename(venv_path)

            print("\nMATRIX STATUS: Welcome to the construct"
                  f"\nCurrent Python: {sys.executable}"
                  f"\nVirtual Environment: {venv_name}"
                  f"\nEnvironment Path: {sys.prefix}"
                  "\n\nSUCCESS: You're in an isolated environment!"
                  "\nSafe to install packages without"
                  "affecting the global system."
                  "\n\nPackage installation path:"
                  f"\n{site.getsitepackages()[0]}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to detect environment: {e}")


if __name__ == "__main__":
    check_env_status()
