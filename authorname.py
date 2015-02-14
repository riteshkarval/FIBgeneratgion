import PyPDF2 as pyPdf
from pyPdf import PdfFileReader
p = r'/home/ritesh/test.pdf'
pdf = PdfFileReader(file(p, 'rb'))
print pdf.documentInfo
print pdf.getNumPages()
info = pdf.getDocumentInfo()
'''
print str(info.author)
print str(info.creator)
print str(info.producer)
print str(info.title)
'''
content=""
content = pdf.getPage(33).extractText() + " \n"
#content = " ".join(content.replace(u"\xa0", u" ").strip().split())
#print content
string=str(content)
print string
