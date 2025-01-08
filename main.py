import cv2
import mediapipe as mp
import pyautogui
import random
import specs
from pynput.mouse import Button, Controller

# Mouse controller
mouse_controller = Controller()

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands_model = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=1
)

def get_fingertip_position(hand_result):
# Extract the index fingertip position from hand landmarks.
    if hand_result.multi_hand_landmarks:
        landmarks = hand_result.multi_hand_landmarks[0]
        fingertip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        return fingertip.x, fingertip.y
    return None, None

def control_mouse(fingertip_x, fingertip_y):
# Move the mouse based on fingertip coordinates.
    if fingertip_x is not None and fingertip_y is not None:
        cursor_x = int(fingertip_x * screen_width)
        cursor_y = int(fingertip_y * screen_height / 2)  # Reduce Y sensitivity
        pyautogui.moveTo(cursor_x, cursor_y)

def perform_gesture_action(landmarks, thumb_to_index_distance):
# Detect gestures and perform corresponding mouse actions.
    if len(landmarks) >= 21:
        if thumb_to_index_distance < 50 and specs.get_angle(landmarks[5], landmarks[6], landmarks[8]) > 90:

            # Move mouse gesture
            return "Move Mouse"
        elif (
            specs.get_angle(landmarks[5], landmarks[6], landmarks[8]) < 50 and
            specs.get_angle(landmarks[9], landmarks[10], landmarks[12]) > 90 and
            thumb_to_index_distance > 50
        ):
            mouse_controller.click(Button.left)
            return "Left Click"
        elif (
            specs.get_angle(landmarks[9], landmarks[10], landmarks[12]) < 50 and
            specs.get_angle(landmarks[5], landmarks[6], landmarks[8]) > 90 and
            thumb_to_index_distance > 50
        ):
            mouse_controller.click(Button.right)
            return "Right Click"
        elif (
            specs.get_angle(landmarks[5], landmarks[6], landmarks[8]) < 50 and
            specs.get_angle(landmarks[9], landmarks[10], landmarks[12]) < 50 and
            thumb_to_index_distance > 50
        ):
            pyautogui.doubleClick()
            return "Double Click"
        elif (
            specs.get_angle(landmarks[5], landmarks[6], landmarks[8]) < 50 and
            specs.get_angle(landmarks[9], landmarks[10], landmarks[12]) < 50 and
            thumb_to_index_distance < 50
        ):
            screenshot = pyautogui.screenshot()
            screenshot_label = random.randint(1, 1000)
            screenshot.save(f"screenshot_{screenshot_label}.png")
            return "Screenshot Taken"
    return None

def process_frame_and_gestures(frame, hand_result):
# Process each video frame, detect gestures, and act accordingly.
    if hand_result.multi_hand_landmarks:
        landmarks = hand_result.multi_hand_landmarks[0]
        mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        # Convert landmarks to (x, y) format
        landmark_positions = [(lm.x, lm.y) for lm in landmarks.landmark]
        thumb_to_index_dist = specs.get_distance([landmark_positions[4], landmark_positions[5]])

        action = perform_gesture_action(landmark_positions, thumb_to_index_dist)
        if action == "Move Mouse":
            fingertip_x, fingertip_y = get_fingertip_position(hand_result)
            control_mouse(fingertip_x, fingertip_y)
        elif action:
            cv2.putText(frame, action, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def run_hand_gesture_control():
# Main loop for hand gesture-based mouse control.
    video_capture = cv2.VideoCapture(0)

    try:
        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                break

            # Flip and convert frame to RGB
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            hand_result = hands_model.process(rgb_frame)

            # Process gestures and update frame
            process_frame_and_gestures(frame, hand_result)

            # Display the frame
            cv2.imshow("Gesture Control", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run_hand_gesture_control()