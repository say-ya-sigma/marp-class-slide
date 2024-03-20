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

# ファイル操作コマンド

# cpコマンド
copy
```bash
cp -i # 事故防止、cpやmvやrmは非常に事故が起きやすい。
cp -r # 再帰的にディレクトリ内をコピー
cp -p # ファイルのメタ情報ごとコピー
```

# mvコマンド
move
```bash
mv -i # 事故防止
mv -f # -fは多くのコマンドでforce(強制)の意味で使われて便利だがお行儀が悪いということになっている。
```

# rmコマンド
remove
```bash
rm -i # 事故防止
rm -f # 強制的に削除
rm -r # 再帰的に削除
```

# ディレクトリ操作コマンド

# pwdコマンド
print working directory
現在居るディレクトリのこと、working directory(作業ディレクトリ)は頻出ワード
```bash
pwd
```
# cdコマンド
ｃhange directory
```bash
cd /home # 絶対パス
cd relativePath # 相対パス
cd .. # .. は一つ上位のディレクトリを表す
```

# 絶対パスと相対パス
* 絶対パス
	* `/home` のような、最上位のルートディレクトリを基準とした指定。
* 相対パス
	* `./relativePath` `relativePath` のような、現在のディレクトリを基準とした指定。

# 特別なディレクトリ
* `.`  現在のディレクトリを表す
* `..` 現在のディレクトリの親のディレクトリを表す
* `~` ログイン直後にユーザーが必ずいるホームディレクトリを表す。
* `/` 最上位階層であるルートディレクトリを表す。システムが動くために必要な安易に触ってはいけないファイルが沢山ある。

# mkdirコマンド
make directory
```bash
mkdir newDir
mkdir -p parent/child
```

# rmdirコマンド
remove directory
```bash
rmdir emptyDir
```
中が空でないと削除できない

# ファイルの内容を表示

# catコマンド
concatenate(連結)
```bash
cat textFile
cat -n textFile # 行数を表示する
cat texts/*　# 複数ファイルを選択すると連結して表示される
```

# moreコマンド
* `スペース` 次のページに進む
* `b` 前の一画面に戻る
* `f` 次の一画面に進む
* `/単語` 単語を検索。 n キーで検索結果をジャンプ。
* `q` ページャコマンドを終了 (quit) します。

# lessコマンド
* `スペース` 次のページに進む
* `b` 前の一画面に戻る
* `f` 次の一画面に進む
* `↑` 前の行に進む
* `↓` 次の行に進む
* `/単語` 単語を検索。 n キーで検索結果をジャンプ。
* `q` ページャコマンドを終了 (quit) します。

# 検索

# findコマンド
```bash
find findDir/ -name wantedFile
find findDir/ -name '*.md' # nameにはワイルドカードが指定できる
find findDir/ -name '*.md' | xargs wc -l # xargsを使ってパイプすると例えばマッチするファイルの行数を数えられる。
find nestedFindDir/ -name '*.md' -type f # directoryを除くこともできる
```
 