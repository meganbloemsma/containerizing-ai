# pip install azure-cognitiveservices-speech
# pip install python-dotenv

# Recognize speech from (default) microphone + cap at 25 words
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_API_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language = "en-US" # default language is currently set to US english

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("\nAs you close your eyes, you focus on the words you want to convey... you take a breath... and you speak:")

    recognized_words = []  # To store recognized words

    while len(recognized_words) < 25:  # Cap recognition at 25 words
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            recognized_text = speech_recognition_result.text
            words = recognized_text.split()  # Split the recognized text into words
            recognized_words.extend(words)  # Add the recognized words to the list

            # Check if the total recognized words exceed the limit
            if len(recognized_words) > 25:
                recognized_words = recognized_words[:25]

            print("\t{}".format(recognized_text)) # Print the recognized text
                  
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("\n(Keep going! You haven't reached 25 words yet!)")
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
            break

    # Output the final recognized words
    recognized_text = ' '.join(recognized_words)
    print("\nThis is what the person actually received:")
    print("\t{}".format(recognized_text))

recognize_from_microphone()