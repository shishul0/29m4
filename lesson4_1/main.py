# def nc(s): # решение за O(N**2)
#     for sym in s:
#         counter = 0
#         for ss in s:
#             if sym == ss:
#                 counter += 1
#         print(sym, counter)
# nc('abc')

# def nc(s): # решение за O(M*N) при том, что M>=N
#     for sym in set(s):
#         counter = 0
#         for ss in s:
#             if sym == ss:
#                 counter += 1
#         print(sym, counter)
# nc('abca')

def nc(s): # решение за O(M+N) (приравнивают к O(N))
    mydct = {}
    for sym in s:
        mydct[sym] = mydct.get(sym, 0) + 1
    for sym, count in mydct.items():
        print(sym, count)
nc('apple')