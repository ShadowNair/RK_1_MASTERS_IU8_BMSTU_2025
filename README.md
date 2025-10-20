# RK_1_MASTERS_IU8_BMSTU_2025

## Задача 1: Анализ эффективности технического отдела

### Студент: Аналитик студенческого департамента
### Отдела: Отдел разработки ПО(ID:1)

## Задание:
Проведите комплексный анализ отдела разработки ПО и предоставьте:

1. Базовая статистика
    * Рассчитайте среднюю зарплату, производительность и опыт сотрудников
    * Определите распределение по должностям (Junior/Middle/Senior/Lead)
    * Найдите сотрудников с perfomance_score > 90
2. Финансовый анализ
    * Рассчитайте общий фонд оплаты труда(ФОТ) отдела
    * Сравните ФОТ с бюджетом отдела, определите процент использования
    * Найдите топ-5 самых высокооплачиваемых сотрудников
3. Анализ проектов
    * Определите количество активных и завершенных проектов отдела
    * Рассчитайте средний ROI по проектам с участием отдела
    * Найдите самый прибыльный проект
4. Анализ навыков
    * Составьте матрицу навыков сотрудников (какие технологии используются)
    * Определите наиболее востребованные и дефицитные навыки в отделе
    * Найдите сотрудников со знанием Python и Docker одновременно
5. Рекомендации
    * Предложите меры по повышению эффективности отдела
    * Определите потребность в обучении сотрудников
    * Рассчитайте потенциальный эффект от повышения производительности на 10%

    # Вывод в терминал
    ```
    INITIATING COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS
    ======================================================================

    EXECUTING EMPLOYEES STATIC ANALYSIS...
    ======================================================================
    EMPLOYEE BASIC STATIC ANALYSIS
    ======================================================================

    Total PO employees: 39
    Count employees with performance > 90%: 9 employees

    Average Parameters Employee:
    avarage_salary        :       187329.31
    avarage_perfomance    :       75.94
    avarage_experience    :       12.23

    Department Distribution Position Category:
    Category  Count  Percentage
    senior     23       58.97
    teamlead      8       20.51
    junior      4       10.26
    middle      3        7.69
    trainee      1        2.56

    Personal info employees with performance > 90:
                        full_name gender birth_date              phone                            email                 position
        Федоров Геннадий Кириллович   male 1985-08-11 +7 (578) 572-74-89    геннадий.федоров@technopro.ru                Team Lead
            Беляев Иван Денисович   male 1999-02-08    8 459 874 27 95         иван.беляев@technopro.ru          Ведущий инженер
        Волков Олег Константинович   male 1995-12-28  8 (484) 595-75-74         олег.волков@technopro.ru      Старший разработчик
    Кузнецов Денис Александрович   male 1969-03-25    8 315 678 63 55      денис.кузнецов@technopro.ru Технический руководитель
        Новикова София Владимировна female 1981-10-18   +7 880 264 69 30      софия.новикова@technopro.ru            Архитектор ПО
            Беляев Антон Алексеевич   male 2003-07-02        82294614615        антон.беляев@technopro.ru            Архитектор ПО
            Петров Роман Валерьевич   male 1981-11-29 +7 (363) 907-34-39        роман.петров@technopro.ru       Главный архитектор
    Богданова Екатерина Алексеевна female 1989-07-08     8 827 604 1121 екатерина.богданова@technopro.ru       Главный архитектор
    Павлова Светлана Константиновна female 1995-07-23 +7 (939) 216-12-36    светлана.павлова@technopro.ru Технический руководитель

    EXECUTING FINANCE ANALYSIS...
    ======================================================================
    FINANCE DEPARTMENT ANALYSIS
    ======================================================================

    Total PO employees: 39
    Total Fund of Wages (FOT): 82,229,645 RUB
    Department budget allocated: 5,000,000 RUB
    Budget utilization: 1644.59
                        full_name                 position  salary     FOT
        Федоров Геннадий Кириллович                Team Lead  233748 2804976
            Иванова Вера Геннадьевна                Team Lead  132293 1587516
            Козлова Любовь Игоревна       Стажер-программист  111180  555900
            Беляев Иван Денисович          Ведущий инженер  145922  583688
    Васильева Варвара Константиновна      Инженер-программист  260855 3130260
            Комаров Петр Павлович      Старший разработчик  158862 1906344
            Зайцев Алексей Олегович      Старший разработчик  274716 3296592
            Смирнова Юлия Николаевна      Младший разработчик   98666  394664
        Волков Олег Константинович      Старший разработчик  130257 1563084
        Белова Анастасия Леонидовна          Ведущий инженер  214596 2575152
    Соловьев Николай Константинович           DevOps инженер  197167 2366004
        Андреева Варвара Дмитриевна      Младший разработчик   87341  786069
    Васильев Станислав Георгиевич      Старший разработчик  270154 3241848
            Тарасов Денис Иванович      Старший разработчик  118074 1416888
        Лебедева Анастасия Антоновна Технический руководитель  204051 2448612
        Семенова Полина Вадимовна        Junior QA инженер  189287 1703583
        Кузнецов Денис Александрович Технический руководитель  235401 2824812
    Семенова Александра Борисовна           DevOps инженер  181154 2173848
        Новикова София Владимировна            Архитектор ПО  270500 3246000
        Лебедев Вячеслав Михайлович        Junior QA инженер   96421  482105
            Волкова Елена Вадимовна            Архитектор ПО  244517 2934204
            Попова Диана Артемовна      Head of Development  231578 1852624
            Беляев Антон Алексеевич            Архитектор ПО  150045 1800540
        Беляева Любовь Геннадьевна           DevOps инженер  215680 2588160
            Зайцев Виталий Никитич          Ведущий инженер  187990 2255880
        Васильев Алексей Витальевич          Ведущий инженер  174908 2098896
        Андреев Александр Леонидович       Главный архитектор  185326 2223912
            Иванов Михаил Борисович      Инженер-программист  231301 2775612
        Павлова Анастасия Артемовна          Ведущий инженер  204673 2456076
            Комаров Петр Валерьевич       Главный архитектор  228250 2739000
            Петров Роман Валерьевич       Главный архитектор  196431 2357172
        Комарова Алена Викторовна              Разработчик  183155 2197860
    Богданова Екатерина Алексеевна       Главный архитектор  118841 1426092
            Зайцев Иван Максимович          Ведущий инженер  204625 2455500
            Беляева Галина Никитична                Team Lead  257690 3092280
        Тарасова Ирина Викторовна           DevOps инженер  137182 1371820
    Павлова Светлана Константиновна Технический руководитель  132919 1595028
            Орлова Яна Викторовна          Ведущий инженер  259591 3115092
            Комарова Любовь Олеговна                Team Lead  150496 1805952

    Top 5 Highest Salaries:
                        full_name            position  salary
            Зайцев Алексей Олегович Старший разработчик  274716
        Новикова София Владимировна       Архитектор ПО  270500
    Васильев Станислав Георгиевич Старший разработчик  270154
    Васильева Варвара Константиновна Инженер-программист  260855
            Орлова Яна Викторовна     Ведущий инженер  259591

    EXECUTING PROJECT ANALYSIS...
    ======================================================================
    PO DEPARTMENT PROJECT ANALYSIS
    ======================================================================

    Total projects analyzed: 6

    Average ROI across projects: 3.79%

    Project Status Distribution:
    Status  Count
    active      4
    completed      1

    Most Profitable Project:
    ID: PROJ_0039
    Name: Проект Появление 2943
    Status: completed
    Profit: 824,238 RUB
    Description: Неудобно выкинуть господь. Человечек бочок провинция приятель актриса рабочий. Недостаток мелочь упорно прошептать разуметься желание.

    EXECUTING SKILLS ANALYSIS...
    ======================================================================
    EMPLOYEE SKILLS ANALYSIS
    ======================================================================

    Total employees analyzed for skills: 39

    Skill Matrix (+: has skill, -: no skill):
                                ФИО AWS C++ Docker Git Java JavaScript Kubernetes Linux Python SQL
        Федоров Геннадий Кириллович   +   +      -   +    +          -          -     -      -   -
            Иванова Вера Геннадьевна   -   -      -   -    +          -          -     +      -   -
            Козлова Любовь Игоревна   +   +      -   +    -          -          -     +      -   -
            Беляев Иван Денисович   -   -      -   -    +          +          -     -      +   -
    Васильева Варвара Константиновна   -   -      -   -    +          +          +     -      +   -
            Комаров Петр Павлович   -   +      -   +    -          +          -     +      -   -
            Зайцев Алексей Олегович   +   +      +   -    -          -          +     -      -   +
            Смирнова Юлия Николаевна   -   -      +   -    -          -          +     +      +   +
        Волков Олег Константинович   -   -      +   +    -          +          -     -      +   -
        Белова Анастасия Леонидовна   -   -      -   +    -          +          +     -      +   -
    Соловьев Николай Константинович   -   -      +   -    +          +          -     -      -   +
        Андреева Варвара Дмитриевна   -   +      -   +    -          +          +     -      -   -
    Васильев Станислав Георгиевич   -   +      +   -    +          -          +     +      -   -
            Тарасов Денис Иванович   +   +      -   -    +          -          -     -      +   -
        Лебедева Анастасия Антоновна   -   +      -   -    -          +          +     -      -   -
        Семенова Полина Вадимовна   +   -      -   -    +          -          -     -      -   -
        Кузнецов Денис Александрович   -   +      +   -    -          -          -     +      +   -
    Семенова Александра Борисовна   -   +      -   -    +          -          -     +      +   -
        Новикова София Владимировна   -   +      -   +    -          -          -     -      -   +
        Лебедев Вячеслав Михайлович   +   -      -   +    +          -          +     +      -   -
            Волкова Елена Вадимовна   -   -      +   -    -          -          +     -      -   -
            Попова Диана Артемовна   -   -      -   +    -          -          -     -      -   +
            Беляев Антон Алексеевич   -   -      -   -    -          -          +     +      +   -
        Беляева Любовь Геннадьевна   -   +      -   -    +          +          -     -      -   +
            Зайцев Виталий Никитич   -   +      -   -    -          -          -     -      +   -
        Васильев Алексей Витальевич   -   +      -   -    -          +          -     -      -   +
        Андреев Александр Леонидович   -   +      +   -    +          +          -     -      -   -
            Иванов Михаил Борисович   +   +      +   +    -          -          -     -      +   -
        Павлова Анастасия Артемовна   +   -      +   -    -          -          -     +      -   -
            Комаров Петр Валерьевич   -   -      -   +    -          -          -     -      -   +
            Петров Роман Валерьевич   -   +      +   -    -          -          -     -      -   -
        Комарова Алена Викторовна   -   -      +   -    -          -          +     -      -   +
    Богданова Екатерина Алексеевна   -   +      -   -    +          +          -     +      -   -
            Зайцев Иван Максимович   +   -      -   -    +          -          -     -      +   -
            Беляева Галина Никитична   -   +      +   -    -          +          +     -      -   +
        Тарасова Ирина Викторовна   -   -      -   -    +          -          -     +      -   -
    Павлова Светлана Константиновна   -   -      +   +    -          +          -     +      +   -
            Орлова Яна Викторовна   +   -      -   +    -          +          -     +      +   -
            Комарова Любовь Олеговна   -   +      +   +    +          -          -     +      -   -

    Most In-Demand Skills (Top 5):
    1. C++
    2. Java
    3. Linux
    4. JavaScript
    5. Docker

    Rare Skills (≤1 employee):
    No rare skills found.

    Employees with Python and Docker: 5
                        full_name                 position
        Смирнова Юлия Николаевна      Младший разработчик
        Волков Олег Константинович      Старший разработчик
    Кузнецов Денис Александрович Технический руководитель
            Иванов Михаил Борисович      Инженер-программист
    Павлова Светлана Константиновна Технический руководитель

    GENERATING STRATEGIC RECOMMENDATIONS...
    ======================================================================
    STRATEGIC RECOMMENDATIONS FOR PO DEPARTMENT
    ======================================================================

    Measures to Improve Department Efficiency:
    1. Повысить среднюю производительность через менторство и оптимизацию процессов

    Identified Training Needs:
    1. Потребность в массовом обучении не выявлена. Рекомендуется индивидуальное развитие.

    Potential Impact of +10% Productivity:
    • Потенциальная экономия ФОТ при росте производительности на 10%: 7,400,668 RUB
    • Допущение: 10% рост производительности позволяет снизить фонд оплаты труда на 9% при сохранении объёма работ
    ======================================================================
    COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS SUMMARY
    ======================================================================

    EMPLOYEE OVERVIEW:
    • Total Employees: 39
    • High Performers (>90%): 9
    • Avg. Salary: 187,329 RUB
    • Avg. Performance: 75.9%
    • Avg. Experience: 12.2 years

    POSITION DISTRIBUTION:
    • senior: 23 (58.97%)
    • teamlead: 8 (20.51%)
    • junior: 4 (10.26%)
    • middle: 3 (7.69%)
    • trainee: 1 (2.56%)

    FINANCIAL METRICS:
    • Total FOT (Payroll): 82,229,645 RUB
    • Department Budget: 5,000,000 RUB
    • Budget Utilization: 1644.59%

    TOP 5 HIGHEST SALARIES:
                        full_name            position  salary
            Зайцев Алексей Олегович Старший разработчик  274716
        Новикова София Владимировна       Архитектор ПО  270500
    Васильев Станислав Георгиевич Старший разработчик  270154
    Васильева Варвара Константиновна Инженер-программист  260855
            Орлова Яна Викторовна     Ведущий инженер  259591

    PROJECT METRICS:
    • Total Projects: 6
    • Average ROI: 3.79%

    PROJECT STATUS DISTRIBUTION:
    Status  Count
    active      4
    completed      1

    MOST PROFITABLE PROJECT:
    • ID: PROJ_0039
    • Name: Проект Появление 2943
    • Status: completed
    • Profit: 824,238 RUB
    • Description: Неудобно выкинуть господь. Человечек бочок провинция приятель актриса рабочий. Недостаток мелочь упорно прошептать разуметься желание.

    SKILLS OVERVIEW:
    • Total Employees: 39
    • Python + Docker Experts: 5

    STRATEGIC RECOMMENDATIONS:

    Measures to Improve Efficiency:
    1. Повысить среднюю производительность через менторство и оптимизацию процессов

    Training Needs:
    1. Потребность в массовом обучении не выявлена. Рекомендуется индивидуальное развитие.

    Potential Impact of +10% Productivity:
    • Estimated FOT savings: 7,400,668 RUB
    • Assumption: 10% рост производительности позволяет снизить фонд оплаты труда на 9% при сохранении объёма работ
  ```

  # Logi
## Basic
```
2025-10-20 06:21:30,894 - Basic Statistics - INFO - Software Infrastructure Analysis System initialization started
2025-10-20 06:21:30,894 - Basic Statistics - INFO - Starting data loading process from JSON file
2025-10-20 06:21:30,912 - Basic Statistics - INFO - Data successfully loaded from file: {}
2025-10-20 06:21:30,912 - Basic Statistics - INFO - Starting data processing for Basic Statistics
2025-10-20 06:21:30,912 - Basic Statistics - INFO - Start create dataframe department PO
2025-10-20 06:21:30,915 - Basic Statistics - INFO - Start create dataframe employees PO
2025-10-20 06:21:30,919 - Basic Statistics - INFO - Start create dataframe project PO
2025-10-20 06:21:31,002 - Basic Statistics - INFO - Starting Basic statics analysis
2025-10-20 06:21:31,002 - Basic Statistics - INFO - Calculating avarage parametrs
2025-10-20 06:21:31,003 - Basic Statistics - INFO - Count Junior/Middle/Senior/TeamLead level
2025-10-20 06:21:31,003 - Basic Statistics - INFO - Create column for category employee from position
2025-10-20 06:21:31,004 - Basic Statistics - INFO - Define employees with perfomance_score > 90
2025-10-20 06:21:31,008 - Basic Statistics - INFO - Basic Statistics analysis completed successfully
```
## Finance
```
2025-10-20 06:21:30,920 - Finance Departament - INFO - Software Infrastructure Analysis System initialization started
2025-10-20 06:21:30,920 - Finance Departament - INFO - Starting data loading process from JSON file
2025-10-20 06:21:30,938 - Finance Departament - INFO - Data successfully loaded from file: {}
2025-10-20 06:21:30,938 - Finance Departament - INFO - Starting data processing for Finance Departament
2025-10-20 06:21:30,938 - Finance Departament - INFO - Start create dataframe department PO
2025-10-20 06:21:30,939 - Finance Departament - INFO - Start create dataframe employees PO
2025-10-20 06:21:30,943 - Finance Departament - INFO - Start create dataframe project PO
2025-10-20 06:21:31,008 - Finance Departament - INFO - Starting Finance Departament analysis
2025-10-20 06:21:31,008 - Finance Departament - INFO - Calculating avarage parametrs
2025-10-20 06:21:31,010 - Finance Departament - INFO - Comparing FOT with department budget
2025-10-20 06:21:31,010 - Finance Departament - INFO - Retrieving top 5 highest salaries
2025-10-20 06:21:31,014 - Finance Departament - INFO - Finance analyze analysis completed successfully
```
## Project
```
2025-10-20 06:21:30,944 - Project - INFO - Software Infrastructure Analysis System initialization started
2025-10-20 06:21:30,944 - Project - INFO - Starting data loading process from JSON file
2025-10-20 06:21:30,959 - Project - INFO - Data successfully loaded from file: {}
2025-10-20 06:21:30,959 - Project - INFO - Starting data processing for Project
2025-10-20 06:21:30,959 - Project - INFO - Start create dataframe department PO
2025-10-20 06:21:30,960 - Project - INFO - Start create dataframe employees PO
2025-10-20 06:21:30,963 - Project - INFO - Start create dataframe project PO
2025-10-20 06:21:31,014 - Project - INFO - Starting Project analysis
2025-10-20 06:21:31,014 - Project - INFO - Analyzing project status distribution
2025-10-20 06:21:31,015 - Project - INFO - Calculating average ROI for all projects
2025-10-20 06:21:31,015 - Project - INFO - Identifying project with highest profit
2025-10-20 06:21:31,016 - Project - INFO - Project analysis completed successfully
```
## Skills
```
2025-10-20 06:21:30,963 - Skills - INFO - Software Infrastructure Analysis System initialization started
2025-10-20 06:21:30,963 - Skills - INFO - Starting data loading process from JSON file
2025-10-20 06:21:30,979 - Skills - INFO - Data successfully loaded from file: {}
2025-10-20 06:21:30,979 - Skills - INFO - Starting data processing for Skills
2025-10-20 06:21:30,979 - Skills - INFO - Start create dataframe department PO
2025-10-20 06:21:30,980 - Skills - INFO - Start create dataframe employees PO
2025-10-20 06:21:30,983 - Skills - INFO - Start create dataframe project PO
2025-10-20 06:21:31,016 - Skills - INFO - Starting Skills analysis
2025-10-20 06:21:31,016 - Skills - INFO - Building employee skill matrix
2025-10-20 06:21:31,018 - Skills - INFO - Analyzing skill demand and rarity
2025-10-20 06:21:31,019 - Skills - INFO - Searching for Python + Docker experts
2025-10-20 06:21:31,025 - Skills - INFO - Skills analysis completed successfully
```
## Recommendation
```
2025-10-20 06:21:30,983 - Recommendations - INFO - Software Infrastructure Analysis System initialization started
2025-10-20 06:21:30,983 - Recommendations - INFO - Starting data loading process from JSON file
2025-10-20 06:21:30,998 - Recommendations - INFO - Data successfully loaded from file: {}
2025-10-20 06:21:30,998 - Recommendations - INFO - Starting data processing for Recommendations
2025-10-20 06:21:30,998 - Recommendations - INFO - Start create dataframe department PO
2025-10-20 06:21:30,999 - Recommendations - INFO - Start create dataframe employees PO
2025-10-20 06:21:31,002 - Recommendations - INFO - Start create dataframe project PO
2025-10-20 06:21:31,025 - Recommendations - INFO - Starting Recommendations analysis
2025-10-20 06:21:31,025 - Recommendations - INFO - Generating efficiency improvement recommendations
2025-10-20 06:21:31,026 - Recommendations - INFO - Identifying employee training needs
2025-10-20 06:21:31,026 - Recommendations - INFO - Calculating financial impact of productivity increase
2025-10-20 06:21:31,026 - Recommendations - INFO - Recommendations analysis completed successfully
```


