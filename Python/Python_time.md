# datetime 時間日期從這裡抓

## 開始之前

datetime再說也是使用python內建函式庫裡的，所以一樣要先匯入：

```python
import datetime, time
```

## 使用方法

1. <kbd>datetime</kbd> datetime.now():目前的日期與時間

```python
>>> datetime.datetime.now()
# datetime.datetime(2018, 8, 7, 16, 24, 43, 466321)
>>> 
``` 

2. <kbd>time</kbd> time():目前日期時間的timestamp值

```python
>>> time.time()
# 1533629765.1890395
``` 

3. <kbd>time</kbd> localtime()

```python 
>>> time.localtime()
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

4. <kbd>datetime</kbd> timedelta()

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
* 一天有 $ 60 \cdot 60 \cdot 24 = 86400 $ 秒
* 一秒等於 1,000,000 微秒

舉個例子，直接扣一毫秒就可以看到秒與微秒的極限：
```python
counter = datetime.timedelta(microseconds=-1)
print(counter)
# -1 day, 23:59:59.999999
print(counter.days, counter.seconds, counter.microseconds)
# -1 86399 999999
```