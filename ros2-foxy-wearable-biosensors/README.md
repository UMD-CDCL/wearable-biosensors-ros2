#  Wearable Biosensor Framework
<p align="center">
<img src="https://github.com/SMARTlab-Purdue/ros2-foxy-wearable-biosensors/blob/master/media/img/ros2_node_structure-1.jpg" width="700" >
</p>

Each package node follows a generalized structure as below figure. We categorized sensor data into three major types, using ROS 2 standard messages and separated per node. Hardware data indicates current battery levels and Bluetooth signal strength. Nodes publish raw data in real-time, with sampling rates based on the individual biosensor hardware specifications. 
Chunk data, collected per node with predefined lengths, provide end-users with a framework for downstream processing (e.g., feature engineering and \ac{ML} applications). 

# ROS2 Parameters
In each sensor node, there are three ROS 2 parameters (_Chuck_Enable_, _Chunk_Length_, _Sensor_Enable_).

1) _Sensor_Enable_:a boolean data type (i.e., _True_ or _False_).
2) _Chuck_Enable_: a boolean data type (i.e., _True_ or _False_).
3) _Chunk_Length_: a float data type to adjust data length per topic. 


# ROS2 Topics
Available topics depend on the individual biosensor hardware specifications. All package topic names follow the following format:
<p align="center">
```python
/biosensors/<sensor_name>/<data_name>
```
</p>

where the _biosensor_name_ is the official name of the targeted biosensors (e.g., _empatica_e4_)and _data_name_ is the biosignal type (e.g., _PPG_raw_ and _PPG_chunk_).