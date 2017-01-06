# /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import sleep


# telnum = re.compile(r'^(\d{8}).+phone":"(\d{0,12}|\d{3,4}[-|\s+]\d{7,8})","name":"(\W*)","aliasName')
# telnum = re.compile(r'^(\d{8}).+phone":"(\d{0,12}|\d{3,4}[-|\s+]\d{7,8})","(?:name|status)":"(\W*)",')
# n = 1
# with open("/home/yulore/Desktop/cootek") as f:
#     for line in f.readlines():
#         # print line
#         record = telnum.search(line).groups()
#         print "line %d: \t%s\t\t%s\t\t" %(n, record[0],record[1])
#         n = n + 1


# number = '2016111022.32585:2016-11-10 22:33:47::push_plat_cootek::cootek 数据处理 {"refid":"0fe14b7f78c9902100cbf551a7ad50b7","phone":"9006056655","name":"华大基因","aliasName":"华大基因","'
# telnum = re.compile(r'^(\d{8}).+phone":"(\d{0,12})","name":"(\W+)","aliasName')
# tel = telnum.search(number).groups()
# print tel
# print "the number are %s and phhone %s and name %s" %(tel[0],tel[1],tel[2])



telNumList = []
lineNum = 0
with open('whitelist-100w.txt', 'rw+') as wlist:
    content = wlist.readlines()
    while lineNum < len(content) :
        if (lineNum % 10000 == 0) :
            whiteList = content[lineNum]
            print "%s the content is: %s" % (lineNum, whiteList)
            telNumList.append(whiteList)
        lineNum += 1
print telNumList
