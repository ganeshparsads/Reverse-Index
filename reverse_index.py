import sys
import json
def list_duplicates_of(seq,item):
    seq = seq.split()
    start_at = -1
    locations = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locations.append(loc)
            start_at = loc
    return locations

if len(sys.argv) < 2:
    print "ERROR:Less number of arguments"
else:
    filename = sys.argv[1]
    file = open(filename, 'r')
    source = file.read()
    file.close()
    removed_duplicates = list(set(source.split()))
    reverse_index = {}
    for word in removed_duplicates: 
        reverse_index[word] = list_duplicates_of(source, word)
    with open('reverse_index.json', 'w') as outfile:
        json.dump(reverse_index, outfile)
