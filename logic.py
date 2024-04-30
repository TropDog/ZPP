import cv2
import numpy as np
from urllib.request import Request, urlopen
from fastapi import File, UploadFile
import shutil, os

#Function with hog algorithm
def count_people_on_img(file_name:str) -> int:
    path = file_name
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    boxes, weights = hog.detectMultiScale(gray, winStride = (5,20))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes: 
        # display the detected boxes in the colour picture
        cv2.rectangle(img, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
    new_path = str("transformed_" + path)
    print(new_path)
    cv2.imwrite(new_path, img)

    return len(boxes)

def count_people_on_img_from_url(url:str) -> int:
    req = Request(
    url=url, 
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    arr = np.asarray(bytearray(webpage), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'
    img = cv2.resize(img, (640, 640))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
 
    boxes, weights = hog.detectMultiScale(gray, winStride = (6,9))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes: 
        # display the detected boxes in the colour picture
        cv2.rectangle(img, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
        
    filename =  os.path.join(str(url), ".jpg")
    cv2.imwrite(filename, img)
    return len(boxes)

def save_images_and_count(files: list[UploadFile] = File(...)):
    result = []
    for file in files:
        file_path = os.path.join("C:\Studia\Lato\Programowanie\Zaawansowane programowanie\ZPP", file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        result.append({file.filename : count_people_on_img(file.filename)})
    return result

