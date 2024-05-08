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

# makeコマンドとは

* UNIXやLinuxなどのOSで利用可能なビルドツール
* ソフトウェアのビルドプロセスを自動化する
* Makefileと呼ばれる特別なファイルを読み込みタスクを実行する

# makeのコマンドランナーとしての使用

* makeは本来ビルドツール
* 汎用コマンドランナーとしても便利に使うことができる
* Makefileに任意のコマンドやスクリプトを記述し、makeコマンドから呼び出せる
* Develop Environment as Code （造語）

# コマンドランナーとしてのmakeの利点

* プロジェクトのメンバー間で実行手順を統一できる
* makeコマンドは多くのUnix/Linuxシステムで利用可能なため、移植性が高い
  * 非常に歴史のあるコマンド
  * 多くのOSに標準搭載されている
  * コマンドの補完


# make開発の経緯

* 初期のUNIXシステム
  * シェルスクリプトを使ってビルドプロセスを自動化
  * スクリプトの管理が複雑になりビルドツールの開発に迫られる
* 1976年、Stuart Feldmanがmakeが開発、UNIXシステムに導入

# 様々な実装

* GNU make
* BSD make
* Microsoft NMAKE
* makeを発展させたツール
  * CMake
  * Antなど
