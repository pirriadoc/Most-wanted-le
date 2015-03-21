def checkio(text):
    dic={}
    textl=text.lower()
    for car in textl:
        if car.isalpha():
            if car not in dic:
                dic[car]=1
            else:
                dic[car]+=1
    print dic
    lisk = dic.keys()
    lisv = dic.values()
    print lisk
    print lisv
    lisks = lisk
    lisvs = lisv
    lisks.sort()
    lisvs.sort()
    print lisk
    print lisv
    mv = lisvs[-1]
    
    

    return 
