import BeautifulSoup
import urllib2
import unicodedata
import string, re

def a():
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program')
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    div = soup.find(id="mw-content-text")

    all_p = []

    for p in div.findAll('p'):
        inner_p = p.getText(separator=u' ')
        pattern = re.compile('[^a-zA-Z0-9\s]')
        inner_p = pattern.sub('', inner_p)
        all_p.append(inner_p)

#    all_words = all_p[0].split()
#    all_words = [i.split()[0] for i in all_p]
#    all_words = all_p

    all_words = []

    for p in all_p:
        all_words.append(p.split())

    word_count = {}
    x = 0
    for word in all_words:
        if word in word_count.keys():
            x = 5
#            word_count[word] += 1
        else:
            x = 3
#            word_count[word] = 1

    print all_words[0]

