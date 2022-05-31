'''
1. url of the github link to download the smart items
2. wget --> downlaod the file
3. make the dst_folder_name called avocado
4. copy the contents of the folder avocado to a new folder
'''

import os
import wget
import zipfile

url = 'https://github.com/decentraland-scenes/avocado/raw/main/Avocado.zip'

wget.download(url)

def get_file_name(url):
    return url.split('/')[-1]

filename = get_file_name(url)
#Perform some tests here to check if its a directory:

dst_folder_name = filename.split('.zip')[0]
print ('/n dst_folder_name',dst_folder_name)

os.makedirs(dst_folder_name,exist_ok=True)
#check that the directory does not exist:

print (dst_folder_name)
with zipfile.ZipFile(filename,'r') as zip_ref:
    zip_ref.extractall(dst_folder_name)

#Add copy the contents from 1 folder to the other:
#Delete the old zip file:

filename = "Avocado.zip"
if os.path.exists(filename):
    os.remove(filename)
    print ('File deleted successfully')


src_folder = ""
dst_folder = ""
def copy_contents(src_folder,dst_folder):
    return None

copy_contents(src_folder,dst_folder)

## Call this function to the bash file and test it. Awesome work.
##How do we update the function here?
## Versioning