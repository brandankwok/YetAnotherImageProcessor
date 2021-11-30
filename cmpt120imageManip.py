# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Brandan Kwok, Kyle Deliyannides
# Date: December 6th, 2021
# Description:

import cmpt120imageProjHelper
import numpy

def applyRed(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      pixel[1] = 0
      pixel[2] = 0
  return pixels

def applyGreen(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      pixel[0] = 0
      pixel[2] = 0
  return pixels

def applyBlue(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      pixel[0] = 0
      pixel[1] = 0
  return pixels

def applySepia(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      Red = pixel[0]
      Green = pixel[1]
      Blue = pixel[2]
      SepiaRed = (Red * .393) + (Green *.769) + (Blue * .189)
      SepiaGreen = (Red * .349) + (Green *.686) + (Blue * .168)
      SepiaBlue = (Red * .272) + (Green *.534) + (Blue * .131)
      if SepiaRed > 255:
         SepiaRed = 255
      if SepiaGreen > 255:
         SepiaGreen = 255
      if SepiaBlue > 255:
         SepiaBlue = 255
      pixel[0] = int(SepiaRed)
      pixel[1] = int(SepiaGreen)
      pixel[2] = int(SepiaBlue)
  return pixels

def applyWarm(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      Red = pixel[0]
      Blue = pixel[2]
      # Scale Red value up
      if Red < 64:
        ScaleUpRed = Red/64*80
      elif Red >= 64 and Red < 128:
        ScaleUpRed = (Red-64)/(128-64) * (160-80) + 80
      else:
        ScaleUpRed = (Red-128)/(255-128) * (255-160) + 160
      # Scale Blue value down
      if Blue < 64:
        ScaleDownBlue = Blue/64*50
      elif Blue >= 64 and Blue < 128:
        ScaleDownBlue = (Blue-64)/(128-64) * (100-50) + 50
      else:
        ScaleDownBlue = (Blue-128)/(255-128) * (255-100) + 100
      pixel[0] = ScaleUpRed
      pixel[2] = ScaleDownBlue
  return pixels

def applyCold(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      Red = pixel[0]
      Blue = pixel[2]
      # Scale Red value down
      if Red < 64:
        ScaleDownRed = Red/64*50
      elif Red >= 64 and Red < 128:
        ScaleDownRed = (Red-64)/(128-64) * (100-50) + 50
      else:
        ScaleDownRed = (Red-128)/(255-128) * (255-100) + 100
      # Scale Blue value up
      if Blue < 64:
        ScaleUpBlue = Blue/64*80
      elif Blue >= 64 and Blue < 128:
        ScaleUpBlue = (Blue-64)/(128-64) * (160-80) + 80
      else:
        ScaleUpBlue = (Blue-128)/(255-128) * (255-160) + 160
      pixel[0] = ScaleDownRed
      pixel[2] = ScaleUpBlue
  return pixels

def rotateLeft(pixels):
  newPixels = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

  for i in range(len(pixels)):
    row = pixels[i]
    row = row[::-1]
    for j in range(len(row)):
        newPixels[j][i] = row[j]

  return newPixels

def rotateRight(pixels):
  newPixels = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

  for i in range(len(pixels)):
    row = pixels[i]
    for j in range(len(row)):
      newPixels[j][len(pixels)-i-1] = row[j]

  return newPixels