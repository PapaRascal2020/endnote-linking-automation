####################################################
#                                                  #
# Automate Tool                                    #
#                                                  #     
# @desc: This file will unzip any epub files and   #
# run any automation scripts on it. The folder     #
# then gets placed into an output folder in which  #
# a user can make edits.                           #
#                                                  #
####################################################

# Import Python Utilities
import os.path
import shutil
import sys
import datetime
import chardet

# Import unidecode to help with ASCII conversion problems.
from unidecode import unidecode

# Get the current Python script location and store.
path = os.path.dirname(os.path.realpath(__file__))

# Import Glob (Directory Lister)
import glob

# Look for files in the folder that end with .epub
html = glob.glob(path+"/*.xhtml")

# Check for new jobs (new epubs in repo folder)
# If 0 then exit
# If 1+ continue.

if len(html) == 0:
    print("No html found to process")
    exit()
else:
    print("Found Item(s): "+str(html)+ "\n\n")
    
#Include BeautifulSoup (HTML Plugin)
from bs4 import BeautifulSoup, Tag


for i, html_file in enumerate(html):
    h = open(html_file).read()
    parser = BeautifulSoup(h,"lxml")
    for link in parser.find_all("a"):
        if link["href"] == "#" and link["name"].startswith("endnote"):
        	new_link = "book-%(pn)s.xhtml#note%(tn)s"
        	idx = int(link["name"].split("-")[1])
        	idy = 0
        	if 0 <= idx <= 16:
        		idy = 2
        	if 15 <= idx <= 43:
        		idy = 3
        	if 42 <= idx <= 53:
        		idy = 4
        	if 52 <= idx <= 71:
        		idy = 5
        	if 70 <= idx <= 77:
        		idy = 6
        	if 76 <= idx <= 88:
        		idy = 7
        	if 87 <= idx <= 104:
        		idy = 8
        	if 103 <= idx <= 117:
        		idy = 9
        	if 116 <= idx <= 127:
        		idy = 10
        	if 126 <= idx <= 133:
        		idy = 11
        	if 132 <= idx <= 155:
        		idy = 12
        	if 154 <= idx <= 160:
        		idy = 13
        	if 159 <= idx <= 182:
        		idy = 14
        	if 181 <= idx <= 198:
        		idy = 15
        	if 197 <= idx <= 206:
        		idy = 16
        	if 205 <=  idx <=  218:
        		idy = 17
        	if 217 <= idx <=  257:
        		idy = 18
        	if 256 <= idx <=  267:
        		idy = 19

        	link["href"] = new_link % {'tn': str(idx), 'pn': str(idy)}

    for endnotes in parser.find_all("a"):
        if endnotes["href"].startswith("book-21.xhtml#endnote-"):
        	noteid = endnotes["href"].split("-")[2]
        	endnotes["name"] = "note"+noteid

	html_to_output = parser

	f = open(html_file, 'w')
	print >> f.write(unidecode(html_to_output))   
	f.close()
