# robosys26_report1

## 概要
長さ, 質量の単位を変換するコマンドである。

## 使用方法
```bash
 ./unitconv.py <数値> <変換前単位> <変換後単位>
```

## 対応単位
### 長さ
- mm
- cm
- m
- km
- inch
- ft

### 質量
- mg
- g
- kg
- t
- lb(ポンド）

## 実行例
- 120mm をcm に変換する
```bash
./unitconv.py 120 mm cm
```

実行結果：
`12.0`

- 2.5m をmm に変換する
```bash
./unitconv.py 2.5 m mm
```

実行結果：
`2500.0`

- １inch をmm に変換する
```bash
./unitconv.py 1 inch mm
```

実行結果：
`25.4`

- 1kg を1g に変換する
```bash
./unitconv.py 1 kg g
```

実行結果：
`1000.0`

## エラー
- 対応していない単位 
- 数値以外の入力 
- 引数不足
- 異なる単位の入力
の場合はエラーメッセージを表示し、終了コード１を返す。

## テスト
以下のコマンドでテストを実行できる。

```bash
./test.bash
```
GitHub Actionsを利用し、push時に複数のpythonバージョンで自動テストを行う。

