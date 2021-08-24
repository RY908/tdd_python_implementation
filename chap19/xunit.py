from __future__ import annotations

class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def setup(self):
        self.was_run = None
        self.was_setup = 1
    def testMethod(self):
        self.was_run = 1

class TestCaseTest(TestCase):
    def setup(self):
        self.test: WasRun = WasRun("testMethod")
    def test_running(self):
        self.test.run()
        assert(self.test.was_run)
    def test_setup(self):
        self.test.run()
        assert(self.test.was_setup)

TestCaseTest("test_running").run()
TestCaseTest("test_setup").run()

