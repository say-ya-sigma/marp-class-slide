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

# DDDとデータベース
<!-- _class: lead -->

# 1 DDDの基本
<!-- _class: lead -->

# DDDとは
* ドメイン駆動設計 **Domain Driven Design**
  * エリックエヴァンス
* ソフトウエア開発の中心は業務知識(ドメイン)
* 業務知識のエキスパート(ドメインエキスパート)との密な協力

# DDDの基本原則 1
* 業務知識の理解し、エキスパートと開発者で共通の語彙を使う
  * 業務知識を **ドメイン** と呼ぶ
  * エキスパートと開発者の共通の語彙を **ユビキタス言語** と呼ぶ
  * **ユビキタス言語** を使用して **ドメイン** の **モデル** を構築する。これがドメインモデル

# DDDの基本原則 2
* ドメインモデルを中心とする設計と開発
  * データベース中心ではない
  * ドメインモデルは業務の概念を正確に表現する
    * 業務の概念を正確に表現するために **オブジェクト指向** を使う

# DDDの基本原則 3
* エンティティと値オブジェクトを基礎として設計する
  * エンティティは識別可能な、IDとなるようなものを持つオブジェクト
  * エンティティはライフサイクルを持つ
  * 値オブジェクトはIDを持たず、属性の集合として扱われる

# note: エンティティと値オブジェクト中心の世界
* エンティティと値オブジェクトはそれぞれクラスで表されます。これらのクラスを中心として設計するため、DDDにおける設計はクラス中心の設計となります。
* これはMVCがデータベース中心の設計だったことの良い対比になっています。

# note: 値オブジェクトの例
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    postal_code: str
    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
```
# note: 値オブジェクトの例
```python
address1 = Address(street="123 Main St", city="Anytown", postal_code="12345")
address2 = Address(street="123 Main St", city="Anytown", postal_code="12345")

print(address1)  # 123 Main St, Anytown, 12345
print(address1 == address2)  # True
```

# note: エンティティの例
```python
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id
```
# note: エンティティの例
```python
user1 = User(user_id=1, name="Alice", email="alice@example.com")
user2 = User(user_id=1, name="Alice", email="alice@example.com")
user3 = User(user_id=2, name="Alice", email="alice@example.com")
print(user1 == user2)  # True
print(user1 == user3)  # False
```

# DDDの基本原則 4
* 集約と集約ルートを使って整理する
  * **集約** は関連するオブジェクトの集合で、一貫性のある操作を保証するための境界を持つ。
  * **集約ルート** は、集約のエントリーポイントで、集約内のオブジェクトに対するすべての操作を管理する。集約ルートを通じてのみ、集約の状態を変更できる。
* 集約はその内部で整合性が保たれている必要があるという特性上、RDBのトランザクションによる強い整合性の境界となる場合が多い。

# note: DDDではDBの設計は後になる

* 業務をドメインモデルとして分析し、必要に応じてクラス図と呼ばれる図などを書きます。
* 値オブジェクト、エンティティ、集約などを用いて設計されたドメインモデルがまず作られます。
* その後集約などの単位で永続化するためにデータベースが用意されます。

# note: 集約の例
```python
from dataclasses import dataclass
# エンティティ
@dataclass(frozen=True)
class OrderItem:
    order_item_id: int
    product_id: int
    quantity: int
    price: int
```

# note: 集約の例
```python
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Order:
    order_id: int
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def total_amount(self) -> float:
        return sum(item.quantity * item.price for item in self.items)
```

# note: 集約の例
```python
order = Order(order_id=1)
order.add_item(OrderItem(product_id=101, quantity=2, price=50.0))
order.add_item(OrderItem(product_id=102, quantity=1, price=150.0))

print(f"Total Amount: {order.total_amount()}") # Total Amount: 250.0
```

# DDDの基本原則 5
* リポジトリを使ってエンティティや集約をデータベースから取得する
  * リポジトリは、エンティティや集約を永続化層から取得、保存するための抽象的なコレクションを提供する。これにより、データアクセスの詳細を隠蔽する。

# note: リポジトリの例
```python
from dataclasses import dataclass
@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: int
```

# note: リポジトリの例
```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
@dataclass
class Order:
    order_id: int
    items: List[OrderItem] = field(default_factory=list)
    def add_item(self, item: OrderItem):
        self.items.append(item)
    def total_amount(self) -> float:
        return sum(item.quantity * item.price for item in self.items)
```

# note: リポジトリの例
```python
from typing import Protocol
class OrderRepository(Protocol):
    def add(self, order: Order) -> None:
        pass
    def get(self, order_id: int) -> Optional[Order]:
        pass
```

# note: リポジトリの例
```python
class InMemoryOrderRepository:
    def __init__(self):
        self.orders: Dict[int, Order] = {}
    def add(self, order: Order) -> None:
        self.orders[order.order_id] = order
    def get(self, order_id: int) -> Optional[Order]:
        return self.orders.get(order_id)
```

# note: リポジトリパターン
* リポジトリはリポジトリパターンとしてMVCに導入されることがある
  * コントローラから呼ぶ場合
  * サービスレイヤーから呼ぶ場合
  * いずれもデータアクセスの隠蔽が目的

# DDDの基本原則 6
* ファクトリを使って集約の生成ルールを表現する
  * ファクトリは、オブジェクトの生成を担当する設計パターン
  * DDDにおいては集約の生成に特定のルールがある場合によく使用される

# note: ファクトリの例
```python
from dataclasses import dataclass
@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: float
```

# note: ファクトリの例
```python
from dataclasses import dataclass, field
from typing import List
@dataclass
class Order:
    order_id: int
    items: List[OrderItem] = field(default_factory=list)
    def add_item(self, item: OrderItem):
        self.items.append(item)
    def total_amount(self) -> float:
        return sum(item.quantity * item.price for item in self.items)
```

# note: ファクトリの例
```python
from typing import List
class OrderFactory:
    @staticmethod
    def create_order(order_id: int, items_data: List[dict]) -> Order:
        order = Order(order_id=order_id)
        for item_data in items_data:
            item = OrderItem(
                product_id=item_data["product_id"],
                quantity=item_data["quantity"],
                price=item_data["price"]
            )
            order.add_item(item)
        return order
```

# note: ファクトリの例
```python
items_data = [
    {"product_id": 101, "quantity": 2, "price": 50.0},
    {"product_id": 102, "quantity": 1, "price": 150.0}
]
order = OrderFactory.create_order(order_id=1, items_data=items_data)
print(f"Order ID: {order.order_id}, Total Amount: {order.total_amount()}")
```

# DDDの基本原則 7
* 巨大なシステムを境界付けられたコンテキストに分ける
  * 「実践ドメイン駆動設計」にある例
    * コラボレーションコンテキスト
    * 認証・アクセスコンテキスト
    * アジャイルプロジェクト管理コンテキスト

# note: 書籍紹介
* 実践ドメイン駆動設計
  * ヴォーン・ヴァーノン
  * 翔泳社 
  * 「エリック・エヴァンスのドメイン駆動設計: ソフトウェアの核心にある複雑さに立ち向かう」よりもかなり後に書かれた本で、より現代の開発に沿った内容になっている。

# note: コンテクストによって語彙が変わる
|コンテキスト|意味|例|
|:--|:--|:--|
|銀行取引コンテキスト|口座(アカウント)とは、負債や信用取引の記録を保持するものである。ある顧客について、その銀行における現在の財務状況を示す。|当座預金口座<br>普通預金口座|
|文学コンテキスト|報告書(アカウント)とは、ある期間における、関連る出来事についての文章を集めたものである。|Amazon.com で、『Into Thin Air: Personal Account of the Mt.Everest Disaster』という書籍が売られている。|

ヴォーン・ヴァーノン. 実践ドメイン駆動設計 (p.59). 翔泳社. Kindle 版. 


# 2 DDDとデータベース設計
<!-- _class: lead -->

# データベースの種類
* RDB
  * リレーショナルモデルに基づくDB
  * MySQL, PostgreSQLなど
* ドキュメント指向DB (NoSQL)
  * MongoDB
  * DocumentDB (AWS)
  * Firestore (GCP)

# ドキュメント指向DBとは
* 特徴
  * ドキュメント形式
  * 柔軟なスキーマ
  * 階層的なデータ構造

# ドキュメント形式
- ドキュメント形式
  - データは**ドキュメント**として保存され、各ドキュメントは**キーと値のペア**からなる構造を持つ。値は**ネストされたオブジェクト**や**配列**を含むことができる。

# 柔軟なスキーマ
- 柔軟なスキーマ
  - **スキーマレス**または**動的スキーマ**を持ち、ドキュメントごとに異なる構造を持つことができる。これにより、データの構造を柔軟に変更できる。

# note: スキーマレス
- DBに入れることの出来るデータが定義されている場合、その定義のことを**スキーマ**といいます。
- RDBには基本的にスキーマがありますが、NoSQL製品の中にはそうでないものが多いです。これを**スキーマレス**といいます。

# 階層的なデータ構造
- 階層的なデータ構造
  - ドキュメント内でデータを**ネスト**させることができ、**オブジェクト指向プログラミングのモデル**に近いデータ構造を扱うことができる。

# DDDにおけるRDBと<br>ドキュメント指向データベースの<br>比較
<!-- _class: lead -->

# RDBの利点
- データの整合性
  - リレーショナルデータベースは、**トランザクション管理**と**ACID特性**を提供し、データの整合性を高いレベルで保証できる。

# note: トランザクション
- 一連のデータベース操作を一つの単位として扱う
  - 途中でエラーが起きた場合処理をロールバックできる
  - 必要に応じてデータをロックする
  - トランザクションが完了するまでデータは書き込まれない

# note: ACID特性
- Atomicity 原子性
- Consistency 一貫性
- Isolation 分離性
- Durability 永続性

# note: 原子性
- トランザクション内のすべての操作は、すべてが完了するか、すべてが完了しないかのどちらかです。
- 途中でエラーが発生した場合、トランザクションはロールバックされ、データベースの状態はトランザクション開始前に戻ります。

# note: 一貫性
- トランザクションが完了すると、データベースは一貫した状態になります。
- データベースの制約（例えば、外部キー制約やチェック制約）が常に満たされることを保証します。

# note: 分離性
- 同時に実行される複数のトランザクションが互いに影響を及ぼさないようにします。
- これにより、トランザクションが独立して実行され、他のトランザクションの中間状態を見ないことを保証します。

# note: 永続性
- トランザクションがコミットされると、その結果は永続的に保存され、システム障害が発生しても失われないことを保証します。

# RDBの利点
- 複雑なクエリのサポート:
  - **SQL**を使用して複雑なクエリを実行でき、データの集計や結合が強力である。

# RDBの利点
- 成熟したエコシステム:
  - 長い歴史と広範なサポートがあり、多くのツールやフレームワークが利用可能です。

# RDBを利用する場合の課題
- オブジェクト-リレーショナルインピーダンスミスマッチ
  - 集約のようなオブジェクト指向の構造をリレーショナルテーブルにマッピングするのが難しい場合があり、特に**ネストされたオブジェクト**や**複雑な関係**を持つ場合に課題が生じることがある。

# RDBを利用する場合の課題
- スキーマの硬直性
  - スキーマの変更が難しく、柔軟性に欠けるため、頻繁な変更には不向きといえる。

# note: マイグレーションとスキーマの硬直性
- RDBはスキーマの硬直性が課題とされることがありますが、成熟したエコシステムがそれを十分に補っているという指摘もあります。
- 多くのORMシステムに同梱されているマイグレーション(移行)システムはスキーマの継続的な変更を可能にしています。

# RDBを利用する場合の課題
- スケーラビリティ
  - 水平スケーリングが難しい場合があります。

# ドキュメント指向DBの利点
- スキーマの柔軟性
  - 多くがスキーマレスであり、データ構造の変更が容易。集約をそのままドキュメントとして保存できるため、オブジェクト指向のモデルと自然に一致する。

# note: スキーマの柔軟性は利点か？
- スキーマが柔軟であることでむしろ開発、運用上の混乱が生じるという主張もあります。
- 前述のとおりRDBでも適切なプロセスを踏めばスキーマの変更が可能なので、利点としては成立していないという意見もあります。

# ドキュメント指向DBの利点
- 水平スケーリングが容易で、非常に大規模なデータセットに対して有効に働く場合があります。

# ドキュメント指向DBを利用する場合の課題
- データの整合性
  - ドキュメント指向DBでは整合性の保証が課題になる場合があり、結果整合性に依存する場合がある。トランザクションが複雑な場合には注意が必要。

# note: 結果整合性
- 即時の整合性は保証しないが、最終的には一貫した状態になることを保証するということです。これは通常RDBのトランザクションによる整合性のレベルよりも低い保証レベルであることを表します。
- DDDでは整合性を担保したいデータが集約という単位でまとまっていることが多く、戦略的に整合性のレベルを結果整合性に抑えることがあります。

# ドキュメント指向DBを利用する場合の課題
- クエリの制限
  - 複雑なクエリや結合が制限されることがあり、データの集計が難しい場合があります。

# note: ドキュメントDBのデータの集計
- 例えばFirestoreではデータを集計用のBigQueryへ同期してBigQueryで集計するパターンがよく使われます。このように集計の課題は別の製品を組み合わせることで解決可能です。
- BigQueryはLooker Studioなどのビジネスインテリジェンスツールとの連携も容易なので、そのような構成を採用するメリットは大きいです。

# DDDにおけるRDBとドキュメント指向DB
- DDDでは値オブジェクト、エンティティ、集約などを用いてデータが入れ子になる前提で設計することから、RDBを利用する場合はそれをテーブルとそれらのリレーションシップで表現し相互変換する必要が生じる。(インピーダンスミスマッチ)
- 上記の課題を**JSONカラム**を多用して解決するくらいならドキュメント指向DBを使った方が良いケースもある。
- トレードオフを考える上で、RDBのよる強力なトランザクション機能を捨ててまでドキュメント指向DBを使うべきかということは留意する必要がある。

# note: JSONカラム
- JSONカラムを使用すると、ネストされたオブジェクトや配列を含む複雑なデータ構造を保存できます。
- 多くのRDBMSは、JSONデータに対するクエリ機能を提供しており、特定のキーや値に基づいてデータを抽出できます。一部のデータベースではインデックスも作成できます。

# Appendix: CQRS（コマンドクエリ責務分離）
  - 読み取り操作（クエリ）と書き込み操作（コマンド）を分けて設計し、システムのスケーラビリティとパフォーマンスを向上させる設計パターン。
  - DDDと関係が深いが、現在アーキテクチャを問わず注目されている。

# 用語の復習
- DDD
  - ドメイン駆動設計のこと。エリックエヴァンスによって提唱された。業務知識とそのモデル化に重きを置く。
- ドメイン
  - 業務知識のこと。業務知識に詳しい人をドメインエキスパートと呼び、業務をシステムに落とせるようにモデル化したものをドメインモデルと呼ぶ。

# 用語の復習
- ユビキタス言語
  - ドメインエキスパートや開発者を含む関係者に共通する語彙のこと。ユビキタス言語の辞書を作り議論を繰り返す場合が多い。
- エンティティ
  - 識別可能なIDとライフサイクルを持つオブジェクト。通常はクラスとして書かれる。

# 用語の復習
- 値オブジェクト
  - 属性の集合として扱われるオブジェクト。通常はクラスとして書かれる。
- 集約
  - 関連するオブジェクトを集めたもの。DDDでは集約を使って設計する。一貫性のある操作を保証する境界の役割がある。

# 用語の復習
- 集約ルート
  - 集約に対する操作などを受け付けるエントリーポイント。集約ルートを通じてのみ集約の状態を変更できるというルールで開発する場合が多い。
- リポジトリ
  - エンティティや集約を永続化層から取得、保存するためのもの。データアクセスの詳細を隠蔽する。DDD以外でも使われる。

# 用語の復習
- ファクトリ
 - DDDにおいては集約の生成に特定のルールがある場合に使用されることが多い。オブジェクトを生成する際には様々な場面で使われる汎用的な設計パターン。
- 境界づけられたコンテキスト
  - システムの大きな境界。境界の中で一貫したユビキタス言語を用いるというルールがある場合が多い。

# 用語の復習
- 実践ドメイン駆動設計
  - ヴォーン・ヴァーノン著の非常に有名なDDDの本。より現代の開発に沿った内容になっている。
- ドキュメント指向DB
  - 集約との相性の良さから、DDDにおいてRDBの他に候補に挙がるDB。MongoDBやFirestoreなどがある。
- スキーマレス
  - DBに入れることの出来るデータを定義しなくてよいという性質。

# 用語の復習
- ACID特性
  - 原子性、一貫性、分離性、永続性という、トランザクションが満たしていて欲しい4つの性質を指す。
- 結果整合性
  - 即時の整合性は保証しないが、最終的に一貫した状態になることを保証するということ。
  