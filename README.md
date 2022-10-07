# 676-assignment-1

GENERAL INFORMATION

Title of Dataset: File Metadata Manifest   
Author: Meghan Berry (megberry@umich.edu)   
Date Created: 2022-10-07
  
DATA & FILE OVERVIEW  
Data Source: https://github.com/morskyjezek/networked-services-labs  
File List:   
file-metadata-manifest.csv (manifest of files contained in networked-services-labs/data directory)  
Assignment1_MB.py (Python script used to generate the file manifest)
  
INFORMATION FOR: file-metadata-manifest.csv  
File Type: csv  
Date Created: 2022-10-07  
Number of rows: 49  
Number of metadata fields: 7
  
Field titles and descriptions:  
filename: name of the file including file extenstion  
absolute_path: the complete path to the file location  
extension: file format extension  
size: file size in bytes  
modify_datetime: date and time of last file modification, format YYYY-MM-DDTHH:MM:SS  
md5-checksum: MD5 checksum produced using Python hashlib module  
sha256_checksum SHA256 file checksom produced using Python hashlib module
