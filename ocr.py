# import cv2
# import pytesseract
#
# #pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#
# img=cv2.imread('stool.PNG')
# img=cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
# # print(pytesseract.image_to_string(img))
#
# # Detecting characters
# hIMG ,wIMG,_ = img.shape
# # print(pytesseract.image_to_boxes(img))
# boxes=pytesseract.image_to_boxes(img)
# for x,b in enumerate(boxes.splitlines()):
#  if x!=0:
#     b=b.split()
#     print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hIMG-y),(w,hIMG-h),(0,0,255),2)
#     cv2.putText(img,b[0],(x,hIMG-y+23),cv2.FONT_HERSHEY_TRIPLEX,1,(50,50,255),1)
#
#
#
# cv2.imshow('Result', img)
# cv2.waitKey(0)







from pytesseract import *
import argparse
import cv2

# We construct the argument parser
# and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image",
                required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-c", "--min-conf",
                type=int, default=0,
                help="minimum confidence value to filter weak text detection")
args = vars(ap.parse_args())

# We load the input image and then convert
# it to RGB from BGR. We then use Tesseract
# to localize each area of text in the input
# image
images = cv2.imread(args["image"])
rgb = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

# Then loop over each of the individual text
# localizations
for i in range(0, len(results["text"])):

    # We can then extract the bounding box coordinates
    # of the text region from the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]

    # We will also extract the OCR text itself along
    # with the confidence of the text localization
    text = results["text"][i]
    conf = int(results["conf"][i])

    # filter out weak confidence text localizations
    if conf > args["min_conf"]:
        # We will display the confidence and text to
        # our terminal
        print("Confidence: {}".format(conf))
        print("Text: {}".format(text))
        print("")

        # We then strip out non-ASCII text so we can
        # draw the text on the image We will be using
        # OpenCV, then draw a bounding box around the
        # text along with the text itself
        text = "".join(text).strip()
        cv2.rectangle(images,
                      (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)
        cv2.putText(images,
                    text,
                    (x+80, y+2 ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 1)

    # After all, we will show the output image
cv2.imshow("Image", images)
cv2.waitKey(0)
