
---
# for loop
### 一般的なfor文の使い方⇓
```python
for 変数 in range(値1, 値2, 値3):
    # ループしたい処理
```
- <font color="red">注意点</font>
    > range()の中は短縮できる。→range(5) # 5回ループする
    - 値1は始まりの数
    - 値2は終わりの数
    - 値3はステップ数

### for loop 代入
```python
for 変数 in データ構造型:
    # ループしたい処理
```
- <font color="Red">**注意する点**</font>
    - 変数にデータ構造型の値が一つづつはいる
    - データ構造型は(list, taple, dict set)に当たる
    - また`enumerate()`や`items()`などで使える

*****
---
# while
#### whileは条件式にあっていたらループをする
```python
while 条件式:
    # 実行したいプログラム
    # 条件を変化　＜ー’’大切！！’’　書かなきゃ無限ループになる
```
- <font color="Red">注意点</font>
    > 条件式の判定が「True」ならループを繰り返す
    > また、条件式のもとを先に書かなきゃいけない



### 実際には⇓のような書き方が多い
```python
while True:
    # 実行したいプログラム
    if 条件式:
        break
        # 条件によって無限ループから脱出する
```
#### ⇑はどのくらいの作業が残っているかわからないときによく使う

*****
---
# print
#### printは画面に結果を表示する
```python
print(文字に出したいやつ) # 一般的に使うやつ
print(データ型, end="文字") # 改行を書き換える
```
- <font color="Red">注意点</font>
    > 改行は「\n」で表すことができる

*****
---
# join
#### joinはリスト型の出力のとき間に文字を挟むことができる
```python
"文字".join(リスト型)
print("文字".join(リスト型)) # 実際はこのように使う
```
- <font color="Red">注意点</font>
    > プリントと使うことが多い。
    > 文字を格納しているリスト型だとよく使う

*****
---
# リスト list 配列
```python
# リストの作成
リスト名 = []

# リストの追加
リスト名.append(値)

# リストの変更
リスト名[変更したい所のindex番号] = 変更したい値

# リストの削除
リスト名.remove(値) # リスト内の値を削除

# リスト内の値を取得
リスと名[取りたい値のindex番号]

# リストのソート sort
リスト名.sort() # リスト自体をソートする
sorted(リスト名) # リスト自体はソートしない

# リストの反転
リスト名.reverse() # リスト自体を反転
reversed(リスト名) # リスト自体は反転しない　オブジェクト名になる
list(reversed(リスト名)) # リスト自害は反転しない

# リストのサイズ変更
リスト名[値1:値2] リスト自体変更はせず、リストのindex番号の値1から値2までを算出できる
```

*****
---
# データ型の変更 to
### int to string
```python
str(数値)
```

### string to int
```python
int("文字")
```

### float to int
```python
int(少数値)
```

### dict to list
```python
list(ディクショナリ名)
```

### set to list
```python
list(セット名)
```

### list to set
```python
set(リスト名)
```

*****
---
# 四捨五入
#### 四捨五入した結果を返す関数
```python
import math
def mround(x, d=0):
        p = 10 ** d
            return float(math.floor((x * p) + math.copysign(0.5, x)))/p
```

*****
---
# 条件分岐 if else
```python
if 条件式:
    # 条件式がTrueだった場合
elif 条件式:
    # 条件式がTrueだった場合
else:
    # 全ての条件式がFalseだった場合
```
*****
---
# 条件式 変数 代入
#### 条件分岐で、変数に代入
```python
変数 = 値1 if 条件式 else 値2
```
- <font color="red">注意点</font>
    > 条件式がTrueだった場合変数に値1が入りFalseだった場合値２が入る

*****
---
# file ファイル操作
#### ファイルの読み込み
```python
with open("ファイル名", "r") as f:
    data = f.read()
```
#### ファイルの書き込み
```python
with open("ファイル名", "w") as f:
    f.write("文字")
```

#### ファイルの追記
```python
with open("ファイル名", "a") as f:
    f.write("文字")
```

*****
---
# 文字の置き換え replace
```python
"文字".replace("変換したい文字", "変換後の文字")
```

*****
---
# bs4 BeautifulSoup requests データの取得
#### 大まかに最初に書くやつ
```python
response = requests.get(取得したいところのURL)
response.encoding = response.apparent_encoding
html = response.text
soup = BeautifulSoup(html, "html.parser")
data = soup.find_all("取得したいタグ名") # dataにタグタイプのものが入る
# 複数のタグを指定する場合 soup.find_all(["a", "b"]) a, b  はタグ名
```

*****
---
# osの実行結果を取得する
#### 例として、lsコマンドの結果をリスト型に格納する⇓
```python
import subprocess as sp

cmd = "ls" # コマンドの指定
proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
std_out, std_err = proc.communicate()
# byte文字列で返るのでstrに
# ls_fine_name にlsで取得したファイル名を格納
ls_file_name = std_out.decode("utf-8").rstrip().split("\n") 
```

### コマンド結果を返す関数
```python
import subprocess
def return_cmd(command):
    return subprocess.Popen(
        command, stdout=subprocess.PIPE, shell=True
    ).stdout.readlines()[0]
```

*****
---
# 