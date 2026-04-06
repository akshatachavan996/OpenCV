# Open_CV
✋Finger Counter (Both Hands)
A real-time computer vision project that detects both hands, identifies Left/Right hand, and counts the number of fingers raised using a webcam.
Built using OpenCV and MediaPipe.
---

🚀 Features
- ✅ Detects two hands simultaneously
- ✅ Identifies Left & Right hand
- ✅ Almost accurate finger counting
- ✅ Real-time webcam processing
- ✅ Hand landmark visualization
---

🛠️ Tech Stack
- Python (Using AI)
- OpenCV
- MediaPipe
---

▶️ Run the Project
python main.py
Press ESC to exit.
---

🧠 How It Works
- MediaPipe detects 21 hand landmarks
- Finger tips are compared with lower joints
- Logic:
  - Thumb → checked horizontally
  - Other fingers → checked vertically
- Displays:
  - Hand type (Left / Right)
  - Number of fingers raised
---

📸 Output
- Shows live webcam feed
- Displays:
  - "Left Hand / Right Hand"
  - "Fingers: X"
---
-------------------------------
Author: Akshata Rajendra Chavan

⭐ Support
If you like this project, give it a ⭐ on GitHub!
