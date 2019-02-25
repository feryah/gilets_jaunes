"""Constructeur de corpus en XML

    Authors:
        XU Yizhou et JIANG Chunyang

    Update:
        2019-02-10

"""
import xml.dom.minidom as minidom
import datetime

CORPUS_TITLE = '"Gilets Jaunes" dans la Presse chinoise de Chine continentale'
AUTHORS = [
    "XU Yizhou",
    "JIANG Chunyang"
]
LANGUAGE = "Chinese"


def main():
    doc = minidom.Document()
    corpus = doc.createElement("corpus")
    doc.appendChild(corpus)

    corpus.appendChild(create_header(doc))

    print(doc.toprettyxml(encoding="utf-8", indent="  ").decode('utf-8'))

def create_header(doc):
    header = doc.createElement("header")
    # title
    title = doc.createElement("title")
    title.appendChild(doc.createTextNode(CORPUS_TITLE))
    # language
    language = doc.createElement("language")
    language.appendChild(doc.createTextNode(LANGUAGE))
    # editors
    editors = doc.createElement("editors")
    cnt = 1
    for ed in AUTHORS:
        editor = doc.createElement("editor")
        editor.appendChild(doc.createTextNode(ed))
        editor.setAttribute("id","ed_"+str(cnt))
        editors.appendChild(editor)
        cnt += 1
    # size
    size = doc.createElement("size")
    nb_texts = doc.createElement("nbTexts")
    nb_texts.setAttribute("nb","")
    nb_words = doc.createElement("nbWords")
    nb_words.setAttribute("nb","")
    size.appendChild(nb_texts)
    size.appendChild(nb_words)
    # update
    update = doc.createElement("update")
    update.appendChild(doc.createTextNode(str(datetime.date.today())))

    # final
    header.appendChild(title)
    header.appendChild(language)
    header.appendChild(size)
    header.appendChild(editors)
    header.appendChild(update)
    return header

def create_text(doc,id, content):
    text = doc.createElement("text")
    text.setAttribute("id", id)
    text.setAttribute("source", content['source'])
    text.setAttribute("date", content['date'])
    text.setAttribute("keywords",content['keywords'])
    text.setAttribute("title",content['title'])
    text.appendChild(doc.createTextNode(content['text']))
    return text


if __name__ == '__main__':
    main()
