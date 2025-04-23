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

# DBの掃除
* 一度DBの掃除をします。
  * make truncate
  * make drop
* 掃除した後、新たにmigrateします
  * make migrate

# モデル定義
* BookCategoryのSQL Alchemyのモデルを定義する
  * orm/models/BookCategory.py

# モデルをalembicに登録
* マイグレーションのターゲットファイルを編集してBookCategoryを編集する
  * migrations/migrate_target.py


# BookCategoryマイグレーション
* BookCategory追加のマイグレーションを生成する
  * make generate-migration m=create_book_categories
* BookCategory追加のマイグレーションを実行する
  * make migrate

# seederを書く
* BookCategoryのSeederを書いてrunコマンドに登録する
  * orm/seeders/book_category_seeder.py
  * orm/seeders/run.py

# seederを実行
* BookCategoryのSeederを含んだseederを実行する
  * make seed

<!--start-->
# 追加コード
* コードを追加したので更新お願いします。
  * cd ~/dev/manage-books
  * git checkout .
  * git clean -f -d
  * git pull

# DBの掃除
* 一度DBの掃除をします。
  * make truncate
  * make drop
* 掃除した後、新たにmigrateします
  * make migrate

# エンティティ定義
* 以下を定義する
  * entity/book/category/BookCategory.py
  * entity/book/category/BookCategoryId.py

# モデルにエンティティを返す関数を追加
* ユースケースにはエンティティの形で渡すルール
  * orm/models/BookCategory.py

# リポジトリを作る
* BookCategoryのリポジトリを作る
  * repository/BookCategoryRepository.py

# リポジトリメソッドを作成する
* 特定のIDのBookCategoryを返すリポジトリメソッドを作成する
  * repository/BookCategoryRepository.py

# DI
* リポジトリのインターフェースと実装をバインドする
  * dependency.py

# サービスメソッドを作成する
* 特定のIDのBookCategoryを返すサービスメソッドを作成する
  * service/BookCategoryService.py

<!--start-->
# 追加コード
* コードを追加したので更新お願いします。
  * cd ~/dev/manage-books
  * git checkout .
  * git clean -f -d
  * git pull

# Requestを書く
* APIのRequestを書く
  * presentation/api/book/category/requests/\_\_init\_\_.py
  * presentation/api/book/category/requests/get_category.py

# Responderを書く
* APIのResponderを書く
  * presentation/api/book/category/responders/\_\_init\_\_.py
  * presentation/api/book/category/responders/get_category.py

# Actionを書く
* APIのActionを書く
  * presentation/api/book/category/actions/\_\_init\_\_.py
  * presentation/api/book/category/actions/get_category.py

# routeを書く
* APIのrouteを書く
  * presentation/route.py

# testを書く
* APIの疎通を確認するためテストを書きます
  * test/api/get_category_test.py

# testを実行する
* pytestを実行する
  * make test