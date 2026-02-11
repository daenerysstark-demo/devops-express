import time
import hashlib
from flask import Blueprint, jsonify

link_generator_bp = Blueprint('link_generator', __name__)

# --- Feature 3: Quick-Link Generator (Weak Hashing) ---
@link_generator_bp.route('/generate-link', methods=['POST'])
def generate_link():
    # Vulnerability: Deterministic hash based on system time
    timestamp = str(time.time())
    token = hashlib.md5(timestamp.encode()).hexdigest()
    
    return jsonify({
        "url": f"/share/{token}",
        "expires_in": "10 minutes",
        "timestamp_used": timestamp # Showing this makes it even easier to crack
    })
