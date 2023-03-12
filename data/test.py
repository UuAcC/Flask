from requests import get

print(get('http://localhost:8000/api/news').json())
print(get('http://localhost:8000/api/news/1').json())
print(get('http://localhost:8000/api/news/999').json())
print(get('http://localhost:8000/api/news/q').json())