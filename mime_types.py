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

mime_list_of_types = list()
match = False

for items in range(elements):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_list_of_types.append({ext: mt})

for items_two in range(files):
    fname = input()  # One file name per line.

    if fname.find('.') != -1:
        extension = fname.split('.')[-1]

        for dictonary in mime_list_of_types:
            for key, value in dictonary.items():
                if key.lower() == extension.lower():
                    match = True
                    print(value)

    if match == False:
        print('UNKNOWN')

    elif match == True:
        match = False

# TODO: optimized script
