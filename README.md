# BongoCatAutoClicker
Steamにある[Bongo Cat](https://store.steampowered.com/app/3419430/Bongo_Cat/)というゲームの宝箱を自動で回収するツール
# 動作確認環境
```
OS:Windows10
CPU:intel core i7-9700
GPU:Nvidia GeForce GTX 1660 SUPER
Python:Python 3.11.3
```
# 使い方
## ファイルのダウンロード
```shell
git clone https://github.com/nekomigame/BongoCatAutoClicker.git
```
or

Download ZIP

![image](https://github.com/user-attachments/assets/664e7d69-56b8-4f49-8629-ee2b00726720)
## ライブラリのインストール
```shell
python -m venv venv
pip install -r requirements.txt
```

## 操作方法
```shell
python GUI.py
```

でツールを起動

![image](https://github.com/user-attachments/assets/8137ebe5-cf1e-4e39-b8a5-08bf77d6f4fa)

画像を選択からクリックする対象の画像を選択し処理開始を押すことで処理が開始されます

dataフォルダに宝箱の画像とBongo Catの画像が入っているのでよければ使ってください
## フェイルセーフ（fail safe）について
dataフォルダにあるBongo Catの画像を選択し処理を開始すると処理終了ボタンが押せなくなってしまいます

これの回避策としてPyAutoGUIのFAILSAFEを有効にしています

なので画面の４つの角のどこかにマウスカーソルを持っていくとフェイルセーフを作動させることができます

# License
MIT License
