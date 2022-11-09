# 자료형 - 리스트 

a = [1,2,3,4]  # a는 벡터 (엄밀히 따져서 벡터는 아니다.)
b = [5,6,7,8]

# print("a : ", a)
# print("b : ", b)
# print(a + b) 


zero_vector = [0, 0, 0]
one_vector = [1, 1, 1]

# unit_vector 
e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 1]


import numpy as np

# numpy.sum() -> np.sum()

a = np.array([1,2,3,4]) # 수학적으로 이게 벡터다. 
b = np.array([1,2,4,5])

print(a)
print(type(a))
print(a+b)
print(a*2)
print(a*b)
print(sum(a*b)) # inner product 내적 


'''
def add(x, y):
    return x + y

n = 3
m = 4
print(add(3, 4))
'''



'''
class student():
    name = "노유미" # value : 값
    def babo(self, x): # method : 동작 
        print(x, " : 는 바보입니다.")

a = student()
print(a.name)
print(a.babo('이경훈'))
'''
