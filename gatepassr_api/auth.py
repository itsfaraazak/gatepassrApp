import identity
import identity.web
import requests
from flask import (
    Blueprint, Flask, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

