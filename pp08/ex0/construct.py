"""
construct.py - Detects and displays Python virtual environment status.

This program checks whether it is running inside a virtual environment
and displays relevant information about the current Python setup.
"""

import sys
import os
import site


def get_venv_name(venv_path: str) -> str:
    """Extract the virtual environment name from its path."""
    return os.path.basename(venv_path)


def detect_virtual_environment() -> tuple[bool, str | None]:
    """
    Detect whether the program is running inside a virtual environment.

    Returns:
        A tuple of (is_in_venv, venv_path).
    """
    # sys.prefix differs from sys.base_prefix when inside a venv
    venv_path: str | None = getattr(sys, "prefix", None)
    base_path: str | None = getattr(sys, "base_prefix", None)

    if venv_path and base_path and venv_path != base_path:
        return True, venv_path

    # Also check the VIRTUAL_ENV environment variable as a fallback
    env_var: str | None = os.environ.get("VIRTUAL_ENV")
    if env_var:
        return True, env_var

    return False, None


def get_package_path() -> str:
    """Return the primary site-packages path for the current environment."""
    paths: list[str] = site.getsitepackages()
    if paths:
        return paths[0]
    return "unknown"


def show_outside_matrix() -> None:
    """Display output when running outside a virtual environment."""
    python_path: str = sys.executable

    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {python_path}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:\n")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate     # On Windows\n")
    print("Then run this program again.")


def show_inside_construct(venv_path: str) -> None:
    """Display output when running inside a virtual environment."""
    python_path: str = sys.executable
    venv_name: str = get_venv_name(venv_path)
    package_path: str = get_package_path()

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print(f"Package installation path:\n  {package_path}")


def main() -> None:
    """Entry point: detect environment and display appropriate info."""
    try:
        in_venv, venv_path = detect_virtual_environment()

        if in_venv and venv_path:
            show_inside_construct(venv_path)
        else:
            show_outside_matrix()
    except Exception as e:
        print(f"Error detecting environment: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
