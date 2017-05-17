import datetime
def comp(l,b):
    a=[]
    for i in l:
        if(len(i)==b):
            a.append(i)
    return a            
visited=[]    
words=[]
final=[]
f=open("word.txt",'r')
for line in f:
    a=line.split(",")
    words.append(a[0])
a=input("enter a word:")
x=input("enter the end point:")
def change(a):
    final=[]
    waste=[]
    for i in words:
        c=0
        b=i
        if(abs(len(a)-len(b))<2):
            if(a in b or b in a):
                final.append(b)
            else:            
                for j in range(max(len(a),len(b))):
                    if(c<2): 
                        try:
                            if(a[j]!=b[j]):
                               c=c+1
                        except:
                            if(abs(len(a)-len(b))==1 and c==0):
                                if((b in a) or (a in b)):
                                    final.append(i)
                                else:
                                    waste.append(i)
                            elif(abs(len(a)-len(b))==1 and c==1):
                                waste.append(i)
                    
                    else: 
                       break;
                if(c==1 or c==0):
                    if(i not in final and i!=a and i not in waste):
                        final.append(i)
    return final            
print(datetime.datetime.now())
final=change(a)

               
                

print(datetime.datetime.now())    
    

       
