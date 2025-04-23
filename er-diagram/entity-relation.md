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

# User系のテーブル

# ユーザーの種類は2種類
- 管理ユーザー
  - 一般ユーザーを作り出せるユーザー
- 一般ユーザー
  - 本を借りるユーザー

# セッションという概念
- 数時間から数日間ログイン状態を維持する
  - ログイン時にセッションを払い出す
  - アクセス時にセッションがあればログイン状態
  - セッションが有効期限切れもしくは存在しなければログイン画面に飛ばす

# セッションはredisで管理することがある
- セッションはAPIアクセスの度に検証されるため、より頻繁にアクセスされることに適したredisなどのデータストアで管理されることも多い。高性能な分値段も高い

# 全てのテーブルにcreated_atとupdated_atをつける
- データがいつ作られたか、いつ編集されたかはデータの種類に関わらず必要になる場合が多い
- ORMがデフォルトでつけることも多い

# admin_usersテーブル
- id
- name
- email
- password
- created_at
- updated_at

# usersテーブル
- id
- name
- email
- password
- created_at
- updated_at

# admin_user_sessionsテーブル
- id
- admin_user_id
- expired_at
- created_at
- updated_at

# user_sessionsテーブル
- id
- user_id
- expired_at
- created_at
- updated_at

# 主キー
- テーブルの各レコードを一意に識別
  - 主キーはそのテーブルの中では重複しない
  - 主キーはNULLであってはいけない
  - 一般的にはidという名前になっていることが多い
  - 一般的にはDBMSによって自動でインクリメントされた番号が振られることが多い

# 外部キー
- あるテーブルの列が別のテーブルの主キーを参照する場合に使われる
- 外部キー制約を設定できる
  - 参照されるデータが存在しない場合、データの挿入や更新を防ぐ
- ER図では制約まで表現されることは稀

# エンティティを書いてみよう
- diagrams.netでエンティティを書いてみよう
  - usersテーブル
  - user_sessionsテーブル
- 主キーにはPKとつけよう
  - Primary Keyの略
- 外部キーにはFKとつけよう
  - Foreign Keyの略

# リレーションシップを書いてみよう
- リレーションシップを書いてER図を完成させてみよう
  - usersテーブル
  - user_sessionsテーブル
- ヒント: user_sessionは過去のものも含めユーザーに対して複数あるから？

# Book系のテーブル

# 同名の書籍の単品管理
- 複数冊の同名の書籍をどうするか
- 書籍のテーブルと書籍在庫のテーブルを作る
- ユーザーには書籍在庫を貸し出す

# カテゴリーはテーブルを作る
- カテゴリーテーブルを作る
- カテゴリーの表記揺れなどを防ぐ
- カテゴリー一覧などのUIにも応用できる

# booksテーブル
- id
- title
- isbn
- author
- publish_year
- publisher
- category_id
- created_at
- updated_at

# book_stocksテーブル
- id
- book_id
- stocked_date
- created_at
- updated_at

# categoriesテーブル
- id
- name
- created_at
- update_at

# エンティティを書いてみよう
- diagrams.netでエンティティを書いてみよう
  - booksテーブル
  - book_stocksテーブル
  - categoriesテーブル

# リレーションシップを書いてみよう
- リレーションシップを書いてER図を完成させてみよう
  - booksテーブル
  - book_stocksテーブル
  - categoriesテーブル
- 本に対して本の在庫は複数ある
- 本に対してカテゴリーは1つ
- カテゴリーには複数の本が属する

# LendingHistoryテーブル

# lending_historiesテーブル
- id
- book_stocks_id
- user_id
- lend_date
- return_deadline_date
- return_date
- created_at
- updated_at


# エンティティを書いてみよう
- diagrams.netでエンティティを書いてみよう
  - lending_historiesテーブル

# リレーションシップを書いてみよう
- リレーションシップを書いてER図を完成させてみよう
  - lending_historiesテーブル
  - book_stocksテーブル
  - userテーブル
