import math as mt
import random as rn
from datetime import date
import time

def d2b(i):
  j=n=0
  while(i>0):
    j+=i%2*10**n
    n+=1
    i//=2
  return j

def d2bS(c,nd=8):
  i=int(c)
  j=str(i%2)
  i//=2
  while(i>0):
    j=str(i%2)+j
    i//=2
  if(len(j)>nd):
    return 0
  return "0"*(nd-len(j))+j

def b2dS(c):
  s=0
  nd=len(c)-1
  for i in c:
    s+=int(i)*2**nd
    nd-=1
  return str(s)

def L2sIP(z):
  return "".join(z[:8])+'.'+"".join(z[8:16])+'.'+"".join(z[16:24])+'.'+"".join(z[24:32])

def subnetX():
  score,best=0,0
  IP = [ str(rn.randrange(0,128)+rn.randrange(0,129)) for i in range(4)]
  print(".".join(IP))
  #1
  print("\n1. να βρείτε την τάξη του δικτύου:\n")
  choice=input("> ")
  x=int(IP[0])
  if(x>239):
    y='E'
  elif(x>223):
    y='D'
  elif(x>191):
    y='C'
  elif(x>127):
    y='B'
  else:
    y='A'
  if(choice==y):
    print("Σωστό!\n")
    score+=5
  else:
    print("Λάθος!\nclass "+y)
  best+=5
  if(x>223):
    print("\n_______________________\nΗμερομηνία: "+str(date.today())+"\n\nΤελικός Βαθμός: ",score,"/",best)
    return
  #2
  print("\n2. να βρείτε τη δυαδική μορφή της IP:\n")
  choice=input("> ")
  IP2=".".join([d2bS(c) for c in IP])
  if(choice==IP2):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+IP2)
  best+=10
  #3a
  print("\n3 i. να βρείτε την προκαθόρισμένη μάσκα στη δυαδική μορφή:\n")
  choice=input("> ")
  if(y=='A'):
    mask="1"*8+"."+"0"*8+"."+"0"*8+"."+"0"*8
  elif(y=='B'):
    mask="1"*8+"."+"1"*8+"."+"0"*8+"."+"0"*8
  elif(y=='C'):
    mask="1"*8+"."+"1"*8+"."+"1"*8+"."+"0"*8
  if(choice==mask):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+mask)
  best+=10
  #3b
  print("\n  ii. να βρείτε την προκαθόρισμένη μάσκα στη δεκαδική μορφή:\n")
  choice=input("> ")
  if(y=='A'):
    mask10="255"+(".0")*3
  elif(y=='B'):
    mask10="255.255"+(".0")*2
  elif(y=='C'):
    mask10="255."*3+"0"
  if(choice==mask10):
    print("Σωστό!\n")
    score+=5
  else:
    print("Λάθος!\n"+mask10)
  best+=5
  #3c
  print("\n  iii. να βρείτε τη διεύθυνση δικτύου στη δυαδική μορφή:\n")
  choice=input("> ")
  x=[int(i) for i in IP2.replace('.','')]
  y=[int(i) for i in mask.replace('.','')]
  z=[str(i[0]*i[1]) for i in zip(x,y)]
  NwAd=L2sIP(z)
  if(choice==NwAd):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+NwAd)
  best+=10
  #3d
  print("\n  iv. να βρείτε τη διεύθυνση δικτύου στη δεκαδική μορφή:\n")
  choice=input("> ")
  NwAd10=".".join([b2dS(i) for i in NwAd.split('.')])
  if(choice==NwAd10):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+NwAd10)
  best+=10
  #4
  hbit=mask.count('0')
  nbit=mask.count('1')
  senario=rn.randrange(2)
  if(senario==0):  #αριθμός υποδικτύων
    nsb=rn.randrange(2,2**(hbit-1))
    if(nsb>1024):
      nsb=rn.randrange(2,1024)
    print("\n4 i. Ζητείται να χωριστεί το δίκτυο\nσε τουλάχιστον "+str(nsb)+" υποδίκτυα.")
    sbit=mt.ceil(mt.log(nsb,2))
    hbit-=sbit
  else: #αριθμός υπολογιστών
    npc=rn.randrange(2**(hbit-1)-2)
    if(npc>1024):
      npc=rn.randrange(2,1024)
    print("\n4 i. Ζητείται να χωριστεί το δίκτυο σε υποδίκτυα\nμε τουλάχιστον "+str(npc)+" υπολογιστές")
    hbit=mt.ceil(mt.log(npc+2,2))
    sbit=32-nbit-hbit
  print("Ποια θα είναι η νέα μάσκα δικτύου?\n")
  choice=input("> ")
  maskS='1'*(nbit+sbit)+'0'*(32-nbit-sbit)
  maskS=maskS[:8]+'.'+maskS[8:16]+'.'+maskS[16:24]+'.'+maskS[24:]
  if(choice==maskS):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+maskS)
  best+=10
  print("\n  ii. Να βρείτε την απώλεια  διευθύνσεων")
  choice=input("> ")
  loss=2*(2**sbit)-2
  if(choice==str(loss)):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+str(loss))
  best+=10
  #5
  print("\n5 i. Πόσους υπολογιστές έχει κάθε υποδίκτυο?")
  choice=input("> ")
  if(choice==str(2**hbit-2)):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+str(2**hbit-2))
  best+=10
  csbn=rn.randrange(1,2**sbit+1)
  if(csbn>1024):
    csbn=rn.randrange(1,1024)
  print("\n  ii. Να βρεθεί το εύρος διευθύνσεων του "+str(csbn)+"ου υποδικτύου")
  tmp=str(d2bS(csbn-1,sbit))
  x=[int(i) for i in IP2.replace('.','')[:nbit]+tmp+IP2.replace('.','')[nbit+sbit:]]
  y=[int(i) for i in maskS.replace('.','')]
  z=[str(i[0]*i[1]) for i in zip(x,y)]
  w=z[:nbit+sbit]+['1']*hbit
  NwAd=L2sIP(z)
  ekAd=L2sIP(w)
  choice=input("> ")
  if(choice==NwAd+" - "+ekAd):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+NwAd+" - "+ekAd)
  best+=10
  print("\n  iii. Να βρεθεί το υποδίκτυο στο οποίο ανήκει η αρχική IP")
  x=[int(i) for i in IP2.replace('.','')[nbit:nbit+sbit]]
  sbnN=1
  for i in range(sbit):
    sbnN+=x[-1-i]*2**i
  choice=input("> ")
  sbnN=str(sbnN)
  if(choice==sbnN):
    print("Σωστό!\n")
    score+=10
  else:
    print("Λάθος!\n"+sbnN)
  best+=10
  print("\n______________________________________\nΗμερομηνία: "+time.strftime("%a, %d %b %Y, %H:%M:%S",time.gmtime(time.time())))
  print("\n\nΤελικός Βαθμός: ",score,"/",best)
