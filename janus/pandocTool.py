# Janus
# Jared Raby
#
# pandocTool.py
# Description:
# Pandoc is a tool that does a lot of text / doc / markdown / etc conversions to various different types. 
# In version 1 it will mostly be used for conversion of documents to PDFs.

import tool

class pandocTool(tool):

    def __init__(self, filetype):
        self.input = filetype

