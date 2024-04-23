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

<style scoped>
section.lead h1 {
  text-align: center;
  font-size: 90px;
}
</style>

<!-- _class: lead -->
# macOSでの<br>Gitインストール手順

# Gitとは？

* バージョン管理システムの一つ
* ソースコードの変更履歴を管理・追跡する

# インストール手順

1. Homebrewのインストール
2. Homebrewを使用してGitをインストール
3. Gitのバージョンを確認

# 1. Homebrewのインストール
公式サイトの通り [https://brew.sh](https://brew.sh)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

# 実行後指示された通りパスを通す
```
==> Next steps:

Add Homebrew to your PATH in /Users/hoge/.zprofile:
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```
下の二行がコマンド
```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

# 補足 パスって何？

* コマンドを実行するとき
  1. コマンドが入力される
  1. **オペレーティングシステム（OS）は実行すべきプログラムを特定する**
  1. コマンドが実行される

* 2に必要な環境変数が「PATH」

# 補足 環境変数って何？

* OSはプログラムの実行に必要な変数を多数管理している
* envコマンドを打つと現在管理している環境変数が見れる

# 環境変数を見るコマンド
```bash
env
echo $PATH #現在のPATHが見れる
```
# 補足 `echo` って何？

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

文字列を与えると文字列を返すコマンド

# 補足 `eval` って何？

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

コマンド等を与えてそれを評価する（実行する）

# 補足 `$()` って何？

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

`()` の内部を評価（実行）して返り値を文字列として展開する

# 補足 `>>` って何？

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

コマンドの出力先をファイルに
* `>` でファイルを置き換え
* `>>` でファイルに追記

# 補足 `.zprofile` って何？

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/hoge/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

シェル（その黒い画面）を起動するたびに実行されているファイル

# 2. Homebrewを使用して<br>Gitをインストール

```bash
brew install git
```

# 3. インストールが完了したらバージョンを確認

```bash
git --version
```
