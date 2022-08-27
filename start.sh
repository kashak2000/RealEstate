#!/bin/bash

run_gunicorn() {
  gunicorn app:app -b 0.0.0.0:5000 --workers=2 2>&1 | tee -a 
}

run_gunicorn