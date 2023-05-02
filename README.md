# IoT Challenge
Challenge for the IoT team's selection process.

# Description

At our company, we currently manage a fleet of 4000 cameras and 1000 Raspberry Pi 4 devices, where each device has 4 connected cameras. Our challenge is to efficiently manage this fleet of devices.

All device information is stored in a cloud-based system that can be accessed via a URL ([device_sample.json](https://raw.githubusercontent.com/eusouagabriel/desafio-iot/main/device_sample.json) is an example that you must use in your application) that requires a JSON file. This file contains information about the device and cameras needed to access the camera stream, both live and historical.

Your challenge is to develop an application that can receive this information and update it locally on the device for other applications to use. The device is running on Linux, and the architecture is ARM 64-bit. Additionally, you must explain the following points:

* The chosen storage technology and the reason behind the choice. As some keys are sent, explain how they will be kept secure.
* The technology used to receive information on the device.
* How this application can be updated.
* Testing, Docker configuration and CI/CD configuration are welcome.

Good luck!
