# CMPT 120 Yet Another Image Processer
# Authors: Brandan Kwok 301462230, Kyle Deliyannides 301459316
# Section: D300
# Date: December 6th, 2021
# Description: Module which contains all manipulation functions for the image processor.

import cmpt120imageProjHelper
import numpy


def applyRed(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the red values and sets Green and Blue values to zero in each pixel of the image
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Set the Green and Blue values to zero
            pixel[1] = 0
            pixel[2] = 0
    return pixels

def applyGreen(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the Green values and sets Red and Blue values to zero in each pixel of the image
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Set the Red and Blue values to zero
            pixel[0] = 0
            pixel[2] = 0
    return pixels

def applyBlue(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the Blue values and sets Red and Blue values to zero in each pixel of the image
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Set the Red and Green values to zero
            pixel[0] = 0
            pixel[1] = 0
    return pixels

def applySepia(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a warm brownish tone by calculating a weighted average of the original R/G/B values for each pixel
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Assign the RGB values
            Red = pixel[0]
            Green = pixel[1]
            Blue = pixel[2]
            # Use the Sepia formula to calculate new RGB values using the min function
            SepiaRed = min(((Red * .393) + (Green * .769) + (Blue * .189)), 255)
            SepiaGreen = min(((Red * .349) + (Green * .686) + (Blue * .168)), 255)
            SepiaBlue = min(((Red * .272) + (Green * .534) + (Blue * .131)), 255)
            # Assign the new RBG values to the original RGB values
            pixel[0] = int(SepiaRed)
            pixel[1] = int(SepiaGreen)
            pixel[2] = int(SepiaBlue)
    return pixels

def applyWarm(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a warm tone by scaling the original Red value up and the Blue value down using formulas
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Assign the Red and Blue values
            Red = pixel[0]
            Blue = pixel[2]
            # Scale Red value up
            if Red < 64:
                ScaleUpRed = Red / 64 * 80
            elif Red >= 64 and Red < 128:
                ScaleUpRed = (Red - 64) / (128 - 64) * (160 - 80) + 80
            else:
                ScaleUpRed = (Red - 128) / (255 - 128) * (255 - 160) + 160
            # Scale Blue value down
            if Blue < 64:
                ScaleDownBlue = Blue / 64 * 50
            elif Blue >= 64 and Blue < 128:
                ScaleDownBlue = (Blue - 64) / (128 - 64) * (100 - 50) + 50
            else:
                ScaleDownBlue = (Blue - 128) / (255 - 128) * (255 - 100) + 100
            # Assign the new Red and Blue values to the original Red and Blue values
            pixel[0] = ScaleUpRed
            pixel[2] = ScaleDownBlue
    return pixels

def applyCold(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a cold tone by scaling the original Red value down and the Blue value up using formulas
    """
    # Set the height and width for the image
    height = len(pixels)
    width = len(pixels[0])
    # Iterate through each pixel in the rows and columns
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            # Assign the Red and Blue values
            Red = pixel[0]
            Blue = pixel[2]
            # Scale Red value down
            if Red < 64:
                ScaleDownRed = Red / 64 * 50
            elif Red >= 64 and Red < 128:
                ScaleDownRed = (Red - 64) / (128 - 64) * (100 - 50) + 50
            else:
                ScaleDownRed = (Red - 128) / (255 - 128) * (255 - 100) + 100
            # Scale Blue value up
            if Blue < 64:
                ScaleUpBlue = Blue / 64 * 80
            elif Blue >= 64 and Blue < 128:
                ScaleUpBlue = (Blue - 64) / (128 - 64) * (160 - 80) + 80
            else:
                ScaleUpBlue = (Blue - 128) / (255 - 128) * (255 - 160) + 160
            # Assign the new Red and Blue values to the original Red and Blue values
            pixel[0] = ScaleDownRed
            pixel[2] = ScaleUpBlue
    return pixels

def rotateLeft(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns altered pixels - rotated 90 degrees left
    """
    # Creates new image with width and height flipped from original image
    newPixels = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

    for i in range(len(pixels)):
        # Iterates through each row of original image temporarily storing each row as variable 'row'
        row = pixels[i]
        for j in range(len(row)):
            # Iterates through each pixel of 'row' storing it in new image starting from bottom left corner
            newPixels[len(pixels[0]) - j - 1][i] = row[j]
    return newPixels

def rotateRight(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns altered pixels - rotated 90 degrees right
    """
    # Creates new image with width and height flipped from original image
    newPixels = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

    for i in range(len(pixels)):
        # Iterates through each row of original image temporarily storing each row as variable 'row'
        row = pixels[i]
        for j in range(len(row)):
            # Iterates through each pixel of 'row' storing it in new image starting from top right corner
            newPixels[j][len(pixels) - i - 1] = row[j]
    return newPixels

def sizeDouble(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a new image with width equal to 2*the original’s width and height equal to 2* the original’s height
    """
    # Set the original height and width for the image
    origheight = len(pixels)
    origwidth = len(pixels[0])
    # Set the new height and width for the new image
    doubleheight = len(pixels)*2
    doublewidth = len(pixels[0])*2
    # Creates new image with width and height doubled from original image
    newpixels = cmpt120imageProjHelper.getBlackImage(doublewidth, doubleheight)
    # Iterate through each pixel in the original rows and columns
    for r in range(origheight):
        for c in range(origwidth):
          origpixel = pixels[r][c]
          # Within the original image iterate through 2x2 pixels
          for i in range(2):
            for j in range(2):
                # Set each calculated 2x2 original pixel to one pixel in the new image
                newpixels[2*r+i][2*c+j] = origpixel
    return newpixels

def sizeHalf(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a new image with width equal to half the original width and height
            Each pixel of the new image will be the average of four adjacent pixels
    """
    # Checks is image can be halved - this is done to prevent a potential crash
    if len(pixels) > 2 or len(pixels[0]) > 2:
        # Creates black image 'newPixels' which has half the height and width of 'pixels'
        newPixels = cmpt120imageProjHelper.getBlackImage(len(pixels[0])//2, len(pixels)//2)
        # Iterates through each pixel in 'newPixels'
        for i in range(len(newPixels)):
           for j in range(len(newPixels[0])):
               # Assigns newPixel[i][j] to the average of the four adjacent pixels
                newPixels[i][j] = average(pixels, i, j)
        return newPixels
    else:
        print("Log: Error. Image too small to half the size.")
        return pixels

def average(pixels, i, j):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
            i - index of row (integer)
            j - index of column (integer)
    Output: Returns a list of RGB values for one pixel
            This pixel is calculated from four adjacent pixels in 'pixels' based off the indexes i and j
    """
    # variables a, b, c, and d are one pixel each.
    # each pixel is adjacent to one another, based off the indexes i and j
    a = pixels[i*2][j*2]
    b = pixels[i*2+1][j*2]
    c = pixels[i*2][j*2+1]
    d = pixels[i*2+1][j*2+1]
    # calculates the average RGB values of all four adjacent pixels and stores it in a list 'pixel'
    pixel = [(a[0]+b[0]+c[0]+d[0])//4, (a[1]+b[1]+c[1]+d[1])//4, (a[2]+b[2]+c[2]+d[2])//4]
    return pixel

def locateFish(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    """

    """"
    Initializes variables to the most extreme values they can be
    this essentially assumes that the top of the fish is the very bottom of the image,
    the bottom of the fish is the very top of the image, left is the very right, and right is the very left.
    """
    top = len(pixels)-1
    bottom = 0
    left = len(pixels[0])-1
    right = 0

    # Iterates through every pixel in the image
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            # Checks if the pixel at [i][j] is yellow in colour
            pixel = pixels[i][j]
            if isYellow(pixel):
                # If pixel is yellow, check to see if these pixels are the top, bottom, left, or right of fish
                # If it is, set respective variables to the indexes of the top, bottom, left, or right
                if top > i:
                    top = i
                if  bottom < i:
                    bottom = i
                if left > j:
                    left = j
                if right < j:
                    right = j
    # Calls drawBox function, passing it the image and the indexes of all four lines to be drawn
    # Stores result as pixels - replacing original image
    pixels = drawBox(pixels, top, bottom, left, right)
    # Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    return pixels

def isYellow(pixel):
    """
    Input:  pixel - list of RGB values
    Output: Returns 'True' or 'False' depending on whether pixel closely resembles yellow
    """
    # Splits list 'pixel' into separate rgb variables
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    # Converts pixels rgb values to hsv and stores as tuple 'hsv'
    hsv = cmpt120imageProjHelper.rgb_to_hsv(r, g, b)
    # Splits tuple 'hsv' into separate hsv variables
    h = hsv[0]
    s = hsv[1]
    v = hsv[2]
    # returns 'True' if hsv values are in range that is close to yellow
    # returns 'False' otherwise
    if ( (h>=45 and h<=65) and (s>=55 and s<=100) and (v>=60 and v<=100)):
        return True
    return False

def drawBox(pixels, top, bottom, left, right):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
            top - integer representing the row of the top line to be drawn
            bottom - integer representing the row of the bottom line to be drawn
            left - integer representing the column of the left line to be drawn
            right - integer representing the column of the right line to be drawn
    Output: Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    """
    # horizontalLength is the length of the two horizontal lines to be drawn
    horizontalLength = abs(left-right)
    # verticalLength is the length of the two vertical lines to be drawn
    verticalLength = abs(top-bottom)

    # Draws both horizontal lines
    for i in range(left, left+horizontalLength):
        pixels[top][i] = [0, 255, 0]
        pixels[bottom][i] = [0, 255, 0]
    # Draws both vertical lines
    for i in range(top, top+verticalLength):
        pixels[i][left] = [0, 255, 0]
        pixels[i][right] = [0, 255, 0]
    # Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    return pixels