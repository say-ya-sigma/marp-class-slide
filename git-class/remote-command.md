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

<!-- _class: lead -->
# Gitのリモートリポジトリに<br>関するコマンド

# GitHubへの接続方式
* Personal Access Tokenを使った方法
  * GitHub独自のトークンを使う
* SSHを使った方法
  * Gitの共有リポジトリで広く使われる方法

# ssh鍵を作る

```bash
ssh-keygen -t ed25519
```

* アルゴリズムは `ed25519`
* 全てデフォルト設定でOK
* `pass phrase` を任意で設定できる。設定する場合は忘れないように。

# ssh鍵を確認する

```bash
ls ~/.ssh
```

```
id_ed25519
id_ed25519.pub
```

* 鍵はペアになっている。
* .pub がパブリック、公開鍵。
* 秘密鍵はコピーしない、なくしたら作り直す。
* 使いまわすのは良くない。目的ごとに作る。

<!-- _class: lead -->
# GitHubに登録する

# リモートリポジトリをクローンする

```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
cd リポジトリ名
```

# 必要に応じてsshのHostを書く


# 作業ブランチを切る

```bash
git switch -c "myname/working"
```

# 変更をコミット

```bash
echo "my name is hoge" >> README.md
git add README.md
git commit -m "fix READMEを更新"
```

# ブランチをpush

```bash
git push origin myname/working
```

# GitHubでPRを作る

* GitHubを見ると先ほど作業ブランチをプッシュした旨が表示されている。
* PRを作成する
