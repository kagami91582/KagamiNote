# csrf_token note

## 原本預期結果

```html
<form action="" method='post'>
    <input type='hidden' name='csrfmiddlewaretoken' value='awsedrtfyguhjokpluhygtfrde'>
    ...
</form>
```

## 出現錯誤

> UserWarning: A {% csrf_token %} was used in a template, but the context did not provide the value. This is usually caused by not using RequestContext. "A {% csrf_token %} was used in a template, but the context "

## token程式碼

```python
@register.tag
def csrf_token(parser, token):
    return CsrfTokenNode()
```

```python
class CsrfTokenNode(Node):
    def render(self, context):
        csrf_token = context.get('csrf_token')
        if csrf_token:
            if csrf_token == 'NOTPROVIDED':
                return format_html("")
            else:
                return format_html('<input type="hidden" name="csrfmiddlewaretoken" value="{}">', csrf_token)
        else:
            # It's very probable that the token is missing because of
            # misconfiguration, so we raise a warning
            if settings.DEBUG:
                warnings.warn(
                    "A {% csrf_token %} was used in a template, but the context "
                    "did not provide the value.  This is usually caused by not "
                    "using RequestContext."
                )
            return ''
```

## 已知

1. 在html當中，已經在form裡加入`{% csrf_token %}`
2. 在進行渲染runserver後，在`{% csrf_token %}`並沒有轉化成html標籤，且轉換成空白
```html
<form action="" method='post'>
                          <<本來應該在的 轉化後消失
    ...
</form>
```
3. 依照上面出現錯誤訊息，在進入`CsrfTokenNode`的時候就被判定`csrf_token != True`

## 嘗試過的方法

* 在setting.py當中輸入`CSRF_COOKIE_SECURE = True` ==> **FAILED** <kbd>403</kbd>
* 在setting.py當中把`'django.middleware.csrf.CsrfViewMiddleware'`隱藏起來
  ==> 雖然成功，不過這只是把csrf機制關閉而已 ==> TEST ONLY
* 在view當中的POST return方式從`render_to_response`改成`render`
  ==> **解決 <kbd>403</kbd> 問題**
```python
#   原來寫法
    return render_to_response('comments.html', locals())
#   改成render
    return render(request, 'comments.html', locals())
```
輸出結果用原始碼看：
![](https://i.imgur.com/k6nRvre.png)

## 結論

`render_to_response`是只有進行渲染，但沒有加入django設定的部份，所以當使用到`{% csrf_token %}`時會導致直接輸出成 ` ` 。

另外`'django.middleware.csrf.CsrfViewMiddleware'`還是別隱藏起來比較好。