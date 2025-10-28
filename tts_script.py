import sys
import pyttsx3

text = sys.argv[1]
output_path = sys.argv[2]
voice_type = sys.argv[3] if len(sys.argv) > 3 else 'default'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voice_type == 'female' and len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
elif voice_type == 'male':
    engine.setProperty('voice', voices[0].id)

engine.save_to_file(text, output_path)
engine.runAndWait()