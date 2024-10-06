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

# 概念やデータに対する考え方
<!-- _class: lead -->

# オブジェクト指向では入れ子構造がよく使われる
* ユーザーは住所を持っている
```python
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
```

# JSONという形式で表すと以下のようになる
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701"
    }
}
```

# RDBとOOPではデータに対する考え方が全然違う
* 用語
  * モデリング、モデル: データ概念の整理やそれに対する考え方
  * インピーダンスミスマッチ: 非効率の原因となる不整合、電子工学からの借用

# データの表現方法:
- オブジェクト指向: データはオブジェクトとして表現され、オブジェクトは属性（プロパティ）とメソッド（動作）を持つ。
- リレーショナルモデル: データはテーブルの行と列として表現され、行はレコード、列はフィールドを表す。

# データの構造:
- オブジェクト指向: データは階層的で、オブジェクトは他のオブジェクトを含むことができる（ネストされた構造）。
- リレーショナルモデル: データはフラットなテーブル構造で、ネストされたデータを表現するのは難しい。

# アイデンティティと参照:
- オブジェクト指向: オブジェクトは一意の識別子（オブジェクトID）を持ち、他のオブジェクトへの直接参照を持つことができる。
- リレーショナルモデル: レコードは主キーと外部キーを使用して他のレコードを参照する。これは間接的な参照方法である。

# 継承:
- オブジェクト指向: クラス継承を使ってコードとデータの再利用が可能。サブクラスはスーパークラスの属性とメソッドを継承する。
- リレーショナルモデル: 継承の概念が直接的には存在せず、継承を表現するためにはテーブルの結合や正規化を駆使する必要がある。

# 操作とクエリ:
- オブジェクト指向: 操作はメソッドとしてオブジェクトに定義され、オブジェクトの内部状態を直接操作する。
- リレーショナルモデル: データ操作はSQLクエリを使って行われ、データベース全体に対して操作を行う。

# トランザクション処理:
- オブジェクト指向: トランザクションはオブジェクトのメソッド呼び出しを通じて管理される。
- リレーショナルモデル: トランザクションはACID（Atomicity, Consistency, Isolation, Durability）特性を持ち、データベース全体の整合性を保証する。

# パフォーマンスとスケーラビリティ:
- オブジェクト指向: オブジェクトのネストや複雑な参照関係がパフォーマンスに影響を与えることがある。
- リレーショナルモデル: 正規化やインデックスの使用によってパフォーマンスを最適化できるが、複雑な結合がパフォーマンスに影響を与えることがある。

# ORMで対処する
<!-- _class: lead -->
