"""wcount.py: count words from an Internet file.

__author__ = "Li Zihan"
__pkuid__  = "1700011735"
__email__  = "chemlzh@pku.edu.cn"
"""

import sys, re
from urllib.request import urlopen
from functools import cmp_to_key

def wcount(lines, topn = 10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    originlst = re.findall('[a-zA-Z\'\-]+', lines)
    lst = list(set(originlst))
    cnt = []
    for i in lst:
        pair = (originlst.count(i), i)
        cnt.append(pair)
    cnt.sort(key = lambda x: (-x[0], x[1]))
    for i in range(0, topn):
        print(cnt[i][1], cnt[i][0])


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
