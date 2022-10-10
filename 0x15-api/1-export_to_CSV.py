#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

    if len(sys.argv) > 1:
        userid = int(sys.argv[1])

    totalTask = 0
    data = []
    name = ''

    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(userid))
    name = users.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    try:
        todo = r.json()
        if len(todo) > 0:
            for task in todo:
                if task['userId'] == userid:
                    if totalTask > 0:
                        data.append([str(task['userId']), name, str(task['completed']), task['title']])
                    totalTask += 1
        else:
            print("Not result")
    except ValueError:
        print("Not a valid JSON")

    with open(str(userid) + '.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
