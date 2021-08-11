# n_l = input()
# cite = input()
# n_l = n_l.split()
# papers = n_l[0]
# maxc = n_l[1] 
# cite = cite.split()
# cite.sort()

def get_h(cite):
    tf = True
    num = -1
    cite.sort()
    for n in range(len(cite)):
        if cite[n] <= (len(cite) - n):
            num += 1
        else:
            break
    return cite[num]      

print(get_h([3, 2, 100, 1]))
print(get_h([3, 3, 100, 1]))
