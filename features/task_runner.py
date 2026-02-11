import pickle
from flask import Blueprint, request

task_runner_bp = Blueprint('task_runner', __name__)

# --- Feature 4: Plugin Task Runner (Insecure Deserialization) ---
class TrustedTask:
    def run(self):
        print("Running trusted task...")

@task_runner_bp.route('/upload-task', methods=['POST'])
def upload_task():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
        
    try:
        task_obj = pickle.load(file)
        
        if hasattr(task_obj, 'run'):
            task_obj.run()
            return "Task executed successfully"
        else:
            return "Invalid task object", 400
    except Exception as e:
        return f"Task execution failed: {str(e)}", 500
