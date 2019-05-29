import re

# 只匹配ascii字符
# regex = re.compile(r"\w+", flags=re.A)

# 匹配时忽略字母的大小写
# regex = re.compile(r"[A-Z]\w*", flags=re.I)

#  使.可以匹配换行
# regex = re.compile(r".+", flags=re.S)

# 使 ^   $ 可以匹配每一行的开头结尾位置
regex = re.compile(r"^北京", flags=re.M)

s = """Welcome to
北京
"""

l = regex.findall(s)
print(l)
