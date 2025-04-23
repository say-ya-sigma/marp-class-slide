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

# ここからの進め方
1. ER図を描く
2. テーブルごとに以下を繰り返す
  1. DBスキーマに落とす
  2. テストデータを入れる
  3. APIを作る

# ER図を描く
* ER図を描く
  * book_categories
  * books
  * book_stocks

# note: book_categoriesテーブル
* book_categories
  * id
  * name
  * created_at
  * updated_at

# note: booksテーブル
* books
  * id
  * title
  * author
  * isbn
  * publisher
  * created_at
  * updated_at

# note: book_stocksテーブル
* book_stocks
  * id
  * book_id
  * stocked_date
  * created_at
  * updated_at

# note: 以下のような関係になる
* book_categories:books
  * 1:多
* books:book_stocks
  * 1:多

# note: 実戦では設計段階でレビューが入る
* 抜け漏れがないか
* リレーションシップは妥当か
* そのデータベースで仕様が満たせるか

# book_categoriesテーブルからやっていく
* book_categories
  * id
  * name
  * created_at
  * updated_at

# git pull
* コードを追加したので更新お願いします。
  * cd ~/dev/manage_books
  * git pull
  * make down
  * make build
  * make up

# create_at, updated_atの共通化
* Mixinを定義する
  * @declared_attrデコレータを使う

# Mixinを使ってUserを修正する
* 先ほど定義したMixinでUserの定義を修正する
  * 全モデルに対してこれを行うのでBase経由で適用する

# User修正のマイグレーションを生成する
* make generate-migration m=add_timestamps
* alembic revision --autogenerate -m "add_timestamps"

# マイグレーションが通らないのでtruncateコマンドを実行する
* make truncate

# User修正のマイグレーションを実行する
* make migrate
* alembic upgrade head

# Seederを実行する
* make seed
