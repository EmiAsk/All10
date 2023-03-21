## Название
### Все 10
## Описание идеи
предоставить людям возможность (программу), улучшающую их навык, не прилагая особых усилий. В данном случае это печать вслепую или умение печатать быстро. Данный скилл очень сильно экономит время и нервы во время работы за ПК. А на сегодняшний день время на вес золота.

## Реализация
Реализовано три класса авторизации в аккаунт: форма входа (SingInForm
), форма регистрации (RegistrationForm), форма восстановления пароля (RecoverPage). Основой является главное окно (MainWindow). Оно позволяет переключаться между вкладками: окно профиля (ProfilePage), окно рейтинга среди локальных пользователей (RatingPage), окно претеста (PretestPage). Уже от окна претеста можно перейти к окну тестирования (TestingPage). После выполнения тестирования диалоговое окно ResultPage сообщает о результате окну статистики (StatisticPage). Из вкладки профиля можно попасть в окно информации (InfoPage) и окно статистики (StatisticPage).
Все данные пользователей (почта, имя, фамилия, фото, хэш пароля, соль) и их попытки (скорость, точность) хранятся в 3 таблицах одной БД.

**Примечание: статистика за год, месяц и день составляется за текущий год, месяц и день соответственно. То есть выбрав "за год", появится статистика за 2021 год (текущий)**

## Функциональность

Готовая программа имеет следующие функции:

### Аккаунт:
  -	Регистрация нового аккаунта
  -	Авторизация аккаунта в системе
  -	Смена пароля аккаунта
  -	Удаление аккаунта с подтверждением действия

### Тренировочные упражнения:
  -	буквенные сочетания
  -	целые слова
  -	цифры
  -	специальные символы (знаки препинания)
  -	набор текста на скорость
  -	набор текста до первой ошибки

### Статистика:
-	скорость печати
- дата и время прохождения
-	точность печати

### Настройки:
-	редактирование профиля
-	выбор текущего урока (упражнения)
-	смена языка ввода
### Помощь:
-	Выведение окна помощи с инструкцией к программе.

## Начало работы
+ Чтобы запустить приложение, нужно открыть файл enter_page.py или же enter_page.exe
 (если у вас нет интерпретатора python).
+ Пароль при регистрации будет сгенерирован автоматически и отправлен на указанную почту
+ В директории проекта есть файл-установщик шрифта расширения “.ttf” (лучше установить для удобства).
+ А теперь можете выполнять тестирование. Улучшайте свои скорость и точность печати и повышайте свой локальный рейтинг!

## Использованные технологии/библиотеки
+ Pyqt5 – основной интерфейс
+ hashlib – хеширование паролей
+ smtplib – отправка писем при регистрации и восст. пароля
+	sqlite3 – чтение и запись данных пользователя и его результата.
+	random – выбор случайного тренировочного предложения
+	re – соответствие символов с нужными
+	time – счёт времени
+	datetime – получение даты
+	pyqtgraph – построение графика статистики

 ## Интерфейс
![image](https://user-images.githubusercontent.com/74973350/226669051-7127f318-d0c6-4861-90b8-baa3ee85be31.png)
![image](https://user-images.githubusercontent.com/74973350/226669071-729b05b4-7965-4cfe-8246-dc4ebf5a5795.png)
![image](https://user-images.githubusercontent.com/74973350/226669090-e296d54d-b246-425b-b645-aa6c483c38e3.png)
![image](https://user-images.githubusercontent.com/74973350/226669103-cb944221-bcb3-4bbc-830c-91853d3b1e47.png)

 
