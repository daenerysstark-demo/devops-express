import os
from flask import Blueprint, request, send_file

downloader_bp = Blueprint('downloader', __name__)

# --- Feature 1: Asset Downloader (Path Traversal) ---
@downloader_bp.route('/download')
def download_asset():
    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400
    
    base_path = os.path.join(os.getcwd(), 'static/assets')
    file_path = os.path.abspath(os.path.join(base_path, filename))
    if not file_path.startswith(os.path.abspath(base_path)):
        return "Access Denied", 403
    
    print(f"Attempting to download: {file_path}") # Debug log
    
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}", 404
