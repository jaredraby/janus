# Janus
# Jared Raby 09/2016
#
# fileConvert.py
# Description:
# Top level node that starts handling the directory identification and prep for the incoming file. # Generates a stack to keep track of pending file conversions, generates identifiers, and serves as
# the information prep area before the system calls the conversion tools.


# Imports
import uuid
import os
import shutil
import errno

# Take a HTTP request and generate a unique file directory for the input and output files of a particular request.
def directoryPrep():
    baseDir = "/tmp/janus-"
    fileId = idGen()
    locDir = baseDir + fileId

    try:
        os.makedirs(locDir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    
    return locDir

# Delete the directory passed in. Used to clean up the /tmp directory once the conversion has been completed
def directoryDelete( dir ):

    try:
        shutil.rmtree(dir)
    except OSError as exeption:
        if exception.errno != errno.EEXIST:
            raise
        
# Generate a UUID for a given file conversion
def idGen():
    fileId = uuid.uuid4()
    return str(fileId)
               

