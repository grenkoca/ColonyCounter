import sys
import numpy as np
from skimage.io import imread
from skimage.exposure import equalize_adapthist
from skimage.color import rgb2lab, gray2rgb, rgb2gray
from skimage.feature import canny
import matplotlib.pyplot as plt
from scipy.ndimage import binary_fill_holes, binary_erosion, binary_dilation
from skimage.morphology.selem import disk
from skimage.feature import blob_dog, blob_log, blob_doh
import warnings
warnings.simplefilter("ignore")

def detect_plate(image):
    """
    Crops to plate and outputs mask (assumes it was taken on a dark background)
    :param image:
    :return:
    """

    lab = rgb2lab(image)
    l = lab[:, :, 0]  # Lum is the only channel we really care about for plate segmentation
    edges = canny(l, 30)
    filled = binary_fill_holes(edges)
    eroded = binary_erosion(filled, disk(10))
    mask = binary_dilation(eroded, disk(10))  # This is the mask

    mask_area = np.count_nonzero(mask)
    plate_radius = np.sqrt(mask_area/np.pi)
    padded_plate_radius = plate_radius + 0.1 * plate_radius

    indices = np.argwhere(mask)
    center = np.mean(indices, axis=0)

    y_min = int(max(0, np.round(center[0] - padded_plate_radius)))
    y_max = int(min(image.shape[0], np.round(center[0] + padded_plate_radius)))
    x_min = int(max(0, np.round(center[1] - padded_plate_radius)))
    x_max = int(min(image.shape[1], np.round(center[1] + padded_plate_radius)))

    cropped_image = image[y_min:y_max, x_min:x_max, :]
    cropped_mask = mask[y_min:y_max, x_min:x_max]
    new_center = np.mean(np.argwhere(cropped_mask), axis=0)

    cropped_mask = binary_erosion(cropped_mask, structure=disk(50))

    return cropped_image, cropped_mask, new_center


def count_cells(image, show_blobs=False):
    image_gray = rgb2gray(image)
    image_gray = equalize_adapthist(image_gray)

    blobs_dog = blob_dog(image_gray, max_sigma=5, min_sigma=1, threshold=0.05)
    if show_blobs:
        blobs_dog[:, 2] = blobs_dog[:, 2] * np.sqrt(2)

        fig, ax = plt.subplots(1, 1)
        ax.imshow(image)
        for blob in blobs_dog:
            y, x, r = blob
            c = plt.Circle((x, y), r, color='r', linewidth=2, fill=False)
            ax.add_patch(c)
        ax.set_axis_off()

        plt.tight_layout()
        plt.show()

    return len(blobs_dog)


if __name__ == "__main__":
    fpath = "./sample_data/IMG_3722.jpg"  # TODO: replace with args
    original_image = imread(fpath)
    plate, mask, centroid = detect_plate(original_image)
    overlay = plate.copy()
    overlay[~mask] = [0, 0, 0]

    n_cells = count_cells(overlay)
    print("%i colonies were found." % n_cells)
