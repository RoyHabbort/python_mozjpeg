import os, magic, uuid, shutil, sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = './'

if len(sys.argv) > 2:
    quality = sys.argv[2]
else:
    quality = 75


def optimizeImage(originalPath):
    tmpFile = '/tmp/' + str(uuid.uuid4())
    command = '/opt/mozjpeg/bin/cjpeg -outfile ' + tmpFile + ' -quality 75 ' + '\'' + originalPath + '\' 2>&1'
    result = os.system(command)
    
    if result == 0:
        print('Complete optimize image ' + originalPath)
        shutil.copy2(tmpFile, originalPath)
        os.remove(tmpFile)
    else:
        print('Image optimization error')
        print(command)


def processDir(dir):
    count = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            fullFileName = os.path.join(root, file);
            mime = magic.Magic(mime=True)
            mimeType = mime.from_file(fullFileName)
            if mimeType == 'image/jpeg' : 
                print('Start optimize for ' + fullFileName)
                optimizeImage(fullFileName)
                count += 1

    print('Complete for ' + str(count) + ' images')


processDir(path)
