import re

p = re.compile("ca.e") 
# . : 하나의 문자  ca.e > cafe, care
# ^ : 문자열의 시작  ^de > desk, destination 
# $ : 문자열의 끝  se$ > case, base

#print(m.group())
def print_match(m):
    if m:
        print(m.group())
    else :
        print("매칭 불가")


m=p.match("ssff")
print_match(m)