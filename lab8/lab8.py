import cv2

# Задание 1 - перевод изображения в полутоновое

# загрузка
img = cv2.imread("lab8/variant-1.jpg")

# Переводим в полутоновое
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imwrite("lab8/variant-1_gray.jpg", gray)  # сохраним
cv2.imshow("gray", gray)
cv2.waitKey(0)  # ожидание нажатия любой клавиши. 0 - бесконечное ожидание
cv2.destroyAllWindows()  # закрытие всех окон


# задание 2 - отслеживание метки

cap = cv2.VideoCapture(0)  # Подключение к веб-камере

while True:
    ret, frame = cap.read()  # ret - получилось ли прочесть кадр, frame - сам кадр
    if not ret:
        break

    # Делаем кадр серым, размываем
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Бинаризация: все темнее 100 становится белым, светлее - черным. _ - порог
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

    # Ищем контуры объектов
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Находим самый большой контур - нашу метку
        main_contour = max(contours, key=cv2.contourArea)
        
        # Получаем координаты рамки
        x, y, w, h = cv2.boundingRect(main_contour)

        # рисуем зеленую рамку толщиной 2 пикселя для метки
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Выведем координаты в левый верхний угол экрана
        cv2.putText(frame, f"X: {x}, Y: {y}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow("Camera Tracking", frame)  # Показываем видео с камеры

    # выход по нажатию на q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# отключение камеры и закрытие окон
cap.release()
cv2.destroyAllWindows()