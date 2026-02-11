import yaml
from flask import Blueprint, request, jsonify

report_generator_bp = Blueprint('report_generator', __name__)

# --- Feature 5: PDF Report Generator (Vulnerable Dependency) ---
@report_generator_bp.route('/generate-report', methods=['POST'])
def generate_report():
    # Vulnerability: Parsing YAML with unsafe load using an old PyYAML version
    config_content = request.form.get('config')
    if not config_content:
        return "No config provided", 400
        
    try:
        data = yaml.load(config_content, Loader=yaml.Loader)
        return jsonify({"status": "Report generated based on config", "config": data})
    except Exception as e:
        return f"YAML Error: {str(e)}", 500
