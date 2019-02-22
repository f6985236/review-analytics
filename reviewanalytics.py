data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f :
		data.append(line)#把line加入清單
		count += 1 # count= count + 1
		if count % 1000 == 0: #餘數要= 0
			print(len(data))#才能用清單算長度

print('檔案讀取完了，總共有',len(data),'筆留言')


#計算一百萬筆留言的平均長度

sum_len = 0
for d in data : #讀取每一個在'data'裡的留言，稱作d
	sum_len += len(d) #sum_len = sum_len + len(d)的快寫

print('平均是',sum_len/len(data))


#算出長度小於一百的留言有多少筆：
#先建立獨立的清單，用以放長度小於100的留言
new = []

for d in data :#每筆在data裡的留言稱作d，forlopp的意思就是把清單裡的東西一個一個拿出來！
	if len(d) < 100 :#如果留言長度<100
		new.append(d)#我就把你裝進這個new清單中
#for loop做完才要print:		
print('一共有',len(new),'筆留言長度小於100')

print(new[0])
#查看清單裡的第一筆留言

#-----把留言裡面有提到單詞「good」的留言篩選出來，並計算有幾筆提到：

good = [] #先建立一個叫做good的清單，用來放我們想要篩選出來的good留言


for c in data: #把data清單中裡面每一行稱作d
	if 'good' in c :
		good.append(c)
print('一共有',len(good),'筆留言裡面有good!')

#超級快寫法：
#good = [ c for c in data if 'good' in c ]  就等於直接建立一個good清單，符合上述條件
#good = [ 1 for c in data if 'good' in c ]  註意這邊的意思，是把符合條件有good的留言，把1裝進清單，print出good清單，就會變成兩萬多筆'1'

print(good[0])

#-----練習，建立一個bad，清單裝"1",然後算有幾筆

bad = [1 for b in data if 'bad' in b]

print(bad)
print('一共有',len(bad),'筆留言裡面有bad')

#-----練習檢驗清單裡有無bad，印出true or false!
#hint:檢驗布林值問句： a in b 是個問句，問a有無在b裡


worse = ['bad' in g for g in  data ]

print(worse) #印出來就會是一百萬筆的true or false

	