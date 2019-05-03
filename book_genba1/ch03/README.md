
# プロジェクト構成

## プロジェクトを作ってみる


Pythonでは__init__.pyを持ってるとパッケージとして識別。Python3.3以降は必須ではなくなった。    


プロジェクト作成    


```
django-admin.py startproject mysite
```


```
cd mysite
python manage.py startapp accounts
```


```
tree
.
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── mysite
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   └── settings.cpython-35.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


```
mkdir accounts/static
mkdir accounts/static/accounts
mkdir accounts/static/accounts/images
touch accounts/static/accounts/images/no-image.png
```


これで作るとstaticの場所がappの下に入るので、ちょっと良くない。    

## ベストプラクティス1


```
mkdir mysite
cd mysite
django-admin.py startproject config .
python manage.py startapp accounts
mkdir static
mkdir static/accounts
mkdir static/accounts/images
touch static/accounts/images/no-image.png
mkdir templates
mkdir templates/accounts
touch templates/base.html
touch templates/accounts/login.html
```

## その他

djangoをシェルで実行もできるよ    


```
python manage.py shell
```

