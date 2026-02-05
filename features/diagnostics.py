import os
from flask import Blueprint, jsonify

diagnostics_bp = Blueprint('diagnostics', __name__)

# --- Feature 2: System Diagnostics (Environment Redaction Bypass) ---
@diagnostics_bp.route('/health')
def health_check():
    # A health check endpoint should ideally return a simple status
    # to confirm the service is operational, without exposing any internal details.
    return jsonify(status="ok")
