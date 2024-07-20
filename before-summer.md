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

# Docker (Linux) をやった
* Dockerをインストールした
* Debianのコンテナを立てた
* コマンドをやった
* 標準入出力をやった

# コンテナ化した世界
* Containerizedがここ10年くらいの合言葉
  * 開発環境
  * プロダクション環境

# Gitをやった
* GitHubが現代の開発の中心
  * CI/CD
* Gitの操作を覚えるのもほとんどマスト
  * 手元のGit-ローカルリポジトリ
  * GitHub-リモートリポジトリ

# RDBMS
* 遥か昔からあらゆる変化に耐えてきた最強のDB方式
* ほとんどのアプリケーションの基盤となっている
  * Web
  * スマホアプリ
  * IoT

# 現代的な開発環境の一例
* Dockerを用意
* FlaskをPythonのコンテナに乗せる
* フロントエンドをnodeのコンテナに乗せる
* PostgreSQLコンテナのデータを永続化

# 現代的な開発環境の一例
* Gitでソースコードを管理
* GitHubを中心にCI/CD
  * dev, stg, prodへのデプロイ
  * バックエンドのテスト、フォーマットチェック
  * フロントエンドのテスト、フォーマットチェック
