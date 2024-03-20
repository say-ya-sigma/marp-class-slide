---
marp: true
theme: "gaia"
header: "授業スライド"
footer: "©2024 seiya sugimoto. All rights reserved."
backgroundColor: white
headingDivider: 1
paginate: true
size: 16:9
---

# ファイルとディレクトリは階層構造になっている
* 自分の手元の環境のディレクトリ構成を管理するのもエンジニアの仕事。
* 職人で言う自分の作業場所の整理整頓。
* エンジニアなら机を汚してもファイル構造を汚さない。

# treeコマンド
```bash
tree
tree -i 
tree -f
tree -if | grep wantedFile # -ifというオプションを使うとgrepというコマンドで検索しやすい形になる。
tree -I wasteDir # -Iというオプションを使うと見たくないファイルを除外できる。
tree -I 'wasteDir|wasteDir2' # |を使うことで複数指定できる
tree -I wasteDir? # ワイルドカード
```


