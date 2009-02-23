import ctags
from ctags import CTags, TagEntry
import sys

try:
    tagFile = CTags('tags')
except:
    sys.exit(1)
    
   
entry = TagEntry()
status = tagFile.setSortType(ctags.TAG_SORTED)
status = tagFile.first(entry)

print tagFile['format']
print tagFile['author']
print tagFile['name']
if status:
    print entry['name']
    print entry['pattern']
    print entry['kind']
    print entry['lineNumber']
    
if tagFile.find(entry, 'findTag', ctags.TAG_PARTIALMATCH):
    print 'found'
    print entry['lineNumber']
    print entry['pattern']
