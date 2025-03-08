import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from tkinter import messagebox

import pyautogui

import click


os.chdir(os.path.dirname(__file__))

pyautogui.FAILSAFE = True

process = False
mousepos = []


def clicker():
    global process, root, mousepos
    global tiEntry, offsetxEntry, offsetyEntry, clicktypeCombobox, grayscaleCombobox, accEntry
    global infoLabel

    if process:
        filename = tiEntry.get()
        infoLabel["text"] = "処理中\nクリックした座標\nx:?y:?"
        if not filename == "":
            try:
                offsetx = int(offsetxEntry.get())
                offsety = int(offsetyEntry.get())
                clicktype = clicktypeCombobox.get()
                grayscale = grayscaleCombobox.get()
                acc = float(accEntry.get())
                if grayscale == "ON":
                    grayscale = True
                else:
                    grayscale = False
                mousepos = list(click.click_img(targetimage=filename,
                                                offset_x=offsetx,
                                                offset_y=offsety,
                                                click_lr=clicktype,
                                                gray_scale=grayscale,
                                                confidence=acc))
                infoLabel["text"] = f"処理中\nクリックした座標\nx:{mousepos[0]}y:{mousepos[1]}"
            except pyautogui.ImageNotFoundException:  # 指定した画像が見つからなかった場合
                pass
            except pyautogui.FailSafeException:  # FailSafe
                messagebox.showerror("フェイルセーフ", "フェイルセーフ作動！\n処理を停止します")
                ProcessManage()
            except Exception as e:  # 想定外のエラーが発生した場合
                if not str(e) == "":
                    messagebox.showerror("エラー", str(e))
                    ProcessManage()
    root.after(1000, clicker)


def ProcessManage():
    global process, spButton
    global tiEntry, offsetxEntry, offsetyEntry, clicktypeCombobox, grayscaleCombobox, accEntry
    global infoLabel

    if spButton["text"] == "処理開始":
        errortext = ""

        # 対象の画像選択の設定
        if tiEntry.get() == "":
            errortext += "クリック対象の画像が選択されていません\n"

        # Xのオフセットの設定
        if offsetxEntry.get() == "":
            errortext += "Xのオフセットが入力されていません\n"
        else:
            try:
                int(offsetxEntry.get())
            except TypeError:
                errortext += "Xのオフセットは整数のみ入力してください\n"

        # Yのオフセットの設定
        if offsetyEntry.get() == "":
            errortext += "Yのオフセットが入力されていません\n"
        else:
            try:
                int(offsetyEntry.get())
            except TypeError:
                errortext += "Yのオフセットは整数のみ入力してください\n"

        # 認識精度の設定
        if accEntry.get() == "":
            errortext += "画像認識の精度が入力されていません"
        else:
            try:
                acc = float(accEntry.get())
                if not (0.0 <= acc and acc <= 1.0):
                    raise TypeError
            except TypeError:
                errortext += "画像認識精度は0～1の間で入力してください\n"

        # エラーがある場合エラー内容を表示して処理終了
        if not errortext == "":
            messagebox.showwarning("エラー一覧", message=errortext)
            return

        # 詳細設定の入力ステータスを入力不可に変更
        offsetxEntry["state"] = "readonly"
        offsetyEntry["state"] = "readonly"
        accEntry["state"] = "readonly"
        clicktypeCombobox["state"] = "disabled"
        grayscaleCombobox["state"] = "disabled"
        spButton["text"] = "処理終了"
        process = True
    else:
        # 詳細設定の入力ステータスを書き込み可能に変更
        offsetxEntry["state"] = "normal"
        offsetyEntry["state"] = "normal"
        accEntry["state"] = "normal"
        clicktypeCombobox["state"] = "normal"
        grayscaleCombobox["state"] = "normal"
        spButton["text"] = "処理開始"
        infoLabel["text"] = "処理停止中"
        process = False


def selecttarget():
    global tiEntry

    # 初期ディレクトリ指定
    iDir = os.path.abspath(os.path.dirname(__file__))
    fTyp = [("画像ファイル", "*.png;*.jpg")]
    file_name = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)
    tiEntry["state"] = "normal"
    tiEntry.delete(0, tk.END)
    tiEntry.insert(tk.END, file_name)
    tiEntry["state"] = "readonly"


root = tk.Tk()
root.title("BongoCatAutoClicker")
root.geometry("600x300+0+0")
root.resizable(False, False)

# クリックする画像の選択
tiLabel = tk.Label(root, text="クリックする対象の画像を選択してください")
tiLabel.place(x=0, y=0)
tiEntry = tk.Entry(root, width=80)
tiEntry.place(x=0, y=20)
tiEntry["state"] = "readonly"
tiButton = tk.Button(root, text="画像を選択", command=lambda: selecttarget())
tiButton.place(x=500, y=17)

# 処理開始、終了
spLabel = tk.Label(root, text="処理の開始終了ボタン")
spLabel.place(x=0, y=60)
spButton = tk.Button(root, text="処理開始",
                     width=10, height=5,
                     command=lambda: ProcessManage())
spButton.place(x=0, y=80)

# 詳細設定
# offsetX
offsetxLabel = tk.Label(root, text="クリックするX座標のオフセット(px)")
offsetxLabel.place(x=150, y=60)
offsetxEntry = tk.Entry(root, width=10)
offsetxEntry.place(x=150, y=80)
offsetxEntry.insert(0, "0")
# offsetY
offsetyLabel = tk.Label(root, text="クリックするX座標のオフセット(px)")
offsetyLabel.place(x=350, y=60)
offsetyEntry = tk.Entry(root, width=10)
offsetyEntry.place(x=350, y=80)
offsetyEntry.insert(0, "0")
# Clicktype
clicktypeLabel = tk.Label(root, text="左・右クリック選択")
clicktypeLabel.place(x=150, y=100)
clicktypeCombobox = ttk.Combobox(
    root, justify="center", values=("left", "right"))
clicktypeCombobox.place(x=150, y=120)
clicktypeCombobox.insert(0, "left")
# grayscale
grayscaleLabel = tk.Label(root, text="画像認識時のグレースケールのON/OFF")
grayscaleLabel.place(x=350, y=100)
grayscaleCombobox = ttk.Combobox(root, justify="center", values=("ON", "OFF"))
grayscaleCombobox.place(x=350, y=120)
grayscaleCombobox.insert(0, "ON")
# Recognition accuracy
accLabel = tk.Label(root, text="画像認識精度（Max:1,Min:0）")
accLabel.place(x=150, y=160)
accEntry = tk.Entry(root, width=10)
accEntry.place(x=150, y=180)
accEntry.insert(0, "0.8")

# info Label
infoLabel = tk.Label(root, text="処理停止中")
infoLabel.place(x=0, y=200)


root.after(1000, clicker)
root.mainloop()
