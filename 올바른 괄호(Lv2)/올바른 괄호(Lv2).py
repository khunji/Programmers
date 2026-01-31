#문제
#괄호가 바르게 짝지어졌다는 것은 '('문자로 열렸으면 반드시 짝지어서 ')'문자로 닫혀야 한다는 뜻이다.
#예를 들어 "()()"또는 "(())()"는 올바른 괄호이다.

#'('또는 ')'로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성하자.

import sys
input = sys.stdin.readline

def solution(a):
    
    balance = 0
    for i in a:
        if i == '(':
            balance+=1
        else:
            balance-=1

        if balance<0:
            return False
           
    
    if balance==0:
        return True
    else:
        return False
        

s = input().strip()#문자열 s를 입력하기
print(solution(s))