source venv\Scripts\activate 
python manage.py migrate 
python manage.py collectstatic --noinput 
python manage.py runserver 
