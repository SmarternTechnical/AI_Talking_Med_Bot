import pygame

def play_mp3(file_path):
    """
    Play an MP3 file using pygame.
    
    Args:
        file_path (str): Path to the MP3 file to play.
    """
    try:
        # Initialize the mixer
        pygame.mixer.init()

        # Load and play the MP3 file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait until the song finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print("Playback finished.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
if __name__ == "__main__":
    play_mp3("output.mp3")  # Replace with your MP3 file path

