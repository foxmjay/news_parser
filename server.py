# -*- coding: utf-8 -*-
from __future__ import print_function
from bottle import route, run,  template ,static_file, redirect , request, response

from apscheduler.schedulers.background import BackgroundScheduler
import time
from parser import hespress_parser
import redis
import json
import os

r = redis.Redis(host="redis",port=6379,db=0)


def job():
    print("Working ..")
    data = hespress_parser()
    r.set("hespress",json.dumps(data))

    #with open('out.html','w') as f :
    #    for elem in data :
    #        f.write('<a href='+elem['href']+' target="_blank"><h3>'+elem['title']+'</h3></a>')



@route('/static/<filepath:path>')
def callback(filepath):
    """
        Serve static files.
    """
    static_path = os.path.dirname(os.path.realpath(__file__))
    return static_file(filepath, root=os.path.join(static_path,"static"))

@route('/')
def home():
    """
        Home Page
    """
    rslt=r.get("hespress")
    data=json.loads(rslt)

    return template('index.html',{"data":data})


if __name__ == "__main__":
    job()
    sched = BackgroundScheduler()
    sched.start()
    job=sched.add_job(job,trigger='interval',hours=1,id="1111")

    #run(host='0.0.0.0', port=8080, debug=True)
    run(server='gunicorn',host='0.0.0.0', port=8080, debug=True, workers=4)

