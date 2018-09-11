import numpy as np
import cv2
import sys
from matchers import matchers
import time

class Stitch:
    def __init__(self, args):
        self.path = args

        fp = open(self.path, 'r')
        filenames = [each.rstrip('\r\n') for each in fp.readlines()]
        print(filenames)

        self.images = [cv2.resize(cv2.imread(each), (480, 320)) for each in filenames]
        self.cout = len(self.images)
        self.left_list, self.right_list, self.center_im = [], [], None
        self.matcher_obj = matchers()
        self.prepare_lists()

    def prepare_lists(self):
        print("Number of images : %d" % self.count)
        self.centerIdx = self.count/2
        print("Center index image : %d" % self.centerIdx)
        self.center_im = self.images[int(self.centerIdx)]
        for i in range(self.count):
            if (i <= self.centerIdx):
                self.left_list.append(self.images[i])
            else:
                self.right_list.append(self.images[i])
            print("Image lists prepared.")

    def leftshift(self):
        base = self.left_list[0]

        for left in self.left_list[1:]:
            H = self.matcher_obj.match(base, left, 'left')
            print("Homograph is : ", H)

            xh = np.linalg.inv(H)
            print("Inverse Homography :", xh)

            ds = np.dot(xh, np.array([base.shape[1], base.shape[0], 1]))
            ds = ds/ds[-1]
            print("final ds=>", ds)

            f1 = np.dot(xh, np.array([0, 0, 1]))
            f1 = f1/f1[-1]
            xh[0][-1] += abs(f1[0])
            xh[1][-1] += abs(f1[1])

            ds = np.dot(xh, np.array([base.shape[1], base.shape[0], 1]))
            offset_y = abs(int(f1[1]))
            offset_x = abs(int(f1[0]))
            d_size = (int(ds[0]) + offset_x, int(ds[1]) + offset_y)
            print("image d_size =>", d_size)

            temp = cv2.warpPerspective(base, xh, d_size)
            temp[offset_y:left.shape[0] + offset_y, offset_x:left.shape[1] + offset_x] = left
            base = temp

        self.leftImage = temp

    def rightshift(self):
        for each in self.right_list:
            H = self.matcher_obj.match(self.leftImage, each, 'right')
            print("Homograph :", H)

            temp_3d = np.dot(H, np.array([each.shape[1], each.shape[0], 1]))
            temp_3d = temp_3d / temp_3d[-1]
            d_size = (int(temp_3d[0]) + self.leftImage.shape[1], int(temp_3d[1]) + self.leftImage.shape[0])
            temp = cv2.warpPerspective(each, H, d_size)
            cv2.imshow("temp", temp)
            cv2.waitKey()

            temp = self.mix_and_match(self.leftImage, temp)
            print("temp shape" % temp.shape)
            print("self.leftimage shape=", self.leftImage.shape)

            self.leftImage = temp

    def mix_and_match(self, leftImage, warpedImage):
        img1_x, img1_y = leftImage.shape[:2]
        img2_x, img2_y = warpedImage.shape[:2]
        print(leftImage[-1, -1])

        t = time.time()
        black_l = np.where(leftImage == np.array([0, 0, 0]))
        black_wi = np.where(warpedImage == np.array([0, 0, 0]))
        print(time.time() - t)
        print(black_l[-1])

        for i in range(0, img1_x):
            for j in range(0, img1_y):
                try:
                    if (np.array_equal(leftImage[j, i], np.array([0, 0, 0])) and np.array_equal(warpedImage[j, i], np.array([0, 0, 0]))):
                        warpedImage[j, i] = [0, 0, 0]
                    else:
                        if(np.array_equal(warpedImage[j, i], [0, 0, 0])):
                            warpedImage[j, i] = leftImage[j, i]
                        else:
                            if not np.array_equal(leftImage[j, i], [0, 0, 0]):
                                # warp_b, warp_g, warp_r = warpedImage[j, i]
                                left_b, left_g, left_r = leftImage[j, i]
                                warpedImage[j, i] = [left_b, left_g, left_r]
                except:
                    pass

        return warpedImage


    def trim_left(self):
        pass

    def showImage(self, string=None):
        if string == 'left':
            cv2.imshow("left image", self.leftImage)
        elif string == "right":
            cv2.imshow("right Image", self.rightImage)
            cv2.waitKey()

if __name__ == '__main__':
    try:
        args = sys.argv[1]
    except:
        args = "txtlists/files1.txt"
    finally:
        print("Parameters : ", args)

    str = Stitch(args)
    str.leftshift()
    str.rightshift()
    print("Done")

    cv2.imwrite("test.jpg", str.leftImage)
    print("image written")
    cv2.destroyAllWindows()

