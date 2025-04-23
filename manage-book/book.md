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

<!-- start -->
# 追加コード
* コードを追加したので更新お願いします。
  * cd ~/dev/manage-books
  * git checkout .
  * git clean -f -d
  * git pull

# Bookを作る
* BookのORMモデルを作る
  * orm/models/Book.py

# マイグレーション作成
* migrate_target.pyに登録
  * migrations/migrate_target.py
* migrationを作成
  * make generate_migration m=create_book

# マイグレーションを実行
* make migrate

# Bookのエンティティを作る
* Bookのエンティティを作る
  * entity/book/\_\_init\_\_.py
  * entity/book/BookId.py
  * entity/book/Book.py

# BookのORMモデルにto_entityを追加する
* BookのORMモデルにto_entityを追加する
  * orm/models/Book.py

