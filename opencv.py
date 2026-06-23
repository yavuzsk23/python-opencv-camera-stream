import cv2

# Kamerayi ac (0 genelde laptopun kendi kamerasidir)
cap = cv2.VideoCapture(0)

print("Kamerayi acmak icin bir tusa basiliyor... Kapatmak icin 'q' tusuna bas!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Goruntuyu ekranda goster
    cv2.imshow('Victus Gozlerini Acti!', frame)

    # 'q' tusuna basinca cik
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
