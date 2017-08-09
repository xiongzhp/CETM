
# coding: utf-8

# # Extracting Solubility

# In[ ]:

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.doc import Paragraph, Heading


# In[5]:

d = Document(  
    Paragraph(u'The procedure was followed to yield a pale yellow solid Hippeastrine Hydrobromide. ( melting point of Amodiaquine is 137 °C)')
)


# In[6]:

d.records.serialize()


# In[37]:

from chemdataextractor.model import BaseModel, StringType, ListType, ModelType

class Solubility(BaseModel):
    value = StringType()
    units = StringType()
    
Compound.solubility = ListType(ModelType(Solubility))


# In[38]:

import re
from chemdataextractor.parse import R, I, W, Optional, merge

# prefix = (R(u'^m\.?p\.?$', re.I) | I(u'melting') + I(u'point')).hide()
prefix = (I(u'solubility')).hide() + Optional(W('=') | I('of') | I('was') | I('is') | I('at')).hide() + Optional(I('in') + I('the') + I('range') + Optional(I('of')) | I('about')).hide()

# delim = R(u'^[:;\.,]$')
value = R(u'^\d+(\.\d+)?$')(u'value')

units = (W(u'nM') | W(u'μM') | W(u'mM') | W(u'μg')| W(u'mg'))(u'units').add_action(merge)

so = (prefix + Optional(R('\w+\s\w+')).hide() + value + units)(u'so')

# units = (W(u'°') + Optional(R(u'^[CFK]\.?$')))(u'units').add_action(merge)
# value = R(u'^\d+(\.\d+)?$')(u'value')
# bp = (prefix + + value + units)(u'bp')


# In[39]:

from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first

class SoParser(BaseParser):
    root = so

    def interpret(self, result, start, end):
        compound = Compound(
            solubility=[
                Solubility(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound


# In[40]:

Paragraph.parsers = [SoParser()]


# In[42]:

d = Document(
    Heading(u'Synthesis of 2,4,6-trinitrotoluene (3a)'),
    Paragraph(u'The procedure was followed to yield a pale yellow solid (solubility is 28 mg/mL)')
)
d.records.serialize()


# In[12]:

d = Document.from_file("../../test1.htm")
d.records.serialize()


# In[ ]:



