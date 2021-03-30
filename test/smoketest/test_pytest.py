"""Test Pytest Module"""
import os
import pytest

RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), 'build_3', 'test_case_1.py')
RES_TEST = pytest.main(["-s", RUTA_ARCHIVO])
if RES_TEST == 0:
    print('paso')
elif RES_TEST == 1:
    print('no paso')
