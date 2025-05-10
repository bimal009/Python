from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, KeyCode
import time
import threading

events = []
recording = True
stop_flag = threading.Event()
ctrl_pressed = False

# Record mouse events
def on_click(x, y, button, pressed):
    global recording
    if recording:
        events.append(('mouse_click', time.time(), x, y, button, pressed))
        
        # Stop recording on right-click
        if button == Button.right and pressed:
            print("Right-click detected. Stopping recording...")
            recording = False
            stop_flag.set()

# Record keyboard events
def on_press(key):
    global recording, ctrl_pressed
    
    if recording:
        events.append(('key_press', time.time(), key))
        
        # Track if Ctrl is pressed
        if key == Key.ctrl_l or key == Key.ctrl_r:
            ctrl_pressed = True
        
        # Check for c key while Ctrl is pressed
        elif ctrl_pressed and (key == KeyCode.from_char('c') or key == KeyCode.from_char('C')):
            print("Stop recording (Ctrl + C detected)...")
            recording = False
            stop_flag.set()
            return False

def on_release(key):
    global ctrl_pressed
    # Reset ctrl_pressed when Ctrl key is released
    if key == Key.ctrl_l or key == Key.ctrl_r:
        ctrl_pressed = False

# Start recording
def record():
    global keyboard_listener, mouse_listener
    print("Recording... Press Ctrl + C or right-click to stop.")
    
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    
    mouse_listener.start()
    keyboard_listener.start()
    
    # Wait until stop_flag is set (either by Ctrl+C or right-click)
    stop_flag.wait()
    
    # Ensure both listeners are stopped
    if mouse_listener.is_alive():
        mouse_listener.stop()
    if keyboard_listener.is_alive():
        keyboard_listener.stop()

# Replay the recorded events
def replay():
    if not events:
        print("No events recorded!")
        return
        
    print("Replaying recorded actions...")
    kb = KeyboardController()
    ms = MouseController()
    
    start_time = events[0][1]
    last_time = start_time
    
    for event in events:
        current_time = event[1]
        # Calculate delay since last event
        delay = current_time - last_time
        if delay > 0:
            time.sleep(delay)
        
        if event[0] == 'mouse_click':
            _, _, x, y, button, pressed = event
            ms.position = (x, y)
            if pressed:
                ms.press(button)
            else:
                ms.release(button)
        elif event[0] == 'key_press':
            _, _, key = event
            try:
                if isinstance(key, KeyCode):
                    kb.press(key.char)
                    kb.release(key.char)
                else:
                    kb.press(key)
                    kb.release(key)
            except AttributeError:
                # Handle special keys
                kb.press(key)
                kb.release(key)
                
        last_time = current_time

# Add a function to handle keyboard interrupt during replays
def keyboard_interrupt_handler():
    kb_listener = keyboard.Listener(on_press=check_for_stop)
    kb_listener.start()
    return kb_listener

# Function to check for Ctrl+C to stop all replays
replay_stop_flag = threading.Event()
def check_for_stop(key):
    global ctrl_pressed
    
    # Track if Ctrl is pressed
    if key == Key.ctrl_l or key == Key.ctrl_r:
        ctrl_pressed = True
    
    # Check for c key while Ctrl is pressed
    elif ctrl_pressed and (key == KeyCode.from_char('c') or key == KeyCode.from_char('C')):
        print("\nCtrl+C detected. Stopping all replays...")
        replay_stop_flag.set()
        return False

    if key == Key.esc:
        print("\nESC key detected. Stopping all replays...")
        replay_stop_flag.set()
        return False

# Main execution
if __name__ == "__main__":
    # Record actions once
    record()
    print("Recording stopped.")
    print(f"Recorded {len(events)} events.")
    
    if not events:
        print("No events were recorded. Exiting.")
        exit()
    
    # Wait a moment before starting replays
    print("Starting 1000 replays in 3 seconds...")
    print("Press Ctrl+C or ESC at any time to stop all replays.")
    time.sleep(3)
    
    # Start keyboard listener to detect stop signals
    kb_interrupt = keyboard_interrupt_handler()
    
    # Replay the recorded events 1000 times
    for i in range(1000):
        if replay_stop_flag.is_set():
            print(f"Stopped after {i} replays.")
            break
            
        print(f"Replay {i+1}/1000")
        replay()
        
        # Small pause between replays
        time.sleep(0.5)
    
    print("All replays completed.")
    
    # Cleanup
    if kb_interrupt.is_alive():
        kb_interrupt.stop()
       