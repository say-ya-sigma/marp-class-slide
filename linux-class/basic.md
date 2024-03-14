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

# Linuxの仕組み
<!-- _class: lead -->

# カーネルとユーザランド
* Linuxはカーネルとユーザランドと呼ばれる領域に分かれる

# カーネル

* OSの中核(kernel)
* ハードウエアと直接やり取りする
* ハードウエアの違いを吸収する

# ユーザランド

* カーネル以外の部分
* 基本的なソフトウエア群
    * ファイルシステム
    * コマンド
    * **シェル**

# シェル
<!-- _class: lead -->

# シェル shell

* 対話型のコマンド入力環境
* コマンド入力を自動化する "シェルスクリプト"
* カーネル(核)に対してシェル(殻)と説明されることが多い

# Bourne shell 系

* Bourne shell `sh`
	* Almquist shell `ash`
		* Debian Almquist shell `dash`
	* Bourne Again shell `bash` (主流)
	* Korn shell `ksh`
		* Z shell zsh `zsh` (主にmac)

# それ以外のシェル

* C shell `csh`
* Friendly interactive shell `fish`
* `cmd.exe` (Windows)
* `PowerShell` (Windows)

# ディストリビューションの誕生

* Linux インストールは難し過ぎる
* そこで Ubuntu 等のディストリビューション
    * Linux+α を簡単にインストールできる
* **パッケージ**でソフトウエアを導入する

# パッケージ
<!-- _class: lead -->

# ソフトウエアの頒布形式
* ソースコード
    * ユーザーがビルドして、バイナリを得る
* バイナリ（実行形式）
    * ディストリビューターの手によってビルドされたものを入手する

# パッケージ
* 主にバイナリ形式
* ディストリビューションごとのリポジトリ等によって管理される
* **パッケージマネージャ**
* **依存**

# パッケージ管理システム
* パッケージの管理
	* パッケージのバージョンの管理
	* パッケージのインストール元（リポジトリ）の管理
	* パッケージの依存の管理
* apt, yum, homebrew

# 依存
* 依存
	* ソフトウエアAのインストールの前提となるライブラリB
    * ソフトウエアAはライブラリBに依存している
* 複数のソフトウエアから依存されているパッケージも

# homebrewを<br>インストールしてみよう
<!-- _class: lead -->