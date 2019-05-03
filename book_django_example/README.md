
djangoのサンプルが乗ってるいい本。


```
git clone https://github.com/PacktPublishing/Django-2-by-Example
```

# e-learningのサンプル


環境を整える

```
cd Chapter12/educa
pip install Django==2.0.5
pip install django-braces --user
pip install django-embed-video --user
pip install django-memcache-status --user
pip install djangorestframework --user
pip install python-memcached --user
```

実行    

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

アクセス    

```
管理画面
http://127.0.0.1:8000/admin/
ログイン
http://127.0.0.1:8000/accounts/login/
コースを編集
http://127.0.0.1:8000/course/mine/
```


