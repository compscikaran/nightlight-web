import numpy as np
import exifread
import rawpy
import imageio

# Convert Bayer to 4 channel RGBa image
def pack_raw(raw, black_level):
    # pack Bayer image to 4 channels
    im = raw.raw_image_visible.astype(np.float32)
    im = np.maximum(im - black_level, 0) / (16383 - black_level)  # subtract the black level
    im = np.expand_dims(im, axis=2)
    img_shape = im.shape
    H = img_shape[0]
    W = img_shape[1]
    return np.concatenate((im[0:H:2, 0:W:2, :],im[0:H:2, 1:W:2, :],
                        im[1:H:2, 1:W:2, :],im[1:H:2, 0:W:2, :]), axis=2)


# Works only on dng files taken using lightroom app
def dng_blacklevel(file):
    f = open(file, 'rb')
    tags = exifread.process_file(f)
    return tags['Image Tag 0xC61A'].values[0].num

# General Method to Calculate Black Level
def calculate_black_level(filename):
    if filename.endswith('.dng'):
        black_level = dng_blacklevel(filename)
    elif filename.endswith('.ARW'):
        black_level = 512
    else:
        raise Exception('File format not supported')
    return black_level

# Render out raw file to .png
def render_raw(image, savename):
    im = rawpy.imread(image)
    rgb = im.postprocess(use_camera_wb=True, half_size=False, no_auto_bright=True, output_bps=8)
    imageio.imwrite(savename, rgb)