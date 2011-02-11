#####################################################################################################
##
##      constants.py - part of duplicatemanager, a script for comicrack
##
##      Author: perezmu
##
##      Copyleft perezmu 2011. 
##
######################################################################################################



##########
#
#   DEFINITIONS


import re
import clr
import System
import System.IO
from System.IO import Path, Directory, File, FileInfo

#
#############   **** USER CONFIGURABLE VARIABLES ***    ###########################################
#
#          see http://code.google.com/p/comicrack-duplicates-manager/wiki/UserConfiguration for details


MOVEFILES = False
REMOVEFROMLIB = False

DUPESDIRECTORY = Path.Combine("C:\\","__dupes__")

C2C_NOADS_GAP = 5           # Difference of pages between c2c and noads

VERBOSE = False             # Logging level (true/false)


#
############   DON'T MODIFY BELOW THIS LINE ######
#

VERSION= "0.2"

SCRIPTDIRECTORY = __file__[0:-len("constants.py")]
RULESFILE = Path.Combine(SCRIPTDIRECTORY, "dmrules.dat")
LOGFILE = Path.Combine(DUPESDIRECTORY, "logfile.log")
(SERIES,NUMBER,VOLUME,FILENAME,PAGECOUNT,FILESIZE,ID,CVDB_ID,FILEPATH,TAGS,NOTES,BOOK) = range(12)

#
#
###########