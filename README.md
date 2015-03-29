# boxer_app
Boxer is complete app. This project has two repositories. Repository name: boxer - for frontend app, boxer_app - backend app with linked frontend app only for testing.

To run complete application: Frontend app should be cloned from https://github.com/codecats/boxer and putted to front directory.
Installation frontend into backed application:
 - ./manage.py collectstatic
 - Update boxer/templates/index.html from frontend index.html - {{ STATIC_URL }}(/app) has to be added


**Full app install**

Clone backend app
```bash
git clone https://github.com/codecats/boxer_app boxer_app
```
Go to cloned app
```bash
cd $_
```
Create virtual enviroment
```bash
virtualenv venv
```
Activate it
```bash
source venv/bin/activate
```
Go to backend content
```bash
cd boxer
```
Install python libs
```bash
pip install -r requirements.txt
```
Now clone frontend app
```bash
git clone https://github.com/codecats/boxer front
```
Go to frontend app
```bash
cd $_
```
Install javascript libs
```bash
bower install
```
Go to backend app
```bash
cd -
```
Collect static files
```bash
./manage.py collectstatic
```
Run server for check if everything is ok.
```bash
./manage.py runserver
```

**run celery**
 - add to supervisor celery worker

tests: 
```bash
(venv)boxer_app/boxer$ celery --app=boxer.celery:app worker --loglevel=INFO 
```
