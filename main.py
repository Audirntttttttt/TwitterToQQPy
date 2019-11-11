import config
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from cqhttp import CQHttp
import rss
import time

time_in_minutes = 20

def job():
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        bot = CQHttp(api_root=config.api_root,
                     access_token = config.access_token,
                     secret = config.secret)

        for i in config.QQ_Group:
            twis = rss.twigen(i[0],time_in_minutes,i[2])
            for k in twis:
                print(k)
                for j in i[1]:
                    bot.send_group_msg(group_id=j, message=k)
                    time.sleep(5)

        for i in config.QQ_Private:
            twis = rss.twigen(i[0],time_in_minutes,i[2])
            for k in twis:
                print(k)
                for j in i[1]:
                    bot.send_private_msg(user_id=j, message=k)
                    time.sleep(5)


        
if __name__ == "__main__":
    job()
    sched = BlockingScheduler()
    sched.add_job(job, 'interval',minutes = 20)
    sched.start()
            

