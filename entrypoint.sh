#!/bin/sh
pip install --upgrade pip && pip install -r requirements.txt && python main.py
#gunicorn app:app --bind 0.0.0.0:5000
#gunicorn --bind 0.0.0.0:5000 backend.app:app