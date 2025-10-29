s_m = """Hello
This is 2nd line
3rd line"""
print(s_m)

l_sm = s_m.split('\n')
print(l_sm)
print('----------')
i = 0
for line in l_sm:
    i += 1
    print(f'{i}: {line}')
print('----------')

print(len(l_sm))
print(len(l_sm[1]))
print(l_sm[1])

s2 = ' |||||| '.join(l_sm)
print(s2)

print('----------')
f = 3363633
sf = 'f={}, {}, {}'.format(f, 4536, 5785)
sf = f'f={f/25}, {36363}, {3636}'
print(sf)

li2 = [ 526, 363653.363, 363267 ]
sli2 = [ str(x) for x in li2 if x > 600 ]

# sli2 = []
# for x in li2:
#     sli2.append(str(x))

print(sli2)
sli2_line = '\t||| '.join(sli2)
print(sli2_line)
