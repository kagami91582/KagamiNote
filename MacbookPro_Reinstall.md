# Mackbook Pro 重灌筆記

久違復活的Gary說個Hi，鑑於最近主力的筆電開始無法負荷了所以就有了這次計畫，順手做了筆記來放個。當然要先說個，每個電腦與設備環境，產生出來的化學效果(咦?)都不一樣，這邊就給大家做個參考，那就開始囉。

## 前因

* 本來要出差可以出國好開心
    * 順勢就準備一筆錢做stand by
    * 然而並沒有，~~不要瞎掰好嗎~~
    ![](https://i.imgur.com/S596utV.png)

* 公司加上自己的東西，256GB真的不夠用
    * 光雙OS就痛苦萬分了
    * 我還只給Windows10一個80GB空間，直接死透
    * 某損友於COSCUP云“還想灌Linux啊，下去”

* 最近SSD價格真心便宜，覺得可以衝一波
    * 絕對不是朋友安麗我，真的

## 前置準備

這次要準備的食材有

* 一個8GB以上的隨身碟
    * 這個會拿來做macOS的安裝碟
    * 不要想著用web recovery，真的危險，原因我後面說
    * 這故事告訴我們，先做功課還是可以玩踩地雷

* 一個你要下手的SSD
    * 這邊選擇的是來自~~國際牙膏大廠~~INTEL 660P 1TB版本
        * ~~INTEL會恨死這句台詞~~
    * 購入價格3000台幣，天價屋也差不多
    ![](https://i.imgur.com/GEwL3mm.jpg)
    * 注意一下，若要買SSD給Macintosh電腦用一定要買特殊規格的SSD
        * 嘿對，我們不一樣，沒有的話就去弄個轉接頭吧
        * 所以這次準備一顆200塊有得找的轉接頭，來自_皮的台中賣家

* 一隻五星螺絲起子
    * 還要找**1.2**的，**1.2**，**1.2**，這真的很重要
    * 開Macbook機殼用的
    * 認識我的都知道我有工具盒，怎麼還要買？
        * 嘿對，我那盒小黃沒這個，我可撥仔
    * 你會看到什麼_華，_華，元_等等的電子材料行很多都放0.8，別買，那給哀鳳拆的
    * 大概長這個樣子，~~這邊不是業配~~
    ![](https://i.imgur.com/pRa9PKg.jpg)
    
* 一台Macbook
    * ~~你在講幹話嗎?~~
    * 這邊的Mac是2015年初版(三代末)的Macbook pro 13"
        * 來自朋友這邊的安心提醒，四代MBP不能換硬碟
    * 先曬人權圖，大致這樣
    ![](https://i.imgur.com/VHSAXnY.png)


## 簡單步驟

1. 準備個8GB以上隨身碟，去用 [磁碟工具程式] 格式化

2. 去App Store抓MacOS，都抓，都可以抓

3. 開terminal自己下指令
    
    * 在10.14(Mojave)輸入
    
    ```
    $ sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/隨身碟名稱
    ```
    
    * 若有跳出清除提醒，大概是下面這樣時，給`Y`
     
    ```
    To continue we need to erase the volume at /Volumes/TRANSCEND.
    If you wish to continue type (Y) then press return: _
    ```

    * 出現`Install media now available at "/Volumes/Install macOS Mojave"`時即可

4. 關機，然後重新開機，立刻按下<kbd>option</kbd>(非mac鍵盤為<kbd>alt</kbd>)不放，直到boot menu出現

5. 選擇剛剛做好的開機碟，接下來就是基本安裝進度了。

## 所謂的“重新安裝”

1. 換上準備好的硬碟(這邊就是剛剛說的SSD了)

2. 插上剛剛做好的USB安裝碟，開機鈕一按下立刻按住<kbd>option</kbd>(非mac鍵盤為<kbd>alt</kbd>)不放

3. 進到開機選單，選擇install macOS disk

4. 進到畫面應該就是macOS工具程式了，先做SSD格式化吧，選擇“磁碟工具程式”
![](https://i.imgur.com/tSAOllv.jpg)

5. 從左邊選擇要安裝的目標碟，這裡當然是選那個愉悅的**1TB**
名稱都可以，不是重點，重要的是一定要用APFS(按MacOS擴充格式(日誌式)就對了)
![](https://i.imgur.com/D8Xd7SQ.jpg)
![](https://i.imgur.com/K6pQsE4.jpg)

6. 完成後就直接關掉視窗即可，回到工具程式選擇“安裝macOS”
![](https://i.imgur.com/jvOPTJb.jpg)

7. 接下來就是一直**繼續**的旅程了
![](https://i.imgur.com/ErNOLnj.jpg)
![](https://i.imgur.com/Bh226fR.jpg)
這邊按“同意”
![](https://i.imgur.com/1qvcX5z.jpg)

8. 磁碟選擇選剛剛的目標碟
![](https://i.imgur.com/UHCjMC3.jpg)
特別注意的是，若沒接上電源線會跳出提示訊息，若你覺得你的電量可以頂住就按“繼續”沒有關係
![](https://i.imgur.com/bLEEdVn.jpg)

9. 接著就放著，放到出現設定畫面的語言選項就完成了
![](https://i.imgur.com/54UL39S.jpg)

## 中間發生的小插曲
硬碟部分是找我高中就認識的朋友(那人是不是在台中英才NOVA的2樓啊)幫忙推個，~~絕不是因為我沒什麼想法~~。在SSD準備好加上轉接頭開機的時候，才想到沒有的話他會用web recovery方式啟動。

你以為這樣就可以安穩開進去工具程式，然後就一路大順暢了?

並沒有，我開了工具程式，選了磁碟工具，然後你猜怎著，**他沒找到那1TB的SSD**。一開始以為是SSD抽到籤王，馬上拿朋友店裡另外一台電腦開BIOS進去看，他是**有讀到的**。

這時和朋友討論，那這樣下去只有一種可能，就是那轉接頭是壞的，不過那時候NOVA也打烊了所以決定之後回來試就先收手。

現在想想還好沒有對那顆轉接頭開刀，不然這文是出不來了。

失望之餘就想說先做那USB碟之後再想辦法，然後他就讀到了，那時我的反應大概就是茱莉亞羅勃茲吧。
![](https://i.imgur.com/Hv3dMzl.png)


## 結尾
以上，大概就是這次更換硬碟的旅程了，1TB爽用之餘之後還要加上工作用的Windows10以及Ubuntu18.04了，那就先這樣，之後有後續會上來跟大家說的(揮手)。
![](https://i.imgur.com/G4fzvO3.jpg)

> 最後更新：2019.08.25 2:09am

