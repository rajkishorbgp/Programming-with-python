import speech_recognition as sr

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1)  # Update with your device index

with my_mic as source:
    print("Say something!")
    while True:
        audio = r.listen(source)  # Listen to the microphone input
        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            # Add your condition to stop the loop
            if text.lower() == "stop":
                print("Speech recognition stopped.")
                break

        except sr.UnknownValueError:
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            print(f"Error: {e}")
