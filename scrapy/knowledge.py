import sqlite3


class Knowledge:

    def insert_synonymous(self, data):
        conn = sqlite3.connect('sinonimos.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO sinonimos VALUES ('{}', '{}', '{}', '{}')".format(
                data['word'],
                data['url'],
                data['font'],
                data['sinonimos']
            ))
        except sqlite3.IntegrityError:
            print("{} ya existe en la base de datos.".format(data['word']))

        # Save (commit) the changes
        conn.commit()

        c.close()
