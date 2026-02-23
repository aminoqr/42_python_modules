import sys
from importlib import metadata
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd


def check_dependencies() -> bool:
    """
    Checks if required Matrix programs are loaded.
    Returns True if all are present, False otherwise.
    """
    deps: list[str] = ["pandas", "numpy", "matplotlib", "requests"]
    all_loaded = True

    print("\nLOADING STATUS: Loading programs...\n")

    for dep in deps:
        try:
            version: str = metadata.version(dep)
            print(f"[OK] {dep} ({version}) - Program ready")
        except metadata.PackageNotFoundError:
            print(f"[ERROR] {dep} is missing from the construct!")
            all_loaded = False

    if not all_loaded:
        print("\nTo enter the construct, run:")
        print("pip install -r requirements.txt\n")

    return all_loaded


def simulate_matrix_data() -> 'pd.Series':
    import pandas as pd
    import numpy as np
    """Generates 1000 data points of Matrix signal fluctuations."""
    try:
        # Use numpy for numerical processing
        raw_data = np.random.randn(1000)
        # Wrap in pandas Series for analysis
        return pd.Series(raw_data, name="Signal_Strength")
    except Exception as e:
        print(f"Simulation glitch: {e}")
        return pd.Series()


def visualize_matrix_data(data: 'pd.Series') -> None:
    import matplotlib.pyplot as plt
    """Creates and saves the signal analysis visualization."""
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data, color='green', linewidth=0.5)
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Data Points")
        plt.ylabel("Fluctuation Amplitude")
        plt.grid(True, linestyle='--', alpha=0.6)

        # Save output to file
        filename = "matrix_analysis.png"
        plt.savefig(filename)
        print(f"\nAnalysis complete! Results saved to: {filename}")
    except Exception as e:
        print(f"Visualization failed: {e}")


def main() -> None:
    """Main execution flow for Exercise 01."""
    try:
        # Phase 1: Dependency Check
        if not check_dependencies():
            sys.exit(1)

        # Phase 2: Analysis (Only runs if dependencies are OK)
        print("\nAll programs loaded. Ready to enter the simulation.")
        print("Analyzing Matrix data...")

        data = simulate_matrix_data()

        if not data.empty:
            print("Generating visualization...")
            visualize_matrix_data(data)

    except Exception as e:
        print(f"CRITICAL ERROR: The Matrix is glitching... {e}")


if __name__ == "__main__":
    main()
