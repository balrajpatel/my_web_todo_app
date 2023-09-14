FILEPATH= 'todo.txt'

def open_fn(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todo_local=file_local.readlines()
        return todo_local


def write_todo(todo_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)


if __name__=='__main__':
    local=open_fn()
    print(local)