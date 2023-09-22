#   Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
#   times it can be divisible.

a = int(input("input a number you want to check"))
print(a)
b = 1
t = 0
while a >= b:
    if a % b == 0:
        t += 1
    b += 1
print(f"{t} time a is divisible by b")

