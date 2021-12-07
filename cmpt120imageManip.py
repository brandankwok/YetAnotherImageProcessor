# CMPT 120 - Yet Another Image Processer
# Authors: Brandan Kwok 301462230, Kyle Deliyannides 301459316
# Section: D300
# Date: December 6th, 2021
# Description: Module which contains all manipulation options for the image processor.
# Project was created and tested on PyCharm

import cmpt120imageProjHelper
import numpy


def applyRed(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the red values and sets Green and Blue values to zero in each pixel of the image
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
            # Set the Green and Blue values to zero
            pixel[1] = 0
            pixel[2] = 0
    return pixels

def applyGreen(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the Green values and sets Red and Blue values to zero in each pixel of the image
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
            # Set the Red and Blue values to zero
            pixel[0] = 0
            pixel[2] = 0
    return pixels

def applyBlue(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns only the Blue values and sets Red and Blue values to zero in each pixel of the image
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
            # Set the Red and Green values to zero
            pixel[0] = 0
            pixel[1] = 0
    return pixels

def applySepia(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a warm brownish tone
            by calculating a weighted average of the original R/G/B values for each pixel
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
            # Split the RGB values
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            # Calculate new RGB values and assign back to the pixel
            pixel[0] = int(min(((red * .393) + (green * .769) + (blue * .189)), 255))
            pixel[1] = int(min(((red * .349) + (green * .686) + (blue * .168)), 255))
            pixel[2] = int(min(((red * .272) + (green * .534) + (blue * .131)), 255))
    return pixels

def applyWarm(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns a warm tone
            by scaling the original Red value up and the Blue value down using formulas
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
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
    Output: Returns a cold tone
            by scaling the original Red value down and the Blue value up using formulas
    """
    # Iterate through each pixel in the rows and columns
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
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
    Output: Returns a new image
            with width equal to 2*the original’s width and height equal to 2* the original’s height
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
               # Assigns the average RGB values of the four adjacent pixels from the original image
               # Variables pixelA-pixelD are the four adjacent pixels which in calculation of the average
               pixelA = pixels[i * 2][j * 2]
               pixelB = pixels[i * 2 + 1][j * 2]
               pixelC = pixels[i * 2][j * 2 + 1]
               pixelD = pixels[i * 2 + 1][j * 2 + 1]
               averageR = (pixelA[0]+pixelB[0]+pixelC[0]+pixelD[0])//4
               averageG = (pixelA[1]+pixelB[1]+pixelC[1]+pixelD[1])//4
               averageB = (pixelA[2]+pixelB[2]+pixelC[2]+pixelD[2])//4
               newPixels[i][j] = [averageR, averageG, averageB]

        return newPixels
    else:
        print("Log: Image too small.")
        return pixels

def locateFish(pixels):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Output: Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    """

    """"
    Initializes variables to the most extreme values they can be
    this essentially assumes that the top of the fish is the very bottom of the image,
    the bottom of the fish is the very top, left is the very right, and right is the very left.
    """
    top = len(pixels)-1
    bottom = 0
    left = len(pixels[0])-1
    right = 0
    foundYellow = False
    # Iterates through every pixel in the image
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixel = pixels[i][j]
            # Converts pixels rgb values to hsv and stores as tuple 'hsv'
            hsv = cmpt120imageProjHelper.rgb_to_hsv(pixel[0], pixel[1], pixel[2])
            # Checks if the pixel at [i][j] has hsv values are in range that is close to yellow
            # (this range is just arbitrary values I came up with)
            if int(hsv[0]) in range(50, 60) and int(hsv[1]) in range(50, 100) and int(hsv[2]) in range(70, 100):
                foundYellow = True
                # If pixel is yellow, check to see if these pixels are the top, bottom, left, or right of fish
                # If it is, set respective variables to the indexes of the top, bottom, left, or right
                if top > i:
                    top = i
                if bottom < i:
                    bottom = i
                if left > j:
                    left = j
                if right < j:
                    right = j

    # If no yellow is found in image, terminate function early
    # This check is done to prevent a crash that occurs if no yellow is found
    if not foundYellow:
        print("Log: No yellow detected in image.")
        return pixels

    # vertical is the length of the two vertical lines to be drawn
    vertical = bottom-top
    # Draws both vertical lines
    for i in range(top, top + vertical):
        pixels[i][left] = [0, 255, 0]
        pixels[i][right] = [0, 255, 0]

    # horizontal is the length of the two horizontal lines to be drawn
    horizontal = right-left
    # Draws both horizontal lines
    for i in range(left, left + horizontal):
        pixels[top][i] = [0, 255, 0]
        pixels[bottom][i] = [0, 255, 0]

    # Returns altered pixels - with a green (0, 255, 0) box drawn around the fish
    return pixels
