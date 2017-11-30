#coding=utf-8;


import urllib.request

import ssl
import json

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
    # 将截取到的json 数据转换成字典
    dic = json.loads(html);
    # 获取到车次信息 进行返回
    return  dic["data"]["result"];

# 处理返回的车次信息
"""
    每一条车次信息 字段对应的位置
    索引为23 对应的软卧
    28 对应的是硬卧
    29 对应的是硬座
    26 对应的是无座
    3  对应的车次
"""
test_flag = 0;
def dealWithTrainInfo(dict):
    # 每一条车次信息以及字段
    for item  in dict:
        temp_list = item.split('|');
        # 以下代码是为了知道字段对应的索引
        # global  test_flag;
        # for i in temp_list:
        #     print('%s--%s',(test_flag,i));
        #     test_flag += 1;
        try:
            # 此处 要进行类型转换 字符串与0作比较，永远都是大于0的
            if int(temp_list[23]) > 0:
                print (temp_list[3]+'--'+'有票');
        except:
            # 在中文前面加上U 表示字符串是unicode 编码
            if temp_list[23] == u'有':
                print(temp_list[3] +'--'+ '有票');
            else:
                print(temp_list[3] +'--'+ "无票");

if __name__ == '__main__':

    dict = getTrainList();
    dealWithTrainInfo(dict);