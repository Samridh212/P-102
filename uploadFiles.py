import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    print("Create A folder Named Filed Uploader In Desktop and put all your files in it , it will be automatically uploaded")
    access_token = 'BV7wJClDUCwAAAAAAAAAAYjd5jmEMCwKI_ek8_MkdqJS3_6p7z53eznmu8EKWMIW'
    transferData = TransferData(access_token)

    file_from = "C:\Users\Samridh Kesarwani\Desktop\FileUploader"
    file_to = "https://www.dropbox.com/home/Test" 

 
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()

