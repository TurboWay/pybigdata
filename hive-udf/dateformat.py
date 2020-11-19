#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 16:12
# @Author : way
# @Site : 
# @Describe: 日期格式化 udf

import sys, datetime

CN_NUM = {
    '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '〇': 0,
    '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2,
    'Ｏ': 0,
}


# 日期转换主函数
def todate(dt):
    dt = dt.strip()
    has_CN = check_CN(dt)
    date = strtodate(dt) if has_CN else inttodate(dt)
    return date


# 判断是否含有中文
def check_CN(dt):
    for i in dt:
        if CN_NUM.get(i):
            return True
    return False


# 中文日期格式处理
def strtodate(dt):
    """
    :param dt: 中文日期 格式：二零一一年一月一日、二零一一年一月
    :return: date 格式：20110101
    """
    date = dt
    try:
        dt, st = dt.strip(), []
        if '日' in dt:
            dt = dt.replace('日', '')
            for ymd in ['年', '月']:
                dt = dt.replace(ymd, '-')
            dt = dt.split('-')
        elif '月' in dt:
            dt = dt.replace('月', '')
            dt = dt.split('年')
        elif '年' in dt or len(dt) == 12:
            dt = dt.replace('年', '')
            dt = [dt]

        for i in dt:
            s = 0
            if '十' in i:
                if len(i) == 1:
                    s = 10
                else:
                    a = i.split('十')
                    s = s + CN_NUM[a[0]] * 10 if a[0] else 10
                    if a[1]: s = s + CN_NUM[a[1]]
            elif len(i) == 1:
                s = '0' + str(CN_NUM[i])
            else:
                s = ''.join([str(CN_NUM[k]) for k in i])
            st.append(str(s))
        date = checkdate('-'.join(st))
    except:
        date = '[ERROR]' + date
    return date


# 数字日期格式处理
def inttodate(dt):
    """
    :param dt: 数字日期 格式：20110101、01/2011、2011-01、2011.01.01、2018.7.5、18-12-3、18.2.3
    :return: date 格式：2011-01-01
    """
    date = dt
    try:
        if '年' not in dt and ('月' in dt or '日' in dt):  # 没有年份的混搭当做异常
            raise RuntimeError()
        dt = dt.replace('年', '-').replace('月', '-').replace('日', '')
        if dt[-1] == '-': dt = dt[:-1]
        dt = dt[:10].replace('.', '-').replace('．', '-').strip()
        if '-' in dt:
            dt = dt.split('-')
            if len(str(dt[0])) == 2:  # yy-mm-dd 中 yy大于60 为20xx 否则 19xx
                dt[0] = '19' + str(dt[0]) if int(dt[0]) >= 60 else '20' + str(dt[0])
            for index, i in enumerate(dt, 0):
                if len(str(i)) == 1:
                    dt[index] = '0' + str(i)
            st = '-'.join(dt)
        elif '/' in dt:
            dt = dt.split('/')
            if len(dt[0]) < 4:
                dt.reverse()
            dt = (str(i) for i in dt)
            st = '-'.join(dt)
        elif len(dt) == 8:
            st = "{0}-{1}-{2}".format(dt[:4], dt[4:6], dt[6:])
        elif len(dt) == 6:
            if int(dt[:4]) >= 1960:  # 前面4位大于1960 认为是yyyy-mm 否则 yy-mm-dd
                st = "{0}-{1}".format(dt[:4], dt[4:6])
            else:
                yyyy = '19' + str(dt[:2]) if int(dt[:2]) >= 60 else '20' + str(dt[:2])
                st = "{0}-{1}-{2}".format(yyyy, dt[2:4], dt[4:6])
        else:
            st = dt
        date = checkdate(st)
    except:
        date = '[ERROR]' + date if date else date
    return date


# 检查日期合法性
def checkdate(dt):
    """
    :param dt: 数字日期 格式：2011、2011-01、2011-01-01
    :return: correctdate 格式：2011、2011-01、2011-01-01
    """
    dt = dt.split('-')
    if dt[0][0] == '0':  # 年份不能以0开头
        raise RuntimeError()
    if len(dt) == 1:  # 只有年
        year, month, day = int(dt[0]), 1, 1
        dt = datetime.datetime(year, month, day)
        correctdate = str(dt)[:4]
    elif len(dt) == 2:  # 年月
        year, month, day = int(dt[0]), int(dt[1]), 1
        dt = datetime.datetime(year, month, day)
        correctdate = str(dt)[:7].replace('-', '')
    else:  # 年月日
        year, month, day = int(dt[0]), int(dt[1]), int(dt[2])
        dt = datetime.datetime(year, month, day)
        correctdate = str(dt)[:10].replace('-', '')
    return correctdate


if __name__ == '__main__':
    for line in sys.stdin:
        cols = line.split('\t')
        for index, col in enumerate(cols, 0):
            if len(col) >= 3:
                if col[:3] == 'UDF':
                    cols[index] = todate(col[3:])
        cols = [col.replace('\n', '') for col in cols]
        sys.stdout.write('\t'.join(cols) + '\n')
