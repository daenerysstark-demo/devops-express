import os
from flask import Blueprint, jsonify

diagnostics_bp = Blueprint('diagnostics', __name__)

# --- Feature 2: System Diagnostics (Environment Redaction Bypass) ---
@diagnostics_bp.route('/health')
def health_check():
    env_vars = os.environ.copy()

    for key, _ in env_vars.items():
        if "PASSWORD" in key or "SECRET" in key:
            env_vars[key] = "[REDACTED]"

    return jsonify(env_vars)
