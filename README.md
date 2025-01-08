# Hand-Gesture-Driven-Mouse-System
This project presents an innovative implementation of a Virtual Mouse System that leverages real-time hand gesture recognition using advanced technologies such as MediaPipe Hands, OpenCV, and PyAutoGUI. The system is designed to provide a seamless and intuitive way of interacting with a computer, eliminating the need for a physical mouse. By detecting and interpreting specific hand gestures via a webcam, the system enables precise control over the cursor and execution of essential mouse actions.

Core Features and Functionalities:
Hand Gesture Detection and Tracking:

Utilizes MediaPipe's Hands module, a highly efficient framework for detecting and tracking 21 key landmarks of the human hand in real-time.
Integrates robust detection algorithms with high accuracy to interpret gestures even in dynamic environments.
Gesture-Based Mouse Controls:

Cursor Movement: The system tracks the index fingertip's position relative to the webcam frame and maps it onto the screen coordinates. Users can control cursor movement with smooth and accurate fingertip tracking.
Mouse Actions:
Left Click: Triggered by detecting a specific angular configuration of the hand involving the thumb and index finger.
Right Click: A unique hand pose is interpreted to simulate a right mouse click.
Double Click: Predefined gestures enable double-click actions with precision.
Screenshot Capture: Recognizes a special gesture to take screenshots, which are saved locally with randomized filenames to avoid overwriting.
Gesture Recognition Logic:

Employs mathematical calculations involving angles between hand landmarks and distances between key points (e.g., thumb and index finger).
Incorporates modularized functions for gesture recognition, enhancing code readability and extensibility.
Real-Time Video Processing:

Integrates OpenCV to capture and process video frames from the webcam.
Displays real-time feedback with overlaid hand landmarks and gesture labels, offering users a visual understanding of system behavior.
Screen Adaptation and Performance Optimization:

Dynamically maps the hand movements within the webcam frame to the dimensions of the screen for responsive and adaptive controls.
Optimizes tracking performance with high detection and tracking confidence thresholds to minimize latency and improve user experience.
How It Works:
The system uses the MediaPipe Hands model to process video frames captured from the webcam. Detected hand landmarks are analyzed to determine the positions of key points, such as the index fingertip and thumb.
Based on landmark positions, the system computes gesture-specific parameters such as angles and distances to classify the gesture being performed.
Corresponding mouse actions are executed using PyAutoGUI for cursor control and the pynput library for mouse clicks.
The processed video feed with gesture annotations is displayed in real-time for visual confirmation.

Applications and Use Cases:
Contactless Interaction: Provides a hygienic, touch-free alternative for controlling computers.
Accessibility: Enables individuals with physical impairments to interact with computers using simple hand gestures.
Innovative Human-Computer Interaction: Offers an engaging solution for smart devices, gaming, and augmented/virtual reality systems.
This project represents a powerful example of integrating computer vision and human-computer interaction principles to create an accessible and futuristic tool for modern computing. Its modular and scalable design makes it suitable for further enhancements and extended applications in robotics, IoT, and AI-driven systems.
