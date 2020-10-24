import unittest

import flask_unittest

def suite():
    from tests.flask_live_test import TestSetup, TestIndex, TestAuth, TestBlog
    from tests.app_factory import app
    suite = flask_unittest.LiveTestSuite(app)
    suite.addTest(unittest.makeSuite(TestSetup))
    suite.addTest(unittest.makeSuite(TestIndex))
    suite.addTest(unittest.makeSuite(TestAuth))
    suite.addTest(unittest.makeSuite(TestBlog))
    return suite
