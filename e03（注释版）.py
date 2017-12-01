# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:25:27 2017

@author: mymac
"""

#coding:utf-8
import urllib2
import re
import os
BOR_amount=0.0
url='http://58921.com/'#打开网页读取网页
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
webpage= urllib2.urlopen(req)
strw=webpage.read()
s=strw.find("电影名称</th><th>总场次/占比")#切片开头
e=strw[s:].find("各平台场次存在重叠，实时与预计票房为程序自行计算，仅供参考")#切片结尾
strw_tab=strw[s:s+e] #切片数据
#print strw_tab
m=[]#新建一个m的列表
m=re.findall(r'<tr class="[a-z]{3,4}"><td><a href="/film/[0-9]+/boxoffice" title=.+</tr>',strw_tab) #把每一部电影的数据作为m列表的一个元素
#print '----------------------'
#print m#输出列表的一个元素用来观察，以方便稍后写正则表达式清理数据
if not m:
    exit()#如果列表m没有元素直接退出程序
for t in m:#历遍列表m的元素
    ss=[]#新建一个列表，每次循环时清空列表
    ss=re.findall(r'(\d+[\.|/]?\d*[\.]?\d*[%]*[^\x00-\xff]*)',t) #把元素中的数字提取出来，[^\x00-\xff]是匹配双字节字符(包括汉字在内)
    print ss
    print ss[-3]#由于列表的倒数第三个元素是实时票房
    if ss:
        BOR_amount+= float(ss[-3]) #累加实时票房
    else:
        print "error"
print "票房总额是:  "+str(BOR_amount)+"万元"
