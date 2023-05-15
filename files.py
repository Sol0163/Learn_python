file = open("Hello.txt", "r")
# a - append r - read w - write

a = file.readlines()
sum = 0
for nm in a:
    sum += int(nm.strip())

print(sum)
file.close()