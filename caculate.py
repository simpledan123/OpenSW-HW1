x = int(input("첫 번쨰 숫자 입력:"))
y = int(input("두 번째 숫자 입력:"))
chose = input("원하는 계산 방식 입력 [+, - 중 선택]")

if chose == "+":
    print(x+y)

elif chose == "-":
    print(x-y)
else : 
    print("error")