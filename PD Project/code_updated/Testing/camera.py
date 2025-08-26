import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('id')#for the usb cam, is 1
args = vars(parser.parse_args())



# Open the default camera (0). On Raspberry Pi, you may need to use 0 or 1 depe>
cap = cv2.VideoCapture(int(args['id']))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display the resulting frame
    cv2.imshow('Camera', frame)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

