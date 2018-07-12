# Tutorial 1 建立 Django 專案  
  
## Step 1  
安裝[Python3](https://www.python.org/)  
  
## Step 2  
為專案建立虛擬環境  
##### Windows  
`python -m venv your_venv_name`  
#### Linux and OS X  
`python3 -m venv your_venv_name`  
  
## Step 3  
啟動虛擬環境  
#### WIndows  
`your_venv_dir\Scripts\activate`  
#### Linux and OS X  
`source your_venv_dir/bin/activate`  
  
啟動虛擬環境成功，command line 前面會出現`(your_venv_name)`  
如果要停用虛擬環境，在 command line 輸入`deactivate`  
  
## Step 4  
安裝 Django  
`pip install django`  
  
## Step 5  
創建 Django 專案  
`django-admin startproject your_project_name`  

## Step 6  
轉換 command lind 路徑至剛剛創建的專案  
`cd your_project_name`  
  
啟動專案  
`python manage.py runserver`  
  
打開瀏覽器輸入 `localhost:8000`  
如果看到歡迎畫面就表示專案創建成功  
在 command line 按下`CTRL + C`組合鍵，可停止專案運行  
  
此時專案資料夾結構應該會長這樣  
project  
├─project  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─\_\_init\_\_.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─settings.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─urls.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─wsgi.py  
└─manage.py　　