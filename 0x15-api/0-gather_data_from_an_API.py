#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        userid = int(sys.argv[1])
    
    totalTask = 0
    completeTask = 0
    titleTask = ''
    name = ''

    r = requests.get('https://jsonplaceholder.typicode.com/users')
    try:
        users = r.json()
        if len(users) > 0:
            for user in users:
                if user['id'] == userid:
                    name = user['name']
        else:
            print("Not result")
    except ValueError:
        print("Not a valid JSON")


    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    try:
        todo = r.json()
        if len(todo) > 0:
            for task in todo:
                if task['userId'] == userid:
                    if task['completed'] == True:
                        if completeTask > 0:
                            titleTask += '\n'
                        completeTask += 1
                        titleTask = titleTask + '\t' + task['title']
                    totalTask += 1
        else:
            print("Not result")
    except ValueError:
        print("Not a valid JSON")

    print('Employee {} is done with tasks({}/{}):'.format(name, completeTask, totalTask))
    print(titleTask)
