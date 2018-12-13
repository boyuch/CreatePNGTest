import unittest
from image_write_lib import *
import os

MY_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'




class TestImages(unittest.TestCase):
    """
    test class
    """
    def compare_images(self, img_fname1, img_fname2):
        """
        compare the two files
        """
        with open(img_fname1,'rb') as infile1, open(img_fname2, 'rb') as infile2:
            img1 = infile1.read()
            img2 = infile2.read()
        return img1 == img2


    def test_yellow(self):
        fname='img_my_yellow.png'
        build_image_yellow(MY_DIR + fname)
        ref_fname = 'img_yellow_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))


    def test_double_red_gradient (self):
        fname='img_my_double_red_gradient.png'
        build_image_double_red_gradient( MY_DIR + fname)
        ref_fname = 'img_red_gradient_double_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_single_red_gradient (self):
        fname='img_my_single_red_gradient.png'
        build_image_single_red_gradient(MY_DIR + fname)
        ref_fname = 'img_red_gradient_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_yellow_gradient_horizontal (self):
        fname='img_my_yellow_gradient_horz.png'
        build_image_yellow_gradient_horizontal(MY_DIR + fname)
        ref_fname = 'img_yellow_gradient_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_cyan_gradient_diagonal (self):
        fname='img_my_cyan_gradient_diag.png'
        build_image_cyan_gradient_diagonal(MY_DIR + fname)
        ref_fname = 'img_cyan_diagonal_gradient_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_green_gradient_inverted (self):
        fname='img_my_green_gradient_inv.png'
        build_image_green_gradient_diagonal_inverted(MY_DIR + fname)
        ref_fname = 'img_green_gradient_invert_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_red_bands_horizontal (self):
        fname='img_my_red_bands_horz.png'
        build_image_red_bands_horizontal(MY_DIR + fname)
        ref_fname = 'img_red_bands_horz_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_blue_bands_vertical (self):
        fname='img_my_blue_bands_vert.png'
        build_image_blue_bands_vertical(MY_DIR + fname)
        ref_fname = 'img_blue_bands_vert_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_plaid (self):
        fname='img_my_plaid.png'
        build_image_plaid_blue_and_red(MY_DIR + fname)
        ref_fname = 'img_plaid_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_banding_gradient (self):
        fname='img_my_banding_gradient.png'
        build_image_banding_with_gradient_red(MY_DIR + fname)
        ref_fname = 'img_banding_gradient_REF.png'
        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))

    def test_trophy_palette (self):
        # read the palette and build a dictionary
        palette_fname = 'HEADACHE.MAP.csv'
        palette_dict = build_palette_dictionary(MY_DIR + palette_fname)
        # print(palette_dict)

        # use that to build the image
        fname='img_my_palette.png'
        build_image_using_palette(MY_DIR + fname, palette_dict)
        ref_fname = 'img_palette_REF.png'
        # self.compare_images( MY_DIR + fname, MY_DIR + ref_fname)

        self.assertTrue(self.compare_images( MY_DIR + fname, MY_DIR + ref_fname))


if __name__ == '__main__':
    unittest.main()
