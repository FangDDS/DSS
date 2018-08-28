#使用select 找出含有h1 目标的元素
soup = BeautifulSoup(html_sample, 'html.parser')
header = soup.select('h1')
print(header[0])
print(header[0].text)
print(header)


#使用select 找出含有a 目标的元素
soup = BeautifulSoup(html_sample, 'html.parser')
alink = soup.select('a')
print(alink)
for link in alink:
	print(link.text)


	CSS属性取得元素
#使用select 找出所有id为title目标的元素(id前面需加#）
alink = soup.select('#title')
print(alink)

#使用select 找出所有class为link目标的元素(class前面需加.）
soup = BeautifulSoup(html_sample)
for link in soup.select('.link'):
	print(link)
	

#使用select找出所有a tag 的href 连结

alinks = soup.select('a')
for link in alinks:
	print(link['href'])