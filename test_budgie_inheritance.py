from Animal import Budgie

def test_budgie_inheritance(self):
    test = Budgie(100,"test",100,"testOwner")
    self.assertEqual(test.reproduce(), "I lay eggs")