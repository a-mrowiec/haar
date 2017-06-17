import os

import cv2


def get_size(original_size):
    r = 100.0 / original_size[1]
    return (100, int(original_size[0] * r))


def rescale_string(input, r):
    return str(int(int(input) * r))


def change_extension_to(path, dest_extension):
    return os.path.splitext(path)[0] + dest_extension


def create_raw_data(indir, outdir, rescale=True):
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            img = cv2.imread(os.path.join(root, f), cv2.IMREAD_GRAYSCALE)
            if rescale:
                new_img = cv2.resize(img, get_size(img.shape))
            else:
                new_img = img
            new_f = change_extension_to(f, '.bmp')  # os.path.splitext(f)[0] + '.bmp'
            cv2.imwrite(os.path.join(outdir, new_f), new_img)


def create_scaled_info(indir, outdir):
    with open(outdir + '/info.txt', 'w') as outfile:
        with open(indir + '/info.txt') as infile:
            for line in infile:
                elements = line.split()
                path_to_image = os.path.join(indir, elements[0])
                orig_image = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)
                original_size = orig_image.shape
                r = 100.0 / original_size[1]
                elements[0] = change_extension_to(elements[0], '.bmp')
                elements[2] = rescale_string(elements[2], r)
                elements[3] = rescale_string(elements[3], r)
                elements[4] = rescale_string(elements[4], r)
                elements[5] = rescale_string(elements[5], r)

                outfile.write(' '.join(elements) + '\n')


create_raw_data('positives-src', 'positives/rawdata')
create_scaled_info('./positives-src', './positives/rawdata')
create_raw_data('neg-src', 'neg/rawdata-ii')
create_raw_data('neg', 'neg/rawdata-remote', False)
