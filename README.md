# AvyUpskill

An React website application to integrate backcountry skiing resources and information in Colorado.

# Table Of Contents 
- [Description](https://github.com/sbrook13/avyupskill_backend#description)
- [Example Code](https://github.com/sbrook13/avyupskill_backend#example-code)
- [Technology Used](https://github.com/sbrook13/avyupskill_backend#technology-used)
- [Setting up for the Application](https://github.com/sbrook13/avyupskill_backend#setting-up-for-the-application)
- [Main Features](https://github.com/sbrook13/avyupskill_backend#main-features)
- [Features in Progress](https://github.com/sbrook13/avyupskill_backend#features-in-progress)
- [Contact Information](https://github.com/sbrook13/avyupskill_backend#contact-information)
- [Link to Frontend Repo](https://github.com/sbrook13/avyupskill_backend#link-to-frontend-repo)

## Description

AvyUpskill is the one-stop-shop for backcountry skiing information in Colorado, in order to educate and empower novice backcountry skiers who don't know where to begin. Guests can get a quick weather report, find upcoming courses to increase their knowledge, beacon parks to practice their skills, low angle zones to get out relatively safely, and link to the CAIC avalanche forecast. Users can login to add comments and provide ratings on those backcountry-zones, as well as log their backcountry days with a journal entry.

## Example Code

### User Model

![User Model](https://i.imgur.com/icGiu6e.png)

### User Serializer / Create User Method

![User Serializer](https://i.imgur.com/B29mMOn.png)

### Profile View

![Profile View](https://i.imgur.com/WVKPnMA.png)

### Weather API View

![Weather View](https://i.imgur.com/zQKLVXZ.png)

### Course Model

![Course Model](https://i.imgur.com/FuFsHTx.png)

### BeautifulSoup Web Scraping Script for Courses

![beautiful Soup](https://i.imgur.com/1JK0Oxw.png)

### Seed Courses with BeautifulSoup

![seed courses](https://i.imgur.com/TYz762F.png)

### Project URLs with rest_framework_jwt Authentication

```
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avyupskill_app.urls')),
    path('auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
    path('token/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('profile/', verify_jwt_token)
]
```

## Technology Used

- Python 3.9.0
- Django
- PostgresSQL database
- django restframework
- BeautifulSoup

## Setting up for the application

```
  python manage.py migrate
```

``` 
  python manage.py seed 
  python manage.py webscrap
```

``` 
  python manage.py runserver 
```

Or access the app LIVE via heroku / firebase at http://avyupskill.firebaseapp.com


## Main Features

- User can login or signup with django-restframework-jwt authentication.
- User can record their backcountry days with a journal entry.
- User can add comments / ratings for backcountry ski zones.
- Guests and Users can see upcoming courses, beacon parks, and backcountry zones in Colorado.

## Features in Progress

- Connect with other users to share information, plan ski days, and learn together.
- Integrate Avalanche Forecast information directly on the page.

## Contact Information

Created by [Shelley Brook](https://www.linkedin.com/in/sbrook13/)


## Link to Frontend Repo

https://github.com/sbrook13/avy-upskill-frontend

