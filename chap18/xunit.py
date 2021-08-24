from __future__ import annotations

class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    def testMethod(self):
        self.was_run = 1

class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.was_run)

TestCaseTest("test_running").run()

