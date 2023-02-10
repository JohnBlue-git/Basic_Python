# Auther: John Blue
# Time: 2023/2
# Object: display how to use continue and break

for i in range(6):
    for j in range(0, 6):
        if i == 0 and j == 4: break
        
        if i == 4: continue

        print("(", i, ",",  j, ")")
