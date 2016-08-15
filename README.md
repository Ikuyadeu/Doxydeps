# 依存関係の変化を利用したコードレビュアー推薦手法への適用-OSSプロジェクトへの適用実験

## 背景
ファイルの変更に対してその変更がどのようなファイルにどの程度影響があるかわからない。
既存研究では変更されたファイルに依存しているファイルが影響を受けることが分かっている。

## アプローチ
依存関係の方向や開発者による影響の変化を調べる。
今回調べる影響は変更が行われたあと、ほかのファイルが何日後に変更されるかを調べる

## 結論
変更されたファイルに依存しているファイルだけでなく、
変更されたファイルが依存しているファイルも変更時間が影響を受ける。
同一の開発者であるかどうか、プロジェクト外部の開発者であるかどうかによって影響の度合いが変わる

## 影響の大きい依存関係
* 変更ファイルに依存しているファイルも依存関係のないファイルと比較して影響を受けている。
* 直接的に依存関係がなくとも依存しているファイルに依存しているといった間接的な依存関係も影響を受けている。

## 同じ人が変更を行った場合
* 早い段階で変更をされる。
* 予想:違う人物であった場合は変更を理解するのに時間がかかる

## 変更がマージだったら？（外部の人間によるまとまった変更）
* 変更が起こりにくい
* 考察:レビューを通しているため変更する必要がない

## 論文に書いてない追加実験結果
* is_merge、same_authorのTrue, Faslseの割合
  * 依存関係ごとに差がある
  * is_mergeの場合は変更されたファイルに依存しているものほど多い
  * 考察：マージのようにまとめて変更を行う場合は影響の大きいようなファイルは変更しにくい
  * 改善：図のパーセンテージの最大最小を切る必要がある

* depender3, 4の場合を追加
  * 数が増えるほど変更時間遅くなる
  * ただしdependeeは超えない
  * 考察：影響の大きさは向き > 距離

* 重複を取り除いてみた
  * dependee, dependee2が特に遅くなりdependee2はotherに近くなった
  * 考察dependerとの重複がなければこれら２つはotherよりも変更するべきではない？

* 時期ごとでので傾向の違い
  * 最近になるほど全体の日数は増える。dependee, dependee2は特に顕著
  * 考察：抽象的なものは初期に開発したっきりで触られにくいから？
  * 最近のコミットでまた早くなったのは最新のコミットでSubdateがNullのものは見ていないから

* コアコミッター（上位５人）を取り除いた
  * depender方向は遅くなり,dependee方向、otherは早くなった（特にother）
  * 考察：詳しくないからこそ変更する場所を選ばない？
  * 考察：otherが特に早いのはdependeeだとそもそもPRが通らないから？

## 今後の研究予定
* 他プロジェクトでの調査
  * データ出力に２０日以上時間がかかるので保留

* どこがプロジェクトが開発と保守が切り替わるタイミングか？(ウォーターフォールではない前提)
  * バージョンX.0に変わったとき
  * 変更コメントのaddとfixの割合が逆転するとき
    * add, make, init, first, define, hello codeなど
    * fix, tweak, improve, delete, revert, update, support, clean upなど
  * 二つのバージョン(Pythonなら3と2など)でのコードクローンの数が増えた時
  * コミットの密度が減ったとき
  * 上で上げたものが一致するかどうか調べる

* 開発者の成長について
  * レビュー経験や開発経験の高い開発者が触れるコードの遷移
  * 既存研究:専門性の高いファイルに依存しているファイルに移る
    * 専門性：該当ファイルを変更した回数を求めていき、だれが一番そのファイルに詳しいか求める
    * 最大の専門性が６０％以下のファイルは信頼性が低い⇒開発者は完全に分業したほうがいい
  * 予想:別ファイルにも移る場合にも向きが関係あるかも
    * 上る：徐々に抽象度の高いコードを変更する
    * とどまる：同じファイル・同じ行ばかり触る
    * 下がる：依存されているファイルに移る（既存研究のもの）
  * タイプ別に一時的に参加か、プロジェクトに参加し続ける人の判断
  * バグを生み出す人の傾向