from django.db import models

class Post(models.Model): #Postというモデルクラス作成
    body = models.CharField(max_length=200) #テキストフィールド作成