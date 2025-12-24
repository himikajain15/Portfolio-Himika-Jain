from flask import Flask, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# Resend configuration
RESEND_API_KEY = os.environ.get('RESEND_API_KEY', 'your-resend-api-key-here')
RESEND_FROM = os.environ.get('RESEND_FROM', 'your@email.com')  # Must be a verified sender in Resend dashboard
RESEND_TO = os.environ.get('RESEND_TO', 'himikajain2110@gmail.com')  # Where messages are sent

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'All fields are required'
            }), 400
        
        return jsonify({
            'success': False,
            'message': 'Send-email disabled (using Formspree)' 
        }), 501

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
