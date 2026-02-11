from flask import Flask, render_template

# Import blueprints
from features.downloader import downloader_bp
from features.task_runner import task_runner_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(downloader_bp)
app.register_blueprint(task_runner_bp)

# --- Frontend Routes ---
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Debug mode on for extra "developer visibility" (also a risk in prod)
    app.run(debug=True, port=5000)
