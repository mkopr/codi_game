'''
extensions

png image/png
TIFF image/TIFF
css text/css
TXT text/plain
'''

'''
files

example.TXT
referecnce.txt
strangename.tiff
resolv.CSS
matrix.TiFF
lanDsCape.Png
extract.cSs
'''

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

elements = 4  # Number of elements which make up the association table.
files = 7  # Number Q of file names to be analyzed.

match = False
mime = {}

for item in range(elements):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime[ext.lower()] = mt

for item in range(files):
    fname = input()  # One file name per line.

    if fname.find('.') != -1:
        extension = fname.split('.')[-1]
        print(mime.get(extension.lower(), 'UNKNOWN'))

    else:
        print('UNKNOWN')
