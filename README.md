# Teleopkeys Keystroke Publisher for ROS 2

Simple node that detects keystrokes from certain keys and interprets them as commands to move robots. It publishes them to the topic '/teleopkeys' as messages of the type [String](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/String.html).

## How to Run

To run this note, you need to install [ROS 2](https://docs.ros.org/en/humble/Installation.html) (Humble is the latest distribution at the time of writing) and [setup the workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).

After everything is setup, run the following commands inside your ROS 2 workspace folder to clone the repository:

```
cd src/
git clone https://github.com/FilipeAlmeidaFEUP/ros2_teleopkeys_publisher.git
```

Again inside the workspace folder, to build and install the dependencies, run the following commands:

```
source install/setup.bash
rosdep install -i --from-path src --rosdistro humble -y
colcon build
```

To run the node execute:
```
ros2 run teleopkeys_publisher teleopkeys_publisher
```

When the node is running, make sure the keyboard inputs are not blocked by the terminal or other window by de-selecting or minimizing them. Once you start pressing the available keys, the terminal will display messages in the following format:
```
[INFO] [1684004330.241555735] [TeleOpKeys]: Ready to read keyboard inputs.
[INFO] [1684004338.782670910] [TeleOpKeys]: Pressed up.
[INFO] [1684004338.896476342] [TeleOpKeys]: Released up.
[INFO] [1684004339.831320590] [TeleOpKeys]: Pressed left.
[INFO] [1684004340.002965885] [TeleOpKeys]: Released left.
[INFO] [1684004340.369623949] [TeleOpKeys]: Pressed right.
[INFO] [1684004340.467356998] [TeleOpKeys]: Released right.
[INFO] [1684004340.948777665] [TeleOpKeys]: Pressed down.
[INFO] [1684004348.055793108] [TeleOpKeys]: Pressed q.
[INFO] [1684004348.261234340] [TeleOpKeys]: Released q.
[INFO] [1684004348.830487471] [TeleOpKeys]: Pressed e.
[INFO] [1684004349.011708976] [TeleOpKeys]: Released e.
[INFO] [1684004349.588772532] [TeleOpKeys]: Pressed space.
[INFO] [1684004349.709970417] [TeleOpKeys]: Released space.
[INFO] [1684004350.251092621] [TeleOpKeys]: Pressed ctrl_l.
[INFO] [1684004351.078519518] [TeleOpKeys]: Pressed shift_l.
[INFO] [1684004352.784016082] [TeleOpKeys]: Released shift_l.
[INFO] [1684004353.349115364] [TeleOpKeys]: Released ctrl_l.

```

## Available Keys

Not all keys are interpreted by the note. The following table shows the ones available and the messages that are published for each one. Keystrokes from other keys are ignored.

<center>

| Keys | Pressed message | Released message |
| :----: | :----: | :----:  |
| Arrow Up / W | `'p_up'` | `'r_up'` | 
| Arrow Down / S | `'p_down'` | `'r_down'` | 
| Arrow Left / A | `'p_left'` | `'r_left'` | 
| Arrow Right / D | `'p_right'` | `'r_right'` | 
| Q | `'p_q'` | `'r_q'` | 
| E | `'p_e'` | `'r_e'` | 
| F | `'p_f'` | `'r_f'` | 
| Space | `'p_space'` | `'r_space'` | 
| Left Shift | `'p_shift_l'` | `'r_shift_l'` | 
| Right Shift | `'p_shift_r'` | `'r_shift_r'` | 
| Left Ctrl | `'p_ctrl_l'` | `'r_ctrl_l'` | 
| Right Ctrl | `'p_ctrl_r'` | `'r_ctrl_r'` | 
| Esc | `'p_esc'` | `'r_esc'` | 

</center>

NOTE: If you want to add more keys, just follow the instructions in the `TODO` comments in the file `teleopkeys_publisher/__init__.py`
