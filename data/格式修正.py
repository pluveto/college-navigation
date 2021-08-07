'''
功能：将文件中的 Id 等字符串表示转换为纯数字表示
使用方法：拖上去
'''

import os
import sys
import re
files = sys.argv[1:]
patterns = [
    ['"id": *"(\d+?)"', '"id": \g<1>'],
    ['"source": *"(\d+?)"', '"source": \g<1>'],
    ['"target": *"(\d+?)"', '"target": \g<1>'],
    ['"level": *"(\d+?)"', '"level": \g<1>'],
]
for file in files:    
    with open(file, encoding="utf-8",mode="r") as f:
        data = f.read()
    for pattern in patterns:
        data = re.sub(pattern[0], pattern[1], data)
    with open(file, encoding="utf-8",mode="w") as f:
        f.write(data)
    print("ok: " + file)
