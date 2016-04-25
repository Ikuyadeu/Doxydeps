# 依存関係の変化を利用したコードレビュアー推薦手法への適用-OSSプロジェクトへの適用実験

## 背景
* プロジェクトのプルリクエストを送られたときに誰がレビューするのが適切かわからない。
* 以前の研究ではレビュー経験の多い人ほど信頼性が高いことが分かっている。
* 行数やファイルパスだけでなくプログラムの実質的な関係からレビュアーを選定したい。

## 問題
* 行やファイルパスよりも開発者と関わりの深そうなパラメータで見てみたい
* クラスや変数の依存関係を調べ開発者の得意領域を定義する

## 関連研究
* 行のみのもの:Baseline Approach: ReviewBot(Balachandram ICSE'13)
* ファイルパスが近いもの:RevFinder (Patanamon Thongtanunam, Who sould review my code?, SANER2015) 

## アプローチ
* 呼び出しなどを含めた依存関係を含んだパラメータ（同一クラス・メソッド・変数）を編集した回数をレビュアーごとにカウントする.
* 次回で新しいプルリクエスが送られたときにそのパラメータを編集した回数で推薦する.
* ファイルパスが近くないものまで呼び出すことができる.