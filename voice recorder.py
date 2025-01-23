import tkinter as tk
from tkinter import messagebox
import pyaudio
import wave
import threading

# Function to start recording
def start_recording():
    global recording
    recording = True
    record_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    threading.Thread(target=record).start()

# Function to stop recording
def stop_recording():
    global recording
    recording = False
    record_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    messagebox.showinfo("Info", "Recording stopped and saved as 'output.wav'")

# Function to record audio
def record():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    while recording:
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

# Create the main window
root = tk.Tk()
root.title("Voice Recorder")
root.geometry("300x150")
root.resizable(False, False)

# Create and place the record button
record_button = tk.Button(root, text="Record", command=start_recording, bg="green", fg="white", font=("Helvetica", 14))
record_button.pack(pady=20)

# Create and place the stop button
stop_button = tk.Button(root, text="Stop", command=stop_recording, bg="red", fg="white", font=("Helvetica", 14))
stop_button.pack(pady=20)
stop_button.config(state=tk.DISABLED)

# Start the Tkinter event loop
root.mainloop()

