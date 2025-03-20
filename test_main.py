from streamlit.testing.v1 import AppTest
import sys
import os
import unittest

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add current directory to path
import database

def test_app():
    at = AppTest.from_file("Home.py").run()    
    assert not at.exception

