Привет! Меня зовут Катя, и я аналитик данных, так же сейчас осваиваю библиотеки машинного обучения TensorFlow .
В данном репозитарии вы можете увидеть некоторые мои работы.
____________________________________________________________________________________
Инструменты анализа данных: SQL, Excel:

Языки программирования и библиотеки: Python, Pandas, math

Системы управления базами данных: MySQL

Средства визуализации данных: Matplotlib, seaborn

Инструменты для машинного обучения: TensorFlow
_________________________________________________________________________________
Проект: Анализ АБ теста Воздействие “тест” - уведомление с помощью пуша (сообщение о товарах и скидках появится в уведомлениях приложения) вместо sms уведомления
Текущая задача:
Проанализировать АБ-Тест, проведенный во всех городах. крупного ритейлера, который присутствует во многих российских городах!

Цель эксперемента

Исследование альтернативного метода воздействия на клиентские покупки с помощью пуш-уведомлений.
Воздействие “контроль” - уведомление о новых товарах и скидках с помощью баннера в приложении
Воздействие “тест” - уведомление с помощью пуша (сообщение о товарах и скидках появится в уведомлениях приложения).
Дизайн эксперимента
Длительность эксперимента - 3 месяца.
География: в эксперименте задействованы все города присутствия в России.
Сплит-система
Клиенты разбиты на две группы одинакового размера случайным образом. 
Таргет-метрики, Конверсия из рекламы в покупку, Средний чек
Необходимо проанализировать и визуализировать результаты, провести сегментацию, а также сделать выводы и сформулировать рекомендации для дальнейших запусков АБ Теста.

Также надо построить таблицу, которая будет в удобной форме хранить результаты АБ Теста.

Структура стартовых данных представлена в презентации

jupyter notebook  https://github.com/Mertsajus4aja/AB-test/blob/main/%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%90%D0%91%20%D1%82%D0%B5%D1%81%D1%82%D0%B0.ipynb

Исследование excel https://github.com/Mertsajus4aja/AB-test/blob/main/%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%90%D0%91%20%D1%82%D0%B5%D1%81%D1%82%D0%B0.xlsx

Презентация проекта https://github.com/Mertsajus4aja/AB-test/blob/main/%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%90%D0%91%20%D1%82%D0%B5%D1%81%D1%82%D0%B0%20%5B%D0%90%D0%B2%D1%82%D0%BE%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%5D.pptx


_________________________________________________________________________________________________________________________________________________________________
Проект:

Калькулятор юнит-экономики онлайн-школы.


Задачей проекта было исследование стартовых данных онлайн-кинотеатра, его маржинальности, активностей подписчиков и пользователей, выявление проблем проекта, а так же предложение по выходу на 25% маржинальность.
Стартовые данные для анализа https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/стартовые%20данные.xlsx

Расчет юнит-экономики, визуализация выполненной работы https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Часть%203%20последняя%20версия%2022..04.xlsx

Результаты анализа, предложение по выходу на 25% маржинальность, а так же визуализация существующих проблем наглядно представлена в презентации
https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Курсовой%20проект.pptx


_______________________________________________________________________________________________

Проект:

Анализ клиентского LTV по когортам времени захода на платформу и сделать выводы, какие когорты лучше, а какие хуже с точки зрения LTV.

Задача: Построить сводную таблицу с абсолютными доходимостями клиентов по месячным когортам. Построить таблицу с клиентским Retention. Рассчитать LTV с помощью усредненных костов для каждой когорты. Сделать выводы относительно хороших и плохих когорт с точки зрения LTV. Посчитать  суммарную прибыль нашей компании по всем клиентам (за всё время).

Стартовые данные https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/стартовые%20данные%20когортного%20анализа.xlsx

Когортный анализ https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Когортный%20анализ.xlsx
___________________________________________________________________________________________________

Проект:

Исследование изменения воронок продаж агрегатора такси.

Задача: Построить последовательную воронку для июля 2021 года для Москвы и Санкт-Петербурга для тарифов “Эконом” и “Комфорт”
Все конверсии должны быть рассчитаны по всем наблюдениям из таблицы (без разбиения по когортам), но в разбивке по городам и тарифам (”Москва-Эконом”, “Москва-Комфорт”, “Санкт-Петербург-Эконом”, “Санкт-Петербург-Комфорт”).

Известно, что на границе июля и августа было имплементировано изменение в процесс назначения водителей: мы теперь дольше ищем водителя, зато находим того, кто находится ближе к клиенту. 
Это было сделано для того, чтобы уменьшить время ожидания водителя после назначения, а следовательно, снизить клиентские отмены, вызванные долгим ожиданием подачи. 

В отдельном текстовом поле ответьте на следующие вопросы:

- *Как бы вы прокомментировали данное изменение с точки зрения данных? Получилось ли достичь общего роста O2R? Если нет, то почему?
- что послужило причиной ухудшения этого звена воронки?

  Стертовые данные  https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Бизнес-2.%20Метрики.xlsx
  
  Результат проведенного анализа воронок продаж  https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Анализ%20бизнес%20метрик%20агрегатора%20такси.xlsx

  __________________________________________________________________________________________
Проект: 

Проверка гипотезы о зависимости коэффициента веса морских котиков и уровня гельминтоза у особей. 
Стартовые данные: данные об обследованных котиках, весе, длинне и уровень C. osculatum желудок.
В результате анализа гипотеза о зависимости веса и коэффициента гельминтоза не подтвердилась.

Результаты анализа, таблицы, визуализация https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/нерпы%20для%20аналитики.xlsx

Презентация к таблицам по анализу https://github.com/Mertsajus4aja/Mertsajus4aja/blob/main/Презентация%20индекс%20группа.pptx

  _______________________________________________________________________________________________________________________________________________________

Контактная информация 
Email: sherbinaekv@gmail.com
