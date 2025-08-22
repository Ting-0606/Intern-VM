import pygame
import pygame.camera
import sys

# Initialize Pygame and camera
pygame.init()
pygame.camera.init()

# Get available cameras
cameras = pygame.camera.list_cameras()
if not cameras:
    print("No cameras found! Please check your webcam connection.")
    sys.exit()

# Create camera object
cam = pygame.camera.Camera(cameras[0], (640, 480))
camera_active = False

print("Webcam Control for Raspberry Pi")
print("=================================")
print("Press 'o' to turn the camera ON")
print("Press 'f' to turn the camera OFF")
print("Press 'q' to quit")

# Create a simple window to display camera feed
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Webcam Feed - Press 'o' to start, 'f' to stop")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o and not camera_active:  # Turn camera ON
                try:
                    cam.start()
                    camera_active = True
                    print("Camera turned ON")
                except Exception as e:
                    print(f"Error starting camera: {e}")
            elif event.key == pygame.K_f and camera_active:  # Turn camera OFF
                cam.stop()
                camera_active = False
                screen.fill((0, 0, 0))  # Clear the screen
                pygame.display.flip()
                print("Camera turned OFF")
            elif event.key == pygame.K_q:  # Quit
                running = False
    
    # If camera is active, get and display the image
    if camera_active:
        try:
            image = cam.get_image()
            screen.blit(image, (0, 0))
            pygame.display.flip()
        except Exception as e:
            print(f"Error getting image: {e}")
            camera_active = False
            cam.stop()

# Clean up
if camera_active:
    cam.stop()
pygame.quit()
sys.exit()