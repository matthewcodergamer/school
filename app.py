import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify, render_template
import logging
import os
from email.utils import formataddr

# Set up logging for better error handling
logging.basicConfig(level=logging.DEBUG)

# School Email Configuration
SCHOOL_EMAIL = "gamerstriper@gmail.com"  # Replace with your email
Recipient_EMAIL = "smithsarah2y@gmail.com"
EMAIL_PASSWORD = "xcro niyz bmgy czkd "  # Replace with your Gmail App Password (NOT your regular password)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render your HTML template here

@app.route("/send_message", methods=["POST"])
def send_message():
    # Get form data
    name = request.form.get("name")
    message = request.form.get("message")

    # Validate data
    if not name or not message:
        return jsonify({"error": "Name and message are required."}), 400

    try:
        # Prepare the email content
        subject = f"Message from {name}"
        email_content = f"Name: {name}\n\nMessage:\n{message}"

        # Set up the MIME email
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = formataddr(('School Name', SCHOOL_EMAIL))  # Use 'From' with your name
        msg['To'] = Recipient_EMAIL  # You can set a different recipient if needed
        msg['Reply-To'] = SCHOOL_EMAIL  # Optionally, add a Reply-To header

        # Attach plain-text email content
        msg.attach(MIMEText(email_content, 'plain'))

        # Send email using SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SCHOOL_EMAIL, EMAIL_PASSWORD)  # Login with email credentials (App Password)
            server.sendmail(SCHOOL_EMAIL, SCHOOL_EMAIL, msg.as_string())  # Send the email

        return jsonify({"success": "Message sent successfully!"}), 200

    except smtplib.SMTPException as e:
        logging.error("Error sending email: %s", str(e))
        return jsonify({"error": "An error occurred while sending the email. SMTP Error."}), 500
    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
