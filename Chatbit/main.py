import openai
import pyttsx3
import speech_recognition as sr
import time
openai.api_key="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"
engine = pyttsx3.init()

def say_question(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_bing(audio)
    except: 
        print('eror')

def generate_response(prompt):
      response = openai.completions.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
        
      )  
      return response['choices'][0]['text']
     
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print('Say hey to start voice conversation')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google_cloud(audio)
                if transcription.lower() == 'hey':
                    filename = 'input.wav'
                    print('Say your Question...')
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1 
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, 'wb') as f:
                            f.write(audio.get_wav_data())
                    text = say_question(filename)
                    if text:
                        print(f'You said: {text}')
                        response = generate_response(text)
                        print(f'Bot says: {response}')
                        speak_text(response)
            except Exception as e:
                print('Eror'.format(e))

if __name__ ==  '__main__':
    main()




    