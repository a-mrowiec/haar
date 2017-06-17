import os

import cv2


def create_raw_data(indir, outdir, rescale=2):
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            img = cv2.imread(os.path.join(root, f), cv2.IMREAD_GRAYSCALE)
            new_img = cv2.resize(img, (int(img.shape[1] / rescale), int(img.shape[0] / rescale)))

            cv2.imwrite(os.path.join(outdir, f), new_img)


create_raw_data('positives-src', 'positives-src')
