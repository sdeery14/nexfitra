# run_tests.py

import unittest
import coverage

# Start coverage measurement
cov = coverage.coverage(branch=True, include='app/*')
cov.start()

# Discover and run tests
tests = unittest.TestLoader().discover('tests')
result = unittest.TextTestRunner(verbosity=2).run(tests)

# Stop coverage measurement
cov.stop()
cov.save()

# Report coverage results
print("\nCoverage Report:\n")
cov.report()
cov.html_report(directory='coverage_html_report')
cov.erase()

# Exit with appropriate status code
if result.wasSuccessful():
    exit(0)
else:
    exit(1)
