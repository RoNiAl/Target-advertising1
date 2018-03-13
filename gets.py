import requests
import IOfile
# Для удобства задаём перменные токену и id приложения с которым работаем
token = '0d8bfe26317c5bdeff47f5df84790c7c98eff0d9c620ee6d2623b3e79729fe2a90047826bf605b343157c'
apl_id = '6395819'

# Функция для проверки групп данных пользователей
# Если группа есть в созданном списке групп, то просто пропускается
# Если группа не обнаружена в списке, то она добавляется в него

def getGroups():
    # Получения списка людей, которых нужно "просканировать"
    listPeople = IOfile.getListPeople()
    # Получение колличества "просканированных людей"
    index = len(listPeople)
    # Инициализация переменной счётчика
    counter = 0
    # Цикл, который получает список групп данных пользователей и обрабатывает его
    while counter < index:
        # Через VK API получаем список групп
        params = {"user_id" : listPeople[counter], "access_token" : token, "count" : "0","v" : "5.73"}
        response = requests.get("https://api.vk.com/method/groups.get", params)
        # Полученный список преобразуем в удобную нам форму для работы с ним
        listUsersGroups = response.json()["response"]["items"]
        # Записываем в переменную список существующих групп
        listGroups = open("listGroups.txt", 'r')
        listIdGroups = listGroups.read()
        listIdGroups = listIdGroups.split('\n')
        listGroups.close()
        # Проверяем, имеется ли группа пользователя уже в списке или нет
        for i in listIdGroups:
            for j in listUsersGroups:
                if i == j:
                    # Если существует, то ПОКА пропускаем
                    continue
                else:
                    # Если не существует, то добавляем
                    listGroups = open("listGroups.txt", 'a')
                    listGroups.write(str(j) + '\n')
                    listGroups.close()
        counter+=1
