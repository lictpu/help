## Учебно-справочный репозиторий лицеистов ТПУ
[![N|Solid](https://portal.tpu.ru/f_lyceum/img/main-logo.jpg)](https://portal.tpu.ru/lyceum)



- [X] mermaid
- [ ] plantuml

## Состав

```python
import telebot
import openai
while True:
    try:

        bot=telebot.TeleBot('5992274775:AAFUjj--15Ep2ulKg0HIUyeYrsSBH4a2l-6c')
        openai.api_key="sk--5OLfN5b9hvMMvVli3l4pT3BlbkFJLlGmXyb6qIq7VS0CzoaY"

        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            response=openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'{message.text}',
                max_tokens=1124,
                n=1,
                stop=None,
                temperature=1,
            )
            bot.send_message(message.chat.id, response.choices[0].text)

        bot.polling()



    except Exception:
        print('error')
        continue

```

[![](https://user-images.githubusercontent.com/114549805/205498470-cedca720-1950-48ab-91b4-5dd23a5ff0a0.png)](https://github.com/lyctpu/help/blob/main/bdtest.py)
 
- latex -папка с latex сборками групп
- dbsql_client_v01.exe - скомпилированный python файл клиента работы с mysql бд
- hem.ipynb - кодирование по таблице Хэмминга в Jupyter Notebook
- python_pascal_trans.py - аналоги команд Паскаля в python
- кодирование0.py - универсальный решатель задач на кодирование
- Исполнение Томскэнергосбыт.xlsx - задача на подбор парамметров- 

![mermaid-diagram-2022-12-04-221612](https://user-images.githubusercontent.com/114549805/205499010-2b56a70b-1df6-4016-afbf-b87646f5cdaa.svg)

![mermaid-diagram-2022-12-04-221910](https://user-images.githubusercontent.com/114549805/205499014-28c15bd3-f64c-4aaa-9603-fa207b2c6749.svg)


```mermaid
flowchart LR

A[10] -->|Аттестация| B(11)
B --> C{ЕГЭ}
C -->D{Мальчик}
C -->E{Девочка}
C -->|Не сдал| K[Подготовка]
K -->|Пересдача|C
D -->|Плохо|F[Армия]
D -->|Хорошо|G[ВУЗ]
E -->|Хорошо|G[ВУЗ]
E -->|Плохо|I[Приключения]
```

```mermaid
journey
    title Рабочий день
    section В лицей
      Завтрак: 5: Me
      Дорога: 4: Me
      Пары: 4: Me
    section Из лицея
      Дорога: 3: Me
      Подготовка: 3: Me
      Кодинг: 5: Me
```

```mermaid
gantt
    title План на Декабрь(диаграмма Ганта)
    dateFormat  YYYY-MM-DD
    section Учебные
    Проект 1     :a1, 2022-12-05, 7d
    Проект 2     :a2, after a1, 7d
    Доделка      :a3, after a2, 7d
    Свободное парение : a4, after a3,1d
    section Неучебные
    В лицее неуч.      :2022-12-27  , 3d
    НГ      : 1d
```



```ch
@startuml
start
partition "[[http://plantuml.com partition_name]]" {
    :read doc. on [[http://plantuml.com plantuml_website]];
    :test diagram;
}
end
@enduml
```
