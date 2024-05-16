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

# ローカルリポジトリとリモートリポジトリ

* リモートリポジトリはサーバーにある
* ローカルリポジトリは各自のPCにある
  * リモートリポジトリを各自コピーして使っている


# cloneしたての状態

* developやmainがローカルにコピーされる

![initial](./image/initial.png)


# ローカルのPCで作業中

* 作業ブランチを切ってそこにコミットを積む

![working](./image/working.png)

# pushした状態

* リモートリポジトリへpushする
* ここでPR/MRやレビューが入る

![push](./image/push.png)

# mergeされる

* レビューが完了してマージされる
* リモートからは作業ブランチは削除する

![merge](./image/merge.png)

# 分散バージョン管理システム

* コピーを各自が持つことから **分散**
* そうではないシステムもあった
  * SVN