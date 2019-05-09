
# URLディスパッチャとURLconf


configのurlsディスパッチャーを追加する。    
accountsアプリにurlsを追加する。    
viewに基本汎用viewを追加する。    
TEMPLATESを追加する。    


```py:setting.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


```
http://127.0.0.1:8000/accounts/index/
```

