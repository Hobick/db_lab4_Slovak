-- Вивести кількість героїв кожного атрибуту
select attribute, count(*) from hero
group by attribute;
-- Вивести кількість греоїв кожого типу атаки
select attack_type, count(*) from hero
group by attack_type;
-- Вивести залежність кількості ролей від атрибуту
select attribute, count(*) from play_role, hero
where hero.name = play_role.name
group by attribute;