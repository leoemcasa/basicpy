
def f_add(task, todo):
    todo.append(task)

def f_undo(todo, redo):
    if not todo:
        print('nada a desfazer')
        return
    #lasttd = todo.pop()
    redo.append(todo.pop())

def f_redo(todo, redo):
    if not redo:
        print('nada a refazer')
        return
    lastrd = redo.pop()
    todo.append(lastrd)

if __name__ == '__main__':
    todo = []
    redo = []

    while True:
        task = input('Tarefa [(l)ist, (u)ndo, (r)edo, (q)uit]: ')
        if task == 'q':
            break
        elif task == 'l':
           # print(todo)
            pass
            #continue
        elif task == 'u':
            f_undo(todo, redo)
           # continue
        elif task == 'r':
            f_redo(todo, redo)
           # continue
        else:
            f_add(task, todo)
        print(f'{todo}')
