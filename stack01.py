a=input("string을 입력하세요")
stack=[]
push_nominee=['(','[','{','<']
pull_nominee=[')',']','}','>']

def check_bracket(a):
    table={'(':')',']':'[','}':'{','>':'<'}
    for ch in a:
        if ch in push_nominee:
            stack.append(ch)
        elif ch in pull_nominee:
           if not stack or table[ch]!=stack.pop():
                return False

        else:
            continue





if check_bracket(a):
    print(True)
else:
    print(False)

