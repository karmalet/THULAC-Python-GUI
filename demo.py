#coding:utf-8

import thulac

thu1 = thulac.thulac(seg_only=False, model_path="./models", deli='/')  #设置模式为行分词模式
a = thu1.cut("我爱北京天安门")

print(a)
