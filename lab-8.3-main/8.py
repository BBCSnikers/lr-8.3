DATABASE = { 
'Серёга': 'Омск', 
'Соня': 'Москва', 
'Миша': 'Москва', 
'Дима': 'Челябинск', 
'Алина': 'Красноярск', 
'Егор': 'Пермь', 
'Коля': 'Красноярск' 
} 
def format_friends_count(friends_count): 
    if friends_count == 1: 
        return '1 друг' 
    elif 2 <= friends_count <= 4: 
        return f'{friends_count} друга' 
    else: 
        return f'{friends_count} друзей' 

def process_query(query): 
    elements = query.split(', ') 
    if elements[0] == 'Анфиса':  
        return process_anfisa(elements[1])  
        return 'None' 

def process_anfisa(query): 
    if query == 'сколько у меня друзей?': 
        count = len(DATABASE) 
        format_friends_count(count) 
        return f'У тебя {format_friends_count(count)}.' 
    elif query == 'кто все мои друзья?': 
        friends_string = ', '.join(DATABASE) 
        return f'Твои друзья: {friends_string}' 
    elif query == 'где все мои друзья?': 
        unique_cities = set(DATABASE.values()) 
        cities_string = ', '.join(unique_cities) 
        return f'Твои друзья в городах: {cities_string}' 
    else: 
        return '<неизвестный запрос>' 
print('Привет, я Анфиса!') 
print(process_query('Анфиса, сколько у меня друзей?')) 
print(process_query('Анфиса, кто все мои друзья?')) 
print(process_query('Анфиса, где все мои друзья?')) 
print(process_query('Анфиса, кто виноват?')) 
print(process_query('Соня, ты где?'))
