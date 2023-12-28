import pygame
import random
def kgf(n):
    if n<4:
        i=n
        j=1
    else:
        k=n
        l=1
        while k>4:
            k=k-4
            l=l+1
        i=k
        j=l
    
    x=(i-1)*100+46
    y=(j-1)*100+46
    llr=[x,y]
    return llr
def hero(x):
    if x==1:
        return i1
    elif x==2:
        return i2
    elif x==3:
        return i3
    elif x==4:
        return i4
    elif x==5:    
        return i5
    elif x==6:    
        return i6
    elif x==7:    
        return i7
    elif x==8:    
        return i8
    elif x==9:   
        return i9
    elif x==10:    
        return i10
    elif x==11:    
        return i_11
    elif x==12:    
        return i12
    elif x==13:    
        return i13
    elif x==14:    
        return i14
    elif x==15:    
        return i15
    elif x==16:    
        return i16   
def zero(d):
    for q in range(1,17):
        if il[q]==d:
            return hero(q)
        else:
            q=q+1            
def noonclick(pos):
    if pos[0]<400&pos[1]>400:
        return 0
    else:
        if pos[1]<90:
            if pos[0]<90:
                return 1
            elif pos[0]<190:
                return 2
            elif pos[0]<290:
                return 3
            elif pos[0]<390:
                return 4
            else: 
                return -1
        elif pos[1]<190:
            if pos[0]<90:
                return 5
            elif pos[0]<190:
                return 6
            elif pos[0]<290:
                return 7
            elif pos[0]<390:
                return 8
            
            else: 
                return -1
        elif pos[1]<290:
            if pos[0]<90:
                return 9
            elif pos[0]<190:
                return 10
            elif pos[0]<290:
                return 11
            elif pos[0]<390:
                return 12
            else: 
                return -1
        elif pos[1]<390:
            if pos[0]<90:
                return 13
            elif pos[0]<190:
                return 14
            elif pos[0]<290:
                return 15
            elif pos[0]<390:
                return 16
            else: 
                return -1
def img(c):
    return "C:/Users/datta/OneDrive/Desktop/Images game/i"+str(c)+".png"
def knowimg(l):
    return l[45]
def knowimgi(i):
    for a in range(1,17):
        if hero(a)==i:
            return a
        else:
            a=a+1
def main(x,y):
    if x%2==0:
        if y==x-1:
            return 1
        else:
            return 0
    else:
        if y==x+1:
            return 1
        else:
            return 0
def lzero(d):
    for q in range(1,17):
        if il[q]==d:
            return lhero(q)
        else:
            q=q+1  
def lhero(x):
    if x==1:
        return i11
    elif x==2:
        return i22
    elif x==3:
        return i33
    elif x==4:
        return i44
    elif x==5:    
        return i55
    elif x==6:    
        return i66
    elif x==7:    
        return i77
    elif x==8:    
        return i88
    elif x==9:   
        return i99
    elif x==10:    
        return i1010
    elif x==11:    
        return i1111
    elif x==12:    
        return i1212
    elif x==13:    
        return i1313
    elif x==14:    
        return i1414
    elif x==15:    
        return i1515
    elif x==16:    
        return i1616



pygame.init()
moves=0

ss1=pygame.mixer.Sound("E:/Python games/Tutorial/sss1.wav")
ss2=pygame.mixer.Sound("E:/Python games/Tutorial/ss2.wav")
ds=pygame.display.set_mode((800,700))
pygame.display.set_caption("Fire")
white=(255,255,255)
run=True
il={}
#
ll=[i for i in range(1,17)]

luk1=random.sample(ll,2)

il[1]=luk1[0]
il[2]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz1=kgf(luk1[0])
zz2=kgf(luk1[1])
i1=pygame.image.load(img(1))
i11=i1.get_rect()
i11.center=zz1
i2=pygame.image.load(img(1))
i22=i2.get_rect()
i22.center=zz2


luk1=random.sample(ll,2)
il[3]=luk1[0]
il[4]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz3=kgf(luk1[0])
zz4=kgf(luk1[1])
i3=pygame.image.load(img(2))
i33=i3.get_rect()
i33.center=zz3
i4=pygame.image.load(img(2))
i44=i4.get_rect()
i44.center=zz4

luk1=random.sample(ll,2)
il[5]=luk1[0]
il[6]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz5=kgf(luk1[0])
zz6=kgf(luk1[1])
i5=pygame.image.load(img(3))
i55=i5.get_rect()
i55.center=zz5
i6=pygame.image.load(img(3))
i66=i6.get_rect()
i66.center=zz6

luk1=random.sample(ll,2)
il[7]=luk1[0]
il[8]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz7=kgf(luk1[0])
zz8=kgf(luk1[1])
i7=pygame.image.load(img(4))
i77=i7.get_rect()
i77.center=zz7
i8=pygame.image.load(img(4))
i88=i8.get_rect()
i88.center=zz8


luk1=random.sample(ll,2)
il[9]=luk1[0]
il[10]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz9=kgf(luk1[0])
zz10=kgf(luk1[1])
i9=pygame.image.load(img(5))
i99=i9.get_rect()
i99.center=zz9
i10=pygame.image.load(img(5))
i1010=i10.get_rect()
i1010.center=zz10


luk1=random.sample(ll,2)
il[11]=luk1[0]
il[12]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz11=kgf(luk1[0])
zz12=kgf(luk1[1])
i_11=pygame.image.load(img(6))
i1111=i_11.get_rect()
i1111.center=zz11
i12=pygame.image.load(img(6))
i1212=i12.get_rect()
i1212.center=zz12

luk1=random.sample(ll,2)
il[13]=luk1[0]
il[14]=luk1[1]
ll.remove(luk1[0])
ll.remove(luk1[1])
zz13=kgf(luk1[0])
zz14=kgf(luk1[1])
i13=pygame.image.load(img(7))
i1313=i13.get_rect()
i1313.center=zz13
i14=pygame.image.load(img(7))
i1414=i14.get_rect()
i1414.center=zz14



luk1=ll
il[15]=luk1[0]
il[16]=luk1[1]


zz15=kgf(luk1[0])
zz16=kgf(luk1[1])
i15=pygame.image.load(img(8))
i1515=i15.get_rect()
i1515.center=zz15
i16=pygame.image.load(img(8))
i1616=i16.get_rect()
i1616.center=zz16





score=0



#

for j in range(4):
        k1=j*100
        for i in range(4):
            k2=i*100
            pygame.draw.rect(ds,white,(k2,k1,100,100),4)
            i=i+1
        j=j+1
pygame.draw.line(ds,white,(0,0),(400,0),4)
pygame.draw.line(ds,white,(0,0),(0,400),4)
pygame.draw.line(ds,white,(400,0),(400,400),4)
pygame.draw.line(ds,white,(0,400),(400,400),4)
st=pygame.font.SysFont('calibri',36)
s1=st.render("Press Y for submit",True,white)
s11=s1.get_rect()
s11.center=(200,450)
pygame.draw.rect(ds,white,(0,400,400,100),4)
sim="Moves : "+str(moves)
s2=st.render(sim,True,white)
s22=s2.get_rect()
s22.center=(200,550)
pygame.draw.rect(ds,white,(0,500,400,100),4)
pygame.draw.line(ds,white,(400,400),(400,600),4)
pygame.draw.line(ds,white,(0,600),(400,600),4)
pygame.draw.line(ds,white,(400,98),(800,98),8)
pygame.draw.line(ds,white,(400,598),(800,598),8)
pygame.draw.line(ds,white,(796,0),(796,600),8)


y=[]
presencelist=[]
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
                c1=event.pos[0]
                c2=event.pos[1]
                c=[c1,c2]
                
                d=noonclick(c)
                if d==-1:
                    print("Please select properly")
                elif d==None:
                    print("Please select properly")   
                else:
                        ss1.play()
                        y.append(d)
                        sd=set(y)
                        y=list(sd)


                        if len(y)==2:

                            pygame.display.update()
                            alpha=120
                            e=zero(y[0])
                            f=zero(y[1])
                            e11=lzero(y[0])
                            f11=lzero(y[1])
                            e1=knowimgi(e)
                            f1=knowimgi(f)
                            e.set_alpha(120)
                            f.set_alpha(120)


                            h1=False
                            h2=False
                            if not h1 and not h2:
                                ds.blit(e,e11)
                                ds.blit(f,f11)
                                h1=True
                                h2=True
                            



                            pygame.display.update()

        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_y:

                if main(e1,f1)==1:

                    e=zero(y[0])
                    f=zero(y[1])
                    presencelist.append([e,e11])
                    presencelist.append([f,f11])
                    score=score+2

                    



                    y=[]
                else:
                    ss2.play()
                    h1=not h1
                    h2=not h2
                    ds.fill((0,0,0))
                    moves=moves+1
                    
                    for j in range(4):
                            k1=j*100
                            for i in range(4):
                                k2=i*100
                                pygame.draw.rect(ds,white,(k2,k1,100,100),4)
                                i=i+1
                            j=j+1
                    pygame.draw.line(ds,white,(0,0),(400,0),4)
                    pygame.draw.line(ds,white,(0,0),(0,400),4)
                    pygame.draw.line(ds,white,(400,0),(400,400),4)
                    pygame.draw.line(ds,white,(0,400),(400,400),4)
                    pygame.draw.rect(ds,white,(0,500,400,100),4)
                    pygame.draw.rect(ds,white,(0,400,400,100),4)
                    pygame.draw.line(ds,white,(400,400),(400,600),4)
                    pygame.draw.line(ds,white,(0,600),(400,600),4)
                    pygame.draw.line(ds,white,(400,98),(800,98),8)
                    pygame.draw.line(ds,white,(400,598),(800,598),8)   
                    pygame.draw.line(ds,white,(796,0),(796,600),8)
    
                    for i in range(0,len(presencelist)):
                        ds.blit(presencelist[i][0],presencelist[i][1])
                    
                    y=[]
                    
                    sim="Moves : "+str(moves)
                    s2=st.render(sim,True,white)
                    s22=s2.get_rect()
                    s22.center=(200,550)
                    ds.blit(s2,s22)    
                    pygame.display.update()                
                    

            if score==16:
                s3=st.render("Congratulation You have won the game",True,white)
                s33=s3.get_rect()
                s33.center=(400,650)
                ds.blit(s3,s33)
                            


                            
                    

                
            
            
    
    s3=st.render("Rules",True,white)
    s33=s3.get_rect()
    s33.center=(600,50)
    s4=st.render("1. Dont click same box",True,white)
    s44=s4.get_rect()
    s44.center=(600,125)
    s5=st.render("   twice continously.",True,white)
    s55=s5.get_rect()
    s55.center=(590,175)
    s6=st.render("2. For matching pairs",True,white)
    s7=st.render("   moves doesnt count.",True,white)
    s66=s6.get_rect()
    s66.center=(590,225)
    s77=s7.get_rect()
    s77.center=(610,275)
    
    s8=st.render("3. Press Y after",True,white)
    s9=st.render("   selecting 2 boxes.",True,white)
    s88=s8.get_rect()
    s88.center=(545,325)
    s99=s9.get_rect()
    s99.center=(585,375)
    t1=st.render("4. Dont click outside",True,white)
    t11=t1.get_rect()
    t11.center=(585,425)
    t2=st.render("   boxes.",True,white)
    t22=t2.get_rect()
    t22.center=(510,475)
    t3=st.render("5. Dont press Y before",True,white)
    t4=st.render("   selecting 2 boxes.",True,white)
    t33=t3.get_rect()
    t33.center=(600,525)
    t44=t4.get_rect()
    t44.center=(590,575)
    
    ds.blit(s1,s11)
    ds.blit(s2,s22)
    ds.blit(s3,s33)
    ds.blit(s4,s44)
    ds.blit(s5,s55)
    ds.blit(s6,s66)
    ds.blit(s7,s77)
    ds.blit(s8,s88)
    ds.blit(s9,s99)
    ds.blit(t1,t11)
    ds.blit(t2,t22)
    ds.blit(t3,t33)
    ds.blit(t4,t44)


    pygame.display.update()

pygame.quit()