names=[]
sub1=[]
sub2=[]
sub3=[]
sub4=[]
sub5=[]
subjects=[]
toppersSub1=[]
toppersSub2=[]
toppersSub3=[]
toppersSub4=[]
toppersSub5=[]
totals=[]
topper=[]
f1=open("marks.txt","r")

for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    sub1.append(list2[1])
    subjects.append(list2[0])
    list3=list1[4].split(":")
    sub2.append(int(list3[1]))
    subjects.append(list3[0])
    list4=list1[5].split(":")
    sub3.append(list4[1])
    subjects.append(list4[0])
    list5=list1[6].split(":")
    sub4.append(list5[1])
    subjects.append(list5[0])
    list6=list1[7].split(":")
    sub5.append(int(list6[1]))
    subjects.append(list6[0])
    total=int(sub1[i])+int(sub2[i])+int(sub3[i])+int(sub4[i])+int(sub5[i])
    totals.append(total)
    
maxSub1=max(sub1)
maxSub2=max(sub2)
maxSub3=max(sub3)
maxSub4=max(sub4)
maxSub5=max(sub5)
maxTotal = max(totals)

for i in range(0,26,1):
    if sub1[i]==maxSub1:
        toppersSub1.append(names[i])
    if sub2[i]==maxSub2:
        toppersSub2.append(names[i])
    if sub3[i]==maxSub3:
        toppersSub3.append(names[i])
    if sub4[i]==maxSub4:
        toppersSub4.append(names[i])
    if sub5[i]==maxSub5:
        toppersSub5.append(names[i])
    if totals[i] == maxTotal:
        topper.append(names[i])

print("Toppers in",subjects[0],"are:",toppersSub1,"with marks",maxSub1)
print("Toppers in",subjects[1],"are:",toppersSub2,"with marks",maxSub2)
print("Toppers of",subjects[2],"are:",toppersSub3,"with marks",maxSub3)
print("Topper of",subjects[3],"is:",toppersSub4,"with marks",maxSub4)
print("Toppers of",subjects[4],"are:",toppersSub5,"with marks",maxSub5)
print("Overall topper is:", topper, "with total marks",maxTotal)
f1.close()
