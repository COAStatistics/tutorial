# Tutorial 4 建立與管理 models  

在 Django 的 models 裡，每一個 class 就是一張資料庫裡的 table 。這裡先簡單介紹如何透過 models 在資料庫新增一張 table，之後會再說明資料庫裡的欄位資料型態，在 Django 裡面如何定義。

## Step 1  
打開`app`資料夾底下的`models.py`  
預設內容應該會長這樣  
```
from django.db import models

# Create your models here.
```  
輸入以下內容新增一個 class  
```
class Profile(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
```  

## Step 2  
在 command line 輸入  
`python manage.py makemigrations`  
目的是建立一個紀錄 models 做了哪些異動的記錄檔  

之後再輸入  
`python manage.py migrate`  
目的在於使用`makemigrations`產生的記錄檔，在資料庫進行 新增/修改/刪除 table  
如果`migrate`後面沒有指定記錄檔，會以最新的記錄檔跟資料庫連結

每次修改過 models 之後，如果有異動到 table 的欄位，就要重新`makemigrations`再`migrate`一次  

## Step 3  
執行過`migrate`在資料庫建立 table 後，打開`app`資料夾底下的`admin.py`  
預設的`admin.py`內容如下  
```
from django.contrib import admin

# Register your models here.
```  
將內容修改成  
```
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Profile)
```  
這樣才能在 admin 後台看到我們剛剛新增的 table  
