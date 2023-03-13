from requests import get, post, delete

print(get('http://localhost:8000/api/news').json())
print(get('http://localhost:8000/api/news/1').json())
print(get('http://localhost:8000/api/news/999').json())
print(get('http://localhost:8000/api/news/q').json())
print(post('http://localhost:8000/api/news').json())
print(post('http://localhost:8000/api/news',
           json={'title': 'Заголовок'}).json())
print(post('http://localhost:8000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())
print(delete('http://localhost:8000/api/news/999').json())
print(delete('http://localhost:8000/api/news/1').json())
