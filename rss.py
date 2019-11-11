import baidu_trans
import feedparser
import time
import re
import pictrans
from datetime import datetime


def search_all(patter,strs):
    str = []
    num = patter.find('"')
    while re.search(patter,strs)!=None:
        result = re.search(patter,strs).span()
        str_one = strs[result[0]+num:result[1]-1]
        str.append(str_one)
        strs = strs[result[1]+1:len(strs)]
    
    return(str)

def content(text):
    p = r'<.*?>'
    return re.sub(p,"  ",text)

def twigen(url,minute,trans):
    messegess = []
    url = "https://rsshub.app/"+url
    d = feedparser.parse(url)
    print("success")
    

    timenow = datetime.utcnow().timestamp()
    print(timenow)
    xxx = d.entries
    print(len(xxx))
    for i in xxx:
        print(time.mktime(i.published_parsed))
        if timenow-time.mktime(i.published_parsed)<60*minute:
            timesss = i.published_parsed
            user = d.feed.title
            twitter = i.summary_detail.value
            print(1)

            vedio_p = r'video src=\".*?\"'
            imgs_p =  r'img src=\".*?\"'
            covers_p = r'poster=\".*?\"'
            url_p = r'href=\".*?\"'

            twitte_content = content(twitter)
            
            #print(twitte_transed)
            print(2)
            #替换<br>
            #翻译

            twitte_media = twitter

            vedio = search_all(vedio_p,twitte_media)
            #print(vedio)
            imgs = search_all(imgs_p,twitte_media)
            #print(imgs)
            covers = search_all(covers_p,twitte_media)
            #print(covers)
            url = search_all(url_p,twitte_media)
            #print(url)

            time.sleep(2)

            medias = ""
            pictrsnsformer = pictrans.picbase()
            if len(imgs) != 0:
                medias = medias + "图片：\n"
                for i in imgs:
                    i = pictrsnsformer.pictobase(i,1)
                    medias = medias + '[CQ:image,cache=0,file=' + i + ']\n'
            if len(vedio)!=0 :
                medias = medias + '视频：\n'
                medias = medias + "视频链接:\n"
                medias = medias + vedio[0]
                medias = medias + "视频封面:\n"
                covers = pictrsnsformer.pictobase(covers[0],0)
                medias = medias + '[CQ:image,cache=0,file=' + covers + ']\n'
            if len(url)!=0 :
                medias = medias + "链接:\n"
                for i in url:
                    medias = medias + i + "\n"
            
            timesss = time.asctime(timesss)
           
            if(trans):
                twitte_transed = baidu_trans.trans(twitte_content)
                messeges = user + "更新：\n\n原文：\n" + twitte_content + "\n\n译文（机翻）：\n" + twitte_transed + "\n" + medias +str(timesss)
            else:
                
                messeges = user + "更新：\n\n原文：\n" + twitte_content + "\n" + medias +str(timesss)
            #print(messeges)

            messegess.append(messeges)
            print(len(messegess))
            time.sleep(10)
            print("-----------------------")

    return messegess

