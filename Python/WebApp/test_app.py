import unittest
from app import app, db
from models import *
from app import get_rows, performance_rank, os_ram_comparison, tag_search

game_1 = db.session.query(game_requirements).filter(game_requirements.appid == 770240).first()
game_2 = db.session.query(game_requirements).filter(game_requirements.appid == 765180).first()
game_3 = db.session.query(game_requirements).filter(game_requirements.appid == 810640).first()
two_input = [game_1, game_3]
three_input = [game_1, game_2, game_3]


class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['Testing'] = True

    def test_performance_rank(self):
        user_cpu = db.session.query(cpubenchmarks).filter(cpubenchmarks.benchmark_score == 9335).first()
        user_gpu = db.session.query(gpubenchmarks).filter(gpubenchmarks.benchmark_score == 5925).first()

        self.assertEqual([], performance_rank(user_cpu, user_gpu, [], 'minimum'))
        self.assertEqual([game_3, game_1], performance_rank(user_cpu, user_gpu, two_input, 'minimum'))
        self.assertEqual([game_3, game_2, game_1], performance_rank(user_cpu, user_gpu, three_input, 'minimum'))
        self.assertEqual([game_3, game_1], performance_rank(user_cpu, user_gpu, two_input, 'recommended'))

    def test_os_ram_comparison(self):
        min_os = 7
        rec_os = 10
        min_ram = 4
        rec_ram = 8
        self.assertEqual([], os_ram_comparison([], min_os, min_ram, 'minimum'))
        self.assertEqual(two_input, os_ram_comparison(two_input, min_os, min_ram, 'minimum'))
        self.assertEqual([], os_ram_comparison(two_input, min_os, min_ram, 'recommended'))
        self.assertEqual([game_3], os_ram_comparison(three_input, rec_os, min_ram, 'recommended'))
        self.assertEqual([game_1, game_2], os_ram_comparison(three_input, min_os, rec_ram, 'recommended'))
        self.assertEqual(three_input, os_ram_comparison(three_input, rec_os, rec_ram, 'recommended'))

    def test_tag_search(self):
        self.assertEqual([], tag_search('', []))
        self.assertEqual(three_input, tag_search('', three_input))
        self.assertEqual(three_input, tag_search('Invalid tag', three_input))
        self.assertEqual([], tag_search('Driving', three_input))
        self.assertEqual([game_2], tag_search('Story Rich', three_input))
        self.assertEqual([game_1, game_3], tag_search('Singleplayer', three_input))
