todo_list = ['A programming','B SQL','C Python','D Dataiku']
new_list = []
new_dict = {}


def seperate_list(items):
    for item in items:
        new_list.append(item.split())
    return new_list

def create_dict(items):
    for item in items:
        parts = item.split()
        key = parts[0]
        value = " ".join(parts[1:])
        new_dict[key] = value
    return new_dict
    
seperate_list(todo_list)
create_dict(todo_list)
print(new_list)
print(new_dict)
