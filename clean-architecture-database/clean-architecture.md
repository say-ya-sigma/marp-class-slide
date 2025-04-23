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

# クリーンアーキテクチャ
<!-- _class: lead -->

# 導入
<!-- _class: lead -->

# 戦略的と戦術的
* 戦略的: 長期的、大局的なものの見方
  * システムの全体的な方針や、長期的なリスクに対する対処など
* 戦術的: 短期的、局所的なものの見方
  * 具体的な事例に対するよい解決法や現在の問題に対する対処など

# クリーンアーキテクチャは<br>戦術的な内容を含む
* クリーンアーキテクチャは、システムとはどうあるべきかについても語るが、クラスとはどうあるべきかについてなども網羅している。
* 部分的、段階的に導入していきやすい考え方だと言える。

# レイヤードアーキテクチャ
* 構成要素とその関係をアーキテクチャと呼ぶとして、構成要素を層(レイヤー)として表現することが多い。
* システムを複数の層に分け、各層が独立した責務を持つようにしたアーキテクチャとなる。
* 図示した時に一見分かりやすくなるが、詳細を欠いているため中盤以降で扱う。

# 依存性逆転の原則 DIP
* Dependency Inversion Principals
* **ビジネスロジックがデータベースに依存**するのではなく**データベースがビジネスロジックに依存**するべきというような考え方。
  * 「抽象に依存」という表現をする。
* 逆転というのは、それまでレイヤードアーキテクチャを採用した場合ビジネスロジックがデータベースなどに依存していたためそう呼ばれる。

# SOLID原則
<!-- _class: lead -->

# SOLID原則
* DIPのようなやつが5種類ある
  * 単一責任の原則 Single Responsibility Principal
  * オープン・クローズドの原則 Open-Closed Principal
  * リスコフの置換原則 Liskov Substitution Principle
  * インターフェース分離の原則 Interface Segregation Principle
  * 依存性逆転の原則 Dependency Inversion Principle

# 単一責任の原則
* 「コンウェイの法則から導かれる当然の帰結。個々のモジュールを変更する理由がたったひとつだけになるように、ソフトウェアシステムの構造がそれを使う組織の社会的構造に大きな影響を受けるようにする。」 Clean Architecture　達人に学ぶソフトウェアの構造と設計 アスキードワンゴ
* 変更するための理由が、一つのクラスに対して一つ以上あってはならない。 

# note: コンウェイの法則
* メルヴィン・コンウェイ
* 1967年
* 「組織が設計するシステムは、その組織のコミュニケーション構造を反映する形になる」という法則。
* 例えば、異なるチームが異なる部分を担当している場合、そのシステムもチーム間のコミュニケーションパターンに基づいたモジュール化がなされる傾向がある。

# note: 逆コンウェイ戦略
* コンウェイの法則を逆手に取って、望ましいシステムアーキテクチャを実現するために組織構造を意図的に設計・変更するアプローチ。
* 「チーム・トポロジー」という書籍などでも触れられている、現代で注目されている概念。

# note: 単一責任の原則の悪い例
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Username: {self.username}\n")
            file.write(f"Email: {self.email}\n")
```

# note: 単一責任の原則の悪い例
* 複数の責務が混在している
  * ユーザー情報の管理
  * ファイルの保存

# note: 単一責任の原則の良い例
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserFileManager:
    def save_to_file(self, user, filename):
        with open(filename, 'w') as file:
            file.write(f"Username: {user.username}\n")
            file.write(f"Email: {user.email}\n")
```

# オープン・クローズドの原則
* 「Bertrand Meyerが80年代に広めた原則。ソフトウェアを変更しやすくするために、既存のコードの変更よりも新しいコードの追加によって、システムの振る舞いを変更できるように設計すべきである。」Clean Architecture　達人に学ぶソフトウェアの構造と設計 アスキードワンゴ
* インターフェースは不変であり、その実装は変更可能であるというように作られる。

# note: オープン・クローズドの原則の例
```python
# abcを使ったインターフェース
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
```

# note: オープン・クローズドの原則の例
```python
# 長方形
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
```

# note: オープン・クローズドの原則の例
```python
# 円
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
```

# note: オープン・クローズドの原則の例
```python
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()
```

# note: オープン・クローズドの原則の例
* AreaCalculatorで新しい形の計算をさせたければ、Shapeを継承してcalculate_area()を実装すればよい
* このような形で作られているFWの機能やライブラリは多い

# リスコフの置換原則
* 「Barbara Liskovが提唱した有名な派生型の定義。1988年に誕生。要するに、交換可能なパーツを使ってソフトウェアシステムを構築するなら、個々のパーツが交換可能となるような契約に従わなければいけないということ。」Clean Architecture　達人に学ぶソフトウェアの構造と設計 アスキードワンゴ

# note: その抽象化正しいですか？
```python
class Bird:
    def fly(self):
        print("Flying")

def make_bird_fly(bird: Bird):
    bird.fly()
```

# note: その抽象化正しいですか？
```python
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")
```

# note: その抽象化正しいですか？
* サブクラスに互換性があることを保証するようなスーパークラスを作る場合、全てのサブクラスが満たす性質だけをスーパークラスに書くべきです。
* 便利だからといってスーパークラスになんでも書いてしまうと、保守不可能なコードになります。

# インターフェース分離の原則
* 「ソフトウェアを設計する際には、使っていないものへの依存を回避すべきだという原則。」Clean Architecture　達人に学ぶソフトウェアの構造と設計 アスキードワンゴ

# note: 分離されていないインターフェース
```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass
```

# note: 通常のワーカーの実装の際は問題ない
```python
class HumanWorker(Worker):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating lunch")
```

# note: 食事をしないワーカーのケース
```python
class RobotWorker(Worker):
    def work(self):
        print("Working")

    # 使っていないeatメソッドにも依存してしまっているため、余計な実装が生える
    def eat(self):
        raise NotImplementedError("Robots don't eat")
```

# note: 分離されているインターフェース
```python
from abc import ABC, abstractmethod
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
```

# noe: 通常のワーカーの実装はこうなる
```python
class HumanWorker(Workable, Eatable):
    def work(self):
        print("Working")
    def eat(self):
        print("Eating lunch")
```

# note: ロボットワーカーの実装はこうなる
```python
class RobotWorker(Workable):
    def work(self):
        print("Working") 
```

# 依存性逆転の原則
* 「上位レベルの方針の実装コードは、下位レベルの詳細の実装コードに依存すべきではなく、逆に詳細側が方針に依存すべきであるという原則。」Clean Architecture　達人に学ぶソフトウェアの構造と設計 アスキードワンゴ

# クリーンアーキテクチャの基本概念とレイヤー
<!-- _class: lead -->

# エンティティ
* ビジネスルールや業務上の重要なオブジェクトを表現する。
* システムのコアとなる部分で他のレイヤーに依存しないことが理想。

# ユースケース
* システムの具体的な動作の定義。
* ビジネスロジックを実装しエンティティを操作。

# アダプタ
* 外部システムなどとのやり取りを調整する。
* データの変換や入力の検証を行う。
* 外部APIを使う際など。

# プレゼンテーション層
* UIやAPIのエンドポイントを扱う。
* ユーザーからの入力を受け取って検証し、ユースケースに渡す。
* ユースケースから戻ってきた値をレスポンスとして返す。

# アプリケーション層
* ユースケースやアプリケーション固有のビジネスロジックを実装する。
* エンティティを操作し、プレゼンテーション層とインフラストラクチャ層の橋渡しをする。

# ドメイン層
* エンティティやビジネスルールを定義する。
* 他のレイヤーに依存しないことが望ましい。

# インフラストラクチャ層
* データベースアクセス、ファイルシステム、ネットワーク通信など外部システムとやり取りを扱う。
* アプリケーションのロジックに対して技術的な詳細を隠蔽する。

# クリーンアーキテクチャと<br>DB
<!-- _class: lead -->

# 隠蔽すべき技術的詳細
* クリーンアーキテクチャにおいて、データベースは隠蔽すべき技術的詳細。

* データベースをアプリケーションから隠蔽することで、長期的な保守性の向上を狙う。

# note: フレームワークは技術的詳細か
* クリーンアーキテクチャでは、フレームワークも技術的詳細とすることがあります。
* このことはフレームワークといえばフルスタックフレームワークを指す現代では奇妙に聞こえます。
* むしろフレームワークを開発の中心に据えるべきだという考え方もあります。

# インフラストラクチャ層
* 外部システムであるDBはインフラストラクチャ層によってアプリケーションから分離される。

* ORMのモデルに依存する層はインフラストラクチャ層だけになる。通常インフラストラクチャ層でエンティティに変換される。

# 依存性逆転の原則
* クリーンアーキテクチャではビジネスロジックがデータベースに直接依存しないことが原則となっている。

* データベースとのやり取りはインターフェースを介して行われる。

# 用語の復習
* 戦略的、戦術的
  * システムの全体的な方針など、長期的で大局的なものの見方を戦略的といい、具体的な事例に対する解決策など、短期的で局所的なものの見方を戦術的という。

* 技術的詳細
  * クリーンアーキテクチャなどでビジネスロジックから隔離されるべきと考えられているもの。DBやフレームワークなど。

# 用語の復習
* レイヤードアーキテクチャ
  * アーキテクチャの構成要素を層に見立てたアーキテクチャ。同心円の図で書かれることもある。

* ビジネスロジック
  * システムを構成するロジックのうち業務知識を表しているもの。DDDの文脈ではドメインロジックにあたる。

# 用語の復習
* 抽象に依存
  * 具体的なデータベースなどではなく、抽出されて概念化されたビジネスロジックのモデルに依存するというような概念。

* 依存性逆転の原則
  * ビジネスロジックがデータベースに依存するのではなく、データベースがビジネスロジックに依存するべきというような考え方。

# 用語の復習
* SOLID原則
  * 単一責任の原則、オープン・クローズドの原則、リスコフの置換原則、インターフェース分離の原則、依存性逆転の原則の頭文字を取ったもの。

* コンウェイの法則
  * 組織が設計するシステムは、その組織のコミュニケーション構造を反映する形になるという法則。

# 用語の復習
* 単一責任の原則
  * 個々のモジュールを変更する理由が一つだけになるようにすること。コンウェイの法則と関連がある。

* オープン・クローズドの原則
  * 既存のコードの変更よりも新しいコードの追加によってシステムの振る舞いを変更できるように設計すべきであるという原則。

# 用語の復習
* リスコフの置換原則
  * 交換可能なパーツを使ってソフトウエアシステムを構築するなら、個々のパーツが交換可能となるような契約に従わなければいけないということ。

* インターフェース分離の原則
  * ソフトウエアを設計する際には、使ってないものへの依存を回避すべきだという原則。

# 用語の復習
* エンティティ
  * ビジネスルールや業務上の重要なオブジェクトを表現したもの。エンティティは他のレイヤーに依存しないことが理想とされる。

* ユースケース
  * システムの具体的な動作の定義のこと。ビジネスロジックを実装しエンティティを操作する。

# 用語の復習
* アダプタ
  * 外部システムなどとのやり取りを調整する。システムの中で外部APIなどを使用する場合に使う。

* プレゼンテーション層
  * 主にAPIのエンドポイントを扱う。APIへのリクエストを検証しユースケースに渡し、戻ってきた値をレスポンスとして返す。

# 用語の復習
* アプリケーション層
  * ユースケースや、アプリケーション固有のロジックを実装する。プレゼンテーション層とインフラストラクチャ層の橋渡しの役割がある。

* ドメイン層
  * エンティティやビジネスルールを定義する層。

# 用語の復習
* インフラストラクチャ層
  * データベースアクセス、ファイルシステム、ネットワーク通信など外部システムとのやり取りを扱う。
