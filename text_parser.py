import BeautifulSoup
import urllib2
import unicodedata
import string, re
import operator
import matplotlib.pyplot as plt

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
        all_p.append(str(inner_p))

    all_words = []

    for p in all_p:
        all_words.append(p.split())

    word_count = {}

    for p in all_words:
        for word in p:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_count = sorted(word_count.items(), key=operator.itemgetter(1))
    sorted_count.reverse()

    all_labels = []
    all_points = []

    for w in sorted_count:
        all_labels.append(w[0])
        all_points.append(w[1])

    plt.cla
    plt.clabel
    plt.clf()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.axis([-10, len(sorted_count) * 1.1, 0, max(all_points) * 1.1])
    plt.title('Zipfs Law Demonstration')
    plt.plot(all_points)

    index = 0

    for xy in zip(range(len(all_points)), all_points):
        if index < 10:
            expected = all_points[0] / (index + 1)
            label = all_labels[index] + \
                    " : " + \
                    str(all_points[index]) + \
                    ", expected : " + \
                    str(expected)
            ax.annotate(label, xy=xy)
        index += 1

    plt.draw()
    plt.show(block=False)

