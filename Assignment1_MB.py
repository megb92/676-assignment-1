import os
from datetime import datetime
import hashlib
import csv

def get_checksum(filePath, checksum_type):
    '''This is a helper function to create a checksum. 
    In this example we will focus on MD5, which can be used to check data integrity.
    
    The filePath value argument be a string representing a valid path.
    The checksum_type argument should be a valid type of checksum.
    
    The function returns the string of characters for an MD5 or SHA256 checksum.
    The is function only allows you to create MD5 or SHA 256 and will result in an error for other types.'''
    checksum_type = checksum_type.lower().replace(' ','')

    with open(filePath, 'rb') as f: #rb = read binary
        bytes = f.read()
        if checksum_type == 'md5':
            hash_string = hashlib.md5(bytes).hexdigest()
        elif checksum_type == 'sha256':
            hash_string = hashlib.sha256(bytes).hexdigest()
        else:
            Raise('{} is not a hash function supported by this program. You must ask for MD5.')
    return hash_string

file_list = list()
for item in os.listdir(os.path.join(os.getcwd(),'data')):
    path = os.path.join('data', item)
    for folderName, subfolders, filenames in os.walk(path):
        for file in filenames:
            file_info = {
            'filename' : file,
            'absolute_path' : os.path.abspath(os.path.join(folderName, file)),
            'extension' : os.path.splitext(os.path.join(folderName, file))[1],
            'size' : os.path.getsize(os.path.join(folderName, file)),
            'modify_datetime' : datetime.strftime(datetime.fromtimestamp(os.path.getmtime(os.path.join(folderName, file))), "%Y-%m-%dT%H:%M:%S"),
            'md5_checksum' : get_checksum(os.path.join(folderName, file), 'md5'),
            'sha256_checksum' : get_checksum(os.path.join(folderName, file), 'sha256')
        }
            file_list.append(file_info)

#print(file_list)
headers = ['filename', 'absolute_path', 'extension', 'size', 'modify_datetime', 'md5_checksum', 'sha256_checksum']

with open('file-metadata-manifest.csv', 'w', newline="") as csvfile:
    fileManifest = csv.DictWriter(csvfile, fieldnames=headers)
    print('writing file manifest CSV')
    fileManifest.writeheader()
    for file in file_list:
        print('adding', file['filename'])
        fileManifest.writerow(file)
    print('Wrote manifest')