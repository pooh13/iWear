cnt=0
with open('C:/Users/USER/Desktop/iWear/SQLTest/postData1118.sql',"w",encoding='UTF-8') as ff:
    for a in range(6):
        a=a+1
        a = "%02d" % a
        for b in range(12):
            b=b+1
            b = "%02d" % b
            for c in range(11):
                c=c+1
                c = "%02d" % c
                for d in range(10):
                    d=d+1
                    d = "%02d" % d
                    for e in range(10):
                        e=e+1
                        e = "%02d" % e
                        for f in range(12):
                            f=f+1
                            f = "%02d" % f
                            s="insert into post (account, userid, photo, time, word, styleNo, accessoriesNo, clothesNo, coatNo, pantsNo, shoesNo) values ('110', 'tata95', 'photos/logo.jpg','2018-01-01 00:00:00.000','今天天氣真好 適合穿搭','ST%s','AC%s','CL%s','CO%s','PA%s','SH%s');" %(str(a),str(b),str(c),str(d),str(e),str(f))
                            ff.write(s+"\n")
                            print(s)