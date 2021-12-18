import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        
        image_name = "img"+str(number)+".png"
        #method is used to save an image to any storage device
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("Snapshot Taken")

    #release the camera
    videoCaptureObject.release()
    
    #closes all the windows that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "sl.A-ZyXakidwwlf55PkdSUbbh-2Z0n_EfMbsc3PX3UerDoPOEnMDpnbL0OslZR2X6V23kzXWAikT-2T1RDRxSdWwE67ABJedLkf5SfCktXsb1YDGkepRQKISOd4EpyVsxMssp9KKE"
    file = image_name
    file_from = file
    file_to = "/Automation/"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("fileUploaded")

def main():
    while(True):
        if((time.time() - start_time)>= 60):
            name = take_snapshot()
            upload_file(name)

main()