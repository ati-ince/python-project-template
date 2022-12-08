# pylint: disable=C0301 #Line too long (%s/%s)
# pylint: disable=C0303 #Trailing whitespace
# pylint: disable=C0304 #Final newline missing
# pylint: disable=C0305 #Trailing newlines (trailing-newlines)
# pylint: disable=W1203 # Use lazy % formatting in logging functions (logging-fstring-interpolation)

""" 
(@ati) ahmed tahir ince
---------------------------
unit testing
"""
import unittest
from modules import Class1

class TestFirst(unittest.TestCase):
    ''' testing azure important methods '''
        
    def setUp(self):
        """Initilizer, set speech and language objs for test
        """   
        # create object to use     
        pass

    def tearDown(self):
        """delete for clean creation
        """        
        # del created ones
        pass

    def test_dosmtng1(self):
        # self.assertEqual('OK', return1, XError(msg)) 
        # raise Exception('message')
        pass
    
    def test_sec(self):
        raise RuntimeError('intentionally RISE!')
