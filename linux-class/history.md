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

# ハードウエアとソフトウエア

* ハードウエア
	* CPU
	* メモリ
	* SSD
* ソフトウエア
	* アプリケーション
	* ミドルウエア
    * **OS**

# OSとは

* ミドルウエアやアプリケーションが動作する環境を提供
	* マルチタスク
		* 本来のコンピュータは同時に 1 つの処理しかできない
        * 各ソフトウェアを非常に短いタイミングで切り替えている
	* 基本的な通信
		* TCP/IP

# Linuxの歴史
<!-- _class: lead -->

# UNIX

* 1960s
* AT&T ベル研究所
* Multics という先行研究
* Ken Thompson

# Multics

* ベル研究所の研究していたOS
* MULTiplexed Information and Computing Service
* time-sharingという概念が導入された

# UNIXが残った

* Multics プロジェクトはそれほど跳ねなかった
* UNIXが他の様々なプロジェクトに流用された
* 送料・メディア代だけで使えた
* 独自に研究・開発・変更ができた

# ライセンス

* AT&T がライセンサーを始める
* AT&T 版 UNIX "Systen V"
* UNIX互換OS
	* 正式にライセンス契約を結んでいないUNIX

# BSD

* カリフォルニア大学バークレー校のUNIX
	* **B**erkeley **S**oftware **D**istribution
* Ken Thompson
* UNIX 界の大きな流れの一つになる
* インターネット・プロトコルの実装

# Linux

* フィンランドの大学生 Linus Torvalds
* 1991年　「僕は今、(UNIX に似た) OS を作っている。」
* 当時の UNIX のイメージ
    * 高いライセンス使用料
    * 企業や大学
* UNIX互換OS として立派に動作するまでになった

# GPL ライセンス

* GPL (GNU General Public License: GNU 一般公衆利用許諾)
* チャードストールマン
    * GNU プロジェクト
* Linux のライセンスとして採用された
* **フリーソフトウエアライセンス**

# フリーソフトウエアライセンス

* プログラムを実行する自由
* ソースの改変の自由
* 利用・再配布の自由
* 改良したプログラムをリリースする権利

# ディストリビューターと<br>ディストリビューション

* Ubuntu, Debian, RHEL等
* バイナリ形式で一般に頒布
* ディストリビューション自体も改変、再配布可能
