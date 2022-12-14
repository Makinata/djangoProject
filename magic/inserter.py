import sqlite3

conn = sqlite3.connect(r'C:\Users\rogev\Documents\!Учеба\!Дз\Архитектура развертывания\курсач\app\db.sqlite3')
cur = conn.cursor()

cur.execute("INSERT INTO place VALUES('Концертный зал', 200, 'Аудио, свет')")
cur.execute("INSERT INTO place VALUES('Коворкинг', 50, 'Проектор')")
cur.execute("INSERT INTO place VALUES('Спортивный зал', 50, 'Спортинвентарь')")
cur.execute("INSERT INTO place VALUES('Площадь', 500, NULL)")

cur.execute("INSERT INTO event_type VALUES('Концерт')")
cur.execute("INSERT INTO event_type VALUES('Лекция')")
cur.execute("INSERT INTO event_type VALUES('Соревнование')")
cur.execute("INSERT INTO event_type VALUES('Прочее')")

cur.execute("INSERT INTO event VALUES('Голоса и танцы 2022', 'Концерт', 'Концертный зал', '10.11.2022', '02:30:00', 'True')")
cur.execute("INSERT INTO event VALUES('Квартирник 2022', 'Концерт', 'Концертный зал', '15.11.2022', '02:00:00', 'False')")
cur.execute("INSERT INTO event VALUES('Презентация ВК: советы по резюме 2022', 'Лекция', 'Коворкинг', '07.11.2022', '01:30:00', 'False')")
cur.execute("INSERT INTO event VALUES('КРОК: направления стажировки 2022', 'Лекция', 'Коворкинг', '17.11.2022', '01:30:00', 'True')")
cur.execute("INSERT INTO event VALUES('Волейбол 2022 отборочный тур 1', 'Соревнование', 'Спортивный зал', '22.11.2022', '03:00:00', 'True')")
cur.execute("INSERT INTO event VALUES('Волейбол 2022 отборочный тур 2', 'Соревнование', 'Спортивный зал', '29.11.2022', '03:00:00', 'True')")
cur.execute("INSERT INTO event VALUES('МИРЭА МЧС осень 2022', 'Прочее', 'Площадь', '29.11.2022', '03:00:00', 'False')")

cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('Голоса и танцы 2022', 'Двигатель Арсений Витальевич', 89154003021)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('Квартирник 2022', 'Поворотник Илья Романович', 89154003022)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('Презентация ВК: советы по резюме 2022', 'Турбина Мария Тимофеевна', 89154003023)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('КРОК: направления стажировки 2022', 'Насос Петр Иванович', 89154003024)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('Волейбол 2022 отборочный тур 1', 'Подшипник Николай Евгеньевич', 89154003025)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('Волейбол 2022 отборочный тур 2', 'Подшипник Николай Евгеньевич', 89154003026)")
cur.execute("INSERT INTO organizer(event_title, fullname, contact_phone) VALUES('МИРЭА МЧС осень 2022', 'Колесо Сергей Сергеевич', 89154003027)")

cur.execute("INSERT INTO guest(event_title, fullname, contact_phone) VALUES('Презентация ВК: советы по резюме 2022', 'Важный Григорий Петрович', 89154003028)")
cur.execute("INSERT INTO guest(event_title, fullname, contact_phone) VALUES('КРОК: направления стажировки 2022', 'Неважный Виталий Васильевич', 89154003029)")
cur.execute("INSERT INTO guest(event_title, fullname, contact_phone) VALUES('МИРЭА МЧС осень 2022', 'Огонь Роза Александровна', 89154003030)")

cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Голоса и танцы 2022', 'Мороз Лилия Алексеевна', 89154003031, 'ИНБО-34-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('МИРЭА МЧС осень 2022', 'Мороз Лилия Алексеевна', 89154003031, 'ИНБО-34-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Презентация ВК: советы по резюме 2022', 'Глупый Николай Николаевич', 89154003032, 'ИКБО-99-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('КРОК: направления стажировки 2022', 'Глупый Николай Николаевич', 89154003032, 'ИКБО-99-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Волейбол 2022 отборочный тур 1', 'Умный Олег Олегович', 89154003033, 'ИКБО-99-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Волейбол 2022 отборочный тур 2', 'Умный Олег Олегович', 89154003033, 'ИКБО-99-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Голоса и танцы 2022', 'Барабан Егор Егорович', 89154003034, 'ИВБО-90-20')")
cur.execute("INSERT INTO participant(event_title, fullname, contact_phone, pgroup) VALUES('Квартирник 2022', 'Барабан Егор Егорович', 89154003034, 'ИВБО-90-20')")