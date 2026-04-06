import cv2
import mediapipe as mp
1
# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Finger tip IDs
tips = [4, 8, 12, 16, 20]

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_idx, hand in enumerate(result.multi_hand_landmarks):

            lm = hand.landmark
            finger_count = 0

            # Get hand label (Left / Right)
            hand_label = result.multi_handedness[hand_idx].classification[0].label

            # Draw hand
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            # -------------------
            # Thumb logic (based on hand)
            # -------------------
            if hand_label == "Right":
                if lm[4].x > lm[3].x:
                    finger_count += 1
            else:  # Left hand
                if lm[4].x < lm[3].x:
                    finger_count += 1

            # -------------------
            # Other 4 fingers
            # -------------------
            for i in range(1, 5):
                if lm[tips[i]].y < lm[tips[i] - 2].y:
                    finger_count += 1

            # Get position to display text
            h, w, _ = frame.shape
            cx = int(lm[0].x * w)
            cy = int(lm[0].y * h)

            # Display hand + count
            cv2.putText(frame,
                        f'{hand_label} Hand',
                        (cx - 50, cy - 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2)

            cv2.putText(frame,
                        f'Fingers: {finger_count}',
                        (cx - 50, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)

    cv2.imshow("Finger Counter (Both Hands)", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()