"""Extraction de textes et construction du corpus

    USAGE:
        python3 main.py [fichier_URL]

    Authors:
        XU Yizhou et JIANG Chunyang

    Update:
        2019-02-10

"""
import sys
from collections import defaultdict

from corpus_builder import *
from parser import *


def main():
    PARSER = {
        'xinhua': xinhua_parser,
        'people': people_parser,
        "huanqiu": huanqiu_parser,
        "ce": ce_parser,
    }

    doc = minidom.Document()
    corpus = doc.createElement("corpus")
    doc.appendChild(corpus)
    corpus.appendChild(create_header(doc))
    texts = doc.createElement("texts")

    URLs = sys.argv[1]
    source = build_source(URLs)

    cnt = 1
    # print(source)
    for site in source:
        for url in source[site]:
            if url:
                content = PARSER[site](url)
                print(url)
                text_id = "_".join([site,str(cnt)])
                text = create_text(doc, text_id, content)
                texts.appendChild(text)
                cnt += 1

    corpus.appendChild(texts)
    print(doc.toprettyxml(encoding="utf-8",indent="  ").decode('utf-8'),
          file=open("corpus.xml","w"))

def build_source(URLs):
    source = defaultdict(list)
    with open(URLs) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                site = line.split()[-1]
            else:
                source[site].append(line)
    return source

if __name__ == '__main__':
    main()
