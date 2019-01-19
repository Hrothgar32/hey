from bs4 import BeautifulSoup
import mechanize
import re
br = mechanize.Browser()


br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open('https://privatehd.to/auth/login')
br.select_form(nr=0)
br.form['email_username'] = 'hrothgar32'
br.form['password'] = 'agh54sdE561Q'
br.submit()
k = br.open('https://privatehd.to/movies?imdb=tt0267913')
g = k.read()
soup = BeautifulSoup(g.decode('utf-8'), 'lxml')
tag = soup.find('div', {'class' : 'block'})
br.open('https://privatehd.to/movies/torrents/' + re.findall('\d+',tag.find('a')['href'])[0] + '?quality=1080p')
soup = BeautifulSoup(br.response().read().decode('utf-8'), 'lxml')
myList = soup('a', {"class" : "torrent-filename"})
br.open(myList[-1]["href"])
soup = BeautifulSoup(br.response().read().decode('utf-8'), 'lxml')
tbody = soup.find('tbody')
goodList = tbody.find_all('a')
i = 0
for link in goodList:
    br.retrieve(link['href'], ''.join(['vegre',str(i),'.torrent']), '')
    i = i + 1