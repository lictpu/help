## Учебно-справочный репозиторий лицеистов ТПУ
[![N|Solid](https://portal.tpu.ru/f_lyceum/img/main-logo.jpg)](https://portal.tpu.ru/lyceum)

 

## Состав

- latex -папка с latex сборками групп
- bdtest.py - код создания и раоты с БД sqlite
- dbsql_client_v01.exe - скомпилированный python файл клиента работы с mysql бд
- ege_templ.py - шаблоны кода для задач ЕГЭ 
- hem.ipynb - кодирование по таблице Хэмминга в Jupyter Notebook
- python шпора.ipynb - функции python c примерами в Jupyter Notebook на DeepNote
- python_pascal_trans.py - аналоги команд Паскаля в python
- кодирование0.py - универсальный решатель задач на кодирование
- Исполнение Томскэнергосбыт.xlsx - задача на подбор парамметров- 

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
    title План на Декабрь(диаграма Гранта)
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

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectivness<br/>and eatures
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```
