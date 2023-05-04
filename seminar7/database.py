path = r'data.txt'

def get_info():
    with open(path, 'r') as data:
        data = data.read().split()
        return data

def save_info(a):
    b = str(a)
    a = str(a)
    with open(path, 'w') as data:
        data.write(a)
