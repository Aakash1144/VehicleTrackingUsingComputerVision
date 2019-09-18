# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:21:04 2019

@author: H355231
"""

import Main
import pandas as pd
import csv
import datetime

ipImgPath="LicPlateImages/5.png"
ipCameraId='1'
lisOfSuspiciousVehicles=['abc','1234']
camera_dict={'1':'Bellandur','2':'BTM','3':'HSR'}


def vehicleDetector(ipImgPath):
    
    vehicleNumber=Main.main1(ipImgPath)


    if vehicleNumber in lisOfSuspiciousVehicles:
        print(ipCameraId)
        print(camera_dict.get(ipCameraId))
        row=[ipCameraId,camera_dict.get(ipCameraId),vehicleNumber,datetime.datetime.now()]
        with open('C:/Users/H355231/Documents/Python Scripts/PythonScript3/OpenCV_3_License_Plate_Recognition_Python-master/OpenCV_3_License_Plate_Recognition_Python-master/Output/Output.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()