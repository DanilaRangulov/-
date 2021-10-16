with open("pokemon_full.json","r") as f:
    p=0 #Максимальное  количество символов в описании
    t=0 # кол-во заглавных букв в названии умений
    u=0 # 
    q=0 # максимальное количество заглавных букв в названии умений
    summ1=0 # общее количество символов в файле
    summ2=0 # кол-во без знаков препинания и пробелов
    for line in f:
        s=line
        if s.find("name")!=-1:
            name=s
        summ1+=len(s)
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                summ2+=1
        if s.find("abilities")!=-1:
            u=1
        if u==1 and s.find("],")==-1:
            s=s.replace(" ", "")
            for i in range(len(s)):
                if ord(s[i])>=65 and ord(s[i])<=90:
                    t+=1
            if t==4:
                g=s
            if t>q:
                q=t
            t=0
        elif s.find("],")!=-1:
            t=0
            u=0
        if s.find("description")!=-1:
            a=len(s)
            if a>p:
                p=a
                name2=name
print(summ1,summ2,name2,g)
