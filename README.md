# ros2-foxy-wearable-biosensors


This paper proposes a new wearable biosensor package for ROS 2 system that is capable of lowering technology entry barrier and expanding the biosensor ecosystem in the robotics field. The wearable type of the biosensors has advantages to develop real-world human-robot interaction (HRI) system since there are no behavioral constraints compared to wired devices. Each biosensor nodes in the package follows a generalized node structure and topic information for user to easily utilize the package. Additionally, we validate the published data from each nodes by comparing to outcomes of reference programs that manufacturer of each biosensor officially provide to read data. Later, we propose one of potential HRI applications applied the proposed package.

# Supported Biosensors (v0.0.1 updated on Sep. 7th 2021)
1) Empatica E4 wristband
2) Emotiv Insight
3) Shimmer3-GSR Unit+
4) Polar H10
5) Vernier Respiration Belt
6) Zephyr Bioharness
7) TBD (will be added new sensors on v0.0.2)



## Contributors
Wonse Jo, Jaeeun Kim, and Dr. Byung-Cheol Min are with [SMART Lab](http://www.smart-laboratory.org/index.html), Department of Computer and Information Technology, [Purdue University](https://www.purdue.edu/), West Lafayette, IN 47907, USA.<br />

<table>
  <tr>
      <td align="center"><a href="https://wonsu0513.github.io/"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/Wonse_Jo.png" width="200px;" alt=""/><br />
          <sub><b><a href="https://wonsu0513.github.io/" title="personal_website">🌍Wonse Jo</b></sub></a><br />
<sub><b>Ph.D. Candidate</b></sub></a><br />
<sub><b><a href="mailto: jow@purdue.edu" title="contact">jow@purdue.edu</a></b></sub></a><br />
</td>



<td align="center"><a href="http://www.smart-laboratory.org/group/Jaeeun_Kim.html"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/Jaeeun_Kim.jpg" width="200px;" alt=""/><br />
              <sub><b><a href="http://www.smart-laboratory.org/group/Jaeeun_Kim.html" title="personal_website">🌍Jaeeun Kim</b></sub></a><br />
<sub><b>Undergradute</b></sub></a><br />
<sub><b><a href="mailto: kim2592@purdue.edu" title="contact">kim2592@purdue.edu </a></b></sub></a><br />


<td align="center"><a href="http://www.smart-laboratory.org/group/bcm.html"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/Dr_Byung-Cheol_Min.png" width="200px;" alt=""/><br />
  <sub><b><a href="http://www.smart-laboratory.org/group/bcm.html" title="personal_website">🌍Dr. Byung-Cheol Min</b></sub></a><br />
<sub><b>Director</b></sub></a><br />
<sub><b><a href="mailto: minb@purdue.edu" title="contact">minb@purdue.edu</a></b></sub></a><br />
  </tr>
</table>


Dr. Robert Wilson, and Dr. Steve McGuire are with Department of Electrical and Computer Engineering, [University of California Santa Cruz](https://www.ucsc.edu/), Santa Cruz, CA 95064, USA.<br />


<table>
  <tr>
<td align="center"><a href="http://www.smart-laboratory.org/group/Wonse_Jo.html"><img src="http://www.smart-laboratory.org/group/Wonse_Jo.png" width="200px;" alt=""/><br />
          <sub><b><a href="http://www.smart-laboratory.org/group/Wonse_Jo.html" title="personal_website">🌍Dr. Robert Wilson</b></sub></a><br />
<sub><b>PostDoc. researcher</b></sub></a><br />
<sub><b><a href="mailto: jow@purdue.edu" title="contact">jow@purdue.edu</a></b></sub></a><br />
</td>


<td align="center"><a href="https://engineering.ucsc.edu/people/smcguire"><img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/Dr_Steve%20McGuire.jpeg" width="200px;" alt=""/><br />
          <sub><b><a href="https://engineering.ucsc.edu/people/smcguire" title="personal_website">🌍Dr. Steve McGuire</b></sub></a><br />
<sub><b>Director</b></sub></a><br />
<sub><b><a href="mailto: steve.mcguire@ucsc.edu" title="contact">steve.mcguire@ucsc.edu</a></b></sub></a><br />
  </tr>
</table>

# Acknowledgements
This  material  is  based  upon  work  supported  by  the  Na-tional  Science  Foundation  under  Grant  No.  IIS-1846221and  byUCSC  Grant  number.  Any  opinions,  findings,  andconclusions  or  recommendations  expressed  in  this  materialare those of the author(s) and do not necessarily reflect theviews of the National Science Foundation andUCSC Grantaffiliation.
