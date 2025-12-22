SYSTEM_PROFILE = {
    "system_name": "Patient Education Assistant",
    "intended_users": ["patients", "general public"],
    "clinical_use": False,
    "stores_phi": False,
    "hipaa_scope": "Out of scope by design",
    "allowed_capabilities": [
        "general health education",
        "preventive care information",
        "health literacy support"
    ],
    "disallowed_capabilities": [
        "diagnosis",
        "treatment recommendations",
        "medication dosing",
        "clinical decision support"
    ],
    "human_oversight_required": True
}
