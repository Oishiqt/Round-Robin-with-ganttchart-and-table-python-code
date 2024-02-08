#RR
def readyQueue (num):
    for i in range (0,process,1):
        for j in range(0, process, 1):
            if copyAr[i] <= num:
                if copyAr[i] == copyAr1[j]:
                    if Pr[j] not in queue:
                        queue.append(Pr[j])
def cbtProcess (curr):
    while copyBt1[i] != 0:
        if copyBt1[i] >= quantum:
            copyBt1[i] -= quantum
            curr += quantum
        else:
            curr += copyBt1[i]
            copyBt1[i] = 0
        cpro = queue[a]
        readyQueue(curr)
        if copyBt1[i] != 0:
            queue.pop(a)
            queue.append(cpro)
        break
    return curr

curr = 0
totalTat = 0
totalWt = 0
Pr = []
Ar = []
Bt = []
Ct = []
Tat = []
Wt = []
queue = []
process = int(input("Enter No. of Process: "))
quantum = int(input("Enter QUANTUM: "))
for i in range(0,process,1):
    Pr.append(f"P{i+1}")
    Ct.append(i)
    Tat.append(i)
    Wt.append(i)
    var = int(input(f"Enter P{i+1} Arrival Time: "))
    Ar.append(var)
    var = int(input(f"Enter P{i+1} Burst Time: "))
    Bt.append(var)
copyAr = Ar.copy()
copyAr1 = Ar.copy()
copyAr.sort()
copyBt1 = Bt.copy()
#CT computation
a = 0
if copyAr[0] != 0:
    curr = copyAr[0]
    Ct.append(copyAr[0])
    Pr.append(f"//")
    readyQueue(curr)
else:
    for i in range(0,process,1):
        if copyAr1[i] == 0:
            readyQueue(curr)
            curr = cbtProcess(curr)
            if copyBt1[i] == 0:
                Ct[i] = curr
                a += 1
            else:
                Ct.append(curr)
                Pr.append(Pr[i])

while a < process:
    if curr < copyAr[a]:
        curr = copyAr[a]
        Ct.append(copyAr[a])
        Pr.append(f"//")
        readyQueue(curr)
        a -= 1
    else:
        for i in range(0,process,1):
            if queue[a] == Pr[i]:
                curr = cbtProcess(curr)
                readyQueue(curr)
                if copyBt1[i] == 0:
                    Ct[i] = curr
                else:
                    Ct.append(curr)
                    Pr.append(Pr[i])
                    a -= 1
                break
    a += 1

#TAT & WT Computation
for i in range(0,process,1):
    Tat[i] = Ct[i] - Ar[i]
    Wt[i] = Tat[i] - Bt[i]
print()
print("P\t|\tAT\t|\tBT\t|\tCT\t|\tTAT\t|\tWT")
for i in range(0,process,1): print(f"{Pr[i]}\t|\t{Ar[i]}\t|\t{Bt[i]}\t|\t{Ct[i]}\t|\t{Tat[i]}\t|\t{Wt[i]}")
print()
copyCt = Ct.copy()
copyCt.sort()
ganttChart = []
for i in range(0,len(Ct),1):
    for j in range(0,len(Ct),1):
        if copyCt[i] == Ct[j]:
            ganttChart.append(Pr[j])
print("GANTT CHART:")
print(f"QUANTUM: {quantum}ms")
print()
print("|",end=" ")
for i in range(len(Ct)): print(f"\t{ganttChart[i]}\t|",end=" ")
print()
print(f"0\t",end=" ")
for i in range(len(Ct)): print(f"\t{copyCt[i]}\t",end=" ")
for i in range(process):
    totalTat+=Tat[i]
    totalWt+=Wt[i]
AveTat = round(totalTat/process,2)
AveWt = round(totalWt/process,2)
print()
print()
print(f"Total TAT: {totalTat} ms")
print(f"Total WT: {totalWt} ms")
print(f"Average TAT: {AveTat} ms")
print(f"Average WT: {AveWt} ms")