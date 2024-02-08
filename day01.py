coeff=[5,-2,0,1,2,4]
string=''
term=len(coeff)-1
for i in range(len(coeff)): #0->3
    if i!=0 and coeff[i]>0:
        string+="+"

    if coeff[i]!=0:
        string+=f"{coeff[i]}x^{term}"
    term-=1
print(string)

term=len(coeff)-1
result=0
x=int(input("input the number"))
for i in range(len(coeff)):
    result+=coeff[i]*x**term
    term-=1
print(result)

