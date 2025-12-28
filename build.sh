#!/usr/bin/env bash

# 1. Xatolik bo'lsa darhol to'xtatish
set -o errexit

# 2. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 3. Statik fayllarni yig'ish (CSS, JS, Rasmlar)
python manage.py collectstatic --no-input

# 4. Bazani yangilash (Migrate qilish)
python manage.py migrate