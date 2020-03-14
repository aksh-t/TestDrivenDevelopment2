class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def setUp(self):
        self.log = "setup "

    def testMethod(self):
        self.log = self.log + "testMethod "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setup testMethod " == test.log)

TestCaseTest("testTemplateMethod").run()