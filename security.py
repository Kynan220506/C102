import cv2
import time
import random
import dropbox

start_time = time.time

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        
        result = False
    return img_name

    print("Snapshot Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(img_name):
    access_token = "2XfyIjDzTs4AAAAAAAAAAX9EsBbrY0lqJYQ3Lz70NUtXgBP3ID3PsODKjWIF_F2L"
    file = img_name
    file_from = file
    file_to = "C:\\Users\\ryans\\Downloads"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()