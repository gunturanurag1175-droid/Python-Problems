"""Without running the code, predict the output of each line below. Then run it and check if you were right:

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
print(10 - 4 // 3 + 1)"""

print(2 + 3 * 4) # # 14  — * before +
print((2 + 3) * 4) # 220  — () overrides precedence
print(2 ** 3 ** 2) #  # 512 — ** is right-associative: 3**2=9, then 2**9=512
print(10 - 4 // 3 + 1) # 110  — // first: 4//3=1, then 10-1+1=10