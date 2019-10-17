import unittest
from util.HTML import HTMLStyle
from testcase.test_dashboard import TestDashboard
from testcase.test_gs2 import TestGs2
from testcase.test_cns import TestCns
from testcase.test_notebook import TestNotebook
from testcase.test_tasklist import TestTasklist

class TestSuite(unittest.TestCase):

    def test_Issue(self):
        suites = unittest.TestSuite()
        # smoke_test.addTests([
        #
        #     unittest.defaultTestLoader.loadTestsFromTestCase()
        # ])
        suites = unittest.defaultTestLoader.discover('testcase', pattern='test_*.py')
        # runner = unittest.TextTestRunner()
        # runner.run(suites)

        outfile = open("./testreport/TestReport.html", "w")
        runner = HTMLStyle(
            stream=outfile,
            title='UI Test Report',
            description='Orion UI Tests'
        )
        runner.run(suites)

if __name__ == '__main__':
    unittest.main()