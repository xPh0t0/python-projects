import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFGsw_Md3rRIbkkIJV5PcFC77N0uDJRSGAHdcayWngdJo6HGN6Lqh7IvwFJDbnxszO0U9DPEd4ZZrO6GSSD3TgrDL0iopcAjytYg9yAMHLz9vbL1gqBLvXyWYKWg14fvSx3gpd0vH_1M'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("Your file has been successfully moved.")




main()
