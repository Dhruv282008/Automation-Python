import cv2
import time
import random
import dropbox

startTime = time.time()

def takePhoto():
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    number = random.randint(0, 99)

    while result:
        ret,frame = videoCaptureObject.read()
        imageName = "Image "+str(number)+".png"
        cv2.imwrite(imageName, frame)
        global startTime
        startTime = time.time()
        print(startTime)
        result = False
        
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return imageName

def uploadImage(imageName):
    access_token = "t4VhnyxseEMAAAAAAAAAASZxDJRC6LA16PLUEC4N5yZcNzMcsRVxKbeXWTE49nVq"
    file_from = imageName
    file_to = "/Security/"+file_from

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while True:
        print(str(time.time())+" Current Time")
        print(str(startTime)+" Start Time")
        print(str(time.time()-startTime)+" Difference In Time")

        if (time.time() - startTime >= 5):
            name = takePhoto()
            uploadImage(name)

main()
