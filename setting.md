
---
# youtube-dl
```
sudo apt install youtube-dl
sudo youtube-dl -U
apt-cache policy youtube-dl 
pip install --upgrade youtube-dl
```
---

*****

# typora
```shell
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
sudo apt install typora
sudo add-apt-repository 'deb https://typora.io ./linux/'
sudo apt-get update
sudo apt-get install typora
```
---

*****
# vagrant上のnvimの設定 自分がやった手順
### vagrant上のubuntuを最新の状態にする
```
sudo apt update
sudo apt upgrade
```
>　上のやつでデフォルトNと
>　インストールインターナショナルを選択
### pipのインストール
```
curl -kL https://bootstrap.pypa.io/get-pip.py | python
```
### pynvimのインストール
```
pip install --user pynvim
```
### pip3のインストール
```
sudo apt install python3-pip
```
### pip3からnvimをダウンロード
```
pip3 install neovim
```
>　おます先生曰く、
>>　neovimはもともと入ってるから軽いらしい。。。

*****

# vagrant上のnvimの設定　多分これでいいやつ
### vagrant上のubuntuを最新状態にする
```
sudo apt update
sudo apt upgrade
```
>　上のやつでデフォルトNと
>　インストールインターナショナルを選択
### pip3のインストール
```
sudo apt install python3-pip
```
### pip3からnvimをダウンロード
```
pip3 install neovim
```
>　おます先生曰く、
>>　neovimはもともと入ってるから軽いらしい。。。

*****
---

# nvim　プラグイン　plugin
#### インターネット上で「vim bootstrap」と検索し、選択しダウンロードをする
##### ⇓普通の端末での操作⇓
```
mv ~/Downloads/generate.vim ~/VagrantBox/vccw/
```
ダウンロードしたファイルをvccwとつながるファイルに移動する

#### ⇓vccwに移動する「vccw上でvagrant up」⇓
```
cp /vagrant/generate.vim ~/.config/nvim/init.vim
```
init.vimに書き換えする


*****
---
# java授業のgit
#### pullの仕方
```
cd java.2020/
git checkout master
git pull origin master
git checkout s20024
git merge master
```
#### pushの仕方

```
git branch #自分のブランチの確認
git add # ファイル名
git commit -m ""
git push origin s20024
```

```
vagrant box add generic/ubuntu2004
sed -i -e 's/ # \(config.vm.network "forwarded_port".*\)$/ \1/' Vagrantfile
vagrant box update
vagrant up
vagrant ssh
vagrant halt
```