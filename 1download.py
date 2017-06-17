import os
import urllib.request

import cv2


def get_size(original_size):
    r = 100.0 / original_size[1]
    return (100, int(original_size[0] * r))


def store_raw_images(neg_images_link, pic_num=1):
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/rawdata-tmp/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/rawdata-tmp/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, get_size(img.shape))
            cv2.imwrite("neg/rawdata-remote/" + str(pic_num) + ".bmp", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

    return pic_num


pic_num = store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03449564')
# pic_num = 299
store_raw_images("http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02914991", pic_num)
