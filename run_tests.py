import sys
import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    runner = unittest.TextTestRunner()
    outcome = runner.run(suite)
    if outcome.wasSuccessful():
        sys.exit(0)
    else:
        print(len(outcome.failures))
        sys.exit(1)
