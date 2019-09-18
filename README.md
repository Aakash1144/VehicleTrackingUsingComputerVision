# VehicleTrackingUsingComputerVision
Suspicious Vehicle Tracking System is a Computer Vision Application that could be used to identify and track and suspicious vehicle .This system is useful in many fields like theft control, raid on migrant-smuggling vehicles

1.	Python Wrapper- this file is having below details:
a.	List of suspicious vehicle to tack
b.	Dictionary containing camera details


Details to Know before executing this application:
1. PythonWrapper.py is the file where the execution starts.
2. In this file we are using input image path variable "ipImgPath"(This would be the frame of the live/stored video footage coming from the CCTV camera installed at specified location with camera id as "ipCameraId").
3. "lisOfSuspiciousVehicles" is used to manage the list of suspicious vehicles which needs to be tracked through the cameras installed at different site locations.
4. "camera_dict" would be acting as data source to hold the details of camera like camera id and its location.(In enhanced version we can manage it by usinf SQL DB)
5. Function defined "vehicleDetector" is wrapper for actual code behind. which will make use of OpenCv library to localize the vehicle number plate and recognize the vehicle number. This vehicle number would be returned by the "vehicleDetector" function.
6. This vehicle number would then be checked in respect of the list of suspicious vehicles (i.e. "lisOfSuspiciousVehicles").
7. If the vehicle number returned by function is matching with any entry in "lisOfSuspiciousVehicles". Then system will log it into the output file(i.e present into the Output Folder).
8. Eventually output file will be having the below details:
CameraId	CameraLocation	Suspicious_Vehicle_Number	TimeStamp
9. Once the output file is generated system would be enhanced to process it further to find the pattern of vehicle detected by different cameras at different timestamps. And eventually this application can help us in knowing the route followed by the vehicle.


