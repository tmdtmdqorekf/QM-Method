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
    return slicedMinterm

# 1의 개수에 따라 오름차순 정렬
def sorting(slicedMinterm):
    sortedMinterm = sorted(slicedMinterm, key=lambda one:one.count('1'))

    print("정렬: ")
    print(sortedMinterm)
    return sortedMinterm

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
def compare(groupOne):
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
        print("newGroupOne:")
        print(newGroupOne)
        print("-----------")

        newGroupOne[i] = list(set(newGroupOne[i]))

    return newGroupOne

def solution(minterm):
    slicedMinterm = toBinary(minterm) # slicedMinterm을 return
    sortedMinterm = sorting(slicedMinterm) # sortedMinterm을 return
    groupOne = numofOnes(sortedMinterm) # groupOne을 return

    while True:
        newGroupOne = compare(groupOne)
        print("new")
        print(newGroupOne)
        if not any(newGroupOne.values()):
            bgroupOne = groupOne
            break
        groupOne = newGroupOne
        
    answer = []
    for values in bgroupOne.values():
        print("values")
        print(values)
        print("------")
        answer.extend(values)
    
    answer = sorted(answer, key=lambda x: x.replace('-', '2'))

    print("answer")
    print(answer)

    return answer # ["0--"]

# minterm 입력 받기
minterm = [6, 2, 62, 63]

solution(minterm)