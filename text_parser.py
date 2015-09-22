import BeautifulSoup
import urllib2
import unicodedata
import string, re
import operator
import matplotlib.pyplot as plt
import math

def a():
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/United_States')
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    div = soup.find(id="mw-content-text")

    all_p = []

    for p in div.findAll('p'):
        inner_p = p.getText(separator=u' ')
        pattern = re.compile('[^a-zA-Z\s]')
        inner_p = pattern.sub('', inner_p)

        all_p.append(str(inner_p))

    all_words = []

    for p in all_p:
        all_words.append(p.split())

    word_count = {}

    for p in all_words:
        for word in p:
            lower_word = word.lower()
            if lower_word in word_count.keys():
                word_count[lower_word] += 1
            else:
                word_count[lower_word] = 1

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
    ax.set_xscale('log')

    all_expected = []
    all_log_points = []

    for index in range(len(all_points)):
        all_log_points.append(math.log(all_points[index]))
        if index < 20:
            expected = all_points[0] / (index + 1)
            all_expected.append(expected)
            label = all_labels[index] + \
                    " : " + \
                    str(all_points[index]) + \
                    ", expected : " + \
                    str(expected)
            print label
        index += 1


    plt.axis([0.8,
              len(all_log_points) * 1.2,
              max(all_log_points) * -0.1,
              max(all_log_points) * 1.1])
    plt.title("""Zipf's Law Demonstration""")
    plt.plot(all_log_points, 'gH', markeredgecolor='g')
    plt.draw()
    plt.show(block=False)

