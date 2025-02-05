from pydub import AudioSegment

def manipulate_audio(file_path):
    sound = AudioSegment.from_file(file_path)
    sound = sound + 10  # Augmenter le volume
    sound = sound.speedup(playback_speed=1.5)  # Accélérer le son
    sound.export("output_audio.wav", format="wav")
