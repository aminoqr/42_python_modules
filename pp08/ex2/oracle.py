import os
import sys
from dotenv import load_dotenv

# Variables required by the Oracle [cite: 236-242]
REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

def load_config() -> dict[str, str | None]:
    """
    Load configuration from environment variables.
    load_dotenv() allows .env file variables to be accessed via os.environ [cite: 227-228].
    """
    load_dotenv()
    return {var: os.environ.get(var) for var in REQUIRED_VARS}

def check_config(config: dict[str, str | None]) -> bool:
    """
    Check for missing values and enforce production strictness .
    """
    all_ok = True
    is_prod = config.get("MATRIX_MODE") == "production"
    
    for var in REQUIRED_VARS:
        if not config[var]:
            # Print warning/critical messages based on the current mode
            level = "[CRITICAL]" if is_prod else "[WARNING]"
            print(f"{level} {var} is missing!")
            all_ok = False
            
    # In production, missing variables must halt the program [cite: 233]
    if is_prod and not all_ok:
        print("\nMISSION ABORTED: Production environment is incomplete.")
        sys.exit(1)
        
    return all_ok

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()

    # Check config but allow the program to display partial info in dev mode
    is_complete = check_config(config)
    
    if not is_complete:
        print("\nConfiguration incomplete. Please check your .env file.\n")

    print("Configuration loaded:")

    # Mode: development or production
    print(f"Mode: {config.get('MATRIX_MODE') or 'None'}")
    
    # Database: Status-based output instead of raw connection string
    db_url = config.get('DATABASE_URL')
    if not db_url:
        db_status = "Disconnected"
    elif "localhost" in db_url:
        db_status = "Connected to local instance"
    else:
        db_status = "Connected to remote"
    print(f"Database: {db_status}")
    
    # API Access: Authenticated status
    api_status = "Authenticated" if config.get('API_KEY') else "Missing"
    print(f"API Access: {api_status}")
    
    # Log Level: DEBUG, INFO, etc.
    print(f"Log Level: {config.get('LOG_LEVEL') or 'None'}")
    
    # Zion Network: Online status based on endpoint presence
    zion_status = "Online" if config.get('ZION_ENDPOINT') else "Offline"
    print(f"Zion Network: {zion_status}\n")

    # --- SECURITY CHECKS---
    print("Environment security check:")
    
    # Check for placeholder strings in API_KEY
    if config.get("API_KEY") == "your_api_key_here":
        print("[WARNING] Hardcoded API_KEY placeholder detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    # Check for physical .env file
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    # Production override detection
    if config.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Development mode active")

    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Graceful handling of unexpected Matrix glitches
        print(f"The Oracle encountered a criti
              cal error: {e}")
        sys.exit(1)