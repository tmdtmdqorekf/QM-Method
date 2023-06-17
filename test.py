# minterm = list(map(int,input().split()))
# minterm = [4, 8, 0, 4, 8, 10, 11, 12, 13, 15]
minterm = [4, 11, 0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15]

print("minterm : ", minterm, "\n")

cnt1, answer, pis, epis, ans, row = [], [], [], [], [], []
    
for i in range(minterm[0]+1): # 1의 개수별 저장공간 생성
    cnt1.append([])
    
for i in range(minterm[1]): # minterm 2진수로 변환
    tmp = str(bin(minterm[i+2])[2:])
    while(minterm[0] > len(tmp)):
        tmp = "0" + tmp
    cnt1[tmp.count('1')].append([tmp, 0])
    pis.append([tmp, 0])
    
print(cnt1)
    
change = 1
while(change): # pi압축
    change =0
    for i in range(len(cnt1)-1):
        ad = []
        while(len(cnt1[i])>0):
            now = cnt1[i].pop()
            for j in range(len(cnt1[i+1])):
                dif, dif_w =0, 0
                for l in range(minterm[0]):
                    if now[0][l] != cnt1[i+1][j][0][l]:
                        dif += 1
                        dif_w = l
                if dif == 1:
                    tmp2 = now[0]
                    tmp2 = tmp2[:dif_w] + "2" + tmp2[dif_w+1:]
                    now[1] += 1
                    cnt1[i+1][j][1] += 1
                    if not(tmp2 in ad):
                        ad.append(tmp2)
                    change = 1
            if now[1] == 0:
                ad.append(now[0])
        for m in ad:
            cnt1[i].append([m, 0])
    if(len(cnt1[len(cnt1)-1])>0):
        if(cnt1[len(cnt1)-1][0][1] != 0):
            cnt1[len(cnt1)-1].pop()

print(cnt1,"cnt1\n")
    
for i in cnt1:
    for j in i:
        if not(j[0] in answer):
            answer.append(j[0])

answer.sort(key = lambda x:x.count("2"))

for i in pis:
    for j in answer:
        same = 0
        for k in range(minterm[0]):
            if(j[k] == "2" or j[k] == i[0][k]):
                same += 1
        if(same == minterm[0]):
            i[1] += 1
            i.append(j)

print(pis, "pis\n")
print("---------------------------------------------------------------------\n")

for i in pis: # epi 추가
        if(i[1]==1 and not(i[2] in epis)):
            epis.append(i[2])

change = 1
while(change):
    change = 0
    pi_tmp = []
    
    for i in pis: # pi 선택
        if(i[1]==1 and not(i[2] in ans)):
            ans.append(i[2])

    for i in range(len(pis)): # pi에서 선택된 pi제거
        tmp = pis.pop()
        tf = 0
        for j in ans:
            if(j in tmp):
                tf += 1
        if(tf == 0):
            pi_tmp.append(tmp)
    
    cul = [] # 컬럼 준비
    pi_tmp.sort(key = lambda x:x[1]) 
    print(pi_tmp,"cul")
    
    for i in range(len(pi_tmp)-1): # 컬럼
        tmp = pi_tmp.pop()
        tf = 0
        for j in pi_tmp:
            count = 0
            for k in range(j[1]):
                if(j[k+2] in tmp):
                    count += 1
            if(count == j[1]):
                change = 1
                tf = 1
        if(tf == 0):
            cul.append(tmp)
    pi_tmp += cul
    print(pi_tmp, "after cul\n")
    
    row = [[i, 0]for i in answer] # 로우 준비
    for i in pi_tmp:
        for j in range(len(i)-2):
            for k in row:
                if(i[j+2] in k):
                    k[1] += 1
                    k.append(i[0])
    row.sort(key = lambda x:x[1])
    print(row, "row")
    
    for i in range(len(row)): # 로우
        if(row[i][1] == 0):
            continue
        for j in range(len(row)-1-i):
            count = 0
            for k in range(row[i][1]):
                if(row[i][k+2] in row[i+j+1]):
                    count += 1
            if(count == row[i][1]):
                for k in pi_tmp:
                    if(row[i][0] in k):
                        k.remove(row[i][0])
                        k[1] -=1
                        change = 1
    print(pi_tmp, "after row\n")
    
    if(change == 0 and len(pi_tmp) != 0): # 페트릭
        tmp = pi_tmp[0][2]
        for i in range(pi_tmp[0][1]):
            if(tmp.count("2") < pi_tmp[0][2+i].count("2")):
                tmp = pi_tmp[0][2+i]
        print(tmp, "petrick\n")
        ans.append(tmp)
        change = 1
        
    pis = pi_tmp[:]
    
    print("---------------------------------------------------------------------\n")

answer.sort()
epis.sort()
ans.sort()
epis = ["EPI"] + epis
answer += epis

for i in range(len(answer)):
    answer[i] = answer[i].replace("2", "-")
for i in range(len(ans)):
    ans[i] = ans[i].replace("2", "-")

print("middle : ", answer)
print("final : ", ans)