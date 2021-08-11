num_of_flowers = input()
petals = input()
num_of_flowers = int(num_of_flowers)
petals = petals.split()
petals = [int(p) for p in petals]
# the thing right on top is used a lot to turn lists with strings in it, into a list with integer values

answer = 0
answer += int(num_of_flowers)

for i in range(int(num_of_flowers)):
    for x in range(i+1, int(num_of_flowers)):
        p = petals[i: x+1]
        if sum(p)/len(p) in p:
            answer += 1
print(answer)
