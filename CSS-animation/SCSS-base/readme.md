# 初見SCSS 一天開竅起手式

## 變數宣告
宣告一個變數，要使用`$`起頭，用`:`接，用`;`結束。
```scss
$variable : value ;
```
要使用這些變數，直接在CSS當中輸入即可，例如:
```scss
div{
    color : $variable ;
}
```
變數的使用，可以在許多地方使用上可以不用一直怕打錯，也不怕每個地方都不一樣，或是顏色有差無法統一變動。
```scss
$font : 'monospace' ;
$bigsize : 30px ;
$main-color : #AAAAAA ;

p{
    font-size : $bigsize ;
}
```
目前可以用的變數形式有

1. 空值，就是`null`
2. 字串，括號可用可不用，例如`安安`、`"安安"`、或是`'安安'`
3. 數值，小數是可以的，例如`3.14159`
另外，數值是可以直接在CSS當中進行計算的，例如
```scss
$num : 20px ;

h1{
    font-size : $num * 2 ;
    //那這邊字型大小會是40px
}
```
4. 布林值，也就只有`true`和`false`
5. 顏色值，可以用色票`#123456`，或是RGB`rgb(100,100,100,0.5)`，還有預設單字們
6. 設定值可以直接串連，常見像是字型就會是
```scss
$font-list: "Microsoft JhengHei", Arial, sans-serif ; 
```
### 變數預設值
變數若要讓他成為預設值，可以直接在後面輸入`!default`，例如
```scss
$num : null ;

h1{
    $num : 20px !default ;
    font-size : $num * 2 ;
    //那這邊字型大小會是40px
}
```

## 編寫方式
Sass和SCSS最有趣的地方，就是巢狀式的階層定義。
例如我們本來可能要召喚一個區塊的東西可能長這樣

![](https://i.imgur.com/WcadLtK.png)

他的CSS原來應該會是
```css
div{
  width: 200px;
  height: 200px;
  padding: 10px;
  border: 1px solid #AAA; 
}
div h1{
  font-size : 40px;
}
div p{
  font-size : 20px;
} 
```
在SCSS當中，我們可以直接將其中的`h1`和`p`直接包建去`div`程式區塊當中，就會變成
```scss
div{
  width: 200px;
  height: 200px;
  padding: 10px;
  border:1px solid #AAA;
  h1{
    font-size:40px;
  }
  p{
    font-size:20px;
  }  
}
```

### 偽元素的寫法
當你遇到偽元素的時候也能直接寫進去，利用`&`去接偽元素，再進行宣告。
偽元素則是一樣放在指定的元素下，例如:
```scss
a{
    color:red;
    &:hover{
        color:blue;
    }
    &.class{}
}
```

## Mixin 混合
通常統一style，或是常見於在不同的瀏覽器設定，都可以利用mixin這種類似function的宣告方式來使用變數。
拿個border-radiusd來試試，例如:
```scss
@mixin border-radius($radius){
  -webkit-border-radius: $radius;  // For Chrome/Safari/opera(new)
     -moz-border-radius: $radius;  // For firefox
      -ms-border-radius: $radius;  // For ie/edge
       -o-border-radius: $radius;  // For opera(old)
          border-radius: $radius; 
}
```
那我們該怎麼使用呢? 利用`@include`的方法，在我們要用的地方來宣告，例如
```scss
.box{
  width:100px;
  height:100px;
  border:2px solid #AAA;

  @include border-radius(10px);
}
```
另外你也能直接宣告預設值進去，那就會變成
```scss
@mixin border-radius($radius : 3px){...}
```
假如你是想要宣告整組style進去，也是沒有問題的，例如我這邊設定背景尺寸，就可以簡單宣告成:
```scss
@mixin bg-setting($bg-size:cover){
    background-size: $bg-size; 
    background-repeat: no-repeat;
    background-position: center;
}

.banner {
    @include bg-setting(cover);    //$bg-size:cover
}
.otehr1 {
    @include bg-setting(20px);     //$bg-size:20px
}
.otehr2 {
    @include bg-setting(contain);  //$bg-size:contain
}
```
對了，裡面若有設定預設值，是可以變動他的。

*吐槽一下，在Sass當中， `@include` 只要用 `+` 就可以了，像下面這樣*
```scss
@mixin bg-setting($bg-size:cover)
    background-size: $bg-size
    background-repeat: no-repeat
    background-position: center

.banner
  +bg-setting(cover)    //$bg-size:cover
.otehr1
  +bg-setting(20px)     //$bg-size:20px
.otehr2
  +bg-setting(contain)  //$bg-size:contain
```

## Extend 繼承/擴充
Extend的意思是，當我要沿用style設定時，你可以利用`@extend`的方式，可以省去重複輸入的困擾，而在其他style上只要輸入擴充、變動的部分即可。

看看案例，例如本來CSS是這樣寫的:
```CSS
.simple{
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.check {
  border: 1px solid green;
  padding: 10px;
  color: #333;
}

.no_check {
  border: 1px solid red;
  padding: 10px;
  color: #333;
}
```
這邊可以看到前面設定幾乎相同，那我可以整理一下變成
```CSS
.simple, .check, .no_check{
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.check {
  border-color:green;
}

.no_check {
  border-color:red;
}
```
若使用繼承方式，就可以不用把全部class召喚在同一個地方，使用的方法是`@extend styleName`，那會變成
```scss
.simple{
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.check {
  @extend .simple;
  border-color:green;
}

.no_check {
  @extend .simple;
  border-color:red;
}
```

## Function 函式
沒錯，你沒有看錯。在SCSS當中也是可以使用函式做簡單處理。
這邊給個簡單例子 讓函式內自己跑計算的話:
```scss
@function calc($num){
  return 100vw / $num ;
}

.test1{
  width: calc(2);
}
.test2{
  width: calc(3);
}
```
另外SCSS當中也內建不少輔助用的工具函式，有:
1. saturation ( $color ) : 抓取顏色飽和度
2. lightness ( $color ) : 抓取顏色亮度
3. adjust-hue ( $color , $degrees) : 更換顏色色調
4. lighten ( $color , $amount ) : 顏色調亮
5. darken ( $color , $amount ) : 顏色調暗

還有更多的內建函式可以直接上去[官網說明](http://sass-lang.com/documentation/Sass/Script/Functions.html)看看。
那要怎麼用呢?，這邊直接利用顏色調暗寫一波:
```scss
$color: #2196f3;

a {
  background-color: $color;
  padding: 10px 15px;
  &:hover {
    background-color: darken($color,10%);
  }
}
```
這邊試一下結果大概是[這樣子](https://jsbin.com/moxidoq/edit?html,css,output)。

## Import 匯入
我們可以先準備一個通用的SCSS檔案，再利用匯入的方法來使用他們。
首先我們要匯入使用的檔名，需要在前面給一個底線`_`，而在使用他們的時候，記住**不要**增加底線即可。
```scss
// _default.scss
$px:32px;
$devBG:url('https://imgs.niusnews.com/upload/imgs/default/intern/0705Scarlett/03.jpg');
```
```scss
// index.scss
@import 'default';

div{
    background: $devBG ;
}
h1{
    font-size: $px ;
}
p{
    font-size: $px / 2 ;
}
```
另外，import也能直接召喚CSS檔案，後面則直接增加路徑即可。
```scss
// index.scss
@import 'css/reset.css';
```