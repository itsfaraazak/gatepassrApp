"""
import json
from flask import (
    Flask, jsonify, request, redirect, Blueprint, send_file
)

bp = Blueprint('email_notifications', __name__, url_prefix='/qr')

@bp.route("/generateqr", methods = ["GET", "POST"])

"""

import smtplib, ssl

port = 1025  # For starttls
smtp_server = "localhost"
sender_email = "my@localhost"
receiver_email = "your@localhost"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

# unencrypted email (probably won't even work on gmail)
from email.mime.text import MIMEText
msg = MIMEText("This is a test email :)")
msg["Subject"] = ""
msg["From"] = sender_email
msg["To"] = receiver_email

with smtplib.SMTP("localhost", port) as server:
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Sucessfully sent email :)")

""" # for an encrypted connection
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

    """