wordDict = {}

with open('document.txt','r') as f:
	for line in f:
		for word in line.split():
			if word in wordDict:
				wordDict[word] += 1
			else:
				wordDict[word] = 1
# (print(key, value) for (key, value) in sorted(wordDict.items(), key=lambda x: x[1],reverse=True))

sorted_dict = sorted(wordDict.items(), key=lambda x:x[1], reverse=True)
"""

sorted_items = sorted_dict.items()
top_five = list(sorted_items)[:5]

sorted_list = []
sorted_list.append(sorted_dict.copy())

for i in range(5):
        print(sorted_list[i])

print(sorted_dict[0])
"""
for i in sorted_dict[0:5]:
	print(i[0],':', i[1])
