##############################
# Библиотека работы с api вк #
##############################


import vk
from Logger import addLog
import time


class VkParser:
    def __init__(self, token):
        # Получение токена
        self.token = token
        # Флаг для проверки валидности токена
        self.valid_token = False
        self.data = None
        self.group_id = None
        self.fields = 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, ' \
                      'photo_200, photo_400_orig, photo_max, photo_max_orig, online, ' \
                      'online_mobile, ' \
                      'lists, domain, has_mobile, contacts, connections, site, education, ' \
                      'universities, schools, can_post, can_see_all_posts, can_see_audio, ' \
                      'can_write_private_message, status, last_seen, common_count, relation, ' \
                      'relatives'
        try:
            # Попытка создания сессии с токеном
            session = vk.Session(self.token)
            self.vk_api = vk.API(session)
            addLog(str(self.vk_api.account.getAppPermissions(v='5.103')))
            addLog('|Parser|: ' + f'Created session with token.')
            self.valid_token = True
        except Exception as e:
            # Если не удалось создать сессию, то создается сессия без токена,
            # что не даёт возможности использования всех функций
            addLog('Parser: ' + str(e))
            session = vk.Session()
            self.vk_api = vk.API(session)
            addLog(str(self.vk_api.account.getAppPermissions()))
            addLog('|Parser|: ' + 'Created default session vk api.')

    def getToken(self):
        # Получение токена, если он валидный
        if self.valid_token:
            return self.token
        addLog('|Parser|: ' + 'Token is invalid.')

    def getDataFromGroup(self, url, offset=None):
        # Попытка получения данных
        self.group_id = url[url.rfind('/') + 1:]
        if self.valid_token:
            try:
                self.data = self.vk_api.groups.getMembers(group_id=self.group_id,
                                                          fields=self.fields,
                                                          v='5.103', offset=offset)
                addLog('|Parser|: ' + 'Successful get data.')
            except Exception as e:
                addLog('|Parser|: ' + str(e))
                self.data = None
        else:
            addLog('|Parser|: ' + 'Token is invalid.')

    def convertData(self):
        if self.data is not None:
            self.data = self.data['items']
            for user in self.data:
                for field in str('id, group_id, first_name, last_name, deactivated, '
                                 + self.fields).split(', '):
                    if field == 'group_id':
                        self.data[self.data.index(user)][field] = self.group_id
                    elif field not in user.keys():
                        self.data[self.data.index(user)][field] = 'NULL'

                self.data[self.data.index(user)] = [str(user[field]) for field in str(
                    'id, group_id, first_name, last_name, deactivated, ' + self.fields).split(', ')]
            addLog('|Parser|: ' + 'Success converted.')
        else:
            addLog('|Parser|: ' + 'Can\'t convert data because program didn\'t get data.')

    def getDataFromGroup_all(self, url):
        self.group_id = url[url.rfind('/') + 1:]
        if self.valid_token:
            try:

                count = self.vk_api.groups.getMembers(group_id=self.group_id,
                                                      fields=self.fields,
                                                      v='5.103', offset=100000000)['count']
                self.data = self.vk_api.groups.getMembers(group_id=self.group_id,
                                                          fields=self.fields,
                                                          v='5.103', offset=count)
                while True:
                    time.sleep(0.06)
                    if count < 1000:
                        self.data['items'].extend(
                            self.vk_api.groups.getMembers(group_id=self.group_id,
                                                          fields=self.fields,
                                                          v='5.103', count=count)['items'])
                        break
                    else:
                        self.data['items'].extend(
                            self.vk_api.groups.getMembers(group_id=self.group_id,
                                                          fields=self.fields,
                                                          v='5.103', offset=count)['items'])
                        count -= 1000
                addLog('|Parser|: ' + 'Successful get data.')
            except Exception as e:
                addLog('|Parser|: ' + str(e))
                self.data = None
        else:
            addLog('|Parser|: ' + 'Token is invalid.')

    def get_count(self, url):
        self.group_id = url[url.rfind('/') + 1:]
        if self.valid_token:
            try:
                return self.vk_api.groups.getMembers(group_id=self.group_id,
                                                     offset=1000000000,
                                                     v='5.103')['count']
            except Exception as e:
                addLog('|Parser|: ' + str(e))
                self.data = None
        else:
            addLog('|Parser|: ' + 'Token is invalid.')
