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

# DBとは
* データを体系的に整理
* データを効率的に管理
* データを共有し活用

# RDBとは
* リレーショナル代数という体系に基づくDB
* SQLを使って管理
* トランザクションによるDB共用時等の一貫性保証

# RDBMS
* RDB管理システム
  * Microsoft SQL Server
  * Oracle Database
  * MySQL, MariaDB
  * Postgres SQL

# テーブル
* RDBには沢山のテーブルが格納されています。それらの実際の姿はどのようなものでしょうか。確認していきましょう。

# ver1.0
* 部署コード(dept_cd: department code)を含む以下のようなデータがある。

| id | name | dept_cd |
|----|------|---------|
| 1  | 宮原 徹  | 10      |
| 2  | 吉田 紘介 | 20      |


# ver 1.1
* 吉田さんが20番の部署と100番の部署の両方に所属している。
* このように、社員は複数の部署に所属する場合がある。
| id | name | dept_cd |
|----|------|---------|
| 1  | 宮原 徹  | 10      |
| 2  | 吉田 紘介 | 20      |
| 3  | 吉田 紘介 | 100     |

# ver1.2 良くないパターン
* 部署コードに無理矢理複数の値を押し込むのは良くない。
* 部署コード20で検索した際に20, 100は引っ掛からない。
| id | name | dept_cd |
|----|------|---------|
| 1  | 宮原 徹  | 10      |
| 2  | 吉田 紘介 | 20, 100  |

# ver1.3
* 社員の表と部署の表に分ける。good.
| id | name   |
|----|--------|
| 1  | 宮原 徹  |
| 2  | 吉田 紘介 |

| id | dept_cd |
|----|---------|
| 1  | 10      |
| 2  | 20      |
| 2  | 100     |