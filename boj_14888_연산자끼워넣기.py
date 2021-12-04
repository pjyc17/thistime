# 문제는 조합을 통해서 연산자를 배열하는 것
# 연산자를 0 1 0 1 로 받으면 리스트에는 [-, /] 가 담기게 만든다.
# 담은 리스트를 조합을 통해 섞어준다. 
# 리스트의 0 번부터 len(list) -1 번까지의 순서로 수의 나열 뒤에 붙여 써준다.
# 수 0번 연산자 0번 수 1번을 놓고 계산을 한다. 
#  
import itertools

N = int(input())
nums = list(map(int, input().split()))
calc = list(map(int, input().split()))
# s = []
chr = ''

# for _ in range(calc[0]):
#     s.append('+')
# for _ in range(calc[1]):
#     s.append('-')
# for _ in range(calc[2]):
#     s.append('*')
# for _ in range(calc[3]):
#     s.append('/')
chr += '+' * calc[0] + '-' * calc[1] + '*' * calc[2] + '/' * calc[3]
lst = []
npn = list(map(list, itertools.permutations(chr)))

for j in range(len(list(npn))):

    plus = nums[0]
    for i in range(len(chr)):
        if list(npn)[j][i] == '+':
            plus += nums[i+1]
        elif list(npn)[j][i] == '-':
            plus -= nums[i+1]
        elif list(npn)[j][i] == '*':
            plus *= nums[i+1]
        elif list(npn)[j][i] == '/':
            if plus < 0:
                plus = -(abs(plus) // nums[i+1])
            else:
                plus //= nums[i+1]
    lst.append(plus)

print(max(lst))
print(min(lst))



