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

# 実際の開発では<br>どういう構成なのか
<!-- _class: lead -->

# デプロイ先を考える
* アプリケーションはどこにデプロイするか
  * AWS
  * GCP
  * Azure
  * それ以外

# デプロイ先から繋ぐDB製品を探す
* GCPなら
  * CloudSQLを使おう
  * AlloyDBも可能性あるな
* 出来る限り運用コストの低いものを選ぶ
  * マネージドって書いてあるやつは楽だぞ

# 互換性のあるOSSのDBの<br>Dockerイメージを探す
* DBは大体Dockerに閉じ込める
* クラウドのマネージドなRDB製品は大体互換DBが書いてある

# ローカルと各種環境にDBを用意する
* ローカルはDockerでDBを用意
* 各種環境ごとのDBを用意する
  * dev環境
  * stg環境
  * prd環境

# 補足 dev環境 stg環境 prd環境

* dev環境は開発部が使う環境
  * ローカルでは検証できない動作の検証
* stg環境は社内で使う環境
  * CSの人たちが使う環境
  * 新しい機能のテスト
  * 商談の際のデモ
* prd環境はお客さんが使う環境
  * 個人情報いっぱい
