import cv2
import numpy
import math
from PIL import Image, ImageEnhance

# =================CONVERT================
def CV2_to_PIL_img(cv2_im):
    """
    Convert Opencv's BGR image to PIL image

    Input:
    --------
        cv2_im: Opencv's BGR

    Output: 
    --------
        PIL Image
    """

    cv2_im = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im)
    return pil_im


def PIL_to_CV2_img(img):
    """
    Convert PIL image to Opencv's BGR image

    Input:
    --------
        img: PIL Image

    Output: 
    --------
        Opencv's BGR Image
    """
    cv_image = numpy.array(img.convert('RGB')) 
    cv_image = cv_image[:, :, ::-1].copy() 
    return cv_image
# ========================================



# =========POLYNOMIAL FUNCTIONS===========
def first_polynomial_function(image):
    """
    Implementation of first polynomial function.

    Input:
    --------
        image: Opencv's BGR Image

    More detail at `Documentation.pdf`
    """

    table = numpy.array([1.657766*i-0.009157128*(i**2) + 0.00002579473*(i**3)
		for i in numpy.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


def second_polynomial_function(image):
    """
    Implementation of second polynomial function.

    Input:
    --------
        image: Opencv's BGR Image
    
    More detail at `Documentation.pdf`
    """

    table = numpy.array([
		-4.263256 * math.exp(-14)+1.546429*i-0.005558036*(i**2)+0.00001339286*(i**3)
		for i in numpy.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
# ========================================



# ===========GAMMA CORRECTION ============
def adjust_gamma(image, gamma=1.0):
    """
    Implementation of gamma correction

    Input:
    --------
        image: Opencv's BGR Image
    
    More detail at `Gamma-Correction.pdf`
    """
	
    invGamma = 1.0 / gamma
    table = numpy.array([((i / 255.0) ** invGamma) * 255
		for i in numpy.arange(0, 256)]).astype("uint8")
		    
    return cv2.LUT(image, table)
# ========================================



# =========CONTRAST & BRIGHTNESS==========
def enhance_contrast(image, factor=1.4):
    """
    Enhance contrast base on PIL->ImageEnhance.
    Default suitable factor is 1,4.

    Input:
        image: Opencv's BGR Image
        factor: contrast's factor
    
    Output:
        Enhanced contrast BGR image
    """

    _image = ImageEnhance.Contrast(
        CV2_to_PIL_img(image)
    ).enhance(factor)
    
    return PIL_to_CV2_img(_image)
# ========================================

# =================METHODS================
def reduce_glare(image):
    """
    Mixed 4 filter:
        1. First polynomial function
        2. Gamma correction: g = 0.75
        3. Second polynomial function
        4. Gamma correction: g = 0.8

    Input: BGR Image.\n
    Output: Reduce glare.
    """
    _image = adjust_gamma(
        second_polynomial_function(
            adjust_gamma(
                first_polynomial_function(image), 
                0.75
            )
        ),
        0.8
    )
    return _image


def mix_filter(image):
    """
    Mixed 4 steps:
        1. Reduce glare
        2. Enhance contract: f = 1.6
        3. Reduce glare
        4. Enhance contract: f = 1.4

    Input: BGR Image.\n
    Output: Reduced glare & clearly image.
    """
    _image = enhance_contrast(
        reduce_glare(
            enhance_contrast(
                reduce_glare(image), 
                factor=1.6
            )
        ), 
        factor=1.4
    )
    return _image
# ========================================