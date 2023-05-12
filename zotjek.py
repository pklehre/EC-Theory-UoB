from pyzotero import zotero
import bibtexparser

zot = zotero.Zotero(library_id='4980316',library_type='group',api_key='Z6twDFkFD0lMq4gNPFv7bMNu')
zot.add_parameters(format='bibtex',style='abbrv')   # Change style as desired.
bib_db = zot.top()

with open('_bibliography/references.bib','w') as bibtex_file:
    bibtexparser.dump(bib_db, bibtex_file)