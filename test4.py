#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\test4.py
# Last Modified: Fri Jun 08 2018
# Modified By: yinchao
###

### 序列化
import pickle
import os
import json

dict_yc = dict()
dict_yc['yc'] = '尹超'
dict_yc['dqwj'] = '大桥未久'

# 创建一个文件夹
if os.path.exists('./output'):
    pass
else:
    os.mkdir('./output')
    
# 创建输出文件
with open('./output/output.txt', 'wb') as f:
    pickle.dump(dict_yc, f)  # 将对象序列化后，写入like file object中

#读取内容
if os.path.isfile('./output/output.txt'):
    with open('./output/output.txt', 'rb') as f:
        dict_yc = pickle.load(f)  # 将一个序列化了的对象从 like-file object 中反序列化读取出来
        print(dict_yc)


# picking with JSON

dict_yc = dict()
dict_yc['yc'] = '尹超'
dict_yc['dqwj'] = '大桥未久'

with open('./output/output_json.txt', 'w', encoding = 'utf-8') as f:
    json.dump(dict_yc, f)  # 将对象序列化后，写入like file object中 with json

if os.path.isfile('./output/output_json.txt'):
    with open('./output/output_json.txt') as f:
        dict_yc = json.load(f)  # 将一个序列化了的对象从 like-file object 中反序列化读取出来
        print(dict_yc)
        
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False) # ensure_ascii 是否使用 ascii 码进行序列化
print(s)



# json 的另一个使用
## 需求，序列化一个类
### 使用 default 参数，制定转换格式，
### 也可以在类中 使用特殊值 __dict__

