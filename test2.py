import unittest
import sys 
import os 

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add current directory to path
import database, stats

class TestCalc(unittest.TestCase):
    def assertListItems(self, subset, superset):
        for item in subset:
            self.assertIn(item, superset)
            
    def test_db_GReason(self):
        return self.assertIsNotNone(database.get_reasons())
    
    def test_db_GQueries(self):
        return self.assertIsNotNone(database.get_queries())

    def test_db_GAll(self):
        return self.assertIsNotNone(database.get_all())
    
    def test_db_GDates(self):
        return self.assertEqual(len(database.get_dates()), 5)
    
    def test_db_GCount(self):
        return self.assertEqual(database.get_count(), 5)
    
    def test_db_GModules(self):
        return self.assertEqual(len(database.get_modules()), 5)
    
    def test_db_GModules_2(self):
        allModules = ["CS2001","CS2002","CS2003","CS2004","CS2005"]
        list1 = database.get_modules()
        Ulist1 = [item[0] for item in list1]
        self.assertListItems(Ulist1, allModules)
    
    def test_db_GEmotions(self):
        return self.assertIsNotNone(database.get_emotions())
    
    def test_db_IDGen(self):
        return self.assertEqual(len(database.id_generator()), 6)
    
#note to self, apply check list method to the class above tests as well
    
class TestStats(unittest.TestCase):
    def assertListItems(self, subset, superset):
        for item in subset:
            self.assertIn(item, superset)

    def test_stats1(self):
        list1, list2 = stats.emotionCount()
        self.assertEqual(len(list1), len(list2))
    
    def test_stats1_2(self):
        emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment',  'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
        list1, list2 = stats.emotionCount()
        self.assertListItems(list2, emotions)

    def test_stats2(self):
        list1, list2 = stats.graphLine()
        return self.assertEqual(len(list1), len(list2))
        
    def test_stats3(self):
        list1, list2 = stats.graphPC()
        return self.assertEqual(len(list1), len(list2))

    def test_stats3_2(self):
        allModules = ["CS2001","CS2002","CS2003","CS2004","CS2005",]
        list1, list2 = stats.graphPC()
        
        self.assertListItems(list1, allModules)
    
    
if __name__ == '__main__':
    unittest.main()