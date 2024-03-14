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
# Gitの基本的なコマンド

# Gitの設定

- ユーザー名とメールアドレスを指定する。
- メールアドレスはGitHubのメールアドレスと揃える。
- この設定がされていないとcommit等様々な操作が行えない。

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

# リポジトリの初期化

- リポジトリの初期化は、`git init`コマンドを使用して行う。

```bash
mkdir my_project
cd my_project
git init
```

# 追跡を追跡するファイルの追加

- 変更の追跡は、`git add`コマンドを使用して行い、ステージングエリアに変更を追加する。

```bash
echo print("Hello, World!") > hello.py
git add hello.py
```

# ステージングに追加した変更の確認

- 変更の確認は、`git status`コマンドを使用して行う。

```bash
git status
```

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   hello.py
```

# ステージングの変更のコミット

- コミットは、`git commit`コマンドを使用して行い、ステージングエリアの変更を確定させる。

```bash
git commit
```

# ステージングエリアとは

* コミットする前の変更を一時的に保存する場所。
  * `git add` コマンドを使用して、変更をステージングエリアに追加します。
  * ステージングエリアに追加された変更は、次のコミットに含まれます。
* `git reset --soft` などを使ってステージングの取り消しができる。

# コミットって何

* コミットは、ファイルやディレクトリの変更を履歴として記録する操作です。
* コミットにはメッセージを含めることができ、変更内容や目的などを記述します。
* コミットは一意の識別子（コミットIDまたはハッシュ値）で識別されます。
