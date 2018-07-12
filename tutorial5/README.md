# Tutorial 5 進階 models  
  
#### [完整說明請參考官方文件](https://docs.djangoproject.com/en/2.0/topics/db/models/)  
下面將會介紹`models`的  
Fields  
Options  
class Meta  
def \_\_str\_\_(self):
  
## Fields  
每個`models`的`Field`分別對應到不同的資料庫欄位型態  
這裡會介紹以下幾種`Fields`，沒介紹的應該用不太到，請自行參考官方文件  
文字類型:`CharField`、`TextField`、`EmailField`  
整數類型:`IntegerField`、`BigIntegerField`、`PositiveIntegerField`、`PositiveSmallIntegerField`  
小數類型:`FloatField`、`FloatField`  
日期類型:`DateField`、`DateTimeField`  
布林類型:`BooleanField`、`NullBooleanField`  
  
#### 文字類型  
1. ##### models.CharField(max_length=255)  
`max_length`是必要的參數，上限為255  
2. ##### models.TextField()  
為一個文字框輸入欄位，若`CharField`長度超過255則使用此類型，可以加上`max_length`參數，但只作用在`client`端，`model`及`database`不起作用。  
3. ##### models.EmailField()  
若不給參數，預設參數為`max_length=254`  
  
#### 整數類型  
1. ##### models.IntegerField()  
整數類型欄位，值的範圍為`-2147483648`至`2147483647`  
2. ##### models.BigIntegerField()  
64位元整數欄位，值的範圍為`-9223372036854775808`至`9223372036854775807`  
3. ##### models.PositiveIntegerField()  
正整數欄位，值的範圍為`0`至`2147483647`  
4. ##### models.PositiveSmallIntegerField()  
小正整數欄位，值的範圍為`0`至`32767`  

#### 小數類型  
1. ##### models.FloatField()  
浮點數欄位，因為精度問題，在數字計算上可能會有誤差。  
2. ##### models.DecimalField(max_digits=10, decimal_places=3)  
十進制欄位，通常使用在計算不可有誤差的地方，如:金額。  
需要`max_digits`及`decimal_places`這2個參數。  
`max_digits`表示此欄位允許的最大位數  
`decimal_places`表示使用幾個位數顯示小數部分  
`12345.67`有7位數，小數部分3位數  
`models.DecimalField(max_digits=7, decimal_places=3)`  


#### 日期類型  
1. ##### models.DateField()  
使用`python`的`datetime.date`為實例來表示`年-月-日`  
2. ##### models.DateTimeField()  
使用`python`的`datetime.datetime`為實例來表示`年-月-日 時:分:秒`  
2個日期類型都有`auto_now`及`auto_now_add`2個可選參數，預設皆為`False`。  
  
若設定參數`auto_now=True`，日期會在資料被新增時自動加入當下的日期時間(新增時指定日期時間無效)，新增後只有在每次使用`object.save()`才會更新日期時間，常常使用在最後編輯的時間。  
  
若設定參數`auto_now_add=True`，日期會在資料被新增時自動加入當下的日期時間(新增時指定日期時間無效)，新增後可隨意修改日期時間，通常用在記錄資料建立的時間。  
  
#### 布林類型  
1. ##### models.BooleanField()  
只有`true`或`false`的資料型態，預設為`false`，如果需要接受`null`，改用`NullBooleanField`  
2. ##### models.NullBooleanField()  
接受`true`、`false`、`null`3種資料型態，預設為`null`，使用此類型，會自動設定`null=True`參數。  
  
## Options  
上面介紹的每個`Field`，除了指定要給的參數為，還有一些參數可供選擇，這裡會介紹以下參數  
`null`  
`blank`  
`choices`  
`default`  
`help_text`  
`primary_key`  
`unique`  
`verbose_name`  
  
##### null  
`name = models.CharField(max_length=10)`  
若不指定此參數，預設值為`null=False`，若設定成`null=True`，此欄位可允許存入`null`值。  
  
##### blank  
`name = models.CharField(max_length=10)`  
若不指定此參數，預設值為`blank=False`，若設定成`blank=True`，此欄位可允許存入`空白`值。  
  
##### choices  
test  
  
##### default  
`name = models.CharField(max_length=10)`  
設定`default=''`，可指定此欄位預設值為何  
`default='低否'`表示此Char欄位預設值為`低否`  
  
##### help\_text  
test  
  
##### primary\_key  
test  
  
##### unique  
test  
  
##### verbose\_name  
test  
  