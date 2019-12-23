import random
cnt=0
with open('C:/Users/USER/Desktop/iWear/SQLTest/postTestData.sql',"a",encoding='UTF-8') as ff:
    for a in range(1):
        a=a+1
        a = "%02d" % a
        for b in range(2):
            b=b+1
            b = "%02d" % b
        #     for c in range(11):
        #         c=c+1
        #         c = "%02d" % c
        #         for d in range(10):
        #             d=d+1
        #             d = "%02d" % d
        #             for e in range(10):
        #                 e=e+1
        #                 e = "%02d" % e
        #                 for f in range(12):
        #                     f=f+1
        #                     f = "%02d" % f
        s="insert into post (account, userid, time, word, styleNo, accessoriesNo, clothesNo, coatNo, pantsNo, shoesNo) values ('62', 'fangTest', '2018-01-01 00:00:00.000','今天天氣真好 適合穿搭','ST%s','AC%s','CL01','CO02','PA03','SH02');" %(str(a),str(b))
        ff.write(s+"\n")
        print(s)
