# Nginx 簡易清除指南

###### Tags: <kbd>nginx</kbd>

這篇會出現，只是怕到時候不小心搞亂，導致爆死的時候，還能用暴力解，砍掉重練而成(等等)。

在那之前可先下info確定一下存放的檔案在哪裡。用brew就好了。

```
$ brew info nginx
```

出來的結果大致上會是這樣

```
nginx: stable 1.17.7 (bottled), HEAD
HTTP(S) server and reverse proxy, and IMAP/POP3 proxy server
https://nginx.org/
Not installed
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/nginx.rb
==> Dependencies
Required: openssl@1.1 ✔, pcre ✔
==> Options
--HEAD
	Install HEAD version
==> Caveats
Docroot is: /usr/local/var/www

The default port has been set in /usr/local/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.

nginx will load all files in /usr/local/etc/nginx/servers/.

To have launchd start nginx now and restart at login:
  brew services start nginx
Or, if you don't want/need a background service you can just run:
  nginx
==> Analytics
install: 34,696 (30 days), 95,063 (90 days), 408,922 (365 days)
install-on-request: 33,276 (30 days), 91,850 (90 days), 389,550 (365 days)
build-error: 0 (30 days)
```

這裡面我們只要這兩句

```
...
Docroot is: /usr/local/var/www

The default port has been set in /usr/local/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.
...
```

記住這兩個位置，接著直接砍

```
$ rm -r /usr/local/var/www
$ rm -r /usr/local/etc/nginx
```

這時候再試應該就會not found了

```
$ nginx --version
command not found: nginx
```