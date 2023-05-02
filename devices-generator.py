import uuid
import base64
import random
import json

# Define the base camera object
camera = {
  "id": "",
  "name": "",
  "rtsp": "",
  "snapshot": "",
  "username": "user",
  "password": "pass"
}

# Define the base device object
device = {
  "id": "",
  "name": "",
  "username": "user",
  "password": "pass",
  "key": "",
  "cameras": []
}

# Generate 1000 random devices
devices = []
for i in range(1000):
  # Generate a new UUID for the device
  device_id = str(uuid.uuid4())

  # Generate a random device name
  device_name = f"Device {i+1}"

  # Generate a random encryption key
  key = base64.b64encode(bytes(random.getrandbits(8) for _ in range(16))).decode()

  # Create a new device object with the generated values
  new_device = device.copy()
  new_device["id"] = device_id
  new_device["name"] = device_name
  new_device["key"] = key

  # Generate random cameras for the device
  cameras = []
  for j in range(4):
    # Generate a new UUID for the camera
    camera_id = str(uuid.uuid4())

    # Generate a random camera name
    camera_name = f"Camera {j+1}"

    # Generate random RTSP and snapshot URLs
    rtsp_url = f"rtsp://user@pass:camera/{j+1}:554"
    snapshot_url = f"http://camera/{j+1}/snapshot.jpg"

    # Create a new camera object with the generated values
    new_camera = camera.copy()
    new_camera["id"] = camera_id
    new_camera["name"] = camera_name
    new_camera["rtsp"] = rtsp_url
    new_camera["snapshot"] = snapshot_url

    # Add the new camera to the list of cameras
    cameras.append(new_camera)

  # Add the cameras to the device object
  new_device["cameras"] = cameras

  # Add the new device to the list of devices
  devices.append(new_device)

with open('devices.json', 'w') as f:
  json.dump(devices, f)
