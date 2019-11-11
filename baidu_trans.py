import requests
import hashlib
import random
import config

def genearteMD5(str):
    hl = hashlib.md5()

    hl.update(str.encode(encoding='utf-8'))

    return hl.hexdigest()

def trans(q):
    if q=="":
        return ""
    fromLang = 'auto'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    appid = config.appid
    secretKey = config.secretKey
    
    sign = appid+q+str(salt)+secretKey
    sign = genearteMD5(sign) 
    
    payload = {"q" : q ,"from" : fromLang ,"to" : toLang ,
                "appid" : appid, "salt" : salt, "sign" : sign}
    
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    
    r = requests.get(url, params=payload)
    
    text = eval(r.text)
    #print(text)
    #text0 = text['trans_result'][0]['dst']
    texts = ''
    try:
        for i in text['trans_result']:
            texts = texts+i['dst']+'\n'
    except KeyError as identifier:
        pass

    return texts


if __name__ == "__main__":
    print(trans('''【お知らせ】\n『Shiny Smily Story』のコール練習動画(試聴動画尺ver.)を投稿しました。\n近々...必要かもしれません？'''))