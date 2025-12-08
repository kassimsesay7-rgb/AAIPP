# ...existing code...
from flask import Flask, send_file, request, make_response
import os

app = Flask(__name__)

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Route to serve the HTML login form
@app.route('/', methods=['GET'])
def home():
    """Serve the HTML login form using send_file"""
    html_file = os.path.join(BASE_DIR, 'TASK-14.1.html')
    return send_file(html_file, mimetype='text/html')

# Serve CSS file via send_file
@app.route('/TASK-14.2.css', methods=['GET'])
def serve_css():
    css_path = os.path.join(BASE_DIR, 'TASK-14.2.css')
    if not os.path.exists(css_path):
        return "CSS file not found", 404
    return send_file(css_path, mimetype='text/css')

# Serve JS file via send_file
@app.route('/TASK-14.3.js', methods=['GET'])
def serve_js():
    js_path = os.path.join(BASE_DIR, 'TASK-14.3.js')
    if not os.path.exists(js_path):
        return "JS file not found", 404
    return send_file(js_path, mimetype='application/javascript')

# ...existing code...
@app.route('/login', methods=['POST'])
def login():
    """Handle login form submission"""
    # Get username and password from form data
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    # Validate input
    if not username or not password:
        return make_response("Missing username or password", 400)
    
    # Print username on successful login (for demonstration)
    print(f"Successful login: Username = {username}")
    
    # Return plain text success message
    msg = f"Login Successful! Welcome {username}"
    return make_response(msg, 200, {'Content-Type': 'text/plain; charset=utf-8'})

# ...existing code...
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)