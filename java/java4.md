# データのいろいろ
### バージョンアップの場合
> バージョンアップでは、偶数の場合安定している
- 例
    > Ubuntuではバージョン16,18,20のようになる  
    また、保証されている期間をちゃんと見る


# トレース表の練習
| 外J | 内I | 結果  | 
| :-: | :-: | :---: | 
| 0   | 0   | #     | 
| 0   | 1   | break | 
| 1   | 0   | #     | 
| 1   | 1   | ##    | 
| 1   | 2   | break | 
| 2   | 0   | #     | 
| 2   | 1   | ##    | 
| 2   | 2   | ###   | 
| 2   | 3   | break | 

# loop
### forの場合
- for (最初の設定;条件式;設定の変更){処理} 
    > 回数が決まっている場合、有利  
    条件式がtrueの場合処理を繰り返す

    例⇓⇓⇓
    ```java
    for (int i = 0; i < 3; i ++){
        //繰り返したい処理
    }
    ```

### whileの場合
- while(条件式){処理}
    > for文と違い、回数が決まっていないものに使える。  
    条件がtrueである場合処理を繰り返す

    例⇓⇓⇓
    ```java
    int i = 0;
    while (i < 3){
        //繰り返したい処理
        i++;
    }
    ```

### do-whileの場合
- do{処理}while(条件式)
    > 最低一回は処理する  
    また、条件式がtrueの場合また繰り返す

    例⇓⇓⇓
    ```java
    int i = 0;
    do {
        System.out.println("Hello !!");
        i++;
    } while (i < 3);

### breakを使う
- if (条件式){break;}
    > ループを終わらせたいときに使用  
    if と一緒に使う場面が多い

# loopの練習（トレース表)
```java
for (int i = 0; i < 5; i ++){
    for (int j = 0; j < 5; j ++){
        Sytem.out.pirnt("#");
        if (j == 2){
            break;
        }
    }
}
```
| 外J | 内I | 結果  | 
| :-: | :-: | :---: | 
| 0   | 0   | #     | 
| 0   | 1   | ##    | 
| 0   | 2   | ###   | 
| 0   | 3   | break | 
| 1   | 0   | #     | 
| 1   | 1   | ##    | 
| 1   | 2   | ###   | 
| 1   | 3   | break | 
| 2   | 0   | #     | 
| 2   | 1   | ##    | 
| 2   | 2   | ###   | 
| 2   | 3   | break | 
| 3   | 0   | #     | 
| 3   | 1   | ##    | 
| 3   | 2   | ###   | 
| 3   | 3   | break | 
| 4   | 0   | #     | 
| 4   | 1   | ##    | 
| 4   | 2   | ###   | 
| 4   | 3   | break | 


***
***
***



# アルゴリズム
# 正確にきれいに書くことが大切