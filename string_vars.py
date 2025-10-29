s = 'sjgoahghwghqog43y3yjqghrjajhwojhrah'
print(len(s))
print(type(s))
print(s)

print(s[:4])
print(s[-4:])
print(s[2:7])
print(s[2:7] + s[-4:])

s1 = 'He said "Yes"'
print(s1)
s2 = "I can't"
print(s2)
s3 = "He said \"I can't\""
print(s3)
s3 = 'He said "I can\'t"'
print(s3)

s4 = """
I can't
he said
"Yes"
"""
print(s4)

s5 = r'He said "Yes"'
print(s5)
print('----------------------')
s6 = 'abca\txyz\ndef\tegew'
print(s6)
s6 = 'abca\txyz\ndef\\tegew'
print(s6)

s6 = r'abca\txyz\ndef\tegew'
print(s6)

s7 = s6.upper()
print(s7)

print(s7.find('-EF'))
print(s7.index('EF'))
print(s7.rfind('E'))
print(s7.rindex('E'))



print('--------------------')
print(ord('a'))
print(ord('A'))
print(ord('\t'))
print(ord('ż'))
print(ord('ł'))
print('ł')


print(chr(67))