### Run 

```
pip install -r requirements.txt
cp .env.example .env 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Swagger
```
http://localhost:8000/api/v1/swagger/
```