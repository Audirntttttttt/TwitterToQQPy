import os, sqlite3
import requests
import time
from urllib import parse  

class picbase:
    def __init__(self):
        super().__init__()
        self.db_file = os.path.join(os.path.dirname(__file__), "pic.db")
        if os.path.isfile(self.db_file):
            os.remove(self.db_file)
        if not self.extable():
            self.oritable()

    def extable(self):
        SQL="SELECT count(*) FROM sqlite_master WHERE type='table' AND name='pics'"
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(SQL)
        values = cursor.fetchall()
        values=bool(values[0][0]) 
        cursor.close()
        conn.commit()
        conn.close()
        return values



    def oritable(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('''
            create table pics(hash VARCHAR(20) primary key,
                                time INT,
                                url VARCHAR(255),
                                delurl VARCHAR(255))
                            ''')
            #cursor.execute()
            
        except Exception as e:
            print('建立错误：', e)
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        pass

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
        
        url='https://sm.ms/api/upload'
        
        file_obj=open(os.path.join(os.path.dirname(__file__),imgname),'rb')
        file={'smfile':file_obj}
        data_result=requests.post(url,data=None,files=file)
        a = data_result.json()
        print(a)
        hash = a["data"]["hash"]
        timeinserver = a["data"]["filename"].split(".")[0]
        url = a["data"]["url"]
        delete = a["data"]["delete"]
        sql = "INSERT INTO pics VALUES("+" '"+hash+"',"+" '"+timeinserver+"',"+" '"+url+"',"+" '"+delete+"')"
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(sql)
            #cursor.execute()
            
        except Exception as e:
            print('插入错误：', e)
            return "faile"
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        return url


    def listpic(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('select * from pics')
            values = cursor.fetchall()
            print(values)
            return 1
        except Exception as e:
            print('查询错误：', e)
            return -1
        finally:
            cursor.close()
            conn.commit()
            conn.close()

