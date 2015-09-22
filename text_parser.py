import BeautifulSoup
import urllib2


def a():
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program')
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    div = soup.find(id="mw-content-text")

    all_p = []

    for p in div.findAll('p'):
        inner_p = p.getText(separator=u' ')
        all_p.append(inner_p)
        all_p.append(' ')

    print all_p

