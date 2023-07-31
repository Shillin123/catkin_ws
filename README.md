# oak_cameras
After pull this package into your own ws, the following command needs to be run in order to work (some necessary depthai libraries for oak camera):
sudo apt-get install ros-noetic-depthai-ros
# launch tree
For single camera: stereo_inertial_node.launch--->kira_preprocessing.launch--->kira_aruco.launch
