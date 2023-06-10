import cv2
import numpy as np


def cartoonify(img_path: str, save_path: str) -> None:
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if img is None:
        print('Image reading error!')
        exit(-1)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.medianBlur(gray_img, 5)

    edges = cv2.adaptiveThreshold(
        gray_img,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    filtered_img = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon_img = cv2.bitwise_and(filtered_img, filtered_img, mask=edges)

    cv2.imwrite(save_path, cartoon_img)


if __name__ == '__main__':
    path = input('image path: ')
    save_path = input('image save path: ')
    cartoonify(path, save_path=save_path)
