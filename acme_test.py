import unittest

import main


file = main.organize_data("employees.txt")
file2 = main.organize_data("employees1.txt")
combination = main.choose_pair(["ASTRID", "RENE"], file2)


class TestEmployees(unittest.TestCase):

    def test_organize_data(self):
        self.assertEqual(main.organize_data("employees.txt"), {'RENE': 'MO10:00-12:00,TU10:00-12:00,'
                                                                       'TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                                                               'ASTRID': 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
                                                               'ANDRES': 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'},
                         "Error when getting the right file format")
        self.assertEqual(main.organize_data('employees1.txt'), {'RENE': 'MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,'
                                                                        'SA14:00-18:00,SU20:00-21:00',
                                                                'ASTRID': 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'},
                         "Error when getting the right file format")
        self.assertEqual(type(main.organize_data('employees.txt')), dict, "Not the expected output")

    def test_make_combinations(self):

        self.assertEqual(main.make_combinations(file, 2), [('RENE', 'ASTRID'), ('RENE', 'ANDRES'),
                                                           ('ASTRID', 'ANDRES')])
        self.assertEqual(main.make_combinations(file2, 2), [('RENE', 'ASTRID')])

    def test_choose_pair(self):

        self.assertEqual(main.choose_pair(["ANDRES", "ASTRID"], file), {'ASTRID': 'MO10:00-12:00,TH12:00-14:00,'
                                                                                  'SU20:00-21:00',
                                                                        'ANDRES': 'MO10:00-12:00,TH12:00-14:00,'
                                                                                  'SU20:00-21:00'})
        self.assertEqual(main.choose_pair(["ASTRID", "RENE"], file), {'RENE': 'MO10:00-12:00,TU10:00-12:00,'
                                                                              'TH01:00-03:00,SA14:00-18:00,'
                                                                              'SU20:00-21:00',
                                                                      'ASTRID': 'MO10:00-12:00,TH12:00-14:00,'
                                                                                'SU20:00-21:00'})
        self.assertEqual(main.choose_pair(["ANDRES", "RENE"], file), {'RENE': 'MO10:00-12:00,TU10:00-12:00,'
                                                                              'TH01:00-03:00,SA14:00-18:00,'
                                                                              'SU20:00-21:00',
                                                                      'ANDRES': 'MO10:00-12:00,TH12:00-14:00,'
                                                                                'SU20:00-21:00'})
        self.assertEqual(main.choose_pair(["ASTRID", "RENE"], file2), {'RENE': 'MO10:15-12:00,TU10:00-12:00,'
                                                                               'TH13:00-13:15,SA14:00-18:00,'
                                                                               'SU20:00-21:00',
                                                                       'ASTRID': 'MO10:00-12:00,TH12:00-14:00,'
                                                                                 'SU20:00-21:00'})

    def test_make_matrix(self):

        self.assertEqual(main.make_matrix("MO", combination), [['RENE', 'ASTRID'], ['MO10:15-12:00', 'MO10:00-12:00']])
        self.assertEqual(main.make_matrix("TU", combination), [['RENE'], ['TU10:00-12:00']])
        self.assertEqual(main.make_matrix("WE", combination), [[], []])
        self.assertEqual(main.make_matrix("TH", combination), [['RENE', 'ASTRID'], ['TH13:00-13:15', 'TH12:00-14:00']])
        self.assertEqual(main.make_matrix("FR", combination), [[], []])
        self.assertEqual(main.make_matrix("SA", combination), [['RENE'], ['SA14:00-18:00']])
        self.assertEqual(main.make_matrix("SU", combination), [['RENE', 'ASTRID'], ['SU20:00-21:00', 'SU20:00-21:00']])


if __name__ == '__main__':
    unittest.main()

