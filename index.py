import facebook
import requests

access_token = "EAAGdXfsupUEBAI6GSZAWkYeg9JERRPZBqeZBj1WfScNJWtqpwutz5DRh6d3t3K2b483DZAJ5XZBvDkgiENM7FnQukNiA6ZB5t9815uYYwj2Cs15ZC4KDkbb7K4R0Yz72RcxqE8dNMZAVrPbAX0gPvXX4S7n6FFDFSo238DlPP1QWSQKuROngBhwBkceOfgBgZBbcZD"
graph = facebook.GraphAPI(access_token=access_token, version="2.1")


resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
