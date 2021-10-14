# Poor man's twitter
It is a small twitter that does not need authentication.

It runs on your frontend with VueJS and communicates to the backend via AXIOS.

In the backend part, Django was used, with the DRF framework.

Installation instructions are as follows.

## PRE-INSTALLED
You need PYTHON 3, GIT

## INSTALLATION
Create directory and env
```
mkdir twitter
cd twitter
python -m venv venv
source venv/bin/activate
```

clone de project
```
git clone https://github.com/raulespecialist/basical-twitter.git
```


install requeriments
```
cd basical-twitter
pip install -r requirements.txt
```

run the project
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Now the project run on http://127.0.0.1:8000/  or API directly http://127.0.0.1:8000/api/twitter/ **
