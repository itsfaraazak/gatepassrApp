import json
from flask import (
    Flask, jsonify, request, redirect, Blueprint, send_file
)
import segno
import io

bp = Blueprint('qr_handling', __name__, url_prefix='/qr')

@bp.route("/generateqr", methods = ["GET", "POST"])
def generate_parent_qr():
    data = "hello world!"
    buff = io.BytesIO()
    segno.make(data, micro=False) \
         .save(buff, kind='png', scale=4, dark='darkblue',
               data_dark='#474747', light='#efefef')
    buff.seek(0)
    return send_file(buff, mimetype='image/png')

# decoder might have to be made in javascript in the front end as we can't send a continous video capture, can we?
# if in python, https://towardsdatascience.com/build-your-own-barcode-and-qrcode-scanner-using-python-8b46971e719e looks promising.