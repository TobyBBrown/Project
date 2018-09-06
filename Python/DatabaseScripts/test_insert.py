import unittest
from data_extract_and_insert import *
from mysql.connector import MySQLConnection, Error


class TestSingleAPIInsert(unittest.TestCase):

    def test_check_id(self):
        true_appid = 400
        false_appid = 529
        self.assertEqual(True, check_id(true_appid))
        self.assertEqual(False, check_id(false_appid))

    def test_insert(self):
        try:
            con = MySQLConnection(host='localhost',
                                  database='test',
                                  user='root',
                                  password='project')
            if con.is_connected():
                print('Connected to database')

            cursor = con.cursor()
            cursor.execute("truncate table testapi")  # empty table before insertion
            insert(1, 'test', 'test', 'test')
            cursor.execute("select * from testapi")
            rows = cursor.fetchall()
            self.assertEqual(cursor.rowcount, 1)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            con.close()

    def test_get_api_data(self):
        appid = 400
        name = 'Portal'
        specs = ("\r\n\t\t\t<p><strong>Minimum: </strong>1.7 GHz Processor, 512MB RAM,"
                 " DirectX&reg; 8.1 level Graphics Card (Requires support for SSE), Windows&reg; 7 (32/64-bit)/Vista/XP, "
                 "Mouse, Keyboard, Internet Connection</p>\r\n\t\t\t<p><strong>Recommended: </strong>Pentium 4 processor "
                 "(3.0GHz, or better), 1GB RAM, DirectX&reg; 9 level Graphics Card, Windows&reg; 7 (32/64-bit)/Vista/XP, "
                 "Mouse, Keyboard, Internet Connection</p>\r\n\t\t\t")
        data = get_api_data(appid, 'minimum')
        self.assertEqual(data[0], appid)
        self.assertEqual(data[1], name)
        self.assertEqual(data[2], specs)


if __name__ == '__main__':
    unittest.main()