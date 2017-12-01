# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:36:01 2017

@author: mymac
"""
from e02 import *
import urllib2
import re
import os

url = 'http://theater.mtime.com/China_Beijing/' # 1.需抓取的网址
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) # 2.模拟浏览器获得网页访问
webpage = urllib2.urlopen(req) #urllib2.urlopen(url[, data][, timeout])#3.打开模拟浏览器获得的网页
strw = webpage.read()#4.阅读网页，这时如果print strw会获得网页的源码
#print strw
tg_start = strw.find('hotplaySvList = [') #5.寻找源码里面的关键字
if tg_start == -1:#6.如果找不到关键字会返回一个-1
	print 'not find start tag'
	os.exit()#6.1 如果找不到关键字退出程序
tmp = strw[tg_start:-1]#赋给tmp切片从开头关键字到源码最后的列表
tg_end = tmp.find(';')#在tmp切片当中寻找关键字
if tg_end == -1 :			#若找不到退出程序
	print 'not find end tag'
	os.exit()
tmp = tmp[len(' hotplaySvList = ['):tg_end]#再次切片，缩小范围，len（）是为了忽略掉hotplaySvList = [
#print tmp
tar_ls = tmp.split("},{") #把切片中关键字   },{   进行切片，样式变成"Id":209688,"Url":"http://movie.mtime.com/209688/","Title":"金刚狼3：殊死一战
#print tar_ls
dict_film = {} # 定义字典
for t0 in tar_ls:#把tar_ls的列表元素依次赋值给t0
	ls_t=t0.split(',')#以逗号为分隔符进行分割     http://www.runoob.com/python/att-string-split.html  样式['"Id":195064', '"Url":"http://movie.mtime.com/195064/"', '"Title":"美女与野兽"}]']
	id=ls_t[0].split(':')[-1].strip() #首先在['"Id":195064'切片，分成"Id"和195064两段，取倒数第一段195064；若把[-1]变为[-2],会输入id
	film=ls_t[-1].split('"')[-2].strip()#切片成'"Title":"美女与野兽"}]'，由于.split('"')把切片切成四段}]和‘美女与野兽’和:和Title
	dict_film[id]=film#把ID当做键，电影名当做值储存到字典
#print ls_t
#print id
#print film
for t in dict_film:    #循环输出字典
	score=mean_audience_score(t)
	print "id: " + t + "  film:  " + dict_film[t] + "   scroe:   " + `score`
    #print "id: "+t+"  film:  ",dict_film[t]
print 'ok  total : '+`len(dict_film)`
