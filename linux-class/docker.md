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

# Docker
<!-- _class: lead -->

# Dockerとは

* Docker, Inc. が運用している**コンテナ**技術
* Go言語で書かれている
* **コンテナ**技術のデファクトスタンダード
* https://www.youtube.com/watch?v=wW9CAH9nSLs

# コンテナとは

* コードと依存関係をパッケージ化する単位
* アプリケーションの実行に必要な全てを含む
	* コード、ランタイム、システムツール、システムライブラリ、設定
* ローカルの開発環境から本番環境まで様々な場面で使われる

# VMとの比較

* Docker
	* Linuxのユーザランドのプロセスとしてコンテナを立ち上げる
	* コンテナ間でカーネルは共有されている
* VM
	* 抽象化されたハードウエア上にOSを乗せる

# この授業におけるDocker

* 環境を一致させる重要性
  * あらゆるソフトウエアにはバージョンがある
  * バージョン差異によって不具合が出たり出なかったりする
  * それぞれの手元にある環境およびサーバー上の環境の一致が大事

# Dockerfile
* Dockerコンテナのイメージのビルド手順を定義するファイル
	* ベースイメージの指定
	* パッケージのインストール
	* ファイルのコピー
	* 環境変数の設定

# devcontainer
* Dockerコンテナ内でVS Codeの開発環境を起動
	* Dockerfile
	* devcontainer.json
* 全員の開発環境が一致する
