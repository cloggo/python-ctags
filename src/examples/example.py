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

print tagFile['name']
print tagFile['author']
print tagFile['format']
if status:
    print entry['name']
    print entry['kind']
    
if tagFile.find(entry, 'findtag', ctags.TAG_PARTIALMATCH | ctags.TAG_IGNORECASE):
    print 'found'
    print entry['lineNumber']
    print entry['pattern']
    print entry['kind']
