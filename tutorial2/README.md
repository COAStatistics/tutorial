# Tutorial 2 建立 Django APP  
  
## Step 1  
在 Django 專案根目錄輸入  
`django-admin startapp your_app_name`  
此時專案結構應該會長這樣　　
project  
├─app  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─migrations.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─\_\_init\_\_.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─\_\_init\_\_.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─admin.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─apps.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─models.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─tests.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─views.py  
├─project  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─\_\_init\_\_.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─settings.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─urls.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─wsgi.py  
└─manage.py　　
  
## Step 2  
打開`settings.py`　　
找到`INSTALLED_APPS`  
將剛剛創建的 APP 加入到`INSTALLED_APPS`底部變成  
```
INSTALLED_APPS = [
	...,
    'your_app_name',
]
```  
  
若想將顯示語言改為繁體中文，在`settings.py`內，找到`LANGUAGE_CODE`，將`en-us`改成`zh-hant`  
```
LANGUAGE_CODE = 'zh-hant'
```  
  
要修改時區變成台北時間，一樣在`settings.py`內，找到`TIME_ZONE`，修改成`Asia/Taipei`  
```
TIME_ZONE = 'Asia/Taipei'
```  
