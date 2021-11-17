python -m venv venv

source venv/Scripts/activate

$ django-admin startproject mysite

$ pip install django

$ pip install django-extensions

$ python manage.py startapp movies

```django
INSTALLED_APPS = [
    # 앱
    'movies',
    # 설치
    'django_extensions'
]
```

base.html 생성/ app 내 index.html 생성

settings.py 에 'DIRS': [BASE_DIR/'templates'], 추가



프로젝트 폴더안의 urls.py 에 path('moives/', include('movies.urls')) 추가

movies앱에 urls.py 생성 

path('', views.index, name='index'),

