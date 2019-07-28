
# blogぽいのを動かす

django girlsを見ながら写経    
https://tutorial.djangogirls.org/ja/
    

自分用のメモ    
django girlsはところどころ動かない状態の残ってるのでは？    
https://github.com/miyamotok0105/python_sample/tree/master/django_sample/django_girls_japan
    

# scaffold

手動で作るパターン    
https://eiry.bitbucket.io/tutorials/tutorial/crud_application.html#id2

ライブラリ使うパターン    
https://github.com/spapas/django-generic-scaffold


```
pip install django-generic-scaffold
```

view.py, models.py, scaffolding.py, templates/books/book_form.html, mysite/urls.py, settings.pyを修正。    


```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/books
```


# アーキテクチャ拡張

リポジトリレイヤー、エンティティレイヤーの追加。    


```
pip install object-mapper
```







# 参考


https://github.com/davidsylvestre/ddd-shop-python
https://github.com/johnnncodes/ddd-python-django

https://qiita.com/kotamatsuoka/items/832ffe97e2a1c19141b4


https://github.com/josecelano/ddd-laravel-sample

用語まとめてる記事
https://equal-001.hatenablog.com/entry/2016/08/21/234515

図がわかりやすい
https://qiita.com/little_hand_s/items/2040fba15d90b93fc124

ボトムアップ
https://qiita.com/kotamatsuoka/items/97dab7518f3ce3ae8355

自分メモ
https://qiita.com/miyamotok0105/private/e29d9a885c483c0b41e2