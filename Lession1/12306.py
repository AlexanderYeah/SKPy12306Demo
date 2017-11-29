#coding=utf-8;


import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context;
target_url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-03&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=PEN&purpose_codes=ADULT"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"

# 获取车辆信息
"""
    https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-03&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=PEN&purpose_codes=ADULT
"""


def getTrainList():
    req = urllib.request.Request(target_url);
    req.add_header("User-Agent",user_agent);
    rsp = urllib.request.urlopen(req);
    html = rsp.read();
    print(html);

if __name__ == '__main__':
    getTrainList();