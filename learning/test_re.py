#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@E-mail:zhengaihua@jd.com
@file: test_re.py
@time: 2021/7/1 17:28
@desc: 正则表达式
@url: https://docs.python.org/zh-cn/3/library/re.html
"""

import re

# re.match 尝试从【字符串的起始位置】匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回none。
# re.match(pattern, string, flags=0)
# pattern     匹配的正则表达式
# string      要匹配的字符串。
# flags       标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

# 匹配对象方法
# group(num=0)    匹配的整个表达式的字符串，group()    可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()    返回一个包含所有小组字符串的元组，从1到所含的小组号。
def match():
    print(re.match(pattern='www', string='www.imeixi.cn', flags=0))
    print(re.match(pattern='www', string='www.imeixi.cn', flags=0).span())
    print(re.match(pattern='www', string='www.imeixi.cn', flags=0).group())
    print(re.match(pattern='www', string='wwww.imeixi.cn', flags=0).span())
    print(re.match(pattern='www', string='wwww.imeixi.cn', flags=0).group())
    print(re.match(pattern='www', string='wwww.imeixi.cn', flags=0).group(0))
    print("-----------")
    print(re.match(pattern='cn', string='www.imeixi.cn', flags=0))

    line = "Cats are smarter than dogs"
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
    match_obj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if match_obj:
        print("matchObj.group() : ", match_obj.group())
        print("matchObj.group(1) : ", match_obj.group(1))
        print("matchObj.group(2) : ", match_obj.group(2))
    else:
        print("No match!!")


# re.search方法
# re.search   扫描整个字符串并返回【第一个】成功的匹配。
# re.search(pattern, string, flags=0)
def search():
    print(re.search('www', 'www.imeixi.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.imeixi.com').span())  # 不在起始位置匹配
    line = "Cats are smarter than dogs"
    search_obj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
    if search_obj:
        print("searchObj.group() : ", search_obj.group())
        print("searchObj.group(1) : ", search_obj.group(1))
        print("searchObj.group(2) : ", search_obj.group(2))
    else:
        print("Nothing found!!")


# 检索和替换
# Python的re模块提供了re.sub用于替换字符串中的匹配项。
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern: 正则中的模式字符串。
# repl: 替换的字符串，也可为一个函数。
# string: 要被查找替换的原始字符串。
# count: 模式匹配后替换的最大次数，默认0表示替换所有的匹配。
# flags: 编译时用的匹配模式，数字形式。
def sub():
    phone = "2004-959-559 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码 : ", num)

    # 移除非数字的内容
    # \D 匹配任意非数字
    num = re.sub(r'\D', "", phone)
    print("电话号码 : ", num)


def match_search_diff():
    line = "Cats are smarter than dogs"
    match_obj = re.match(r'dogs', line, re.M | re.I)
    if match_obj:
        print("match --> matchObj.group() : ", match_obj.group())
    else:
        print("No match!!")
    match_obj = re.search(r'dogs', line, re.M | re.I)
    if match_obj:
        print("search --> searchObj.group() : ", match_obj.group())
    else:
        print("No match!!")


# sub() 中 repl 参数是一个函数
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


def sub_repl_function():
    s = 'A23G4HFD567'
    # \d+ 匹配任意数字，匹配1个或多个的表达式
    # (?P < name > …) 命名组合）类似正则组合，但是匹配到的子串组在外部是通过定义的 name 来获取的。
    print(re.sub(r'(?P<value>\d+)', double, s))


# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.compile(pattern[, flags])
#     pattern : 一个字符串形式的正则表达式
#     flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
#         re.I 忽略大小写
#         re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
#         re.M 多行模式
#         re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
#         re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
#         re.X 为了增加可读性，忽略空格和 # 后面的注释
def re_compile():
    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
    m = pattern.match('Hello World Wide Web')
    print(m)
    print(m.group(0))
    print(m.span())
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))


def re_compile_2():
    pattern = re.compile(r'\d+')
    m = pattern.match('one12twothree34four')
    print(m)
    m = pattern.match('one12twothree34four', 2, 10)
    print(m)
    m = pattern.match('one12twothree34four', 3, 10)
    print(m)
    print(m.group(0))
    print(m.start(0))
    print(m.end(0))
    print(m.span(0))


# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# 语法格式为：
#   findall(string[, pos[, endpos]])
#     string : 待匹配的字符串。
#     pos : 可选参数，指定字符串的起始位置，默认为 0。
#     endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
def re_findall():
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)
    print(result1)
    print(result2)


# re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个【迭代器返回】。
#     re.finditer(pattern, string, flags=0)
#         pattern	匹配的正则表达式
#         string	要匹配的字符串。
#         flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
def re_finditer():
    it = re.finditer(r"\d+", "12a32bc43jf3")
    for _match in it:
        print(_match.group())


# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
# re.split(pattern, string[, maxsplit=0, flags=0])
#     pattern	匹配的正则表达式
#     string	要匹配的字符串。
#     maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
#     flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
def re_split():
    # '\W'	匹配非数字字母下划线
    re_list = re.split(r'\W+', 'runoob, runoob, runoob.')
    print(re_list)
    re_list = re.split(r'\W+', ' runoob, runoob, runoob.')
    print(re_list)
    re_list = re.split(r'\W+', ' runoob, runoob, runoob.', 1)  # 只分割1次
    print(re_list)
    re_list = re.split(r'a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
    print(re_list)


def name():
    # sms = "【HIDance舞蹈】尊敬的客户，2021-05-20的课程：芭蕾四级班已签到，本次划课2.00课时，剩余通用课时:29.50课时，剩余总课时通用课时：29.50，一对一：0.00，一对二：1.00。"
    sms = "【HIDance舞蹈】尊敬的客户，2021-06-28的课程：一对一已签到，本次划课1.00课时，剩余一对一:16.00课时，剩余总课时通用课时：11.00，一对一：16.00，一对二：17.00。"
    pattern = re.compile("尊敬的客户，(?P<date>.*)的课程：(?P<category>.*)已签到，本次划课(?P<subtract>.*)课时，"
                         "剩余(?P<category_>.*):(?P<category_left>.*)课时，剩余总课时通用课时：(?P<sum>.*)，一对一：(?P<single>.*)，一对二：(?P<double>.*)。")
    match_obj = pattern.search(sms)
    print(match_obj.group("date"))
    print(match_obj.group("category"))
    print(match_obj.group("subtract"))
    print(match_obj.group("category_"))
    print(match_obj.group("category_left"))
    print(match_obj.group("sum"))
    print(match_obj.group("single"))
    print(match_obj.group("double"))
    print(match_obj.groups())


if __name__ == '__main__':
    name()
