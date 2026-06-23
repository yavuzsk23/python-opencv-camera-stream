import cv2

# Open the camera (0 is usually the laptop's built-in webcam)
cap = cv2.VideoCapture(0)

print("Pressing a key to open the camera... Press 'q' to close!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the image on the screen
    cv2.imshow('DE_yavuzsk08236_TR', frame)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
