import os
import subprocess
import sys

# 言語と単語の取得
language = input("プログラム言語を入れてください:")
word = input("調べる単語を入れてください:")

# ファイルの取得
# ↓いつかそのまんまの拡張子で表示できるようになりたい
# ファイル追加のときできたらいいな
if language in ["python", "py", "python3"]:
    file_name = "python.md"
elif language in ["java", "ja"]:
    file_name = "java.md"
elif language in ["javascript", "js"]:
    file_name = "javascript.md"
elif language in ["setting", "set"]:
    file_name = "setting.md"
elif language in ["md", "markdown", "MarkDown", "MD"]:
    file_name = "markdown.md"
elif language in ["text", "test"]:
    file_name = "text.md"
elif language in ["it", "IT", "acvance"]:
    file_name = "internet.md"
elif language in ["study", "std", "time"]:
    os.system("python3 ../study/test.py")
    sys.exit()
else:
    sys.exit()

# ファイルの読み込み
with open(file_name, "r") as f:
    data = f.read()

# ファイルの分割
split_data = data.split("*****")

# 単語が入っているか検出
total = []
for data in split_data:
    if word in data:
        # インターネットのやつはわかりやすいように赤文字で表示するため
        if language in ["it", "IT", "acvance"]:
            total.append(data.replace(word, '<font color="red">' + word + "</font>"))
        else:
            total.append(data)

# 単語が入っていなかった場合
if len(total) == 0:
    print("検索結果がありませんでした。")
    sys.exit()

# 単語が入っていた場合

# データをパッシングに挿入
with open("../../passing/passing.md", mode="w") as f:
    f.write("\n---\n".join(total))

# OSがWindowsなのかUbuntuなのかを取得
with open("../../osname.txt", "r") as f:
    os_name = f.read()

# OSがUbuntuだった場合
if os_name == "Ubuntu":
    os.system("typora ../../passing/passing.md &")

# OSがWindowsだった場合
else:
    os.system("code ../../passing/passing.md")
