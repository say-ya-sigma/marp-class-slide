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


# Baseにメソッドを追加
* Baseにsaveメソッドとdeleteメソッドを追加
  * orm/settings.py

# BookCategoryのidにinit=False
* BookCategoryのORMモデルのidにinit=Falseをつける
  * orm/models/BookCategory.py

# seederを編集する
* BookCategoryのSeederにエラーが出るのでIDを取っ払う
  * orm/seeders/book_category_seeder.py

# リポジトリのメソッドを書く
* リポジトリメソッドにCRUDを追加
  * repository/BookCategoryRepository.py

# サービスメソッドを書く
* サービスメソッドを書く
  * createだけ書いた
  * service/BookCategoryService.py

# コントローラーを書く
* ADRパターンで書いた
  * createだけ書いた

# テストを書く
