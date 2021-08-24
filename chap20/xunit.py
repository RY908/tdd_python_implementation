from __future__ import annotations

class TestCase:
    def __init__(self, name):
        self.name = name
    def set_up(self):
        pass
    def tear_down(self):
        pass
    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()

class WasRun(TestCase):
    def set_up(self):
        self.log = "set_up "
    def test_method(self):
        self.log = self.log + "test_method "
    def tear_down(self):
        self.log = self.log + "tear_down "

class TestCaseTest(TestCase):
    def test_template_method(self):
        test: WasRun = WasRun("test_method")
        test.run()
        assert("set_up test_method tear_down " == test.log)

TestCaseTest("test_template_method").run()

