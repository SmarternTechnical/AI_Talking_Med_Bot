from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3", language="en"):
    """
    Converts text to speech and saves it as an audio file.

    Args:
        text (str): Text to convert into speech.
        output_file (str): Filename for the output audio file.
        language (str): Language code for the text (default is "en" for English).
    """
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the audio file
        tts.save(output_file)
        print(f"Speech saved to '{output_file}'")

        # Optionally, play the audio file
        os.system(f"start {output_file}" if os.name == "nt" else f"open {output_file}")

    except Exception as e:
        print("An error occurred:", e)

# Example usage
if __name__ == "__main__":
    text = "Hello! This is an example of text-to-speech conversion in Python."
    text_to_speech(text)

