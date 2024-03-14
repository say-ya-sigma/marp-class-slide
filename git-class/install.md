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

- バージョン管理システムの一つ
- ソースコードの変更履歴を管理・追跡する

# インストール手順

1. Homebrewのインストール
2. Homebrewを使用してGitをインストール
3. Gitのバージョンを確認

# 1. Homebrewのインストール
公式サイトの通り [https://brew.sh](https://brew.sh)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
※ 実行後指示された通りパスを通す

# 2. Homebrewを使用して<br>Gitをインストール

```bash
brew install git
```

# 3. インストールが完了したらバージョンを確認

```bash
git --version
```
