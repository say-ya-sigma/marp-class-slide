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

# リポジトリ紹介
* Pythonを使ったバックエンド
* クリーンアーキテクチャを採用

# 技術スタック
* ORM: SQL Alchemy
* Web Framework: Flask (FastAPIでも良かったかも)
* Validation Tool: Pydantic
* Linter & Formatter: Ruff
* Package Management: Poetry (uvの方が良いかも)
* Test: Pytest
* DI: Injector
* DB: PostgreSQL

# manage-booksをcloneする
```bash
cd ~/dev
git clone https://github.com/say-ya-sigma/manage-books.git
```

# dockerを立ち上げる

# make upする
```bash
cd manage-books
make up
```

# vs codeでmanage-booksを開く

# dev container
* vs code機能
* ディレクトリを開発用のdocker containerで開くことができる
  * vs codeのプラグインが参照する環境がdocker containerの環境になる
  * vs codeで開くターミナルがdocker container内のターミナルになる


# パッケージのインストール
* vs codeのターミナルでmake installする
```bash
make install
```

# サーバー起動
* vs codeのターミナルでmake flask-upする
```bash
make flask-up
```

# hello world
* localhost:8080にアクセスする
* hello-worldが表示される。

# APIを叩いてみる
* localhost:8080/user/1にアクセスする
  * エラーが出る
  * DBの用意が出来ていない

# DBを用意する
* DB用のコンテナは既に立ち上がってる
* vs codeのターミナルでmake migrateする
  * DBのテーブルのスキーマなどが定義される

# DBに検証用のデータを入れる
* vs codeのターミナルでmake seedする
  * 検証用のデータが入る

# APIを叩いてみる
* localhost:8080/user/1にアクセスする
  * 値が返って来る

# ディレクトリ/ファイル紹介
* `app/`
  * アプリケーションのコードが入っています。
* `docker/`
  * `docker` から使用するファイルが入っています。
* `README.md`
  * そのリポジトリで最初に読むべきファイルです。


# ディレクトリ/ファイル紹介
* `Makefile`
  * コマンドランナとして使っています。
  * 実行すべきコマンドが分からなくなった時に読むチートシートとしても使えます。
* `compose.yml`
  * docker composeで立ち上がるコンテナやその他のリソースが書かれています。

# `app/entity/` ディレクトリ
* クリーンアーキテクチャのエンティティ(ドメイン)
* また、エンティティを構成する値オブジェクトが置かれています
* `pydantic` で書かれています

# `app/error/` ディレクトリ
* Pythonの `Exception` クラスを継承したエラークラスが置かれています。
* 基本的にPythonの生の `Exception` はコード中では使わないです。
* どんなエラークラスが raise されたかということがエラーの内容を知る手がかりになります。

# `app/migrations/` ディレクトリ
* マイグレーション用のファイルが入っています。
* マイグレーションを実行することで、DBのテーブルのスキーマなどが定義されます。
* マイグレーション用のファイルは `SQLAlchemy` のモデルファイルから自動生成できます。

# `app/orm/` ディレクトリ
* ORMのモデルが入っています。
* アプリケーションからDBへアクセスする際はORMのモデルを使います。
* DBのスキーマ定義は実質このディレクトリで行われます。

# `app/presentation/` ディレクトリ
* flaskのコントローラーが入っています。
* コントローラーはADRパターンと呼ばれるパターンで書かれています。ファットコントローラーに対処することができます。
* `Action` と `Request` と `Responder` などが入っています。

# `app/repository/` ディレクトリ
* `SQLAlchemy` のモデルを使ってエンティティを返すリポジトリクラスが入っています。
* ここがDB由来のクラスとエンティティとの境界になります。

# `app/service/` ディレクトリ
* エンティティを使ってレスポンスを構築するサービスクラスが入っています。
* クリーンアーキテクチャで言うところのユースケースに該当します。
