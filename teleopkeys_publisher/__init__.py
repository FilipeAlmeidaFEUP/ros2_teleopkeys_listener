from pynput import keyboard
from pynput.keyboard import Key
import rclpy
from std_msgs.msg import String

class TeleOpKeys:
    def __init__(self) -> None:
        self.node = rclpy.create_node('TeleOpKeys')
        self.publisher = self.node.create_publisher(String, 'teleopkeys', 10)
    
    def listen_to_keystrokes(self):
        self.node.get_logger().info('Ready to read keyboard inputs.')
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            while rclpy.ok() and listener.running:
                rclpy.spin_once(self.node, timeout_sec=0.1)

    def on_press(self, key):
        key = self.read_key(key)
        if key == None: return
        self.node.get_logger().info('Pressed ' + key + '.')
        msg = 'p_' + key
        self.publisher.publish(self.publisher.msg_type(data=msg))

    def on_release(self, key):
        key = self.read_key(key)
        if key == None: return
        self.node.get_logger().info('Released ' + key + '.')
        msg = 'r_' + key
        self.publisher.publish(self.publisher.msg_type(data=msg))

    def read_key(self, key):
        char = getattr(key, 'char', None)
        if isinstance(char, str):
            #TODO add more lines to the match-case if more character keys are needed
            match char:
                case 'w': return 'up'
                case 's': return 'down'
                case 'a': return 'left'
                case 'd': return 'right'
                case 'q': return 'q'
                case 'e': return 'e'
                case 'f': return 'f'
                case _ : return None
        else:
            #TODO add more lines to the match-case if more special keys are needed
            match key:
                case Key.up: return 'up'
                case Key.down: return 'down'
                case Key.left: return 'left'
                case Key.right: return 'right'
                case Key.space: return 'space'
                case Key.shift_l: return 'shift_l'
                case Key.shift_r: return 'shift_r'
                case Key.ctrl_l: return 'ctrl_l'
                case Key.ctrl_r: return 'ctrl_r'
                case Key.esc: return 'esc'
                case _ : return None



def main(args = None):
    rclpy.init()
    
    teleopkeys = TeleOpKeys()
    teleopkeys.listen_to_keystrokes()

if __name__ == "__main__":
    main()