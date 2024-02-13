a=input("string을 입력하세요")
stack=[]
push_nominee=['(','[','{','<']
pull_nominee=[')',']','}','>']
for i in a:
    if i in push_nominee:
        stack.append(i)
    elif i in pull_nominee:
        out=stack.pop()
        if out=='(' and i==')':
            pass
        elif out=='[' and i==']':
            pass
        elif out=='{' and i=='}':
            pass
        elif out=='<' and i=='>':
            pass
        else:
            break

    else:
        continue

if not stack:
    print("알맞습니다")
else:
    print("짝이 맞지 않습니다")
