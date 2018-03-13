# Функция которая считывает данных пользователь в массив и возращает его
def getListPeople():
    listPeople = open("listPeople.txt", 'r')
    response = listPeople.read()
    response = response.split('\n')
    listPeople.close()
    return response


