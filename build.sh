#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Statik fayllar uchun
python manage.py collectstatic --no-input

# Migratsiyalarni majburan yangilash
python manage.py makemigrations --noinput
python manage.py migrate --noinput