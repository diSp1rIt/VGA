########################################
# Библиотека логирования данных в файл #
########################################


def addLog(text):
    # Добавление строки лога
    with open('apigv.log', 'a') as f:
        f.write(text + '\n')


def getLogs():
    # Получение всех строк
    with open('apigv.log', 'r') as f:
        return ''.join(f)


def clearAll():
    # Очистка логов
    with open('apigv.log', 'w'):
        pass
