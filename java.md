# print
#### printは画面表示する関数
```java
System.out.println("文字"); // 改行がある
System.out.print("文字"); // 改行がない
System.out.printf("文字"); // 書式を指定できる https://techacademy.jp/magazine/31996
```

# printf
```java
int x = 1;
System.out.printf("x=%d", x); // %dのところにxを代入。pythonのf関数と似てる
```

*****
---
# ArrayList array list arraylist
#### listサイズを変更できるリスト
```java
import java.util.ArrayList; // ArrayListのインポート

ArrayList<型> 変数 = new ArrayList<型>();
```

#### ⇓String型で例える⇓
```java
import java.util.ArrayList; // ArrayListのインポート

ArrayList<String> hoge = new ArrayList<String>(); // hogeというArrayListの作成

// addでリストの追加
hoge.add("huga"); // hogeにhugaを追加

// setでリストの上書きインデックス番号の次に変更したい文字
hoge.set(1, "hugahuga"); // hugaをhugahugaに変更

// removeで削除、インデックス番号を指定
hoge.remove(0); // hogeからインデックス0の要素を削除

// getで取得
hoge.get(1); // hogeからインデックス1の要素を表示

```

*****
---
# Math.pow Math 二乗 **
```java
int x = 2;
Math.pow(2,2); // 2の2乗がdouble型で返される
// int型で取りたいばあいは頑張れ！！ｗ
```

*****
---
# sort 並び替え
#### 昇順
```java
import java.utilArrays;
Arrays.sort(リスト名);
```
#### 降順
```java
import java.utillArrays;
Arrays.sort(リスト名);
int 変数名 = リスト名.length;
int[] 降順にしたいリスト名 = new int[a.length];
for (int i = 0; i < 変数名 ; i ++) {
	pas[i] = a[変数名 - i - 1];
}
```

*****
---
# list
#### 普通のlist 配列
```java
型[] リスト名 = new 型[サイズ値];
```
#### ⇓int[]で例える
```java
int[] hoge = new int[3];
```

*****
---
# for loop 
```java
for (int 変数 = 0; 変数 < まわいしたい値; 変数++){
    // ループしたい処理
}
```
- <font color="red">注意点</font>
    > for内の3つを注意する

#### ⇓実際書く例
```java
for (int i = 0; i < 10; i ++){
    // 10回ループする
}
```
#### for each スタイル
```java
for (型 変数名: リスト名){
    // 変数にリスト要素がひとつづつ入る
}
```

*****
---
# 四捨五入
```java
Math.round(数値１/数値２);
```
- <font color="red">注意点</font>
    > 数値１にdouble型を入れる

*****
---
# double to int
```java
double hoge;
(int)hoge; // ここでint型で数値が返される
```

*****
---
# string to int
```java
Integer.valueOf(文字).intValue();
```

*****
---
# int to string
```java
Integer.toString(数値);
```

*****
---
# binarystring binary 2進数表記
```java
String ret = String.format("%8s", Integer.toBinaryString(値 & 0xFF)).replace(' ', '0');
```
- <font color="red">注意点</font>
    > %8sのところの数字で、0で埋める数を指定。
    > 0xFFのところのFFのところでビットの表せる数を16進数で指定

*****
---
# 条件式 変数 代入
### 条件分岐で、変数に代入する方法
```java
変数 = 条件式 ? 式1 : 式2;
```
- <font color="red">注意点</font>
    > 条件式が成り立ったら変数に式１を代入
    > 成り立たなかったら式２を代入

### 実際に描くやつ⇓
```
String str = (hoge < huga) ? "hogeはhugaより小さい": "hogeはhugaより大きい";
```


