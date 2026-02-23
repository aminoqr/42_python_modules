# sys: Provides access to Python interpreter variables and functions
# os: Provides OS-level utilities (here used for path manipulation)
# site: Provides access to site-specific configuration, including package paths
import sys
import os
import site


def check_matrix_status() -> None:
    """
    Detects whether Python is running inside a virtual environment
    and displays relevant environment information.

    Uses Matrix-themed messaging for user feedback.
    """
    try:
        # ------------------------------------------------------------------
        # ENVIRONMENT DETECTION LOGIC:
        # ------------------------------------------------------------------
        # sys.prefix: The path to the Python installation being used.
        #          In a virtual environment, this points to the venv directory.
        #
        # sys.base_prefix: The path to the base Python installation.
        #                  This always points to the system/global Python,
        #                  even when inside a virtual environment.
        #
        # COMPARISON:
        # - If sys.prefix == sys.base_prefix:
        #       We are in the GLOBAL/SYSTEM Python environment.
        #       Both paths point to the same location (no venv active).
        #
        # - If sys.prefix != sys.base_prefix:
        #       We are INSIDE a virtual environment.
        #       sys.prefix points to the venv, while sys.base_prefix
        #       still points to the original Python installation.
        # ------------------------------------------------------------------
        if sys.prefix == sys.base_prefix:
            # Global environment detected - no virtual environment is active
            print("\nMATRIX STATUS: You're still plugged in\n")

            # sys.executable: Full path to the Python interpreter binary
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")

            print("""WARNING: Your're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate   # On Windows

Then run this program again.""")
        else:
            # Virtual environment detected - sys.prefix differs
            # from sys.base_prefix
            print("\nMATRIX STATUS: Welcome to the construct\n")

            # Display environment information:
            # sys.executable: Path to the venv's Python interpreter
            print(f"Current Python: {sys.executable}")
            # os.path.basename(sys.prefix): Extracts just the venv folder name
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            # sys.prefix: Full path to the virtual environment directory
            print(f"Environment Path: {sys.prefix}\n")

            print("""SUCCESS: You're in an isolated environment!
Safe to install pacakges without affecting
the global system.\n""")

            # site.getsitepackages(): Returns list of paths where packages
            # are installed
            # [0] gets the primary site-packages directory for this environment
            print("Package installation path:")
            print(site.getsitepackages()[0])
    except (AttributeError, IndexError, OSError) as e:
        # Handle potential errors:
        # - AttributeError: If sys attributes don't exist (rare edge cases)
        # - IndexError: If getsitepackages() returns an empty list
        # - OSError: If there are filesystem-related issues
        print(f"CRITICAL ERROR: The Matrix is glitching... {e}")


if __name__ == "__main__":
    check_matrix_status()
