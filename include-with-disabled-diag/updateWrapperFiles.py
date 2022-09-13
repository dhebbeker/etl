import glob
import os
import os.path
from jinja2 import Template

listOfOldHeaders = glob.glob('etl/*.h') + glob.glob('etl/*.hpp')
for oldHeader in listOfOldHeaders:
    os.remove(oldHeader)

templateFileName = os.path.abspath('disable-diag-wrapper.template')
with open(templateFileName, "r") as templateFile:
    template = Template(templateFile.read())

listOfHeaders = [os.path.basename(x) for x in glob.glob('../include/etl/*.h') + glob.glob('../include/etl/*.hpp')]
for header in listOfHeaders:
    outputFileName = os.path.abspath('etl/' + header)
    with open(outputFileName, "w") as outputFile:
        outputFile.write(template.render(basename = header))
