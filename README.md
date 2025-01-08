# Hand-Gesture-Driven-Mouse-System
*This project implements an advanced Virtual Mouse System that uses real-time hand gesture recognition for controlling a computer interface. By leveraging state-of-the-art computer vision technologies, such as MediaPipe Hands, OpenCV, and PyAutoGUI, this system provides an innovative and efficient method for interacting with a computer without the need for traditional input devices like a physical mouse or touchpad. The system tracks hand landmarks in real-time using a webcam and maps the recognized gestures to control cursor movement and execute various mouse functions with high accuracy.*

## Core Features and Functionalities:

### Hand Gesture Detection and Tracking:
1. This system employs MediaPipe's Hands module, a deep learning-based framework that detects and tracks 21 key landmarks of the human hand.
2. The hand landmarks are tracked with high precision and minimal latency, making real-time interaction with the system feasible. The model also adapts to varying lighting conditions and hand orientations.
3. Detection works for a single hand and provides continuous tracking over time, offering robustness against partial occlusions and slight hand movements.

### Gesture-Based Mouse Controls:

#### Cursor Movement: 
The system tracks the index fingertip's position relative to the webcam frame and maps it onto the screen coordinates. Users can control cursor movement with smooth and accurate fingertip tracking.

#### Mouse Actions:
1. Left Click: Triggered by detecting a specific angular configuration of the hand involving the thumb and index finger.
2. Right Click: A unique hand pose is interpreted to simulate a right mouse click.
3. Double Click: Predefined gestures enable double-click actions with precision.
4. Screenshot Capture: Recognizes a special gesture to take screenshots, which are saved locally with randomized filenames to avoid overwriting.

### Gesture Recognition Logic:
1. The recognition system calculates the angular relationships between the hand landmarks, such as the angle between the thumb and index finger and the distances between key hand joints (e.g., thumb-to-index distance).
2. These measurements are used to categorize gestures with high accuracy. For example, angles greater than or less than specific thresholds represent different mouse actions, such as clicks, drags, or screenshots.
3. Gesture recognition is highly modular, allowing easy expansion for additional gestures or customization for specialized applications. The codebase is designed for extensibility and includes several helper functions for geometric calculations and landmark handling.

### Real-Time Video Processing:
1. OpenCV is used to capture and process video frames from the webcam. Each frame is flipped for mirror-view and converted from BGR to RGB format for compatibility with MediaPipe.
2. Hand landmarks are drawn on each processed frame, providing visual feedback to the user for easier interaction.

### Screen Adaptation and Performance Optimization:
1. Screen Mapping: The hand gestures are mapped proportionally to the screen resolution, maintaining spatial accuracy while reducing sensitivity for smoother cursor control. The vertical movement is adjusted by scaling the y-axis to limit excessive cursor speed, enhancing usability.
2. Detection Confidence and Optimization: The model uses a minimum confidence threshold (0.75) for both detection and tracking to filter out false positives and improve accuracy. Additionally, various optimization techniques are implemented, such as frame skipping during periods of minimal hand movement to ensure real-time processing.

## How It Works:
The system uses the MediaPipe Hands model to process video frames captured from the webcam. Detected hand landmarks are analyzed to determine the positions of key points, such as the index fingertip and thumb.
Based on landmark positions, the system computes gesture-specific parameters such as angles and distances to classify the gesture being performed.
Corresponding mouse actions are executed using PyAutoGUI for cursor control and the pynput library for mouse clicks.
The processed video feed with gesture annotations is displayed in real-time for visual confirmation.

## Applications and Use Cases:
1. Contactless Interaction: Provides a hygienic, touch-free alternative for controlling computers.
2. Accessibility: Enables individuals with physical impairments to interact with computers using simple hand gestures.
3. Innovative Human-Computer Interaction: Offers an engaging solution for smart devices, gaming, and augmented/virtual reality systems.


This project represents a powerful example of integrating computer vision and human-computer interaction principles to create an accessible and futuristic tool for modern computing. Its modular and scalable design makes it suitable for further enhancements and extended applications in robotics, IoT, and AI-driven systems.
