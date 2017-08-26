# -*- coding: utf-8 -*-
'''
这根据 品牌关键词 组合内容的主程序，totxt.py---20170731
'''
import urllib2,requests
import socket,sys,random,time,os,re,chardet
import lxml.etree as etree
from useragent import pcualist
import getinfo
reload(sys)
sys.setdefaultencoding('utf-8')
def errlog(kw,bf):
    with open('errfn.txt','a') as yc:
        yc.write(kw+'\terr:'+bf+'\n')
    yc.close()
#User Agent
def getua():

    User_Agent = pcualist()

    headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Cookie':'freshGuide=1; BIDUPSID=7AD6B1F0076AD0D5E2810FF36119FB56; __cfduid=dbd033b635bd1268fdaefa87e2d34c1261470191700; PSTM=1472281639; BAIDUID=F44B09D83A8074889DE20E167B6F4EBB:FG=1; MCITY=-153%3A268%3A; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02234882544; H_PS_PSSID=1468_20792_18240_21125_17001_20856_20733_20837_20885',
                'Host':'baike.baidu.com',
                'Referer':'https://baike.baidu.com/',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':User_Agent
    }
    return headers

#去掉html
def gotdes(html):
    link = re.compile("<.*?>")
    info2 = re.sub(link,'',info)
    return info2
def getcode(url):
    r = requests.get(url, allow_redirects = False)
    return str(r.status_code)
f1=open('ex.txt','r')
exs=f1.readlines()
f1.close()
logsfile = 'logs'
nowday=time.strftime('%Y%m%d')

with open('mk.txt','r') as us:
    fs=us.readlines()

for x,gurl in enumerate(fs,1) :
    ur = 'http://baike.baidu.com/search/word?word=%s'%gurl.strip()
    try:
        scode=getcode(ur)
        print str(scode),gurl.strip()
    except Exception,e:
        print e
        pass
    res = requests.head(ur)
    lt=res.headers['Location']
    if 'none' in lt:
        print 'first search is no res'
        try:
            req1 = urllib2.Request(lt,headers=getua())  #
            #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            r1 = urllib2.urlopen(req1)
            html1 = r1.read()
        except Exception,e:
            print 'lose',e
            continue
        page1 = etree.HTML(html1.lower())
        t1=page1.xpath('//dl[@class="search-list"]')
        t1num=len(t1)
        if t1num == 0 :
            errlog(gurl.strip(),'no res of baike')
            continue
        nnewurl=t1[0].xpath('dd[1]/a/@href')[0]
        print 'second search url is ',nnewurl  #得到第二层地址
    elif 'word' in lt:
        res = requests.head(lt)
        if 'baike.baidu.com' in res.headers['Location']:
            nnewurl=res.headers['Location']
        else:
            nnewurl='http://baike.baidu.com'+res.headers['Location']
        print 'have a redict agen',nnewurl
    else:
        print 'redict 302, ',lt
        nnewurl=lt
        #print nnewurl,lt
    #一这一步，得到了搜索词的最终百科页，然后开始抓取页面的内容
    try:
        req = urllib2.Request(nnewurl,headers=getua())
        r = urllib2.urlopen(req)
        html = r.read()

        print '网址已经得到',x,nnewurl
        flog=open(logsfile,'a')
        flog.write(str(x)+'\t ###  \t'+nnewurl+'\t ###  \tYY\n')
        flog.close()
        inum1 = random.choice(range(2,5))
        #print inum1
        time.sleep(inum1)
    except Exception,e:
        flog=open(logsfile,'a')
        flog.write(str(x)+'\t ###  \t'+ur+'\t ###  \tNN\n')
        flog.close()
        print 'NN',x,nnewurl,e
        continue
    content = ''
    page = etree.HTML(html.lower())
    t=page.xpath('//h1/text()')
    #print len(t),'title'
    if len(t) == 0 :
        #pass
        continue
    tit= t[0]
    des11=page.xpath('//div[@class="lemma-summary"]')
    if len(des11) == 0 :
        print 'n'
        continue
    des1=des11[0].xpath('string(.)')
    des11=page.xpath('//div[@class="para"]')
    bklist=des11[1:4]
    #dessss=gotdes(info)
    txt=''
    for bkstr in bklist:
        bks =bkstr.xpath('string(.)')
        txt+='<p>'+bks.strip()+'</p>'
    #print des1+txt
    print 'get price'
    prices=getinfo.gettext(gurl.strip())
    titles= gurl.strip()+random.choice(exs).strip()
    #print 'get pic url'
    #picurl=getinfo.getpic(gurl)
    print 'get related'
    rela=getinfo.getrelate(gurl)
    content='%s<p>%s<p>%s%s<p>相关推荐：</p>%s'%(titles,des1.strip(),txt,prices,rela)
    savefile = 'res/'+titles+'.txt'
    fres2=open(savefile.decode('utf-8'),'w')
    fres2.write(content+'\n')
    fres2.close()
    print titles+' finish !'
    inum = random.choice(range(3,9))
    time.sleep(inum)