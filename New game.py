import pygame

# Initialize pygame
pygame.init()

# Load sounds
try:
    lightening_sound = pygame.mixer.Sound("thunder.mp3")
    earthquake_sound = pygame.mixer.Sound("earthquake.mp3")
    acid_rain_sound = pygame.mixer.Sound("rain.mp3")
    tornado_sound = pygame.mixer.Sound("tornado.mp3")
    print("Sounds loaded successfully.")
except pygame.error as e:
    print(f"Error loading sound files: {e}")

def play_test_sound():
    try:
        print("Playing test sound...")
        lightening_sound.play()
        pygame.time.wait(2000)  # Wait 2 seconds to allow sound to play
        lightening_sound.stop()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

# Test sound playback
play_test_sound()

pygame.quit()
