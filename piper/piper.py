import os
import subprocess
import winsound
import uuid

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command execution failed with return code {e.returncode}")
    except FileNotFoundError:
        print("Error: One of the files or executables not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def play_audio_file(audio_file_path):
    try:
        winsound.PlaySound(audio_file_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"Error: {str(e)}")



if __name__ == "__main__":
    parent_directory = os.path.dirname(os.path.abspath(__file__))

    audio_file_name =  "isfile_ko_kya_nam_du??.wav"

    command_to_execute = rf"Get-Content {parent_directory}\text\Demo.txt | {parent_directory}\piper.exe -m {parent_directory}\model\en_US-kusal-medium.onnx -c {parent_directory}\model\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json -f {parent_directory}\audio\{audio_file_name}"

    execute_command(f"powershell.exe -Command \"{command_to_execute}\"")

    audio_file_path = rf"{parent_directory}\audio\{audio_file_name}"

    # play_audio_file(audio_file_path)
