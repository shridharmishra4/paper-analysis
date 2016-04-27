#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  predictor.py
#  
#  Copyright 2014 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import Tkinter
import re
import tkFileDialog
from cStringIO import StringIO

import nltk
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

pattern = re.compile(r"^/")

# filename=""
text = []
activelist = []


def convert_pdf_to_txt(filename):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(filename, 'r+')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


def Commondialog():
    root = Tkinter.Tk()
    root.withdraw()

    raw_input("Press enter to select the file")

    filename = tkFileDialog.askopenfilename()
    print filename
    return filename


def Black_list(word):  # string has to be passed
    black_list = ['distribution', 'frequency', 'For', '.', ',', 'is', '>', '>>>', '(', ')', '<', 'of', 'in', 'we',
                  'for', 'the', 'a', 'an', 'another', 'no', 'some', 'any', 'my', 'our', 'their', 'her', 'his', 'its',
                  'each', 'every', 'certain', 'it', 'this', 'that', 'that', 'which', 'who', 'whom', 'whose',
                  'whichever', 'whoever', 'whomever', 'anybody', 'anyone', 'anything', 'each', 'either', 'everybody',
                  'everyone', 'everything', 'neither', 'nobody', 'no one', 'nothing', 'one', 'somebody', 'someone',
                  'something', 'both', 'few', 'many', 'several', 'all', 'most', 'none', 'some', 'what', 'Hello']
    black_list.sort()
    if word in black_list:
        # print '1'
        return True
    else:
        return False


def delete_words(text):
    count = 0

    for items in text:

        if not Black_list(items):
            # print items
            activelist.append(items)
            count += 1


def frequency(text):
    freq = nltk.FreqDist(text)
    keys = freq.keys()
    print keys[:50]


def main():
    f = Commondialog()
    text = nltk.word_tokenize(convert_pdf_to_txt(f).lower())
    delete_words(text)
    frequency(activelist)
    return 0


if __name__ == '__main__':
    main()
