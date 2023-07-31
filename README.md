# oak_cameras

After pull this package into your own ws, the following command needs to be run in order to work (some necessary depthai libraries for oak camera):
sudo apt-get install ros-noetic-depthai-ros

# launch tree
To launch a single camera, run command: roslaunch oak_cameras stereo_inertial_node.launch

For single camera: stereo_inertial_node.launch--->kira_preprocessing.launch--->kira_aruco.launch

With these, we are able to launch a single oak camera and add all point cloud filters except the cam_complementry one (used for multiple cameras). The aruco_code is also added.

# multiple cameras test
To test the launching of multiple cameras, run the command: roslaunch oak_cameras kira_oaks_test.launch

kira_oaks_test.launch--->kira_camera.launch

camera_config.yaml configures the id number of oak_pro and oak_wide cameras
