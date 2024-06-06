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

# CI（Continuous Integration）
* CIを行うタイミング
  * GitHubのPR
  * メインブランチへのマージ
* CIで行う項目
  * コードのフォーマット/型チェック
  * ビルド
  * 単体テスト
  * 結合テスト

# CD（Continuous<br>Delivery/Deployment）
* アプリケーションを自動的に本番環境に配信
* Continuous Deliveryは手動のデプロイ承認を含む
* Continuous Deploymentは完全に自動化
* リリースプロセスを効率化
* 人的エラーを減らす
* 顧客へのフィードバックループを早める

# 開発チームと運用チームがあった
* 開発チーム dev.
  * 新機能の開発
  * バグ修正
* 運用チーム ops.
  * インフラの構築
  * デプロイ、リリース
  * ログの収集

# アジャイル開発の流行という背景
* 小さな機能単位を頻繁にリリース
  * リリースサイクルの短縮のニーズ
* フィードバックループの重視
  * 顧客フィードバックの恩恵をチームが受ける

# devとopsの統合 DevOps
* 一つのチームでdev.もops.も
  * 新機能の開発
  * バグ修正
  * インフラ構築
  * デプロイ、リリース
  * ログの収集

# ops.の仕事もコードで書きたい
* IaC インフラストラクチャーasコード
  * Dockerの普及
* **Continuous Deployment**
* **Continuous Delivery**

# DevOpsにおけるCI/CDの重要性
<!-- _class: lead -->

# Four Keys
* 開発生産性と関連が深いとされる4つの指標
  * **デプロイの頻度**
  * **変更のリードタイム**
  * 変更障害率
  * **サービス復元時間**

# DevOpsの三つの道
* **フロー**
* フィードバック
* 継続的な実験と学習

# CI/CDの発展
<!-- _class: lead -->

# 背景
* アジャイル開発方法論の普及
* クラウドコンピューティングの発展に伴い広まる

# ツール、サービス
* クラウドプロバイダー等が関連サービスを提供
  * AWS: CodeBuild
  * GCP: CloudBuild
  * Azure: Pipelines
  * GitHub: GitHub Actions
  * CircleCI: CircleCI
* DevOpsの普及とともに、企業での導入が加速

# IaC（Infrastructure as Code）
* インフラストラクチャの構成をコードで管理するプラクティス
* ツール
  * Terraform
  * AWS CDK
* CI/CDパイプラインと統合される
