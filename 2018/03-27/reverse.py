a = "1686f596"
b = "5646f537"
c = "76765726"
d = "37f52756"
e = "c6c696b6"
i = 0
nums = []
while i < 8:
	nums.append(int(a[i:i+2][::-1], 16))
	i += 2
i = 0
num1 = []
while i < 8:
	num1.append(int(b[i:i+2][::-1], 16))
	i += 2
i = 0
num2 = []
while i < 8:
	num2.append(int(c[i:i+2][::-1], 16))
	i += 2
i = 0
num3 = []
while i < 8:
	num3.append(int(d[i:i+2][::-1], 16))
	i += 2
i = 0
num4 = []
while i < 8:
	num4.append(int(e[i:i+2][::-1], 16))
	i += 2
num = nums[::-1] + num1[::-1] + num2[::-1] + num3[::-1] + num4[::-1]
flag = ""
for j in num:
    flag += chr(j)
print(flag)