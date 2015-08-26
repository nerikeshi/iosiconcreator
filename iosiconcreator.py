# -*- coding: utf-8 -*-
import sys
import os
from PIL import Image
import copy
import shutil

# アイコンのサイズとファイル名を指定する。今後アイコンが増えた場合は本変数を修正すること。
iconList = [
    # icon-29.png
    # (iPhone Spotlight(iOS6), iPhone設定(iOS6), iPad設定(iOS7,8)) 29×29
    [(29, 29), "icon-29.png"],

    # icon-29@2x.png
    # (iPhone設定(iOS6, 7), iPad設定(iOS6, 7, 8)) 58×58
    [(58, 58), "icon-29@2x.png"],

    # icon-29@3x.png
    # (iPhone設定) 87×87
    [(87, 87), "icon-29@3x.png"],

    # icon.png
    # (iOS6 ホーム用)	57×57
    [(57, 57), "icon.png"],

    # icon@2x.png
    # (iOS6 retina　ホーム用)	114×114
    [(114, 114), "icon@2x.png"],

    # icon-60@2x.png
    # (iOS7 retina　ホーム用)	120×120
    [(120, 120), "icon-60@2x.png"],

    # icon-60@3x.png
    # (iOS8 retina　ホーム用)	180×180
    [(180, 180), "icon-60@3x.png"],

    # icon-small.png
    # (iOS6 Spotlight検索用)	29×29
    [(29, 29), "icon-small.png"],

    # icon-small@2x.png
    # (iOS6 RetinaのSpotlight検索用およびiOS7用)	58×58
    [(58, 58), "icon-small@2x.png"],

    # icon-small-40@2x.png
    # (iOS7 設定用)	80×80
    [(80, 80), "icon-40@2x.png"],

    # iTunesArtwork
    # (iOS6 app store用/拡張子なしでOK)	512×512
    [(512, 512), "iTunesArtwork"],

    # icon-72.png
    # (iOS6 ホーム用)	72×72
    [(72, 72), "icon-72.png"],

    # icon-72@2x.png
    # (iOS6 Retinaホーム用)	144×144
    [(144, 144), "icon-72@2x.png"],

    # icon-76.png
    # (iOS7 ホーム用)	76×76
    [(76, 76), "icon-76.png"],

    # icon-76@2x.png
    # (iOS7 Retinaホーム用)	152×152
    [(152, 152), "icon-76@2x.png"],

    # icon-small-40.png
    # (iOS7 Spotlight検索用)	40×40
    [(40, 40), "icon-small-40.png"],

    # icon-small-40@2x.png
    # (iOS7 Retina Spotlight検索用)	80×80
    [(80, 80), "icon-small-40@2x.png"],

    # icon-small-40@3x.png
    # (iPhone Spotlight(iOS8))	120×120
    [(120, 120), "icon-small-40@3x.png"],

    # icon-small-50.png
    # (iOS6 Spotlight検索用)	50×50
    [(50, 50), "icon-small-50.png"],

    # icon-small-50@2x.png
    # (iOS6 RetinaのSpotlight検索用)	100×100
    [(100, 100), "icon-small-50@2x.png"],

    # iTunesArtwork
    # (iOS6およびiOS7 Retina app store用/拡張子なしでOK)	1024×1024
    [(1024, 1024), "iTunesArtwork@2x"]

]

# エラー時に出力するusage文字列　
usage = "usage : python iosiconcreator.py xxx.png(1024x1024)"
# 出力対象のディレクトリ
outputDir = "./icons"

# 引数にファイル名を指定してしない場合、エラー
if len(sys.argv) < 2:
    print usage
    quit()

# ベースになるファイルパスをコマンドライン引数から取得
filePath = sys.argv[1]
print "base file = "+filePath

# 取得したファイルが存在しない場合、エラーメッセージを表示して終了。
if not os.path.exists(filePath):
    print "error base file not found."
    print usage
    quit()
print "base file exists."

# 出力先が既に存在する場合、一旦削除
if os.path.exists(outputDir):
    try:
        shutil.rmtree(outputDir)
        print "outputDir remove success."
    # 削除時に例外が発生した場合、メッセージを出力して処理終了　
    except OSError:
        print "failed remove outputDir."
        raise

# 出力先のディレクトリを作成　
try:
    os.makedirs(outputDir)
    print "create outputDir success."
except OSError:
    print "failed create outputDir."
    raise

# # # # # # # # # # ここから各種サムネイルの生成# # # # # # # # # #
for iconInfo in iconList:
    size = iconInfo[0]
    iconFilename = iconInfo[1]
    iconImage = Image.open(filePath)
    iconImage.thumbnail(size, Image.ANTIALIAS)
    iconImage.save(outputDir+"/"+iconFilename, "PNG")
    print iconFilename+" "+str(size[0])+"x"+str(size[1])+" created."
print "icon all data create success."
