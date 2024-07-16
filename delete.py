# def update_todo(todo_id: int, new_name: str, new_description: str):
#     update_todo_query = '''
#         UPDATE todo
#         SET name = %s, description = %s
#         WHERE id = %s;
#     '''
#     cursor.execute(update_todo_query, (new_name, new_description, todo_id))
#     conn.commit()
#     return Response('Todo updated successfully', 200)
