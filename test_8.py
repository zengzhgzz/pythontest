# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
height = input('悄悄告诉我你的身高(m)是：')
weight = input('悄悄告诉我你的体重(kg)是：')
bmi =weight/height**2
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
else:
    print("严重肥胖")

