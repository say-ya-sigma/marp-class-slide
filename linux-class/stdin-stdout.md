# 通常の標準入出力

* 標準入力
	* キーボード
* 標準出力
	* ターミナルエミュレータ
* 標準エラー出力
	* ターミナルエミュレータ

# リダイレクト
 * 標準出力をファイルにリダイレクト

```bash
ls > ls-output
cat ls-output
```

# アペンド
* 標準出力をファイルにアペンド(追記)

```bash
ls >> ls-output
cat ls-output
```

# 標準エラー出力のリダイレクト
* 標準エラー出力は扱いが違う
	* `2>` を使う
	* `&1` は標準出力と同じファイルへ出力することを示す

```bash
ls not-exist > ls-error-output-miss
ls not-exist 2> ls-error-output
ls not-exist > ls-error-output-another 2>&1
```

# パイプ
* コマンドの標準出力を別のコマンドの標準入力へ

```bash
ls -l /usr/bin | less # lessへのパイプ、出力を少しずつ表示できる
ls -l /usr/bin | grep apt # grepへのパイプ、出力を絞り込める
```

# grepと正規表現


# 正規表現

| 記号  | 意味               |
| :-- | ---------------- |
| ^   | 行頭               |
| $   | 行末               |
| .   | 任意の一字            |
| *   | 直前文字の 0 回以上の繰り返し |
| +   | 直前文字の 1 回以上の繰り返し |
| []  | []の中の任意の一字       |
| ^   | []の中で使われると否定     |
| \   | エスケープ            |

# 正規表現の例

```bash
cat sample.py | grep '^def' # defで始まる行、関数の定義
cat sample.py | grep ':$' # :で終わる行、関数やクラスの定義
cat sample.py | grep 'print\(.*\)' # 何かしらをprintしている文
```
