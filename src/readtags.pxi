cdef extern from "readtags.h":
    ctypedef struct tagFile

    ctypedef enum tagSortType "sortType":
        TAG_UNSORTED
        TAG_SORTED
        TAG_FOLDSORTED

    ctypedef struct fileType "file":
        short format
        tagSortType sort

    ctypedef struct statusType "status":
            int opened
            int error_number

    ctypedef struct programType "program":
        char *author
        char *name
        char *url
        char *version

    ctypedef struct tagFileInfo:
        statusType status
        fileType file
        programType program


    ctypedef struct tagExtensionField:
        char* key
        char* value

    ctypedef struct addressType "address":
        char* pattern
        unsigned long lineNumber

    ctypedef struct fieldsType:
        unsigned short count
        tagExtensionField *list

    ctypedef struct tagEntry:
        char* name
        char* file

        addressType address

        char* kind
        short fileScope

        fieldsType fields

    ctypedef enum tagResult:
        TagFailure
        TagSuccess


    tagFile* ctagsOpen "tagsOpen" (char *filePath, tagFileInfo *info)
    tagResult ctagsSetSortType "tagsSetSortType" (tagFile* file, tagSortType type)
    tagResult ctagsFirst "tagsFirst" (tagFile *file, tagEntry *entry)
#C++:    char *ctagsField "tagsField" (tagEntry *entry, char *key) except +MemoryError
    char *ctagsField "tagsField" (tagEntry *entry, char *key)
    tagResult ctagsFind "tagsFind" (tagFile *file, tagEntry *entry, char *name, int options)
    tagResult ctagsNext "tagsNext" (tagFile *file, tagEntry *entry)
    tagResult ctagsFindNext "tagsFindNext" (tagFile *file, tagEntry *entry)
    tagResult ctagsClose "tagsClose" (tagFile *file)
