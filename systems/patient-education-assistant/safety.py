from config import SYSTEM_PROFILE

DISALLOWED_KEYWORDS = [
    "diagnose",
    "diagnosis",
    "prescribe",
    "prescription",
    "dosage",
    "dose",
    "treatment",
    "medication",
    "drug",
    "emergency"
]

def violates_policy(user_input: str) -> bool:
    """
    Checks whether user input violates non-clinical system policy.
    """
    for keyword in DISALLOWED_KEYWORDS:
        if keyword in user_input.lower():
            return True
    return False

