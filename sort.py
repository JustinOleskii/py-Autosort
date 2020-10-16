import os
import glob
import shutil
from os import path

folderLocation = glob.glob(r"C:\Users\joash\Downloads\*")

documentExtensions = ['.pdf', '.docx', '.doc', '.ppt', '.txt']
mediaExtensions = ['.png', '.jpg', '.jpeg', 'mp4', '.PNG', '.mp4', '.mp3', '.svg']
applicationExtensions = ['.exe', '.msi']
compressedExtensions = ['.zip', '.7z', '.rar']
filesExtensions = ['.apk']

documentFolder = r"C:\Users\joash\Downloads\Documents"
mediaFolder = r"C:\Users\joash\Downloads\Media"
applicationFolder = r"C:\Users\joash\DownloadsApplications"
compressedFolder = r"C:\Users\joash\Downloads\Compressed"
filesFolder = r"C:\Users\joash\Downloads\Files"

for f in folderLocation:
    if os.path.splitext(f)[1] in documentExtensions:
        if(path.exists(documentFolder)):
            shutil.move(f, documentFolder)
        else:
            os.mkdir(documentFolder)
            shutil.move(f, documentFolder)
    
    if os.path.splitext(f)[1] in mediaExtensions:
        if(path.exists(mediaFolder)):
            shutil.move(f, mediaFolder)
        else:
            os.mkdir(mediaFolder)
            shutil.move(f, mediaFolder)

    if os.path.splitext(f)[1] in applicationExtensions:
        if(path.exists(applicationFolder)):
            shutil.move(f, applicationFolder)
        else:
            os.mkdir(applicationFolder)
            shutil.move(f, applicationFolder)

    if os.path.splitext(f)[1] in compressedExtensions:
        if(path.exists(compressedFolder)):
            shutil.move(f, compressedFolder)
        else:
            os.mkdir(compressedFolder)
            shutil.move(f, compressedFolder)

    if os.path.splitext(f)[1] in filesExtensions:
        if(path.exists(filesFolder)):
            shutil.move(f, filesFolder)
        else:
            os.mkdir(filesFolder)
            shutil.move(f, filesFolder)