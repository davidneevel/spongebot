listText = [u'M', u'a', u'i', u'n', u' ', u'S', u't', u'r', u'e', u'e', u't', u' ', u'i', u's', u' ', u'B', u'O', u'O', u'M', u'I', u'N', u'G', u' ', u't', u'h', u'a', u'n', u'k', u's', u' ', u't', u'o', u' ', u'o', u'u', u'r', u' ', u'i', u'n', u'c', u'r', u'e', u'd', u'i', u'b', u'l', u'e', u' ', u'T', u'A', u'X', u' ', u'C', u'U', u'T', u' ', u'a', u'n', u'd', u' ', u'R', u'e', u'f', u'o', u'r', u'm', u' ', u'l', u'a', u'w', u'.', u' ', u'"', u'T', u'h', u'i', u's', u' ', u's', u'h', u'o', u'w', u's', u' ', u's', u'm', u'a', u'l', u'l', u'-', u'b', u'u', u's', u'i', u'n', u'e', u's', u's', u' ', u'o', u'w', u'n', u'e', u'r', u's', u' ', u'a', u'r', u'e', u' ', u'm', u'o', u'r', u'e', u' ', u't', u'h', u'a', u'n', u' ', u'j', u'u', u's', u't', u' ', u'o', u'p', u't', u'i', u'm', u'i', u's', u't', u'i', u'c', u',', u' ', u't', u'h', u'e', u'y', u' ', u'a', u'r', u'e', u' ', u'r', u'e', u'a', u'd', u'y', u' ', u't', u'o',u' ', u'g', u'r', u'o', u'w', u' ', u't', u'h', u'e', u'i', u'r', u' ', u'b', u'u', u's', u'i', u'n', u'e', u's', u's', u'e', u's', u'.', u'"', u' ', u'h', u't', u't', u'p', u's', u':', u'/', u'/', u't', u'.', u'c', u'o', u'/', u'w', u'9', u'a', u'w', u'6', u'8', u'U', u'w', u'O', u'j']
print listText

lenText = len(listText)
print "length = %d" % lenText

reconstituted = ""
for i in range(lenText):
    if listText[i].isalpha():
        try:
            if i % 2 == 1:
                listText[i] = listText[i].capitalize()
                
            else:
                listText[i] = listText[i].lower()
            
            reconstituted += listText[i]
        except: 
            print "skipped a letter"
    else:
        if listText[i] == '"':
            reconstituted += "\"" 
            print i
        else:
            reconstituted += listText[i]

print listText
print reconstituted
reconstituted

    