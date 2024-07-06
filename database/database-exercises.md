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

# database exercisesリポジトリをクローン

```bash
cd dev
git clone https://github.com/say-ya-sigma/database-exercises.git
cd database-exercises
```

# コンテナ起動

```bash
make up
```

# シーディング

```bash
make seed
```

# Database clientをインストール

* ExtensionsタブでDatabase clientを検索
* install
* Databaseタブが出てきたら成功

# コネクションを追加する

* Add connection(+)をクリックする
* または Create Connectionボタンをクリック

# 設定項目を入力

* PostgreSQLタブを選ぶ
* Host Portはデフォルトのまま
* それ以外の設定項目の値についてはcompose.ymlを参照

# 接続する

* Connectを押す
* 接続できたらSaveを押す

# Databaseタブから確認する

* DatabaseタブからDBの中身を確認します

# postgresqlをインストールする

```bash
brew install postgresql
```

# postgresqlのコンソールを開く

* コネクションの行の `OpenTerminal` を開く
