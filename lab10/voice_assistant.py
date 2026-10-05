import cv2 
import json
import pyaudio
import pyttsx3
import requests
from vosk import Model, KaldiRecognizer



MODEL_PATH = "lab10/vosk-model-small-ru-0.22"
API_URL = "https://dog.ceo/api/breeds/image/random"

engine = pyttsx3.init()  # объект движка речи
model = Model(MODEL_PATH)  # модель распознавания речи
rec = KaldiRecognizer(model, 16000)  # распознаватель, 16000 - частота дискретизации звука

current_url = ""  # для ссылок на картинки

def speak(text):
    print(f"Ассистент: {text}")
    engine.say(text)  # ставим текст в очередь на озвучку
    engine.runAndWait()  # проигрываем

def load_image():
    global current_url
    data = requests.get(API_URL).json()
    current_url = data["message"]


p = pyaudio.PyAudio()  # объект для работы со звуком
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)  # открываем поток с микрофона
stream.start_stream()


load_image()  # Загружаем первую картинку при старте
speak("Ассистент готов. Слушаю команду.")

while True:  # цикл прослушивания
    data = stream.read(4000, exception_on_overflow=False)  # чтение куска аудио
    
    if rec.AcceptWaveform(data):  # отдаем кусок распознавателю
        result = json.loads(rec.Result())  # результат распознавания в виде json
        command = result.get("text", "").lower()  # получаем и обрабатываем распознанный текст
        
        if not command:
            continue  # если ничего не распознали
            
        print(f"Вы сказали: {command}")

        if "показать" in command:
            img_data = requests.get(current_url).content  # Скачиваем картинку
            with open("temp.jpg", "wb") as f: 
                f.write(img_data)
            img = cv2.imread("temp.jpg")
            cv2.imshow("Dog", img)
            cv2.waitKey(1000)  # показываем секунду
            speak("Картинка на экране.")

        elif "сохранить" in command:
            img_data = requests.get(current_url).content
            with open("dog_saved.jpg", "wb") as f:
                f.write(img_data)
            speak("Сохранено как dog_saved.jpg")

        elif "следующая" in command:
            load_image()
            speak("Картинка обновлена.")

        elif "порода" in command:
            # Получаем чистую породу из ссылки
            breed = current_url.split("/")[-2]
            speak(f"Порода собаки: {breed}")


        elif "разрешение" in command:
            img_data = requests.get(current_url).content
            with open("temp.jpg", "wb") as f:
                f.write(img_data)
            img = cv2.imread("temp.jpg")
            h, w, _ = img.shape
            speak(f"Разрешение картинки: {w} на {h} пикселей")

        elif "выход" in command or "стоп" in command:
            speak("Выключаюсь.")
            break
            
        else:
            speak("Команда не распознана, повторите.")
