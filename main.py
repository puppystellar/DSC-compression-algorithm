from datetime import datetime
from imgProcessing import imgProcessing
from shapeFinding import ShapeFinding
from codeProcessing import CodeProcessing
from encode2 import Encode
from decode import Decode
import datetime

# Choose dataset: drive PH2 Massachusetts
dataset = 'PH2'
# Preprocess the images
start = datetime.datetime.now()
imgProcessing(dataset)
end1 = datetime.datetime.now()
print('\n','imgprocessing time consuming:',end1-start)

# Search the set of shapes
mode = ShapeFinding(dataset)
end2 = datetime.datetime.now()
print('shapefinding time consuming:',end2-end1)
# Process the codebooks
CodeProcessing()
end3 = datetime.datetime.now()
print('codeprocessing time consuming:',end3-end2)
# Encoder
Encode(dataset, mode)
end4 = datetime.datetime.now()
print('encoding time consuming:',end4-end3)
# Decoder
# Decode()
#end5 = datetime.datetime.now()

print('\n','imgprocessing time consuming:',end1-start)
print('shapefinding time consuming:',end2-end1)
print('codeprocessing time consuming:',end3-end2)
print('encoding time consuming:',end4-end3)
print(mode)
# print('decoding time consuming:',end5-end4)