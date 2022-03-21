# -*- coding: utf-8 -*-
"""
質數---列出1~100之間的質數
"""
count=0
for i in range(2,100):
    num=0
    for j in range (1,i+1):
        if(i % j ==0):
            num+=1
        continue      
    if num ==2:
        print(i,end="\t")
        count+=1
print()
print("="*30)
print("1~100的質數總共有",count,"個")