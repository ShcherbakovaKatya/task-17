f = open('24_demo.txt').readline()
k = 0
mx = 0
for i in range(len(f)- 1):
    if f[i] == 'X' and f[i + 1] =='X':
        k += 1        
        if k > mx:
            mx = k
    else:
        k += 1
    
print(mx)