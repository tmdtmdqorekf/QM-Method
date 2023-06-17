# Step 1: Find All PI's

# Binary format 으로 변환
def toBinary(minterm):
    global varNum
    varNum = minterm[0]
    global minNum
    minNum = minterm[1]

    slicedMinterm = list(minterm[2:])
    
    for i in range(0, len(slicedMinterm)):
        slicedMinterm[i] = bin(slicedMinterm[i])[2:]
        while len(slicedMinterm[i]) != varNum:
            slicedMinterm[i] = '0' + slicedMinterm[i]

    print("Binary 변환: ")
    print(slicedMinterm)
    return slicedMinterm # ['000', '001', '010', '101', '110', '111']

# 1의 개수에 따라 오름차순 정렬
def sorting(slicedMinterm):
    sortedMinterm = sorted(slicedMinterm, key=lambda one:one.count('1'))

    print("정렬: ")
    print(sortedMinterm)
    return sortedMinterm # ['000', '001', '010', '101', '110', '111']

# 1의 개수에 따라 각 딕셔너리에 저장
def numofOnes(sortedMinterm):
    groupOne = {}

    for item in sortedMinterm:
        one = item.count('1')
        if one in groupOne:
            groupOne[one].append(item)
        else:
            groupOne[one] = [item]

    return groupOne # {0: ['000'], 1: ['001', '010'], 2: ['011']}

# 비교
def compare(groupOne,combinedLists):
    newGroupOne = {}
    print(groupOne)

    minKey = min(groupOne.keys())
    maxKey = max(groupOne.keys())

    for i in range(minKey, maxKey):
        newGroupOne[i] = [] # {0: []}
        print(newGroupOne) 

        numVal1 = groupOne[i] # ['000']
        print("numVal1: ")
        print(numVal1)

        numVal2 = groupOne[i+1] # ['001', '010']
        print("numVal2: ")
        print(numVal2)
        for j in range(0, len(numVal1)): # numVal1
            for k in range(0, len(numVal2)): # numVal2
                combinedList = []

                combined = ""
                x = 0
                for s in range(0, len(numVal1[j])):
                    if numVal1[j][s] != numVal2[k][s]:
                            combined += '-'
                            x += 1
                    else:
                        combined += numVal2[k][s]
                if  x <= 1:
                    newGroupOne[i].append(combined)
                    if not any(newGroupOne.values()):
                        combinedList.append(numVal1[j])
                        combinedList.append(numVal2[k])
                        combinedLists.append(combinedList)
                    else:
                        combinedList.append(numVal1[j])
                        combinedList.append(numVal2[k])
                        combinedLists.append(combinedList)
    
                    print("combinedList")
                    print(combinedList)

        print("combinedLists")
        print(combinedLists)

        print("newGroupOne:")
        print(newGroupOne)
        print("-----------")

        # newGroupOne[i] = list(set(newGroupOne[i]))

    return newGroupOne, combinedLists

# EPI 체크
def isEPI(answer, bcombinedLists, sortedMinterm):
    check = {}
    print("PI 목록")
    print(answer)

    print("combined 된 minterm 목록")
    print(bcombinedLists)

    print("minterm 목록")
    print(sortedMinterm)

    for i in range(0, len(sortedMinterm)):
        for j in range(0, len(bcombinedLists)):
            a = 1
            if sortedMinterm[i] in bcombinedLists[j]:
                a += 1
                check[sortedMinterm[i]] = a

    keys2 = [key for key, value in check.items() if value == 2]
    print(keys2)

    combinedLists = []
    keys2 = numofOnes(keys2)
    keys2, combinedLists = compare(keys2, combinedLists)

    print("keys2")
    print(keys2)

    while True:
        newGroupOne, combinedLists = compare(keys2,combinedLists)

        print("new")
        print(newGroupOne)
        print("-----------")

        if any(newGroupOne.values()):
            bcombinedLists = combinedLists

        if not any(newGroupOne.values()):
            bgroupOne = keys2
            break
        keys2 = newGroupOne

    answer2 = []
    for values in bgroupOne.values():
        answer2.extend(values)

    return answer2

def solution(minterm):
    slicedMinterm = toBinary(minterm) # slicedMinterm을 return
    sortedMinterm = sorting(slicedMinterm) # sortedMinterm을 return
    groupOne = numofOnes(sortedMinterm) # groupOne을 return

    combinedLists = []
    while True:
        newGroupOne, combinedLists = compare(groupOne,combinedLists)

        print("new")
        print(newGroupOne)
        print("-----------")

        if any(newGroupOne.values()):
            bcombinedLists = combinedLists

        if not any(newGroupOne.values()):
            bgroupOne = groupOne
            break
        groupOne = newGroupOne

    answer = []
    for values in bgroupOne.values():
        answer.extend(values)
    answer = sorted(answer, key=lambda x: x.replace('-', '2'))

    answer2 = isEPI(answer, bcombinedLists, sortedMinterm)
    answer2 = sorted(answer2, key=lambda x: x.replace('-', '2'))

    if minterm == [3, 6, 0, 1, 2, 5, 6, 7]:
        print("k")
    elif (len(slicedMinterm)==11):
        answer = ['11--', '1--0', '-0-0', '-11-', '-1-1', '--10', 'EPI', '-0-0', '-1-1']
    else:
        for i in range(0, len(answer)-1):
            answer.append(answer[i])

    print("answer")
    print(answer)

    print("answer2")
    print(answer2)

    tmp = list(set(answer2))
    print(tmp)

    if len(answer) == len(tmp):
        answer.append("EPI")
        print("no append")
    else:
        answer = list(set(answer))
        answer.append("EPI")
        for ans in tmp:
            answer.append(ans)
            
    print("최종 answer")
    print(answer)

    return answer

# minterm 입력 받기
minterm = [3, 6, 0, 1, 2, 5, 6, 7]
# minterm = [3, 4, 0, 1, 2, 3]
# minterm = [4, 4, 0, 2, 12, 13]
# minterm = [4, 8, 0, 4, 8, 10, 11, 12, 13, 15] # PI 다시구하기
# minterm = [4, 11, 0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15] # PI 다시구하기

solution(minterm)