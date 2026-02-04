import os
from flask import Blueprint, jsonify

diagnostics_bp = Blueprint('diagnostics', __name__)

# --- Feature 2: System Diagnostics (Environment Redaction Bypass) ---
@diagnostics_bp.route('/health')
def health_check():
    # Vulnerability: Shallow copy + weak redaction logic
    env_vars = os.environ.copy() # Shallow copy
    
    # "Redact" sensitive keys
    for key, value in env_vars.items():
        if "PASSWORD" in key or "SECRET" in key:
            env_vars[key] = "[REDACTED]"
            
    # Intentional Flaw: The 'env_vars' dict is cleaner, but let's simulate 
    # a developer mistake where they accidentally expose the raw os.environ 
    # or the redaction logic is just easily bypassed if other keys are used.
    # For this demo, we will return the "redacted" list, but let's assume 
    # the vulnerability is that the user can ask for specific keys via a parameter 
    # that bypasses the redaction filter, OR simply that the redaction is incomplete.
    
    # Let's simple return the JSON. 
    # If the user asks for JSON, we send the dict.
    return jsonify(env_vars)
