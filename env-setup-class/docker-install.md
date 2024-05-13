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

<style>
section.lead h1 {
  text-align: center;
  font-size: 90px;
}
</style>

# Dockerのインストール
<!-- _class: lead -->

# brew install --cask
brewでインストールしたい
https://formulae.brew.sh/cask/docker
```bash
$ brew install --cask docker
```

# homebrew-caskとは
* GUIアプリケーション向けのHomebrewの拡張
* アイコンをドラッグしてインストールしなくて済む
  * 操作ミスをなくす
  * 手元の環境構築のコード化

# caskでインストールすると入るパッケージ
* Docker
* Docker Desktop
* Docker Compose

# launchpadを開いてDockerを開こう
* Dockerと書かれたアイコンをクリック
  * Docker Desktopが開く
  * 規約にAccept
  * サーベイ(アンケート)をスキップ
  * Docker Hubへのログインは一旦スキップ
  * ダッシュボード画面になったら準備完了
