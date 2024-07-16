import psycopg2
from models import UserRole, UserStatus
import utils
from session import Session
from utils import Response


# def connect(): # connect func
#     conn = psycopg2.connect(database = 'lesson',user = 'postgres',host = 'localhost',
#                             port = 5432,password = '703')


# def delete_user(username: str):
#     delete_user_query = '''
#         DELETE FROM users
#         WHERE username = %s;
#     '''
#     cursor.execute(delete_user_query, (username,))
#     conn.commit()
#     return ('User deleted',200)


#@commit
# def delete_todo(todo_id: int):
#     delete_todo_query = '''
#         DELETE FROM todo
#         WHERE id = %s;
#     '''
#     cursor.execute(delete_todo_query, (todo_id,))
#     conn.commit()
#     return Response('Succes delete', 200)