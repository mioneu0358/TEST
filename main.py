# cpu,gpu 차이 CPU는 한개의 데이터를 처리하지만, GPU는 여러개의 데이터를 한번에 처리한다.
import sys

#리스트 멤버 메서드
# extend(iterable)
# remove(x) 처음으로 나오는 x를 삭제

# from collections import deque
# dq = deque(["Apple", "Banana", "Coconut"])
# print(dq)


#리스트 컴프리헨션
#리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공한다. 흖나 요옫는 각 요소가 다른 시퀀스나
#이터러블한 객체에 어떤 연산을 적용한 결과 리스트를 만들거나, 어떤 조건을 만족하는 요소들을 구성된 서브 시퀀스를 만드는 것이다.
# squares = []
#
# for x in range(10):
#     squares.append(x**2)
#
# print(squares)
# print(x)        #x라는 변수가 아직 존재한다.

#map함수 사용
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

#리스트 컴프리헨션 사용
# squares = [x**2 for x in range(10)]
# print(squares)
# print(x)    #NameError: name 'x' is not defined

#리스트 컴프리헨션 사용법
#[표현식 for 변수 in iterable객체 if 조건]
# 표현식 = 값으로 평가 받을수 있는 식

#예제
# vec = [-4,-2,0,2,4]
# a = [x*2 for x in vec]  #원소들을 2배로 만든 리스트
# b = [x for x in vec if x>0] #음수원소들을 제외한 리스트
# c = [abs(x) for x in vec]   #원소들의 절대값들로 이루어진 리스트

# fruits = [" Apple ", " Banana ", " Coconut "]
# a = [x.strip(' ') for x in fruits]  #앞뒤 공백을 제거한 문자열 원소들로 이루어진 리스트
# b = [(x,x**2 for x in range(6))] #x와 x의 제곱을 담은 튜플이 원소로 이루어진 리스트

# vec = [[1,2,3],[4,5,6],[7,8,9]]
# a = [num for elem in vec for num in elem]   # 2중 for문을 활용하여 원소값 넣어주기
# for elem in vec:
#   for num in elem:    이 코드와 위의 코드가 같다.


#중첩된 리스트 컴프리헨션
#리스트 컴프리헨션의 첫 표현식으로 임의의 표현식이 올 수 있는데 다른 리스트 컴프리헨션도 가능하다. 이를 중첩된 리스트 컴프리헨션이라고 한다.

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
#
# transposed = [[row[i] for row in matrix] for i in  range(4)]
# print(transposed)
#[[1, 5, 9],
# [2, 6, 10],
# [3, 7, 11],
# [4, 8, 12]]

# 이 예제는 중첩된 리스트 컴프리헨션에 대한 좋은 예이지만, 더 간단한 방법도 존재한다.
# 이 경우 복잡한 흐름문 대신 내장 함수 zip()을 사용하면 더 간단하게 해결할 수 있다.
# transposed2 = list(zip(*matrix))
#리스트 앞의 *은 unpacking연산자다.

# 연습문제
# 파이썬의 input()함수는 실행속도가 비교적 느리기 때문에 문제 풀 때 시간초과가 날 수 있다.
#sys모듈의 sys.stdlin.readline()함수를 사용하자.
#queue 대신엔 collection 모듈의 deque를 사용하자.
import sys
#
# n = int(sys.stdin.readline())
# stack = []
# for i in range(n):
#     stack.append(int(sys.stdin.readline()))
# stick = 0
# cnt = 0
# for i in stack[::-1]:
#     if stick < i:
#         cnt +=1
#         stick = i
# print(cnt)


#정환쌤 코드
import sys

# n = int(sys.stdin.readline())
# stack = [int(sys.stdin.readline()) for _ in range(n)]
#
# max_stick = 0
# cnt = 0
#
# while stack:
#     stick = stack.pop()
#     if stick > max_stick:
#         max_stick = stick
#         cnt += 1
# print(cnt)


from collections import deque
n = int(sys.stdin.readline())

people = deque(range(1,n+1))
stage = 1

while len(people) > 1:
    num = stage ** 3 % len(people)
    for _ in range(num):
        people.append(people.popleft())
    people.pop()
    stage += 1
print(people[0])
