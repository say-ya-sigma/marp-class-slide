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

# 公開鍵暗号方式

* 公開鍵と秘密鍵の2つの鍵を使用する暗号方式
  * 公開鍵は誰でも知ることができる。暗号化に使用
  * 秘密鍵は受信者だけが知っている。復号化に使用
* 代表的なアルゴリズムにはRSAや楕円曲線暗号などがある

<!-- _class: lead -->
# ssh-keygenを使った公開鍵と秘密鍵の生成

# ssh-keygenコマンドを使って、SSHの公開鍵と秘密鍵のペアを生成
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
* `-t rsa`: RSA暗号方式を指定
* `-b 4096`: 鍵の長さを4096ビットに指定（デフォルトは2048ビット）
* `-C "your_email@example.com"`: 鍵にコメントを付与（通常はメールアドレスを使用）

# 鍵の保存場所を指定（デフォルトは`~/.ssh/`ディレクトリ）
* 秘密鍵: `~/.ssh/id_rsa`
* 公開鍵: `~/.ssh/id_rsa.pub`

# パスフレーズの設定（オプション）

* 秘密鍵を保護するために使用され、鍵の使用時にパスフレーズの入力が求められる
* パスフレーズを設定しないこともできる
* 追加のセキュリティ対策

# SSHの設定ファイル（~/.ssh/config）のHostセクション

* SSHの設定ファイル（`~/.ssh/config`）では、`Host`セクションを使用して、特定のSSHホストに対する設定を定義できる

# `Host`セクション
```
Host example
    HostName example.com
    User john
    Port 2222
    IdentityFile ~/.ssh/example_rsa
```

# `Host`セクションの基本オプション
* `HostName`: 実際の接続先ホスト名やIPアドレスを指定
* `User`: ログインするユーザー名を指定
* `Port`: SSHサーバーが使用するポート番号を指定（デフォルトは22）
* `IdentityFile`: 使用する秘密鍵のパスを指定

# sshコマンドをエイリアスで呼び出せる
`Host`セクションを書いている場合
```bash
$ ssh example
```
`Host`セクションを書いていない場合 
```bash
$ ssh john@example.com -p 2222 -i ~/.ssh/example_rsa
```
