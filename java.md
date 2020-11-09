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
import java.util.ArrayList; //ArrayListのインポート

ArrayList<型> 変数 = new ArrayList<型>();
```

#### ⇓String型で例える⇓
```java
import java.util.ArrayList; //ArrayListのインポート

ArrayList<String> hoge = new ArrayList<String>(); //hogeというArrayListの作成

// addでリストの追加
hoge.add("huga"); //hogeにhugaを追加

// setでリストの上書きインデックス番号の次に変更したい文字
hoge.set(1, "hugahuga"); // hugaをhugahugaに変更

// removeで削除、インデックス番号を指定
hoge.remove(0); //hogeからインデックス0の要素を削除

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
