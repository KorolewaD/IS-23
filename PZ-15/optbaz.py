import sqlite3 as sq
import info_optbaz
with sq.connect('optbaz.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS tovari (
        id_tovara INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        opisanie TEXT NOT NULL,
        edeniza izmerenia TEXT NOT NULL
    )""")
# with sq.connect('optbaz.db') as con:
#     cur = con.cursor()
#     con.executemany("INSERT INTO tovari VALUES (?,?,?,?)", info_optbaz.tovari)
#     con.commit()

with sq.connect('optbaz.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS magazini (
        id_magazina INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        adres TEXT NOT NULL,
        telefon TEXT NOT NULL
    )""")
# with sq.connect('optbaz.db') as con:
#      cur = con.cursor()
#      con.executemany("INSERT INTO magazini VALUES (?,?,?,?)", info_optbaz.magazini)
#      con.commit()

with sq.connect('optbaz.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS zayavki_magazinov (
        id_zayavki INTEGER PRIMARY KEY AUTOINCREMENT,
        id_magazina INTEGER NOT NULL,
        data_zayavki DATE NEXN NOT NULL,
        FOREIGN KEY (id_magazina) REFERENCES magazini(id_magazina)
    )""")
# with sq.connect('optbaz.db') as con:
#      cur = con.cursor()
#      con.executemany("INSERT INTO zayavki_magazinov VALUES (?,?,?)", info_optbaz.zayavki_magazinov)
#      con.commit()

with sq.connect('optbaz.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS kolvo_tovarov(
        id_kolva INTEGER PRIMARY KEY AUTOINCREMENT,
        kolvo INTEGER NOT NULL,
        id_tovara INTEGER NOT NULL,
        FOREIGN KEY (id_tovara) REFERENCES tovari(id_tovara)
    )""")
# with sq.connect('optbaz.db') as con:
#      cur = con.cursor()
#      con.executemany("INSERT INTO kolvo_tovarov VALUES (?,?,?)", info_optbaz.kolvo_tovarov)
#      con.commit()



with sq.connect('optbaz.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS sclad(
        id_sclada INTEGER PRIMARY KEY AUTOINCREMENT,
        id_magazina INTEGER NOT NULL,
        id_tovara INTEGER NOT NULL,
        kolvo_na_sclade INTEGER,
        FOREIGN KEY (id_magazina) REFERENCES magazini(id_magazina),
        FOREIGN KEY (id_tovara) REFERENCES tovari(id_tovara)
    )""")
# with sq.connect('optbaz.db') as con:
#     cur = con.cursor()
#     con.executemany("INSERT INTO sclad VALUES (?,?,?,?)", info_optbaz.sclad)
#     con.commit()
# Была добавлена таблица "Sclad" в виду невозможности создания запроса без ее существования
with sq.connect('optbaz.db') as con: 
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
        id_sostav INTEGER PRIMARY KEY AUTOINCREMENT,
        id_zayavki INTEGER,
        id_tovara INTEGER,
        kolichestvo INTEGER,
        FOREIGN KEY (id_tovara) REFERENCES tovari (id_tovara),
        FOREIGN KEY (id_zayavki) REFERENCES zayavki_magazinov (id_zayavki)
)""")
# with sq.connect('optbaz.db') as con:
#     cur = con.cursor()
#     con.executemany("INSERT INTO sostav VALUES (?,?,?,?)", info_optbaz.sostav)
#     con.commit()


# SQL-запросы на выборку данных:

with sq.connect('optbaz.db') as con:
    cur = con.cursor()
    print('1. Вывести список всех товаров и их описания:')
    cur.execute("SELECT name, opisanie FROM tovari")
    res1 = cur.fetchall()
    print(res1)
    print('2. Вывести список всех магазинов и их адресов:')
    cur.execute("SELECT name, adres FROM magazini")
    res2 = cur.fetchall()
    print(res2)
    print('3. Вывести список всех заявок магазинов и даты, на которые они были поданы:')
    cur.execute("SELECT id_zayavki, data_zayavki FROM zayavki_magazinov")
    res3 = cur.fetchall()
    print(res3)
    print('4. Вывести список товаров и количество их наличия на складе:')
    cur.execute("SELECT id_tovara, kolvo FROM kolvo_tovarov")
    res4 = cur.fetchall()
    print(res4)
    print('5. Вывести список товаров и количество их наличия на складе в порядке убывания количества:')
    cur.execute("SELECT id_tovara, kolvo FROM kolvo_tovarov ORDER BY kolvo DESC")
    res5 = cur.fetchall()
    print(res5)
    print('6. Вывести список всех заявок магазинов и товаров, которые были в них заказаны:')
    cur.execute("SELECT id_zayavki, id_tovara FROM sostav") 
    res6 = cur.fetchall()
    print(res6)
    print('7. Вывести список всех товаров, у которых на складе количество меньше минимально допустимого(15):')
    cur.execute("SELECT id_tovara, kolvo FROM kolvo_tovarov WHERE kolvo < 15")
    res7 = cur.fetchall()
    print(res7)
    print('8. Вывести список всех заявок магазинов, которые были сделаны в определенный период времени(2023.02.20-2023.03.29):')
    cur.execute("SELECT id_zayavki FROM zayavki_magazinov WHERE data_zayavki BETWEEN '2023.02.20' AND '2023.03.29'")
    res8 = cur.fetchall()
    print(res8)
    print('9. Вывести список всех магазинов, у которых суммарное количество товаров на складе меньше заданного значения(1000):')
    cur.execute("SELECT id_magazina FROM sclad WHERE kolvo_na_sclade < 1000")
    res9 = cur.fetchall()
    print(res9)


# SQL-запросы на обновление данных из БД:
with sq.connect('optbaz.db') as con:
    cur = con.cursor()
    #1. Обновить количество товара на складе для конкретного товара
    cur.execute("UPDATE sclad SET kolvo_na_sclade = 12345 WHERE kolvo_na_sclade = 123")
    #2. Обновить название товара в заявке
    #3. Обновить количество товара в заявке
    # Задания 2 и 3 преподаватель разрешил не делать
    #4. Обновить адрес магазина, который подал заявку
    cur.execute("UPDATE magazini SET adres='пл. Чехова, 47' WHERE id_magazina=(SELECT id_magazina FROM zayavki_magazinov WHERE id_zayavki=513)")
    #5. Обновить дату заявки для конкретного магазина
    cur.execute("UPDATE zayavki_magazinov SET data_zayavki='2023.02.05' WHERE id_magazina = 22")
    #6. Обновить количество товара на складе для нескольких товаров
    cur.execute("UPDATE sclad SET kolvo_na_sclade=656565 WHERE (id_tovara = 1) or (id_tovara = 5)")
    #7. Обновить описание товара и количество на складе для конкретного товара
    cur.execute("UPDATE tovari SET opisanie='ягода' WHERE id_tovara = 7")
    cur.execute("UPDATE sclad SET kolvo_na_sclade=950 WHERE id_tovara = 7")
    #8. Обновление количества товаров на складе, учитывая выполненную заявку магазина
    cur.execute("UPDATE sclad SET kolvo_na_sclade=((SELECT kolvo_na_sclade FROM sclad WHERE id_tovara=(SELECT id_tovara FROM sostav WHERE id_zayavki=513)) - (SELECT SUM(kolichestvo) FROM sostav WHERE id_tovara=(SELECT id_tovara FROM sostav WHERE id_zayavki=513))) WHERE id_tovara=(SELECT id_tovara FROM sostav WHERE id_zayavki=513)")    
    #9. Обновление количества товаров на складе, учитывая выполненную заявку магазина с учетом конкретного товара
    cur.execute("UPDATE sclad SET kolvo_na_sclade=((SELECT kolvo_na_sclade FROM sclad WHERE id_tovara=1) - (SELECT SUM(kolichestvo) FROM sostav WHERE id_tovara=1)) WHERE id_tovara=1")
    #10. Обновить название магазина, который подал заявку, и адрес магазина для конкретной заявки
    cur.execute("UPDATE magazini SET name='Крупинка', adres='пр. Бубновый, д.33' WHERE id_magazina=(SELECT id_magazina FROM zayavki_magazinov WHERE id_zayavki = 517)")
    #11. Обновить название магазина в заявке, которую подал конкретный магазин
    # Отказ от задания 11
    #12. Обновить адрес магазина и количество товара в заявке для конкретного товара
    cur.execute("UPDATE magazini SET adres='пр. Петропаловский, 16' WHERE id_magazina= (SELECT id_magazina FROM zayavki_magazinov WHERE id_zayavki=(SELECT id_zayavki FROM sostav WHERE id_tovara=6))")
    cur.execute("UPDATE sostav SET kolichestvo=896 WHERE id_tovara=10")
    #13. Обновить описание товара и количество на складе для нескольких товаров
    cur.execute("UPDATE tovari SET opisanie='Дерево' WHERE (id_tovara = 2) or (id_tovara=3)")
    cur.execute("UPDATE sclad SET kolvo_na_sclade=99999 WHERE (id_tovara = 2) or (id_tovara=3)")


# SQL-запросы на удаление данных из БД:
with sq.connect('optbaz.db') as con:
    cur = con.cursor()
    # 1. Удаление заявки магазина и соответствующих записей в таблице состава
    cur.execute("DELETE FROM zayavki_magazinov WHERE id_zayavki=511")
    cur.execute("DELETE FROM sostav WHERE id_zayavki=511")
    # 2. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, не имеющим заявок в таблице "Состав"
    cur.execute("DELETE FROM sclad WHERE id_tovara NOT IN (SELECT id_tovara FROM sostav)")
    # 3. Удалить из таблицы "Заявки магазинов" все заявки магазинов, адрес которых начинается на "ул. Ленина"
    cur.execute("DELETE FROM zayavki_magazinov WHERE id_magazina IN (SELECT id_magazina FROM magazini WHERE adres LIKE 'ул. Ленина%')")
    # 4. Удалить из таблицы "Состав" записи, соответствующие товарам, которых нет на складе (количество = 0)
    cur.execute("DELETE FROM sostav WHERE id_tovara IN (SELECT id_tovara FROM sclad WHERE kolvo_na_sclade=0)")
    # 5. Удалить из таблицы "Магазины" магазины, в которых не было заявок в течение последнего месяца
    cur.execute("DELETE FROM magazini WHERE id_magazina NOT IN (SELECT id_magazina FROM zayavki_magazinov WHERE data_zayavki BETWEEN '2023.02.05' AND '2023.04.07')")
    # 6. Удалить из таблицы "Товары" товары, которые не были заказаны ни разу
    cur.execute("DELETE FROM tovari WHERE id_tovara NOT IN (SELECT id_tovara FROM sostav)")
    # 7. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, которые не были заказаны ни разу
    cur.execute("DELETE FROM sclad WHERE id_tovara NOT IN (SELECT id_tovara FROM sostav)")
    # 8. Удалить из таблицы "Состав" записи, соответствующие заявкам, которые были поданы более месяца назад
    cur.execute("DELETE FROM sostav WHERE id_zayavki IN (SELECT id_zayavki FROM zayavki_magazinov WHERE data_zayavki BETWEEN '2023-01-01' AND '2023-03-31')")

