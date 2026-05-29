# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is a Python-based application that automatically records student attendance using facial recognition technology. The system captures live video from a webcam, identifies registered users by comparing their faces with stored images, and records attendance with the current date and time.

## Features

* Real-time face recognition using a webcam
* Automatic attendance marking
* Student face database management
* Unknown person detection and alert system
* Attendance records stored in CSV format
* Duplicate attendance prevention for the same day
* User-friendly visual interface with face labels

## Technologies Used

* Python
* OpenCV
* DeepFace
* Pandas
* CSV File Handling

## System Workflow

1. Load registered student images from the database folder.
2. Capture live video from the webcam.
3. Detect and recognize faces using DeepFace.
4. Compare detected faces with registered student images.
5. If a match is found:

   * Display the student's name.
   * Record attendance with date and time.
6. If no match is found:

   * Display an "Unknown Person Detected" warning.
7. Store attendance records in the Attendance.csv file.

## Project Structure

FaceAttendanceSystem/

├── main.py

├── Attendance.csv

├── database/

│   ├── Student1.jpg

│   ├── Student2.jpg

│   └── Student3.jpg

└── venv/

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install required dependencies:

```bash
pip install opencv-python pandas deepface tf-keras
```

4. Add student images to the database folder.
5. Run the application:

```bash
python main.py
```

## Future Enhancements

* Firebase/MySQL integration
* Attendance dashboard
* Student ID support
* Attendance reports and analytics
* Anti-spoofing and liveness detection
* Email and notification services


