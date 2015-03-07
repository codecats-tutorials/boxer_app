# boxer_app
Boxer is complete app. This project has two repositories. Repository name: boxer - for frontend app, boxer_app - backend app with linked frontend app only for testing.

To run complete application: Frontend app should be cloned from https://github.com/codecats/boxer and putted to front directory.
Installation frontend into backed application:
 - ./manage.py collectstatic
 - Update boxer/templates/index.html from frontend index.html - {{ STATIC_URL }}(/app) has to be added


