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

# ORMの基本(SQL Alchemy)
<!-- _class: lead -->

# モデルの宣言1
https://docs.sqlalchemy.org/en/20/orm/quickstart.html 
```python
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass
...
```

# モデルの宣言2
```python
...
class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
...
```

# モデルの宣言3
```python
...
class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

# 一つずつ見て行く
<!-- _class: lead -->

# Pythonのtypingモジュール
```python
from typing import List
from typing import Optional
...
```

* Pythonのバージョン3.5から
  * 2015 9月13日

# 脱線 PythonとTypeHint
<!-- _class: lead -->

# PEP484 Type Hints
https://peps.python.org/pep-0484/

Python 3.5から

最初に紹介されるのはこの形

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

# PEP484 ジェネリクス

世の中には型の引数を持つ型というのがある

```python
from typing import Dict, List, Optional

class Node:
    ...

class SymbolTable(Dict[str, List[Node]]):
    def push(self, name: str, node: Node) -> None:
        self.setdefault(name, []).append(node)

    def pop(self, name: str) -> Node:
        return self[name].pop()
...
```
# PEP484 ジェネリクス
```python
...
    def lookup(self, name: str) -> Optional[Node]:
        nodes = self.get(name)
        if nodes:
            return nodes[-1]
        return None
```

# PEP526 Syntax for Variable Annotations
https://peps.python.org/pep-0526/

Python 3.6から

```python
primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: ClassVar[Dict[str, int]] = {}
```

# PEP560 Core support for typing module and generic type
https://peps.python.org/pep-0560/

Python 3.7から

* Pythonの実装であるCPythonに手を加えた
  * 結果型ヒントを使った場合のパフォーマンスの問題が解決された

# PEP561 Distributing and Packaging<br>Type Information
https://peps.python.org/pep-0561/

Python 3.7から

PEP 484 は、型指定を段階的に簡単に導入できるようにすることを目的として、Python に型ヒントを導入しました。現在、型指定情報は手動で配布する必要があります。

# PEP561 Distributing and Packaging<br>Type Information

この PEP は、既存のツールを活用して最小限の作業で型情報をパッケージ化して配布するための標準化された手段と、型チェッカーがモジュールを解決して型チェック用にこの情報を収集するための順序を提供します。

# PEP544 Protocols: Structural subtyping (static duck typing)
https://peps.python.org/pep-0544/

Python 3.8から

例えばこういうのがある

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None:
        ...
```

# PEP544 構造的部分型

そしてこういうのがある

```python
class Resource:
    ...
    def close(self) -> None:
        self.file.close()
        self.lock.release()
```

# PEP544 構造的部分型

こう書ける

```python
def close_all(things: Iterable[SupportsClose]) -> None:
    for t in things:
        t.close()

f = open('foo.txt')
r = Resource()
close_all([f, r])  # OK
close_all([1])     # Error: 'int' has no 'close' method
```

# PEP586 Literal Type
https://peps.python.org/pep-0586/

Python 3.8から

```python
from typing import Literal

def accepts_only_four(x: Literal[4]) -> None:
    pass

accepts_only_four(4)   # OK
accepts_only_four(19)  # Rejected
```

# PEP589 TypedDict: Type Hints for Dictionaries  with a Fixed Set of Keys
https://peps.python.org/pep-0589/
Python 3.8から

Dictに型を付けることができる

```python
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int
```

# PEP589 TypedDict: Type Hints for Dictionaries  with a Fixed Set of Keys
```python
movie: Movie = {'name': 'Blade Runner',
                'year': 1982}
```

# PEP591 Adding a final qualifier to typing
https://peps.python.org/pep-0591/

Python 3.8から

```python
from typing import final

@final
class Base:
    ...
```

# PEP591 Adding a final qualifier to typing
```python
class Derived(Base):
# Error: Cannot inherit from final class "Base"
    ...
```

# PEP591 Adding a final qualifier to typing

methodへのfinal

```python
from typing import final

class Base:
    @final
    def foo(self) -> None:
        ...
```

# PEP591 Adding a final qualifier to typing
```python
class Derived(Base):
    def foo(self) -> None:
# Error: Cannot override final attribute "foo"
# (previously declared in base class "Base")
        ...
```

# PEP591 Adding a final qualifier to typing

変数に対するFinal

```python
from typing import Final

RATE: Final = 3000
```

# PEP591 Adding a final qualifier to typing
```python
class Base:
    DEFAULT_ID: Final = 0

RATE = 300  # Error: can't assign to final attribute
Base.DEFAULT_ID = 1  # Error: can't override a final attribute
```

# PEP585 Type Hinting Generics In Standard Collections
https://peps.python.org/pep-0585/
Python 3.9から


```python
>>> list[str]
<class 'list'>
>>> tuple[int, ...]
<class 'tuple'>
>>> collections.ChainMap[str, list[str]]
<class 'collections.ChainMap'>
```

# PEP604 Allow writing union types as X | Y
https://peps.python.org/pep-0604/
Python 3.10から

allow writing `Union[X, Y]` as `X | Y`

https://peps.python.org/pep-0646/

# PEP647 User-Defined Type Guards
https://peps.python.org/pep-0647/
Python 3.10から

```python
class Person(TypedDict):
    name: str
    age: int
```
# PEP647 User-Defined Type Guards
```python
def is_person(val: dict) -> "TypeGuard[Person]":
    try:
        return isinstance(val["name"], str) and isinstance(val["age"], int)
    except KeyError:
        return False
```
# PEP647 User-Defined Type Guards
```python
def print_age(val: dict):
    if is_person(val):
        print(f"Age: {val['age']}")
    else:
        print("Not a person!")
```


# PEP646 Variadic generics
https://peps.python.org/pep-0646/
Python 3.11から

```python
Shape = TypeVarTuple('Shape')

class Array(Generic[*Shape]): ...

Height = NewType('Height', int)
Width = NewType('Width', int)
x: Array[Height, Width] = Array()
```

# PEP646 Variadic generics

```python
Time = NewType('Time', int)
Batch = NewType('Batch', int)
y: Array[Batch, Height, Width] = Array()
z: Array[Time, Batch, Height, Width] = Array()
```

# PEP 655: Marking individual TypedDict items as required or not-required
https://peps.python.org/pep-0655/
Python 3.11から

```python
class Movie(TypedDict):
   title: str
   year: NotRequired[int]
```

# PEP 655: Marking individual TypedDict items as required or not-required

```python
m1: Movie = {"title": "Black Panther", "year": 2018}  # OK
m2: Movie = {"title": "Star Wars"}  # OK (year is not required)
m3: Movie = {"year": 2022}  # ERROR (missing required field title)
```

# PEP 655: Marking individual TypedDict items<br>as required or not-required

```python
class Movie(TypedDict, total=False):
   title: Required[str]
   year: int
```

# PEP 673: Self type
https://peps.python.org/pep-0673/
Python 3.11

```python
class MyLock:
    def __enter__(self) -> Self:
        self.lock()
        return self

    ...
```

# PEP 673: Self type

```python
class MyInt:
    @classmethod
    def fromhex(cls, s: str) -> Self:
        return cls(int(s, 16))

    ...
```

# PEP 675: Arbitrary literal string type
https://peps.python.org/pep-0675/
Python 3.11から

```python
def run_query(sql: LiteralString) -> ...
    ...
```

# PEP 675: Arbitrary literal string type
```python
def caller(
    arbitrary_string: str,
    query_string: LiteralString,
    table_name: LiteralString,
) -> None:
    run_query("SELECT * FROM students")       # ok
    run_query(query_string)                   # ok
    run_query("SELECT * FROM " + table_name)  # ok
    run_query(arbitrary_string)               # type checker error
    run_query(                                # type checker error
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )
```

# PEP 681: Data class transforms
https://peps.python.org/pep-0681/
Python 3.11から

```python
# The create_model decorator is defined by a library.
@typing.dataclass_transform()
def create_model(cls: Type[T]) -> Type[T]:
    cls.__init__ = ...
    cls.__eq__ = ...
    cls.__ne__ = ...
    return cls
```

# PEP 681: Data class transforms

```python
# The create_model decorator can now be used to create new model classes:
@create_model
class CustomerModel:
    id: int
    name: str

c = CustomerModel(id=327, name="Eric Idle")
```

# PEP 692: Using TypedDict for more precise **kwargs typing
https://peps.python.org/pep-0692/
Python3.12から

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
  name: str
  year: int

def foo(**kwargs: Unpack[Movie]): ...
```

# PEP 698: Override Decorator for Static Typing
https://peps.python.org/pep-0698/
Python 3.12から

```python
from typing import override

class Base:
  def get_color(self) -> str:
    return "blue"
```
# PEP 698: Override Decorator for Static Typing

```python
class GoodChild(Base):
  @override  # ok: overrides Base.get_color
  def get_color(self) -> str:
    return "yellow"

class BadChild(Base):
  @override  # type checker error: does not override Base.get_color
  def get_colour(self) -> str:
    return "red"
```

# ORMの基本(SQL Alchemy)
<!-- _class: lead -->

# モデルの宣言1
https://docs.sqlalchemy.org/en/20/orm/quickstart.html 
```python
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass
...
```

# モデルの宣言2
```python
...
class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_colum(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
...
```

# モデルの宣言3
```python
...
class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_colum(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

# 一つずつ見て行く
<!-- _class: lead -->

# Pythonのtypingモジュール
```python
from typing import List
from typing import Optional
...
```

* Pythonのバージョン3.5から
  * 2015 9月13日

# sqlalchemy
```python
...
from sqlalchemy import ForeignKey
from sqlalchemy import String
...
```

* mapped_columnに渡されている
  * テーブルの型や制約に関するクラス

# sqlalchemy.orm DeclarativeBase
```python
...
from sqlalchemy.orm import DeclarativeBase
...
```

* Declarative 宣言的
  * User とはこういうものです！(宣言)
  * <=> 手続き的
* Base 基底(クラス)
  * ORMのモデル全ての継承元

# sqlalchemy.orm Mapped
```python
...
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
...
```

* Mapped
  * ORMでマップされた属性が正確に型付けされるためのクラス
* mapped_column
  * DeclarativeBase内でColumnオブジェクトを生成するための関数

# sqlalchemy.orm relation
```python
...
from sqlalchemy.orm import relationship
...
```

* Relationship APIの関数

# Baseクラスを宣言している
```python
class Base(DeclarativeBase):
    pass
...
```

* 全てのORMモデルに共通する処理を書く

# __tablename__の宣言

```python
...
class User(Base):
    __tablename__ = "user_account"
...
```

* これはデータベース上のテーブル名と対応する
* `__name__`のような特殊な書き方がPythonにはある

# mapped columnの生成1

```python
...
    id: Mapped[int] = mapped_colum(primary_key=True)
...
```

* primary keyとしてテーブルにカラムが作られる
* そのカラムがこのクラスのid要素にマップされる
* マップされる際にはint型がつく

# mapped columnの生成2

```python
...
    name: Mapped[str] = mapped_column(String(30))
...
```

* 長さ30のVARCHARでテーブルにカラムが作られる
* そのカラムがこのクラスのname要素のにマップされる
* マップされる際にはstr型がつく

# mapped columnの生成3

```python
...
    fullname: Mapped[Optional[str]]
...
```

* Optional あってもいいしなくてもいい任意要素
* テーブル上にnullable(nullを取り得る)なカラムが作られる

# relationship User側

```python
...
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
...
```

# relationship User側

https://docs.sqlalchemy.org/en/20/orm/relationship_api.html
* List["Address"]はモデルクラス名を指定している
* back_populates
> Indicates the name of a relationship() on the related class that will be synchronized with this one. 

# relationship User側

```python
...
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
...
```

# relationship User側

https://docs.sqlalchemy.org/en/20/orm/relationship_api.html
* cascade
> The available cascades are `save-update`, `merge`, `expunge`, `delete`, `delete-orphan`, and `refresh-expire`. An additional option, all indicates shorthand for "`save-update`, `merge`, `refresh-expire`, `expunge`, `delete`", and is often used as in "`all`, `delete-orphan`" to indicate that related objects should follow along with the parent object in all cases, and be deleted when de-associated.

# Address側を見てみる

```python
class Address(Base):
    ...
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    ...
```

# __repr__

```python
...
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
```

* representation
* printをしたときや、ログの出力などの時に値がどう見えるか