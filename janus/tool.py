# Janus
# Jared Raby 09/2016
#
# tool.py
# Description:
# Tools take in a given file of a speicifc format, convert it, and return the resulting file.
# All tools inherit this base type and only inherit the base commands.

import subprocess

class tool():
    def __init__(self, filetype):
        self.filetype = filetype
        self.callInput = "pandoc %s --latex-engine=xelatex -o %s".format(self.filetype.name, self.filetype.output)

    def call(self):
        subprocess.call(self.callInput, shell=True)


