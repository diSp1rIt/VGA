import sqlite3 as sql
from Logger import *


class SQL:
    def __init__(self, dbase):
        self.db = dbase
        self.data = None
        self.valid_db = False
        self.fields = 'id, group_id, first_name, last_name, deactivated, ' \
                      'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, ' \
                      'photo_200, photo_400_orig, photo_max, photo_max_orig, online, ' \
                      'online_mobile, ' \
                      'lists, domain, has_mobile, contacts, connections, site, education, ' \
                      'universities, schools, can_post, can_see_all_posts, can_see_audio, ' \
                      'can_write_private_message, status, last_seen, common_count, relation, ' \
                      'relatives'
        try:
            self.con = sql.connect(self.db)
            self.cur = self.con.cursor()
            self.valid_db = True
            addLog('|SQL|: Successful created SQL session')
        except Exception as e:
            addLog('|SQL|: ' + str(e))

    def get_user(self, id):
        if self.valid_db:
            try:
                self.data = self.cur.execute('''SELECT * FROM users WHERE id = ?''',
                                             (id,)).fetchall()
            except Exception as e:
                addLog('|SQL|: ' + str(e))
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def add_user(self, data=None):
        if self.valid_db:
            if data is not None:
                if (int(data[0]),) in self.cur.execute('SELECT id FROM users').fetchall():
                    group_id = self.cur.execute('SELECT group_id FROM users WHERE id = ?',
                                                (data[0],)).fetchall()[0][0]
                    if data[1] not in group_id:
                        self.cur.execute('''UPDATE users
                        SET group_id = ?
                        WHERE id = ?''', (group_id + ', ' + data[1], data[0]))
                        addLog('|SQL|: Data has been updated.')
                    else:
                        addLog('|SQL|: User already exist.')
                else:
                    self.cur.execute('''INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(data))
                    addLog('|SQL|: Added user.')
            else:
                addLog('|SQL|: Data is None.')
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def get_all(self):
        if self.valid_db:
            try:
                return self.cur.execute('''SELECT * FROM users''').fetchall()
            except Exception as e:
                addLog('|SQL|: ' + str(e))
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def get_age(self, group_id=None):
        if self.valid_db:
            if group_id is not None:
                try:
                    return self.cur.execute(f'''SELECT id, first_name, last_name, bdate FROM users
                    WHERE group_id IN (SELECT DISTINCT group_id FROM users
                        WHERE group_id LIKE "%,_{group_id},_%" 
                        OR group_id LIKE "%,_{group_id}" 
                        OR group_id LIKE "{group_id}" 
                        OR group_id LIKE "{group_id},_%") 
                    and bdate LIKE "%.%.%"''').fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
            else:
                try:
                    return self.cur.execute(
                        '''SELECT id, first_name, last_name, bdate FROM users
                        WHERE bdate LIKE "%.%.%"'''
                    ).fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def get_sex(self, group_id=None):
        if self.valid_db:
            if group_id is not None:
                try:
                    return self.cur.execute(f'''SELECT id, first_name, last_name, sex FROM users
                    WHERE group_id IN (SELECT DISTINCT group_id FROM users
                        WHERE group_id LIKE "%,_{group_id},_%" 
                        OR group_id LIKE "%,_{group_id}" 
                        OR group_id LIKE "{group_id}" 
                        OR group_id LIKE "{group_id},_%")''').fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
            else:
                try:
                    return self.cur.execute(
                        'SELECT id, first_name, last_name, sex FROM users'
                    ).fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def get_curent(self, group_id):
        if self.valid_db:
            if group_id is not None:
                try:
                    return self.cur.execute(f'''SELECT * FROM users WHERE group_id IN 
                    (SELECT DISTINCT group_id FROM users
                        WHERE group_id LIKE "%,_{group_id},_%" 
                        OR group_id LIKE "%,_{group_id}" 
                        OR group_id LIKE "{group_id}" 
                        OR group_id LIKE "{group_id},_%")''').fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
            else:
                addLog('|SQL|: Group didn\'t chosen.')
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')

    def get_banned(self, group_id=None):
        if self.valid_db:
            if group_id is not None:
                try:
                    return self.cur.execute(f'''SELECT id, first_name, last_name, deactivated 
                    FROM users
                    WHERE group_id IN (SELECT DISTINCT group_id FROM users
                        WHERE group_id LIKE "%,_{group_id},_%" 
                        OR group_id LIKE "%,_{group_id}" 
                        OR group_id LIKE "{group_id}" 
                        OR group_id LIKE "{group_id},_%") AND deactivated = "banned"''').fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
            else:
                try:
                    return self.cur.execute(
                        '''SELECT id, first_name, last_name, deactivated FROM users
                        WHERE deactivated = "banned"'''
                    ).fetchall()
                except Exception as e:
                    addLog('|SQL|: ' + str(e))
        else:
            addLog('|SQL|: ' + 'DataBase isn\'t valid.')
