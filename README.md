# robosys26_report1

## 概要
長さの単位を変換するコマンドunitconv.pyである。

## 使用方法
`./unitconv.py <数値> <変換前単位> <変換後単位>`

## 対応単位
- mm
- cm
- m
- km

## 実行例
120mm をcm に変換する

`./unitconv.py 120 mm cm`

実行結果：

`12.0`

2.5m をmm に変換する

`./unitconv.py 2.5 m mm`

実行結果：

`2500.0`

## エラー
対応していない単位、数値以外の入力、引数不足の場合はエラーメッセージを表示し、終了コード１を返す。

## テスト
以下のコマンドでテストを実行できる

`./test.bash`

GitHub Actionsを利用し、push時に複数のpythonバージョンで自動テストを行う。

