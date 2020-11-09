# 引数を変数に代入
```shellscript
hoge=$1 # hogeに引数が渡される
# コマンドとして使う場合は$を使う
# 例⇓⇓⇓
echo "$hoge"
```

*****
---

# 変数にコマンド結果を入力
```shellscript
hoge=`huga` # hogeにhugaの実行結果の標準入力がはいる
# コマンドとして使う場合は$を使う
# 例⇓⇓⇓
echo "$hoge"
```

*****
---
# comment コメントアウト
```shellscript
# シャープのあとに記入
```

*****
---
# loop ループ　for
#### for
```shellscript
for 変数 in 1 2 3
do
    # ループさせたい処理
done
```
- <font color="red">注意点</font>
    > 1 2 3 の順でiに代入される

#### for 多分こんな感じで使う
```shellscript
for i in `seq 1 +1 10`
do
    # ループさせたい処理
done
```
- <font color="red">注意点</font>
    > 引数1は始まり　引数2はステップ　引数3は終わり

*****
---
# loop ループ while
#### while
```shellscript
while true
do
    # ループしたい処理
    # ループのbreak
done
```

*****
---
# if 条件分岐 
```shellscript
if [条件式] ; then
    # 条件式が成り立った場合の処理
elif [条件式] ; then
    #  条件式が成り立った場合の処理
else
    # 条件式が成り立たなかった場合の処理
fi
```
*****
---
# input read 入力
```shellscript
read -p "入力時のコメント" 変数
# 変数に入力値を代入する
```

# 基本 head 
```shellscript
#!/bin/sh
```

*****
---
# sleep 秒間　時間
#### sleep のあとに数値を入れると数値分の秒数を待ってくれる
```shellscript
sleep 数値
```
