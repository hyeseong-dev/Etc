n = input().upper() # 입력 및 대문자화 
t = [] # 알파벳 개수 저장할 list 
for i in set(n): # 입력받은 알파벳 중 unique한 알파벳만 
    t.append(n.count(i)) # 개수 
idx = [i for i,x in enumerate(t) if x == max(t)] # 최대값 위치 
if len(idx)>1: print("?") # 최대값이 여러개면 ? 출력 
else : print(list(set(n))[t.index(max(t))]) # 최대값이 하나면 해당 알파벳 출력

