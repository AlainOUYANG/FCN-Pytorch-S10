# -*- coding:utf8 -*-
import glob
import cv2
import os

# To save cutted subImgs, change SAVE to True
SAVE=False
DATA_PATH='/Users/Ouyangzuokun/Projet_s10/depth/*.bmp'
SAVE_PATH='./Rebuild_DB/cut_depth/'

# cut Image into 100x100-pixel subImgs with a stride of 50 pixel
def cutImg(Image):
    [X, Y] = Image.shape
    subImgs = []
    # print('X=' + str(X) + '; Y=' + str(Y) + '; X//50=' + str(X//50) + '; Y//50=' + str(Y//50))
    for j in range(0, Y-51, 50):
        for i in range(0, X-51, 50):
            if ((i // 50 < (X-51) // 50) and (j // 50 < (Y-51) // 50)):
                subImgs.append(Image[i : i + 100, j : j + 100])
            elif ((i // 50 < (X-51) // 50) and (j // 50 == (Y-51) // 50)):
                subImgs.append(Image[i : i + 100, Y - 100 : Y])
            elif ((i // 50 == (X-51) // 50) and (j // 50 < (Y-51) // 50)):
                subImgs.append(Image[X - 100 : X, j : j + 100])
            else:
                subImgs.append(Image[X - 100 : X, Y - 100 : Y])

    return subImgs

# displays all the subImgs
def showCutImgs(subImgs):
    for i in range(len(subImgs)):
        cv2.imshow(str(i), subImgs[i])
    cv2.waitKey(0)

# displays the subImgs contain enough information > 50%
def showCutImgsValuable(subImgs):
    threshold = 0.5 * 2550000
    for i in range(len(subImgs)):
        subImgSum = cv2.sumElems(subImgs[i])
        if (subImgSum[0] >= threshold):
            cv2.imshow(str(i+1), subImgs[i])
    cv2.waitKey(0)

# save cutted subImgs
def saveCutImgs(subImgs, dir_path):
    for i in range(len(subImgs)):
        cut_dir_path = dir_path.split('.')[0]
        nameImg = cut_dir_path.split('/')[-1] + '_' + str(i) + '.bmp'
        dir_path_save = SAVE_PATH + cut_dir_path.split('/')[-1] + '/'
        Imgs_dir_save = SAVE_PATH + cut_dir_path.split('/')[-1] + '/' + nameImg
        if not os.path.exists(dir_path_save):
            os.makedirs(dir_path_save)
        cv2.imwrite(Imgs_dir_save, subImgs[i])


def main():
    dir_path =  DATA_PATH    # The images' paths
    Imgs = []
    # Read all images under the directory
    imgs_path = glob.glob(dir_path)
    for path in imgs_path:
        Imgs.append(cv2.imread(path, 0))

    # To display all cutted subImgs, uncomment next line
    # showCutImgs(cutImg(Imgs[0]))

    # To display cutted subImgs with enough information, uncomment next line
    # showCutImgsValuable(cutImg(Imgs[0]))

    # If SAVE = True, save the cutted subImgs
    if SAVE:
        for path in imgs_path:
            saveCutImgs(cutImg(Imgs[imgs_path.index(path)]), path)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
