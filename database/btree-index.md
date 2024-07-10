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

# インデックスとは何か
* データベース内のデータへのアクセスを高速化するためのデータ構造
* 通常、キーとそのキーに対応するデータの位置情報から構成される
* 一つ以上のカラムに基づいて作成される
* データベース管理システム（DBMS）がインデックスを管理する
* テーブルの外部に保存される

# PostgreSQLにおける確認方法
* psqlで`\di`コマンド
* psqlで`\d likes`コマンド
* Database Clientのindex項目
* など

# btreeインデックス
* 1970年に登場
* 10年経たないうちに「普遍的」とまで呼ばれるように
* ほとんど全てのRDBにおいて標準的なインデックスの実装
  * MySQL
  * PostgreSQL

# btreeインデックスの特徴1
* キーと値をキーでソートされた状態で保持する
* DBを固定サイズの「ページ」に分割する
  * ページは一度に読み書きされる単位
  * ページサイズは通常4KB
  * 各ページは「アドレス」で識別できる

# btreeインデックスの特徴2
* ページからページへ「参照」を持てる
  * 1ページ内の子ページへの参照数を分岐係数と呼ぶ
  * 任意の数の分岐を持つツリー構造になる
* ツリーはバランスが保たれる
* ツリーの深さはO(log n)
  * ほとんど3レベルから4レベル
  * ページサイズが4KBで分岐係数が500のツリーは最大で256TBを保存できる

# btreeの参考実装を見てみよう
* 小さいBTree
* BTreeの成長の様子
* バランスが取れて行く様子

# インデックスを貼ってみよう

# EXPLAINを使ってSELECTコマンドを解析してみる
```sql
EXPLAIN ANALYZE SELECT * from likes WHERE post_id=3;
```

# インデックスを貼ってみる
```sql
CREATE INDEX likes_post_id_index ON likes (post_id);
```

# EXPLAINを使ってSELECTコマンドが改善していることを確認する
```sql
EXPLAIN ANALYZE SELECT * from likes WHERE post_id=3;
```
