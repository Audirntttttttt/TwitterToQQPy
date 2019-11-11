import os,re
import requests
import time
from urllib import parse  

class picbase:
    def __init__(self):
        super().__init__()
    
    def pictobase(self,url,type):
        if type == 2:
            imgname = url
        else:    
            if type==1:
                url = url.split("?")
                img_src = url[0]
                res = dict(parse.parse_qsl(url[1]))
                img = requests.get(img_src,res)
                imgname = str(time.time())+"."+res["format"]
            elif type==0:
                img = requests.get(url)
                imgname = str(time.time())+url[len(url)-4:len(url)]
            with open(imgname, 'ab') as f:
                f.write(img.content)
                f.close()
        print(os.path.join(os.path.dirname(__file__),imgname))
        url='https://sm.ms/api/upload'
        file_obj=open(os.path.join(os.path.dirname(__file__),imgname),'rb')
        file={'smfile':file_obj}
        data_result=requests.post(url,data=None,files=file)
        a = data_result.json()
        print(a)
        if a["success"] == "True":
            url = a["data"]["url"]
        else:
            string = a["message"]
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  
            url = re.findall(pattern,string)[0]
        return url
