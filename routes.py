"""Routes Module"""
# pylint: disable=C0301
import sys
import os
from flask import Flask, jsonify
from flask_cors import CORS
import pytest
from api.testresults import TestResults
from lib.logs.logger import Logger

APP = Flask(__name__)
CORS(APP)

@APP.route('/test1')
def test1():
    """ Method to run Test Case 1 """
    Logger.info("Ejecutando Caso de Prueba 1")
    test_route = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test', 'smoketest', 'build_3', 'test_case_b3_1.py'))
    try:
        result_code = pytest.main(["-s", test_route])
        TestResults.log_test_results(result_code)
    except RuntimeError:
        Logger.error("Test Fallido" + str(sys.exc_info()[0]))
    return jsonify(Logger.logger_content())

@APP.route('/test2')
def test2():
    """ Method to run Test Case 2 """
    Logger.info("Ejecutando Caso de Prueba 2")
    test_route = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test', 'smoketest', 'build_3', 'test_case_b3_2.py'))
    try:
        result_code = pytest.main(["-s", test_route])
        TestResults.log_test_results(result_code)
    except RuntimeError:
        Logger.error("Test Fallido" + str(sys.exc_info()[0]))
    return jsonify(Logger.logger_content())

@APP.route('/test3')
def test3():
    """ Method to run Test Case 3 """
    Logger.info("Ejecutando Caso de Prueba 3")
    test_route = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test', 'smoketest', 'build_3', 'test_case_b3_3.py'))
    try:
        result_code = pytest.main(["-s", test_route])
        TestResults.log_test_results(result_code)
    except RuntimeError:
        Logger.error("Test Fallido" + str(sys.exc_info()[0]))
    return jsonify(Logger.logger_content())

@APP.route('/test4')
def test4():
    """ Method to run Test Case 4 """
    Logger.info("Ejecutando Caso de Prueba 4")
    test_route = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test', 'smoketest', 'build_3', 'test_case_b3_4.py'))
    try:
        result_code = pytest.main(["-s", test_route])
        TestResults.log_test_results(result_code)
    except RuntimeError:
        Logger.error("Test Fallido" + str(sys.exc_info()[0]))
    return jsonify(Logger.logger_content())

@APP.route('/test5')
def test5():
    """ Method to run Test Case 5 """
    Logger.info("Ejecutando Caso de Prueba 5")
    test_route = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test', 'smoketest', 'build_3', 'test_case_b3_5.py'))
    try:
        result_code = pytest.main(["-s", test_route])
        TestResults.log_test_results(result_code)
    except RuntimeError:
        Logger.error("Test Fallido" + str(sys.exc_info()[0]))
    return jsonify(Logger.logger_content())

if __name__ == '__main__':
    APP.run()
