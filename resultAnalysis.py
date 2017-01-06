# /usr/bin/env python
# -*- coding: utf-8 -*-


import re


with open('/home/yulore/Desktop/whitelist-80w-testresult', 'r') as inFile:
    for content in inFile.readlines():
        patten = re.compile(r'.+(号码.*毫秒).*')
        result = patten.search(content)
        if (result != None):
            str = result.group(1)
            with open('/home/yulore/Desktop/whitelist-80w-testresult-time', 'a') as outFile:
                outFile.write(str+'\n')