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

<style scoped>
section.lead h1 {
  text-align: center;
  font-size: 90px;
}
</style>

# SQLクライアント
<!-- _class: lead -->

# SQLクライアントの役割

 **データベース接続**: データベースの接続情報を保持して管理できる。
* **SQLクエリ実行**: GUIからSQLクエリを入力できる。
* **結果表示**: 実行されたクエリの結果を表示できる。
* **スキーマブラウジング**: データベース内のスキーマ構造を閲覧できる。
* **データ編集**: テーブル内のデータを直接編集できる。

# プロダクト紹介<br>vscode-database-client

* cweijan/vscode-database-client
  * VSCodeの拡張としてSQLクライアント機能を利用できる。
  * フリープラン/プレミアムプランがある。
  * GitHubで開発されていた（？）
  * フリープランでも多くの機能が使える。

# プロダクト紹介<br>DBeaver

* DBeaver
  * 初版リリース 2011年
  * 現在まで開発が続いている
  * コミュニティバージョン/プロバージョンがある
  * コミュニティバージョンでも非常に多機能

# プロダクト紹介<br>DataGrip

* DataGrip
  * JetBrains社製のIDEに付属する
  * 多機能
  * 高品質

# vscode-database-client<br>を使ってみよう

* 自分が使っている
* インストールが手軽
* SQLToolsが代替として考えられる

# SELECTをしてみよう

```sql
SELECT * FROM users WHERE name='Alice';
```

# INSERTをしてみよう

```sql
INSERT INTO users (name, email) VALUES ('AA', 'email@example.com');
```

# UPDATEをしてみよう

```sql
UPDATE users SET name='XavierF' WHERE id=24;
```

# DELETEをしてみよう

```sql
DELETE FROM "users" WHERE "id"=24;
```
