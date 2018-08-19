for tech in soup.select('.tech'):
	if(len(tech.select('h2')) >0):
		h2	 = tech.select('h2')[0].text
		time = tech.select('.time')[0].text
		a	= tech.select('a')[0]['href']
		print(time,h2,a)