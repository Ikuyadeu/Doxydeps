import sys
import csv
import re
from collections import Counter
import treetaggerwrapper

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    CSV_PASS = "DepsR\\" + (ARGV[1]) + "\\"
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

    
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')
def getwords(doc):
    tags = [x.lemma for x in treetaggerwrapper.make_tags(tagger.tag_text(doc), exclude_nottags=True) if not re.search("[0-9a-f]{10,}|[^0-9A-Za-z]", x.lemma)]
    return  tags[0] if len(tags) > 0 else list()

csvname = CSV_PASS + "one_double_message.csv"
csvname_w = CSV_PASS + "one_double_message3.csv"
with open(csvname, encoding="utf-8") as csvfile:
    dep_writer = csv.writer(open(csvname_w, "w", encoding="utf-8"), lineterminator="\n")
    kind_reader = csv.DictReader(csvfile)
    kind_message = [(x['message'], x['fmessage']) for x in kind_reader if x['futureNo'] != x['commitNo']]
    print("getkindmessage")
    counter = Counter(kind_message)
    dep_writer.writerow(('before_word','after_word', 'score'))
    for word, cnt in counter.most_common():
        dep_writer.writerow((word[0], word[1], cnt))