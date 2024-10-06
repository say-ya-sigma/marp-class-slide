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

# ORMとは
<!-- _class: lead -->

# ORMは二つの世界の橋渡しをするライブラリ
* オブジェクト指向モデル
* リレーショナルモデル

# ORMを理解することの重要性
* WebアプリケーションエンジニアはORMを介してDBを触る
* アプリケーションからSQLを直に実行するのはよくないこととされている
* ただし運用上SQLも書く

# ORMの例
* Laravelに採用されているEloquent
* Ruby on Railsに採用されているActiveRecord
* Pythonでよく採用されているSQL Alchemy
