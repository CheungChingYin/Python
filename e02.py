#coding:utf-8
import urllib2
import  re
def mean_audience_score(FilmId): #把e01的字典dict_film字典的键，即是电影的id作为形参
	arv=0.0#初始化评分
	sc_url="http://movie.mtime.com/"+FilmId+"/"#打开网页，把电影ID输入到网址后面方便切换到不同的电影获取评分
	sc_req=urllib2.Request(sc_url, headers={'User-Agent' : "Magic Browser"})
	sc_page=urllib2.urlopen(sc_req)
	sc_strw=sc_page.read()
	sc_str=re.findall(r'<span class="db_point ml6">+\d+\.+\d+</span>',sc_strw)
	'''
re.findall(pattern, string[, flags]):
搜索string，以列表形式返回全部能匹配的子串
print sc_str时会反馈一个多元素的列表['<span class="db_point ml6">9.0</span>', '<span class="db_point ml6">9.0</span>', '<span class="db_point ml6">9.0</span>']
正则表达式http://www.cnpythoner.com/post/300.html			http://deerchao.net/tutorials/regex/regex.htm
	'''
	if len(sc_str)==0: #如果抓不到评分就返回一个零分
		return arv
	for tt in sc_str:#把列表sc_str中的元素序号赋予为tt
		scsc=re.findall(r'\d+\.+\d',tt)#抓取每个元素中的评分
		arv=arv+float(scsc[0])#全部评分累加
	return arv/len(sc_str)#返回一个平均数，len(sc_str)是计算有多少个元素（即多少个评分）
'''	
在第一个程序的输出电影id和电影名称的地方加入
for t in dict_film:
	scroe=mean_audience_score(t)
	print "id: "+t+"  film:  "+dict_film[t]+"  scroe:  "+`scroe`
这样在输出第一题结果的同时把第二题也输出了
'''