# Smart Attendance Monitoring System with Fingerprint and Face Recognition

This project implements a Smart Attendance Monitoring System that combines fingerprint and face recognition technologies to accurately mark and track attendance. The system offers a reliable, efficient, and user-friendly solution for attendance management, eliminating manual processes and proxy errors.

## Paper

Disabled read here

## Abstract

The Smart Attendance Monitoring System employs biometric verification through fingerprint and face recognition modules to simplify attendance tracking. By combining these technologies, the system achieves an accuracy of 83%. The project addresses the challenges of manual attendance marking, proxy errors, and report generation. The system is designed for educational institutions, corporate offices, and various other applications.

## Features

- Dual-layer biometric verification using fingerprint and face recognition.
- Efficient attendance marking and recording.
- Automated report generation.
- High accuracy in attendance tracking.

## Prerequisites

- Raspberry Pi (tested on Raspberry Pi 4 model B with 8GB RAM).
- Fingerprint optical reader module (R307 used in testing).
- Python 3.8+ (compatible with Raspberry Pi OS and Windows 10/11).
- Required Python libraries (opencv, numpy, pandas, etc.).

## Setup

1. Clone this repository to your Raspberry Pi or computer.
2. Install the necessary Python libraries using `pip install -r requirements.txt`.
3. Setup the hardware (Raspberry Pi, fingerprint module).
4. Customize settings and configurations in the code as required.

## Usage

1. Run the main script: `python attendance.py`.
2. Use the GUI to enroll new users and start marking attendance.
3. The system supports both single-level and parallel attendance marking.
4. Attendance records are automatically generated and stored in CSV format.

## Results

- Tested accuracy of face recognition: ~83%.
- Tested accuracy of fingerprint recognition: ~60% for correct fingerprints.
- Combined accuracy (weighted scheme): ~78.4%.

## Conclusion and Future Scope

The Smart Attendance Monitoring System offers an innovative approach to attendance tracking using dual-layer biometric verification. The system's accuracy and user-friendly features make it suitable for various applications, including education, corporate, and access control. Future improvements include enhancing attendance counting efficiency and integration with existing systems.
