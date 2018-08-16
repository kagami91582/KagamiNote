# datetime 時間日期從這裡抓

## 開始之前

datetime再說也是使用python內建函式庫裡的，所以一樣要先匯入：

```python
import datetime, time
```

## 使用方法

#### <kbd>datetime</kbd> datetime.now():目前的日期與時間

```python
datetime.datetime.now()
# datetime.datetime(2018, 8, 7, 16, 24, 43, 466321)
``` 

#### <kbd>time</kbd> time():目前日期時間的timestamp值

```python
time.time()
# 1533629765.1890395
``` 

#### <kbd>time</kbd> localtime()

```python 
time.localtime()
# time.struct_time(
#   tm_year=2018, 
#   tm_mon=8, 
#   tm_mday=7, 
#   tm_hour=16, 
#   tm_min=21, 
#   tm_sec=53, 
#   tm_wday=1, 
#   tm_yday=219, 
#   tm_isdst=0
# )
```

#### <kbd>datetime</kbd> timedelta()

```python
today = datetime.datetime.now()
print(today)
# datetime.datetime(2018, 8, 7, 16, 29, 37, 809224)

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
# datetime.datetime(2018, 8, 8, 16, 29, 37, 809224)
```

值得注意的是，括弧內可以使用的只有**days(日)，seconds(秒)，microseconds(微秒)**，而他們的範圍是：
* 可使用的天數幾乎無限，正負99,999,999天
* 一天有 `60*60*24 = 86400` 秒
* 一秒等於 1,000,000 微秒

舉個例子，直接扣一毫秒就可以看到秒與微秒的極限：
```python
counter = datetime.timedelta(microseconds=-1)
print(counter)
# -1 day, 23:59:59.999999
print(counter.days, counter.seconds, counter.microseconds)
# -1 86399 999999
```

#### <kbd>datetime</kbd> isoweekday():回傳星期日期
```python
today = datetime.datetime.now()
today.isoweekday()
# 2  <--編輯的時候是星期二
```

## 日期與時間戳的轉換

#### 從 datetime 到 timestamp
要讓datetime轉成timestamp，首先要先確認手上資料的格式必須是像上面試過的`time.localtime()`輸出結果一樣再往下做。

別急著拉回去看那是什麼畫面，大概長這樣：
```python
time.struct_time(tm_year=2018,tm_mon=8,tm_mday=7,tm_hour=16,tm_min=21,tm_sec=53,tm_wday=1,tm_yday=219,tm_isdst=0)
```

假設目前手上有個時間是`2018.3.6 22:34:56`，先利用`time.strftime()`轉化出來：

```python
data = time.strftime('2018.3.6 22:34:56','%Y.%m.%d %I:%M:%S')
```

等等，後面這是什麼鬼？python要給它格式才會知道你剛剛打的這一串日期是什麼，這些格式碼大概有：
* %y : 年(兩位數)
* %Y : 年(四位數)
* %m : 數字月份
* %b : 英文月份(Jan~Dec)
* %B : 英文月份(January~Decenber)
* %d : 月份天(也就是1~31日)
* %j : 年份天(1~366天)
* %H : 時(24小時制)
* %I : 時(12小時制)
* %p : AM/PM
* %M : 分
* %S : 秒
* %w : 數字星期(星期天為0~6)
* %a : 英文簡化星期(Mon~Sun)
* %A : 英文完整星期(Monday~Sunday)
* %U : 一年中的星期数(0~53)，星期日開始
* %W : 一年中的星期数(0~53)，星期一開始
* %Z : 時區
* %% : %，對，就是%


#### 從 timestamp 到 datetime

至於要timestamp轉成datetime形式倒是簡單許多，大概有下面幾種
* `time.localtime(timestamp)`
* ``

```python
# datetime轉timestamp

# timestamp轉datetime

```