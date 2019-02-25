"""Generates url candidates

    USAGE:
        python3 build_url.py [dst_fichier_URL]

    Authors:
        XU Yizhou et JIANG Chunyang

    Update:
        2019-02-24

"""
import sys
from urllib import request
from bs4 import BeautifulSoup
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
MATCHER = re.compile("https://translate.google.com.+\\&u=(.+?)\\&prev")
BASES = {
    'xinhua': "https://www.google.com/search?q=-%E9%BB%84%E9%A9%AC%E7%94"
              "%B2+-%E9%BB%84%E8%83%8C%E5%BF%83+site:http://www"
              ".xinhuanet.com/world/&lr=&safe=active&as_qdr=all&tbs=cdr"
              ":1,cd_min:11/17/2018,"
              "cd_max:2/17/2019&ei=mMlyXJTpGa6YlwSEu7jIBg&start=0&sa=N"
              "&ved=0ahUKEwiUleik6NTgAhUuzIUKHYQdDmk4FBDy0wMIgQE&biw=1223&bih=679",
    'people': "https://www.google.com/search?q=-%E9%BB%84%E9%A9%AC%E7"
              "%94%B2+-%E9%BB%84%E8%83%8C%E5%BF%83+site:http://world"
              ".people.com.cn/n1/&lr=&safe=active&as_qdr=all&tbs=cdr:1,"
              "cd_min:11/17/2018,"
              "cd_max:2/17/2019&ei=YfdyXJ_tL5GAacvNloAN&start=0&sa=N"
              "&ved=0ahUKEwjfof_5k9XgAhURQBoKHcumBdA4ChDy0wMIjAE&biw=1223&bih=679",
    'huanqiu': "https://www.google.com/search?q=-%E9%BB%84%E9%A9%AC%E7"
               "%94%B2+-%E9%BB%84%E8%83%8C%E5%BF%83+site:http://world"
               ".huanqiu.com&lr=&safe=active&as_qdr=all&tbs=cdr:1,"
               "cd_min:11/17/2018,"
               "cd_max:2/17/2019&ei=ftdyXKvsIabylwT1xreoBg&start=0&sa=N"
               "&ved=0ahUKEwiro7vF9dTgAhUm-YUKHXXjDWU4ChDy0wMIgQE&biw=1223&bih=679",
    'ce': "https://www.google.com/search?q=-%E9%BB%84%E9%A9%AC%E7%94%B2"
          "+-%E9%BB%84%E8%83%8C%E5%BF%83+site:http://intl.ce.cn/qqss"
          "/&lr=&safe=active&as_qdr=all&tbs=cdr:1,cd_min:11/17/2018,"
          "cd_max:2/17/2019&ei=CthyXO-sM4aclwS876dY&start=0&sa=N&ved"
          "=0ahUKEwjv2a2I9tTgAhUGzoUKHbz3CQs4ChDy0wMIiwE&biw=1223&bih=679",
}

def main():
    dump_url(BASES, sys.argv[1])

def dump_url(url_dict:dict, dump_to:str):
    """Dumps urls to file

    Args:
        url_dict: key:sitename, value:google search base, cf BASES
        dump_to: destination path

    """
    with open(dump_to, 'w', encoding="utf-8") as w_handle:
        for k, v in url_dict.items():
            w_handle.write("# {}\n".format(k))
            if k in ['people','ce']:
                for u in url_candidate_catched(url_base(v)):
                    if not u.startswith("http"):
                        w_handle.write("http://{}\n".format(u))
                    else:
                        w_handle.write("{}\n".format(u))
            else:
                for u in url_candidate(url_base(v)):
                    if not u.startswith("http"):
                        w_handle.write("http://{}\n".format(u))
                    else:
                        w_handle.write("{}\n".format(u))


def url_candidate(url_base:list):
    """Generates a list of urls ready for parsing.

    Args:
        url_base: a list of base urls

    Returns:
        a list of url candidates ready for parsing

    """
    candidates = []
    for base in url_base:
        req = request.Request(base, headers=HEADERS)
        page = request.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        candidates.extend([url.text.strip() for url in soup.find_all('cite',
                                                          class_="iUh30")])
    return candidates

def url_candidate_catched(url_base:list):
    """Generates a list of urls ready for parsing.

    In case of missing hard links, namely for urls from "people" and "ce"

    Args:
        url_base: a list of base urls

    Returns:
        a list of url candidates ready for parsing

    """
    candidates = []
    for base in url_base:
        req = request.Request(base, headers=HEADERS)
        page = request.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        url_raw = [
            url['href']
            for url in soup.find_all(
                'a',
                class_="fl",
                href=True
            )
        ]

        candidates.extend(
            [
                MATCHER.findall(x)[0]
                for x in url_raw if MATCHER.findall(x)
            ]
        )
    return candidates



def url_base(seed:str, base_num=5):
    """Generates a list of base urls.

    Args:
        seed: seed url
        base_num: number of pages to follow, default : 5

    Returns:
        a list of base urls

    """
    return [
        seed.replace("&start=0", "&start=" + str(base*10))
        for base in range(base_num)
    ]

if __name__=="__main__":
    main()