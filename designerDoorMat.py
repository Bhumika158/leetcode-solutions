N,M= 7,21

# for i in range(1,N,2):
#     print((".|."*i).center(M,"-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,0,-2):
#     print((".|."*i).center(M,"-"))

pattern = [(".|."*i).center(M,"-") for i in range(1,N,2)]

print("\n".join(pattern + ["WELCOME".center(M,"-")] + pattern[::-1]))