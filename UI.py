import streamlit as st
# from sa.audio_recorder_streamlit import audio_recorder
# from SAR.st_audiorec import st_audiorec
import os
# import uuid
from speech2text import *
import subprocess

def get_recently_modified_file(directory):
    files = os.listdir(directory)

    files = [os.path.join(directory, f) for f in files if os.path.isfile(os.path.join(directory, f))]
    file_modification_times = [(f, os.path.getmtime(f)) for f in files]

    file_modification_times.sort(key=lambda x: x[1], reverse=True)

    if file_modification_times:
        return file_modification_times[0][0]
    else:
        return None


st.title("Banking Talking Assistant")
st.title("Audio Recorder")
# audio0 = audiorecorder("Click to record", "Click to stop recording")

"""
Hi🤖 just click on the voice recorder and let me know how I can help you today?
"""

# wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')

if st.button('start recording'):
    txt1 = recognize()


def execute_python_file(file_path):
    try:
        subprocess.run(["python3", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {file_path}: {e}")

    

audio_location = os.path.dirname(os.path.abspath(__file__))
# audio_file_name = str(uuid.uuid4()) + ".wav"
# audio0.export(f'{audio_location}\audio_files\{audio_file_name}', format="wav")
directory_path0 = f'{audio_location}\piper\text'
recent_file0 = get_recently_modified_file(directory_path0)
st.write(recent_file0)
directory_path = f'{audio_location}\piper\audio'
recent_file = get_recently_modified_file(directory_path)
audio_file = open(recent_file, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='wav')