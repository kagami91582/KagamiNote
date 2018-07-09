# (JavaScript) AJAX拯救蒼生

## 說明AJAX是什麼東西

AJAX = Asynchronous JavaScript and XML

稱為非同步的JS和XML技術，向Server端傳送請求並取回資料，在Client利用JavaScript處理來自伺服器收到的回應，就可以不用重整頁面狀態下直接載入資料。

## 接收資料格式

主要使用的接收資料，以Json和XML為主，看看下面這兩個範例

### JSON

```jsx
{
	"note": {
		"firstName": "John",
		"lastName": "Smith",
		"sex": "male",
		"age": 25,
		"address": {
			"streetAddress": "21 2nd Street",
			"city": "New York",
			"state": "NY",
			"postalCode": "10021"
		},
		"phoneNumber": [
			{
				"type": "home",
				"number": "212 555-1234"
			},
			{
				"type": "fax",
				"number": "646 555-4567"
			}
		]
	}
}
```

實際上在網路上若有支援json格式的顯示，會變成這樣

![](https://i.imgur.com/pfriLY5.png)

### XML

```xml
<note>
    <firstName>John</firstName>
    <lastName>Smith</lastName>
    <sex>male</sex>
    <age>25</age>
    <address>
        <streetAddress>21 2nd Street</streetAddress>
        <city>New York</city>
        <state>NY</state>
        <postalCode>10021</postalCode>
    </address>
    <phoneNumber>
        <type>home</type>
        <number>212 555-1234</number>
    </phoneNumber>
    <phoneNumber>
        <type>fax</type>
        <number>646 555-4567</number>
    </phoneNumber>
</note>
```

眼尖的人會發現這其實結果是相同的，只是JSON讓資料較為輕量
可以利用 https://jsonformatter.org/xml-formatter 確認一下這兩份差別

## 如何接收
### 使用jQuery的 **getJSON**
利用get去抓JSON資料，函式去抓取資料，用data去盛再去處理

![](https://i.imgur.com/HsTDC1W.png)

例如在 https://httpbin.org/ip 當中，可以看到一個有包著origin參數的IP位置，那我們要撈回來就是像這樣。(其中#ip是在html中，指定置換的位置。)

```javascript
$.getJSON('https://httpbin.org/ip',function(data){
    $('#ip').text('data.origin');
});
```

## 練習部分
*使用httpbin的資料進行測試 https://httpbin.org*

IP位置(FCC練習增加) https://kagami91582.github.io/mono-test/AJAXTest/index.html
JSON檔案 https://kagami91582.github.io/mono-test/AJAXTest/index2.html
XML檔案 https://kagami91582.github.io/mono-test/AJAXTest/index3.html
