# 中かっこの省略
```java 
if (条件式)
    // しょり
else
    // 処理
```
この書き方でも動く
- 注意点
    > else ifや elseブロックでも中かっこは省略できるが、間違えやすいので推奨ではない
- 注意点
    > 直後のステートメントにのみ分岐の対象になる



# swich文
    |     | switch(式){    |     | 
    | --- | -------------- | --- | 
    |     | case 値 1      |     | 
    |     | 処理１         |     | 
    |     | break          |     | 
    |     | case 値 2      |     | 
    |     | break          |     | 
    |     | case 値 3      |     | 
    |     | break          |     | 
    |     | case 値 4      |     | 
    |     | break          |     | 
    |     | default        |     | 
    |     | 処理 n         |     | 
    |     | break          |     | 
    |     | }              |     | 

```java
int a = 1;
switch(a) {
    case 1:
        System.out.println("one");
        break;
    case 2:
        System.out.println("two");
        break;
    default:
        System.out.println("other");
        break;
}
```
のように記述
- <font color="red">注意点</font>
    > break;を描かないと最後まで処理する





# continue
> 処理をスキップしたいときに使う
- <font color="red">注意点</font>
    > for文なら遷移式 while文なら条件式に戻る

continueの達するとそれ以降のループは処理されず、ループの最初からまた処理されます
```java
for ( int i = 0; i < 10; i++){
    System.out.print(i);
    if (8 < i){
        continue;
    }
    System.out.print(",");
}
```

```java
for (int i = 0; i < 10; i++){
    System.out.print(i);
    System.out.print(",");
}
```

## 問題
コンソロールに４を表示したい。だが、実際は０　１行だけ直すと４になる			変える１行はどこ						
```java
package Test11;						
public class Main {			
	public static void main(String[] args) {						
		int total = 0;
		for (int i = 0; i < 5; i++) {					
			if (i % 2 == 0) {
				break;			
			}
			total += i;				
		}					
		System.out.println(total);				
	}						
							
}
```
トレース表
| i   | total | syori | 
| :-: | :---: | :---: | 
| 0   | 0     | 0     | 
| 1   | 0     | break | 
| 2   | 0     |       | 

直す場所⇓⇓  
break => continue
***
直した後のトレース表
| I   | total | 処理              | 
| :-: | :---: | :---------------: | 
| 0   | 0     | continue          | 
| 1   | 1     | total = total + 1 | 
| 2   | 1     | continue          | 
| 3   | 4     | total = total + 3 | 
| 4   | 4     | continue          | 
| 5   | 4     | none              | 