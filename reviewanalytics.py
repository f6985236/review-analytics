data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f :
		data.append(line)#把line加入清單
		count += 1 # count= count + 1
		if count % 1000 == 0: #餘數要= 0
			print(len(data))#才能用清單算長度

print('檔案讀取完了，總共有',len(data),'筆留言')

sum_len = 0
for d in data : #讀取每一個在'data'裡的留言，稱作d
	sum_len += len(d)

print('平均是',sum_len/len(data))


	