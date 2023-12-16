import psycopg2
from init import get_pass

username = 'postgres'
password = get_pass()
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
select attribute, count(*) from hero
group by attribute
'''
query_2 = '''select attack_type, count(*) from hero
group by attack_type;
'''

query_3 = '''
select attribute, count(*) from play_role, hero
where hero.name = play_role.name
group by attribute;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    print('1. Вивести кількість героїв кожного атрибуту \n')
    cur.execute(query_1)

    for row in cur:
        print(row)

    print('2. Вивести кількість греоїв кожого типу атаки \n')
    cur.execute(query_2)

    for row in cur:
        print(row)

    print('3. Вивести залежність кількості ролей від атрибуту \n')
    cur.execute(query_3)

    for row in cur:
        print(row)
