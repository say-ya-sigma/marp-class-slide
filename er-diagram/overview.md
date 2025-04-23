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

# ER図
<!-- _class: lead -->

# ER図
- Entity Relationship Diagram
  - Entity テーブル
  - Relationship 関連

# 多数のテーブルの管理
- RDBではテーブルを分割する
  - RDBMSが管理するテーブルの数はかなり多くなる
- 管理するツールが必要
  - それぞれのテーブルがどういう意味を持っているのか
  - テーブル同士はどういう関連を持っているのか

# ER図
- こうした多数のテーブルを管理するために、それぞれのテーブルがどういう意味を持っていて、テーブル同士が互いにどういう関係にあるのか、ということを明示するために作る図をER図（Entity-Relationship Diagram：実体関連図）と呼びます。
  - ミック. 達人に学ぶDB設計 徹底指南書 (p.125). 翔泳社. Kindle 版.

# リレーションシップ
- あるテーブルの主キーが、他のテーブルに列として含まれている
  - 二つのテーブルの間には意味的な関連があることになる
- 同書籍より

# 1対1
- あまり見かけない。
- 二つのテーブルのレコードが1対1に対応する
  - 二つのテーブルの主キーが一致する
  - 一つのテーブルにまとめてしまっても問題ない
- 同書籍より抜粋、一部改変

# 1対多
- 最もよくある関連のタイプ
- 基本的に正規化によって生まれる関連はこのカテゴリに属す。
- 二つに分かれる
  - 1対多
  - 0または1対多
  - 更に「多」についても、「0 以上」と「1以上」の場合がある
- 同書籍より抜粋、一部改変

# 多対多
- 最初に業務要件からテーブルを作っていくと、この多対多の関連を持ったテーブル群ができあがることがある。
- リレーショナルデータベースの「お約束」として、この多対多の関連は作ってはならない、ということになっている。
- 同書籍より抜粋、一部改変

# 中間テーブル
- 多対多のリレーションをRDBMS上で表現するために中間テーブルと呼ばれるテーブルが作られることがある。
- 中間テーブルを設けることで多対多の関係が1対多の関係の組み合わせで表現できる。

# ER図を描くツール
<!-- _class: lead -->

# draw.io(diagram.net)
- JGraph Ltd.
- OSS(Apache license)
- Java, HTML5, Javascript
- https://github.com/jgraph/drawio

# miro
- オンラインホワイトボードのmiro
- ER図も書ける
- https://miro.com/ja/diagramming/er-diagram/

# mermaid
- テキストで書ける
- OSS MIT license
- LLMと相性がいい
- https://github.com/mermaid-js/mermaid

# 他にも色々
- 本当に多くのツールでER図が書ける
- そもそも規格化されてるので
