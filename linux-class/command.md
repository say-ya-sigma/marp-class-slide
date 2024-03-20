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

# ファイルには権限がある
* rwx(read write execute)
* user:group
* 最も基本的なセキュリティ

# ファイルにはメタ情報がある
* 使用している容量
* 最終更新日

# lsコマンド
```bash
ls
ls -l # ファイルには権限 rwx(read write execute) と user:group がある。容量や最終更新日も表示される。
ls -a # dot fileと呼ばれる先頭に.がついているファイルがある。通常のlsコマンド等から除外される。何かのソフトウエアの設定ファイルなどがこの形式で書かれる。
```

# ドットファイル
* システムの設定等が格納されていることが多い
* 通常のファイル表示では隠される
* `.bashrc`
	* `bash` が立ち上がる度に実行されている

