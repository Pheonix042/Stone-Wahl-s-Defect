hh=int(input('Horizontal hexagone number:'))
vv=int(input('Vertical hezagone number:'))
h1=hh+2
v1=vv+2
h=list(range(2,h1))
v=list(range(2,v1))
line=2*h1
atomno=[str(line)]
for li in v:
    q=li-2
    li = 2*max(h)+int(atomno[q])
    z=li
    atomno.append(str(z))
#print('Atom number at the end of every line',atomno)
SrNo=[]
Xco=[]
Yco=[]
# Master loop will be initiating here
m=list(range(1,v1))
for num in m:
    if num==1:
        templist=list(range(1,1+int(atomno[0])))
        for num1 in templist:
            if num1==1:
                X=1.212435
                Y=2.1
            else:
                X=1.212435+x1
                if num1%2==0:
                    Y=0.7
                else:
                    Y=0
            if num1==1:
                x1=0
            else:
                x1=X
            SrNo.append(num1)
            Xco.append(round(X,6))
            Yco.append(round(Y,6))
    else:
        templist=list(range(int(atomno[num-2])+1,1+int(atomno[num-1])))
        #print(templist)
        if num%2==0:
            for num3 in templist:
                tt=templist[0]
                if num3==tt:
                    X=Xco[num3-2]
                else:
                    X=Xco[num3-2]-1.212435
                if num3%2==0:
                    Y=(num-1)*2.8-(num-2)*0.7
                else:
                    Y=(num-1)*2.1
                SrNo.append(num3)
                Xco.append(round(X,6))
                Yco.append(round(Y,6))
        else:
            for num5 in templist:
                tt=templist[0]
                if num5==tt:
                    X=Xco[num5-2]
                else:
                    X=Xco[num5-2]+1.212435
                if num5%2==0:
                    Y=(num-1)*2.8-(num-2)*0.7
                else:
                    Y=(num-1)*2.1
                SrNo.append(num5)
                Xco.append(round(X,6))
                Yco.append(round(Y,6))   
# Loop for finding of neighbouring atoms
genlist=list(range(1,int(atomno[v1-2])+1))
#print(genlist)
R=[]
M=[]
L=[]
neigh=list(range(1,v1))
for lineno in neigh:
     if lineno==1:
        atttt=list(range(1,1+int(atomno[0])))
        for atom in atttt:
            if atom==1:
                r=int(atomno[lineno])
                m=2
                l=""
            else:
                if atom%2==0:
                    if atom==2:
                        r=3
                        m=1
                        l=""
                    else:
                        if atom!=int(atomno[0]):
                            r=atom+1
                            l=atom-1
                            tempm=int(atomno[0])
                            m=(tempm-atom)*2+atom+1
                        else:
                            l=atom-1
                            tempm=int(atomno[0])
                            m=(tempm-atom)*2+atom+1
                            r=""
                else:
                    r=atom+1
                    l=atom-1
                    m=""
            R.append(r)
            M.append(m)
            L.append(l)  
     else:
         att=list(range(1+int(atomno[lineno-2]),1+int(atomno[lineno-1])))
         if lineno%2==0:
             for atom in att:
                 if atom%2==0:
                     tempm=int(atomno[lineno-1])
                     if atom!=int(atomno[v1-2]):
                         m=(tempm-atom)*2+atom+1
                     else:
                         m=""
                 else:
                     tempm=int(atomno[lineno-2])+1
                     m=atom-(atom-tempm)*2-1
                 if atom==int(atomno[lineno-2])+1:
                     r=""
                     l=atom+1
                 elif atom==int(atomno[lineno-1]):
                     r=atom-1
                     if atom==int(atomno[1]):
                         l=1
                     else:
                         l=""
                 else:
                     r=atom-1
                     l=atom+1
                 R.append(r)
                 L.append(l)
                 M.append(m)
         else:
             for atom in att:
                 if atom%2==0:
                     tempm=int(atomno[lineno-1])
                     if lineno!=(v1-1):
                         m=atom+1+(tempm-atom)*2
                     else:
                         m=""
                 else:
                     tempm=int(atomno[lineno-2])+1
                     m=atom-(atom-tempm)*2-1
                 if atom==int(atomno[lineno-2])+1:
                     r=atom+1
                     l=""
                 elif atom==int(atomno[lineno-1]):
                     r=""
                     l=atom-1
                 else:
                     r=atom+1
                     l=atom-1
                 R.append(r)
                 L.append(l)
                 M.append(m)
# Coding for SW defect stars here
print('Position of bond which is to be rotated')
col=int(input('Hexagone Row number:'))
row=int(input('Hexagone Column number:'))
if row%2==1:
    a1=col*2+int(atomno[row-2])+1
    a2=int(atomno[row])-col*2
    l1=a1     
    r1=a1+2   
    rot1=a1+1 
    l2=a2   
    r2=a2-2 
    rot2=a2-1 
    L[r1-1]=rot2
    R[rot1-1]=l2
    R[l2-1]=rot1
    L[rot2-1]=r1
else:
    coll=hh-col
    a1=int(atomno[row-2])+1+coll*2
    a2=int(atomno[row])-coll*2
    r1=a1
    l1=a1+2
    rot1=a1+1
    r2=a2
    rot2=a2-1
    l2=a2-2
    L[r1-1]=rot2
    R[rot1-1]=l2
    R[l2-1]=rot1
    L[rot2-1]=r1
# codes for modifiying co-ordinates of affected atoms
# 1st line modification
Xco[rot1-1]=Xco[rot1-1]-0.7
Xco[rot2-1]=Xco[rot2-1]+0.7
Yco[rot1-1]=Yco[rot1-1]+0.7
Yco[rot2-1]=Yco[rot2-1]-0.7
Atom_no=int(atomno[vv])
genlist=list(range(1,int(atomno[v1-2])+1))
for mn in genlist:
    if M[mn-1]=="":
        M[mn-1]=L[mn-1]
        L[mn-1]=""
    else:
        pass
    if R[mn-1]=="":
        R[mn-1]=M[mn-1]
        M[mn-1]=L[mn-1]
        L[mn-1]=""
    else:
        pass
myfile=open('./SW_defect.xyz','w')
myfile.write('{}\t \n'.format(Atom_no))
for nn in genlist:
    #print(SrNo[nn-1], 'C', Xco[nn-1], Yco[nn-1], 0, 2, R[nn-1], M[nn-1], L[nn-1])
    myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t \n'.format(SrNo[nn-1], 'C', Xco[nn-1], Yco[nn-1], 0, 2, R[nn-1], M[nn-1], L[nn-1]))
myfile.close()    
quitt=input('Press enter to quit')
