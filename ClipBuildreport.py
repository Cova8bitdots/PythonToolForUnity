#!/usr/bin/env python
# coding: UTF-8

import sys;
import os;


def Usage():
	print('Usage: python3 FilePath outputPath')
	print("Argument")
	print("\tFilePath:path of UnityEditor.log ")
	print("\toutputPath:OutputPath")
	print("")


# ここからメイン
if len(sys.argv) < 3:
	Usage()
	sys.exit()


# コマンドラインパース
filePath = sys.argv[1]
outputPath = sys.argv[2]

# 区切り行
SPLIT_LINE = "-------------------------------------------------------------------------------"
isStartRead = False

# Logファイル読み取り
result = ""
print("===== Read File =====")
with open(filePath, 'r', encoding="UTF-8") as fp:
	s_line = fp.readline()
	while s_line:		
		# 区切り行になったらフラグ反転
		if SPLIT_LINE in s_line :
			# フラグが戻るときに最後の行も追加する
			if (isStartRead) :
				result += s_line
			isStartRead = 1-isStartRead
			
		# 読み取りフラグが立っていればパース
		if isStartRead:
			result += s_line
		s_line = fp.readline()

# ファイル掃き出し
print("===== Write File =====")
with open(outputPath, 'w', encoding="UTF-8") as fp:
	fp.write(result)
