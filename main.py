import pytest
import os


if __name__ == '__main__':

    pytest.main(['-s', '-q', 'testsuits', '--alluredir', './report/xml'])
    os.system('allure generate ./report/xml  ./report --clean')
