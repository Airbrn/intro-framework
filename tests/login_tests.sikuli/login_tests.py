import unittest
from _lib import *
import HTMLTestRunner

import os

class LoginTests(unittest.TestCase):
    # Execute BEFORE each Test
    def setUp(self):
        # # Write test name into the Textbox file
        # testName = '.'.join(self._testMethodName.split('.')[-2:])
        # f = open(os.path.join(os.getcwd(), 'tools', 'textbox', 'textbox.txt'), 'wb')
        # f.write(testName)
        # f.close()
        Browser.Start("file:///C:/Project/content/SampleWebpage_for_demos_125dpi.html?usrname=sfdsfd&psw=sdfsdf")

    # Execute AFTER each test
    def tearDown(self):
        pass

    def test01login(self):
        username = "Pesho"
        password = "potnoto"
        UIActions.ClickPage()
        UIActions.PageDown()
        click(Login_UI.enter_username)
        type(username)
        click(Login_UI.enter_password)
        type(password)
        click(Login_UI.login_button)
        sleep(2)
        clipboard = UIActions.CopyAllClipboard()
        success = "You successfully Logged in! :)"
        assert success

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

    # #Use it to add manually test cases - handy when debugging a specific part of the set
	# suite = unittest.TestSuite() -
    # suite.addTest(SmokeTests('test_100_Start_Browser'))
    # suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

    outfile = open("Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='LoginTests Report', description="Some descr")
    runner.run(suite)
    outfile.close()