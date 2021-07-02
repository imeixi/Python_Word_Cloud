#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@E-mail:zhengaihua@jd.com
@file: sms_hidance_filter.py
@time: 2021/7/2 11:36
@desc:
@url: 
@version: 1.0
"""
import re


def filter_sms(hi_dance_sms):
    # print(hi_dance_sms)
    # pattern = re.compile("尊敬的客户，(?P<date>.*)的课程：(?P<category>.*)已签到，本次划课(?P<subtract>.*)课时，"
    #                      "剩余(?P<category_>.*):(?P<category_left>.*)课时，剩余总课时通用课时：(?P<sum>.*)，一对一：(?P<single>.*)，一对二：(?P<double>.*)。")
    # match_obj = pattern_date.search(hi_dance_sms)
    # print(match_obj.groups())
    pattern_date = re.compile("【HIDance舞蹈】尊敬的客户，(?P<date>.*)的课程")
    pattern_category = re.compile("课程：(?P<category>.*)已签到，")
    pattern_subtract = re.compile("本次划课(?P<subtract>.*)课时，")
    pattern_category_left = re.compile("剩余(?P<category_>.*):(?P<category_left>.*)课时，剩余总课时")
    pattern_sum = re.compile("剩余总课时通用课时：(?P<sum>.*?)，")
    pattern_single = re.compile("一对一：(?P<single>.*?)(。|，)")
    pattern_double = re.compile("一对二：(?P<double>.*)。")

    match_dict = dict()
    try:
        match_dict["date"] = pattern_date.search(hi_dance_sms).group("date")
        match_dict["category"] = pattern_category.search(hi_dance_sms).group("category")
        match_dict["subtract"] = pattern_subtract.search(hi_dance_sms).group("subtract")
        match_dict["category_"] = pattern_category_left.search(hi_dance_sms).group("category_")
        match_dict["category_left"] = pattern_category_left.search(hi_dance_sms).group("category_left")
        match_dict["sum"] = pattern_sum.search(hi_dance_sms).group("sum")
        match_dict["single"] = pattern_single.search(hi_dance_sms).group("single")
        match_dict["double"] = pattern_double.search(hi_dance_sms).group("double")
    except AttributeError:
        # print("解析出错。。。。\n", hi_dance_sms)
        pass
    return match_dict


if __name__ == '__main__':
    # 打开短信文件
    with open("resource/message.csv", "r") as f:
        sms_list = f.readlines()

    # 读取body值
    hi_dance_1v1 = []
    hi_dance_1v2 = []
    hi_dance_class = []
    hi_dance_all = []
    hi_dance_data = []
    for sms in sms_list:
        sms_cols = sms.split(',')
        if len(sms_cols) > 14:
            body = sms_cols[14]
            if body.__contains__("HIDance"):
                hi_dance_all.append(body)
                # 过滤短信
                hi_dance_data.append(filter_sms(body))

                if body.__contains__("一对一已签到"):
                    hi_dance_1v1.append(body)
                elif body.__contains__("一对二已签到"):
                    hi_dance_1v2.append(body)
                else:
                    hi_dance_class.append(body)

    # for msg in hi_dance_1v1:
    #     print(msg)
    # for msg in hi_dance_1v2:
    #     print(msg)
    # for msg in hi_dance_class:
    #     print(msg)
    print(len(hi_dance_data))
    for data in hi_dance_data:
        print(data)