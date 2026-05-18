names=[]
english=[]
math=[]
physics=[]
chemistry=[]
biology=[]
toppersEng=[]
toppersMath=[]
toppersPhysics=[]
toppersChemistry=[]
toppersBiology=[]
totals = []
topper = []
f1=open("marks.txt","r")

for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    english.append(list2[1])
    list3=list1[4].split(":")
    math.append(int(list3[1]))
    list4=list1[5].split(":")
    physics.append(list4[1])
    list5=list1[6].split(":")
    chemistry.append(list5[1])
    list6=list1[7].split(":")
    biology.append(int(list6[1]))
    
maxEng=max(english)
print(maxEng)
maxMath=max(math)
print(maxMath)
maxPhysics=max(physics)
print(maxPhysics)
maxChemistry=max(chemistry)
print(maxChemistry)
maxBiology=max(biology)
print(maxBiology)

for i in range(0,26,1):
    if english[i]==maxEng:
        toppersEng.append(names[i])
    if math[i]==maxMath:
        toppersMath.append(names[i])
    if physics[i]==maxPhysics:
        toppersPhysics.append(names[i])
    if chemistry[i]==maxChemistry:
        toppersChemistry.append(names[i])
    if biology[i]==maxBiology:
        toppersBiology.append(names[i])


for i in range(0,26,1):
    total=int(english[i])+int(math[i])+int(physics[i])+int(chemistry[i])+int(biology[i])
    totals.append(total)

maxTotal = max(totals)

for i in range(0,26,1):
    if totals[i] == maxTotal:
        topper.append(names[i])

print("Toppers in English are:",toppersEng,"with marks",maxEng)
print("Toppers in Math are:",toppersMath,"with marks",maxMath)
print("Toppers of Physics are:",toppersPhysics,"with marks",maxPhysics)
print("Topper of Chemistry is:",toppersChemistry,"with marks",maxChemistry)
print("Toppers of Biology are:",toppersBiology,"with marks",maxBiology)
print("Overall topper is:", topper, "with total marks", maxTotal)
