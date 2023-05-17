from pyzotero import zotero
import bibtexparser
from bibtexparser.bwriter import BibTexWriter

zot = zotero.Zotero(library_id='4980316',library_type='group',api_key='Z6twDFkFD0lMq4gNPFv7bMNu')
zot_db = zot.everything(zot.top(sort='date'))
writer = BibTexWriter()
writer.add_trailing_comma = True
str_bibs = ''

for bib in zot_db:
    extra = bib['data']['extra']
    itemID = bib['key']
    bib_item = zot.item(itemID,format='bibtex',style='abbrv')
    bib_item.entries[0]['note']=''
    str_bib = bibtexparser.dumps(bib_item, writer).split('\n')
    if len(extra)!=0:
        str_bib.insert(-2, " bibtex_show = {true},"+"\n "+extra)
    else:
        str_bib.insert(-2, " bibtex_show = {true},")
    str_bibs += '\n'.join(str_bib)+'\n'

str_bibs = str_bibs.split('\n')
ids = []
for i, line in enumerate(str_bibs):
    if '@' in line:
        if line in ids:
            new_line = line[:-1]+'_'+str(i)+','
            str_bibs[i] = new_line
            ids.append(new_line)
        else:
            ids.append(line)

str_bibs = '\n'.join(str_bibs)

with open('_bibliography/references.bib','w') as bibtex_file:
    bibtex_file.write(str_bibs)

# with open('_bibliography/references.bib','w') as bibtex_file:
#     bibtexparser.dump(bib_db, bibtex_file, writer)


