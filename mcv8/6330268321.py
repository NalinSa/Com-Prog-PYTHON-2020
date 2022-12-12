def bow(s):
    file_name=open(s)
    a=[]
    l=[]
    count=[]
    BoW=[]
    u=""
    x=["(", ")", "-", "_", "[", "]", '"', "'", ';', ':', '<', '>', '.', ',']
    stopwords=open("stopwords.txt")
    for line in stopwords:
        line=line.split()
        for e in line:
            if e!="\n":
                a.append(e)
        
    for line in file_name:
        for e in line:
            if e in x:
                u+=" "
            else:
                u+=e
        u=u.lower()
    u=u.split()
    for e in u:
        if e not in a:
            l.append(e) #ได้ list ที่มีแต่พิมพ์เล็กและตัด stopword ออกไปแล้ว
    c=0
    for e in l:
        for i in range(len(l)):
            if e in l[i]:
                c+=1
        count.append(c)
        c=0
    for i in range(len(l)):
        BoW.append([l[i],count[i]])
        
    stopwords.close()
    return BoW
    
#-------------------------------
def fhash(w,M):
    a=0
    for i in range(len(w)):
        a+=ord(w[i])*37**i
        b=a%int(M)
    return b



#--------------------------------
s=input("File name = " )
file_name=open(s)
a=["y","Y","n","N"]
usef=input("Use feature hashing ? (y,Y,n,N) ")
while usef not in a:
    print("Try again")
    usef=input("Use feature hashing ? (y,Y,n,N) ") 

if  usef =="N" or usef=="n":
    u=""
    x=["(", ")", "-", "_", "[", "]", '"', "'", ';', ':', '<', '>', '.', ',']
    linecount=0
    alphacount=0
    char=""
    for line in file_name:
        linecount+=1 #นับจำนวนบรรทัด
        for e in line:
            if e in x:
                u+=" " #นับจำนวนคำ(word count)
            else:
                u+=e
            
        
        
        line=line.lower()
        for e in line:
            
            if e!="\n":   #นับอักขระ
                char+=e
        
            if "a"<=e<="z" or "0"<=e<="9": #นับจำนวนตัวอักษรอังกฤษและตัวเลขเท่านั้น
                 alphacount+=1     
        
        line=line.split()
        
            
    u=u.split()
    print("-------------------")
    print("char count =",str(len(char))) #จำนวนอักขระ
    print("alphanumeric count =", str(alphacount)) #จำนวนตัวอักษากับตัวเลข
    print("line count =",str(linecount))#จำนวนบรรัด
    print("word count =",str(len(u)))#จำนวนคำ
    print("BoW =",bow(s))
#-----------------------------------------------------------------------------
elif usef =="Y" or usef=="y":
    M=input("M = ")
    u=""
    x=["(", ")", "-", "_", "[", "]", '"', "'", ';', ':', '<', '>', '.', ',']
    linecount=0
    alphacount=0
    char=""
    for line in file_name:
        linecount+=1 #นับจำนวนบรรทัด
        for e in line:
            if e in x:
                u+=" " #นับจำนวนคำ(word count)
            else:
                u+=e
            
        
        
        line=line.lower()
        for e in line:
            
            if e!="\n":   #นับอักขระ
                char+=e
        
            if "a"<=e<="z" or "0"<=e<="9": #นับจำนวนตัวอักษรอังกฤษและตัวเลขเท่านั้น
                 alphacount+=1     
        
        line=line.split()
        
            
    u=u.split()
    n1=[]
    countfh=0
    n2=[]
    n3=[]
    for e in u:
        n1.append(fhash(e,M))
    for i in range(len(n1)):
        for j in range(len(n1)):
            if i==n1[j]:
                countfh+=1
        n2.append(countfh)
        n3.append([str(i),countfh])
        
        
        
    print("-------------------")
    print("char count =",str(len(char))) #จำนวนอักขระ
    print("alphanumeric count =", str(alphacount)) #จำนวนตัวอักษากับตัวเลข
    print("line count =",str(linecount))#จำนวนบรรัด
    print("word count =",str(len(u)))#จำนวนคำ
    print("BoW =",n3)
    
file_name.close()