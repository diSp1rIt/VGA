########################################
# Библиотека логирования данных в файл #
########################################


def addLog(text):
    # Добавление строки лога
    with open('vua.log', 'a') as f:
        f.write(text + '\n')


def getLogs():
    # Получение всех строк
    with open('vua.log', 'r') as f:
        return ''.join(f)


def clearAll():
    # Очистка логов
    with open('vua.log', 'w'):
        pass
