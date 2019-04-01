"""nettoyage de textes


"""

import xml.etree.cElementTree as ET
import sys

def main():
    tree = ET.ElementTree(file=sys.argv[1])
    corpus = tree.getroot()
    for text in tree.iterfind('texts/text'):
        print(text.attrib)




if __name__ == "__main__":
    main()