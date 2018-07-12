# Tutorial 3 管理後臺 ADMIN  
  
## Step 1  
要創建使用者帳號，需先在資料庫建立使用者的 Table ，在 command line 輸入  
`python manage.py migrate`  
  
## Step 2  
待 Table 創建完成之後  
輸入`python manage.py createsuperuser`建立管理員帳號  
  
依提示輸入管理員帳號、信箱地址、密碼、確認密碼  
完成後輸入`python manage.py runserver`啟動專案  
  
## Step 3  
打開瀏覽器，在網址輸入`localhsot:8000/admin`進入後臺登入頁面  
輸入剛剛建立的管理員帳號密碼登入