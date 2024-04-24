# wearable-biosensors-ros2

This repo is a modification of the https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors. 

Following are the modifications.

1.Dockerized the whole thing.

2.Added the device name for the vernier respiration belt and the MAC ID of the polar h10.

3.Added the custom cdcl_umd_msgs message type and used the Vitals.msg to publish hr and bpm, this message type includes data along with its time stamp.

# Instructions to run

Setup the USB driver

Create a file call vstlibusb.rules and put it in /etc/udev/rules.d. Add the following lines to that file
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="08f7", MODE="0666"
SUBSYSTEM=="usb_device", ATTRS{idVendor}=="08f7", MODE="0666"
```
 
Tutorial links on how to use the devices

[Vernier Respiration Belt](https://www.vernier.com/video/measure-respiration-rate-using-go-directrespiration-belt/)

[Polar h10](https://www.youtube.com/watch?v=vw0WV-PWtcw)


For building the docker container
After cloning the repo,navigate to the cdcl:humble-jammy-biosensors folder and run the build.sh script
```bash
./build.sh
```

For running the docker container, run the run.sh script 
```bash
./run.sh
```

To open a new terminal, run the exec.sh script
```bash
./exec.sh
```

# Insider the docker container

Once you are inside the docker container, navigate to the cdcl_ws
```bash
cd /home/cdcl/cdcl_ws
source install/setup.bash
```
Then you can run the vernier belt as well as the polar h10.

For vernier respiration belt
```bash
ros2 run vernier_respiration_belt vernier_respiration_belt_node
```
** This might fail sometimes, try to run this again to make it work.


You can also use the launch file to run the device
```bash
ros2 launch vernier_respiration_belt ros2-vernier_respiration_belt.launch.py
```

To view bpm data,

```bash
ros2 topic echo /biosensors/vernier_respiration_belt/bpm
```

For polar h10,
You will have to connect the polar h10 to your laptop manually via bluetooth

```bash
ros2 run polar_h10 polar_h10_node
```
In case of failures, turn the bluetooth OFF and ON or even try forgetting the device and pair it again and run the above node again.

You can also use the launch file to run the device
```bash
ros2 launch polar_h10 ros2-polar_h10.launch.py
```
 
To view hr data,

```bash
ros2 topic echo /biosensors/polar_h10/hr
```

You can view the below screen recording for reference

[Screen recording for running docker and sensors](https://drive.google.com/file/d/14l6fuuWFUu5sC5KvVBY2Smud53hI5ljI/view?usp=sharing)

For more details refer the below document

[Biosensors Usage](https://docs.google.com/document/d/1ji_ld5PAxg2iyJmVmD80gJB9F_bvRxsRa4P2T5g4Mi4/edit?usp=sharing)

# Original REAMDE
# ros2-foxy-wearable-biosensors


<p align="center">
<img src="/media/img/ros2_biosensor_pkg.png" width="700" >
</p>


Wearable biosensors enable continuous human data capture, facilitating the development of real-world Human-Robot Interaction (HRI) systems. However, a lack of standardized libraries and implementations add extraneous complexity to HRI system designs, and preclude collaboration across disciplines and institutions. Here, we propose a novel wearable biosensor package for the Robot Operating System 2 (ROS 2). The package standardizes biosensor HRI integration, lowers the technical barrier of entry, and expands the biosensor ecosystem in the robotics field. Each biosensor package node follows a generalized node and topic structure concentrated on ease of use. Current package capabilities, listed by the biosensor, highlight package standardization. Collected example data demonstrates integration of each biosensor into ROS 2. Standardization of a biosensors package for ROS 2 will greatly simplify use and cross-collaboration across many disciplines.



# Requirements
* ROS2 foxy
* Install [Emotiv App](https://www.emotiv.com/my-account/downloads/)
* Install [Emaptica E4 streaming server](https://developer.empatica.com/windows-streaming-server-usage.html) on an additional Window machine (Win10)
* Install python libraries:
```bash
$ pip3 install open-e4-client pexpect websocket-client
```

# Installation
```bash
$ cd ~
$ source /opt/ros/foxy/setup.bash
$ git clone https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors.git
$ cd ros2-foxy-wearable-biosensors
$ colcon build --symlink-install
$ source install/setup.bash
```

# Supported Wearable Biosensors 

## v0.0.1, updated on Sep.11th 2021.

1) [Empatica E4 wristband](ros2-foxy-wearable-biosensors/empatica_e4)
2) [Emotiv Insight](/ros2-foxy-wearable-biosensors/emotiv_insight)
3) [Shimmer3-GSR Unit+](/ros2-foxy-wearable-biosensors/shimmer3_gsr)
4) [Polar H10](/ros2-foxy-wearable-biosensors/polar_h10)
5) [Vernier Respiration Belt](/ros2-foxy-wearable-biosensors/vernier_respiration_belt)
6) [Zephyr Bioharness](/ros2-foxy-wearable-biosensors/zephyr-ros-master)
7) TBD (will be added new sensors on v0.0.2)


## Contributors
Wonse Jo, Jaeeun Kim, and Dr. Byung-Cheol Min are with [SMART Lab](http://www.smart-laboratory.org/index.html), Department of Computer and Information Technology, [Purdue University](https://www.purdue.edu/), West Lafayette, IN 47907, USA.<br />

<table>
  <tr>
<td align="center"><a href="https://www.purdue.edu/"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Purdue_University_seal.svg/150px-Purdue_University_seal.svg.png" width="100px;" alt=""/><br />
         </a><br />
<sub><b>Purdue University</b></sub></a><br />
<sub><b> </b></sub></a><br />
</td>


<td align="center"><a href="https://wonsu0513.github.io/"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/contributors/Wonse_Jo.png" height="200px;" alt=""/><br />
          <sub><b><a href="https://wonsu0513.github.io/" title="personal_website">🌍Wonse Jo</b></sub></a><br />
<sub><b>Ph.D. Candidate</b></sub></a><br />
<sub><b><a href="mailto: jow@purdue.edu" title="contact">jow@purdue.edu</a></b></sub></a><br />
</td>



<td align="center"><a href="http://www.smart-laboratory.org/group/Jaeeun_Kim.html"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/contributors/Jaeeun_Kim.jpg" height="200px;" alt=""/><br />
              <sub><b><a href="http://www.smart-laboratory.org/group/Jaeeun_Kim.html" title="personal_website">🌍Jaeeun Kim</b></sub></a><br />
<sub><b>Undergradute</b></sub></a><br />
<sub><b><a href="mailto: kim2592@purdue.edu" title="contact">kim2592@purdue.edu </a></b></sub></a><br />
</td>


<td align="center"><a href="http://www.smart-laboratory.org/group/bcm.html"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/contributors/Dr_Byung-Cheol_Min.png" height="200px;" alt=""/><br />
  <sub><b><a href="http://www.smart-laboratory.org/group/bcm.html" title="personal_website">🌍Dr. Byung-Cheol Min</b></sub></a><br />
<sub><b>Director</b></sub></a><br />
<sub><b><a href="mailto: minb@purdue.edu" title="contact">minb@purdue.edu</a></b></sub></a><br />
</td>

  </tr>
</table>


Dr. Robert Wilson, and Dr. Steve McGuire are with HARE Lab, Department of Electrical and Computer Engineering, [University of California Santa Cruz](https://www.ucsc.edu/), Santa Cruz, CA 95064, USA.<br />


<table>
  <tr>
<td align="center"><a href="https://www.ucsc.edu/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/The_University_of_California_1868_UCSC.svg/150px-The_University_of_California_1868_UCSC.svg.png" width="100px;" alt=""/><br />
         </a><br />
<sub><b>University of California,</b></sub></a><br />
<sub><b> Santa Cruz</b></sub></a><br />
</td>

<td align="center"><a href="https://engineering.ucsc.edu/people/smcguire"><img src="/media/contributors/Dr_Robert_Wilson.png" height="200px;" alt=""/><br />
                    <sub><b><a href="https://engineering.ucsc.edu/people/smcguire" title="personal_website">🌍Dr. Robert Wilson</b></sub></a><br />
<sub><b>PostDoc. researcher</b></sub></a><br />
<sub><b><a href="mailto: robert.wilson@ucsc.edu" title="contact">robert.wilson@ucsc.edu</a></b></sub></a><br />
</td>


<td align="center"><a href="https://engineering.ucsc.edu/people/smcguire"><img src="/media/contributors/Dr_Steve%20McGuire.jpeg" height="200px;" alt=""/><br />
          <sub><b><a href="https://engineering.ucsc.edu/people/smcguire" title="personal_website">🌍Dr. Steve McGuire</b></sub></a><br />
<sub><b>Director</b></sub></a><br />
<sub><b><a href="mailto: steve.mcguire@ucsc.edu" title="contact">steve.mcguire@ucsc.edu</a></b></sub></a><br />
</td>

  </tr>
</table>

(TBD) We are looking for new contributors to expand the biosensor ecosystem on ROS 2 environment. Please contact us if you are interested.


<table>
  <tr>
<td align="center"><a href="https://www.ucsc.edu/"><img src="/media/contributors/TBD_Contributors.png" width="150px;" alt=""/><br />
         </a><br />
<sub><b></b></sub></a><br />
<sub><b></b></sub></a><br />
</td>

<td align="center"><a href="https://engineering.ucsc.edu/people/smcguire"><img src="/media/contributors/TBD_Contributors.png" width="150px;" alt=""/><br />
          <sub><b><a href="http://www.smart-laboratory.org/group/Wonse_Jo.html" title="personal_website">🌍TBD</b></sub></a><br />
<sub><b>(TBD)position</b></sub></a><br />
<sub><b><a href="mailto: TBD@TBD.COM" title="contact">TBD@TBD.COM</a></b></sub></a><br />
</td>


<td align="center"><a href="https://engineering.ucsc.edu/people/smcguire"><img src="/media/contributors/TBD_Contributors.png" width="150px;" alt=""/><br />
          <sub><b><a href="http://www.smart-laboratory.org/group/Wonse_Jo.html" title="personal_website">🌍TBD</b></sub></a><br />
<sub><b>(TBD)position</b></sub></a><br />
<sub><b><a href="mailto:TBD@TBD.COM" title="contact">TBD@TBD.COM</a></b></sub></a><br />
</td>

</tr>
</table>

# Acknowledgements
<img align="right" height="100" src="https://user-images.githubusercontent.com/31596980/132916706-0a88c07a-1624-4bd1-bb1d-0da9c2930feb.png">
<img align="right" height="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/NSF_logo.png/220px-NSF_logo.png">

This material is based upon work supported by the National Science Foundation under Grant No. IIS-1846221 and by DARPA under grant HR0011-18-2-0043. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation or DARPA.
