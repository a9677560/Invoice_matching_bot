# TOC-Project-2022-master（發票兌獎機器人）

## Outline

- [構想](#構想)
- [安裝](#安裝)
- [指令表](#指令表)
- [詳細步驟](#詳細步驟)

## 構想

由於現在人的生活都太忙碌，所以都沒什麼時間去對發票，有些幸運兒
甚至因此與千萬大獎失之交臂，令人惋惜。因此，便開發了這個對發票機器人。

## 功能

目前有以下三個功能：
- 1.查詢當期中獎號碼
- 2.查詢前期中獎號碼
- 3.兌獎功能

P.S.兌獎功能有加入人性化兌獎機制，只要輸入後三碼，就能先進行初步的兌獎。考量到發票本身的中獎機率，所以設定為對到了特獎、特別獎、或頭獎的後三碼後，才會繼續要求輸入前五碼。

## 安裝

1.使用以下指令來安裝pip 虛擬環境：
```sh
pip install -r requirements.txt
```
P.S.安裝pygraphviz時可能會遇到問題,詳情請參考此文章
[點我](https://pygraphviz.github.io/documentation/stable/install.html)

2.修改.env內的環境變數（`line_channel_secret` 和 `line_channel_access_token`）

3.開啟ngrok

4.執行 `app.py`

## 指令表
- 當期號碼
- 前期號碼
- 兌獎
- 使用說明

## 詳細步驟
##### 當期和前期號碼：
![image](https://github.com/a9677560/TOC-Project-2022-master/blob/main/img/pic1.jpg)

