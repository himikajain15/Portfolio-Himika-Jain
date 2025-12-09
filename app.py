from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'himikajain2110@gmail.com')

mail = Mail(app)

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
        
        # Create email message
        msg = Message(
            subject=f"Portfolio Contact from {name}",
            recipients=['himikajain2110@gmail.com'],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        
        # Send email
        mail.send(msg)
        
        return jsonify({
            'success': True,
            'message': 'Email sent successfully!'
        })
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to send email. Please try again.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
