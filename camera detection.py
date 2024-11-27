import cv2
import mediapipe as mp
import screen_brightness_control as sbc

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Inisialisasi OpenCV
cap = cv2.VideoCapture(0)

# Fungsi untuk mengatur kecerahan berdasarkan posisi jari
def set_brightness_from_hand_position(brightness):
    try:
        sbc.set_brightness(brightness)
    except Exception as e:
        print(f"Error setting brightness: {e}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Konversi warna BGR ke RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Proses gambar untuk deteksi tangan
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Ambil koordinat jari telunjuk dan jempol
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Hitung jarak antara jari telunjuk dan jempol
            dx = index_finger_tip.x - thumb_tip.x
            dy = index_finger_tip.y - thumb_tip.y
            distance = (dx**2 + dy**2)**0.5

            # Normalisasi jarak untuk mengatur kecerahan
            normalized_distance = min(max(distance, 0.0), 1.0)  # Pastikan jarak berada dalam rentang 0.0 hingga 1.0
            brightness = int(normalized_distance * 1000)  # Skala kecerahan dari 0 hingga 100

            # Atur kecerahan berdasarkan jarak antara jari telunjuk dan jempol
            set_brightness_from_hand_position(brightness)

            # Gambar tangan dan landmark di layar
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()