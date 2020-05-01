import re

string = input("")

# if string == " ": # 문장 자체가 공백인 경우 
#     print(0)
# else : 
#     words = string.split(" ") # 띄어쓰기로 구분
#     print(words)
#     words = string.split('\t')
#     print(words)
    
#     while '' in words : #문장 양쪽에 있는 공백이 없어질 때까지 반복
#         words.remove('')


# 아래는 re표현을 이요한 개 간단한 방법
p = re.compile(r'\S+')
m = p.findall(string)
print(len(m))
        
# print(len(words))