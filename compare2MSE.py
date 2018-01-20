from skimage.measure import structural_similarity as ssim
from xlwt import Workbook
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return m


wb = Workbook()
ws = wb.add_sheet("10vs10", cell_overwrite_ok=True)

path1 = "./MSE/c_normal_1/"
path2 = "./MSE/c_normal_2/"
images1 = []
images2 = []

for x in os.listdir(path1):
    if os.path.isfile(path1 + x):
        images1.append(path1 + x)

for x in os.listdir(path2):
    if os.path.isfile(path2 + x):
        images2.append(path2 + x)

print(images1)
print(images2)

for a in range(len(images1)):
    ws.write(4 * a, 0, "c_normal_1")
    ws.write(4 * a + 1, 0, "c_normal_2")
    ws.write(4 * a + 2, 0, "mse")
    ws.write(4 * a, 1, "img" + str(a))
    for b in range(len(images2)):
        img1 = cv2.imread(images1[a])
        img2 = cv2.imread(images2[b])

        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        mean_square_error = compare_images(img1_gray, img2_gray)
        # print(mean_square_error)

        ws.write(4 * a + 1, b + 1,  "img" + str(b))
        ws.write(4 * a + 2, b + 1, str(mean_square_error))

wb.save("./result_c_normal.xls")
