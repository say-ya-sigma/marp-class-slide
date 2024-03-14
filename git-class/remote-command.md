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

# ssh鍵を作る

```bash
ssh-keygen -t ed25519
```

* `GitHub` への `SSH` アクセスに使用する
* アルゴリズムは `ed25519`
* `pass phrase` が求められる。なくても良いがあったほうがセキュア。

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

# GitHubに登録する

# リモートリポジトリをクローンする

```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
cd リポジトリ名
```

# 作業ブランチを切る

```bash
git checkout -b "myname/working"
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