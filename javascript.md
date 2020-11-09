
---
# console.log 出力　print
#### 出力にconsole.log();を使う
```javascript
console.log("hello world");
```
- <font color="red">注意点</font>
    > 右に改行が入る
    
####　改行が入らない場合
```javascript
process.stdout.write("hello world");
```
このように書く

- <font color="red">注意点</font>
    > javascriptでは数値＋文字列ができる。
    > 　この場合文字列の連結として出力される
```javascript
console.log(100 + "回トイレに行った" ); // 例題
```


*****
---
# comment コメント
####　コメントアウトは//で行う
```javascript
// ここはコメントやで〰
```
- <font color="red">注意</font>
    > 文字列中に//を書いてもコメントアウトされない。

####　複数行のコメントアウト
> 複数行の場合/*  */ を使う
```javascript
/*
ここはコメントアウトされている場所デス。ｗ
*/
```
こんな感じで書く

*****
---
#　変数の設定
####　var 変数名 = データ; のように書く
```javascript
var hoge = "hogehoge"; // 変数が文字列の場合
var hoge = 数値; // 変数が数値の場合
var hoge = []; // 変数がリスト型の場合
```
このように書く

*****
---
#　random ランダム
#### ランダムはrandom関数を使う
```javascript
var random = Math.random() * 10; // この関数は０〜９の間のランダムな浮動小数点数を返す
var random = Math.random() * 5; // この関数は０〜４の間のランダムな浮動小数点数を返す
```
#### 実際にはこんな書き方をする
```javascript
var random = parseInt(Math.random() * 10) // この関数は０〜９のランダムな整数型を返す
var random = parseInt(Math.random() * 5) // この関数は０〜４のランダムな整数型を返す

var random = parseInt(Math.random() * 10) + 1; // この関数は１〜１０のランダムな整数型を返す
var random = parseInt(Math.random() * 5) + 5; // この関数は５〜９のランダムな整数型を返す
```

*****
---
# parseInt int型にする
```javascript
parseInt(float型);
```
このように書くとfloat型をint型にしてくれる

*****
---
#　演算子
#### 演算子にはいろいろある
```
=　代入演算子
+　足す
-　引く
*　掛ける
/　割る
%　余り
+= 左の値に右の値をたす
-= 左の値に右の値を引く
++ 左の値を＋１する
-- 左の値をー１する
```

*****
---
#　if文の書き方　条件分岐
####　ifは条件に分かれて処理してくれる
```javascript
if (条件式) {
    // 条件式が成立した場合の処理
} else if (条件式) {
    //条件が成立した場合の処理
}　else　{
    //条件式が成立しなかった場合の処理
}
```
-　<font color="red">注意点</font>
    > 条件式の書き間違いで変数を書き換えてしまう場合がある

*****
---
# 条件式　比較演算子
####　条件式と比較演算子の種類
```javascript
hoge == huga // hogeとhugaがおなじ場合
hoge != huga // hogeとhugaが違う値だった場合
hoge < huga // hogeがhugaより小さい場合
hoge > huga // hogeがhugaより大きい場合
hoge <= huga // hogeがhuga以下だった場合
hobe >= huga // hogeとhuga以上だった場合
```

*****
---
# while ループ　loop
#### whileは条件式の成り立つ間ループしてくれる
```javascript
while (条件式){
    // 条件式の成り立つ間ループされる
    // 繰り返し処理したいコードを書く
    条件式の変化　// 条件式の変化させるコードを書かないと無限ループになる
}
```

*****
---
#　for ループ　loop
#### forは処理のループをしてくれる
```javascript
for (変数の設定; 条件式; 条件式の変化){
    // 繰り返したい処理のコード
}

// ⇓のように省略することも可能だが
//   省略すると無限ループになる
for (;;;){
    // 繰り返したいコード
}
```
#### ⇓実際はこんな感じで書く⇓
```javascript
for (var i = 0; i < 10; i++){
    // このループでは１０回ループする
}
```

*****
---
# input 標準入力　インプット
#### １行の取得
```javascript
process.stdin.resume();
process.stdin.setEncoding('utf8');

var 変数 = ""; // 変数の定義
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
reader.on('line', (line) => {
    変数 = line; // 変数にに入力値を代入
    
});
reader.on('close', () => {
    // 変数を使った処理
    
});
```
-　<font color="red">注意点</font>
    > 文字列として入力される

####　複数行の取得
```javascript
var 変数 = []; // リスト型の定義
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
reader.on('line', (line) => {
    lines.push(変数); // リストに格納していく

});
reader.on('close', () => {
    // リスト型を使った処理
});
```

*****
---
# list リスト　
####　リスト型の使い方
```javascript
var hoge = []; // リストの指定
hoge.push(変数); // リストに格納
hoge.length; // リストの長さ
hoge[数値] = 変数; // リストの数値のインデックス番号に変数を入れる

for (var huga in hoge){
    // hugaにhogeの値が１つづつ入る
    // 注意点！！順番になるとは限らない
} 

for (var huga of hoge){
    // hugaにhogeの値が順番に入る
}

hoge.forEach (huga => {
    // hugaにhogeの値を順番良く入れる
    // １つ上の var of のに似ている
})
```

*****
---
# 文字の分割　リスト化
#### 文字をリスト型にする
```javascript
var huga = hoge.split("分割したい文字");
// hugaにhogeの分割したい文字で分割されたリストが入る
```






