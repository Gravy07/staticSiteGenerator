import unittest
import sys

def run_suite_per_file():
    loader = unittest.TestLoader()
    suite = loader.discover("src")

    total_tests = 0
    failures = 0
    errors = 0

    print("=" * 60)
    print(f"{'Test File':<35} | {'Count':<6} | {'Status'}")
    print("=" * 60)

    # unittest.discover groups tests hierarchically:
    # top-level suite -> module suites -> TestCase suites -> test methods
    for module_suite in suite:
        for file_suite in module_suite:
            count = file_suite.countTestCases()
            if count == 0:
                continue

            # Extract module name from the first test case in this file suite
            first_test = list(file_suite)[0]
            # Dig down if nested
            while isinstance(first_test, unittest.TestSuite):
                first_test = list(first_test)[0]

            module_name = first_test.__class__.__module__

            # Run this specific file's suite quietly
            runner = unittest.TextTestRunner(verbosity=0, stream=open('/dev/null', 'w'))
            result = runner.run(file_suite)

            status = "OK"
            if result.failures or result.errors:
                status = f"FAIL (F:{len(result.failures)} E:{len(result.errors)})"

            print(f"{module_name:<35} | {count:<6} | {status}")

            total_tests += count
            failures += len(result.failures)
            errors += len(result.errors)

    print("=" * 60)
    print(f"Total: {total_tests} tests across all suites.")

    if failures > 0 or errors > 0:
        print(f"FAILED (failures={failures}, errors={errors})")
        sys.exit(1)
    else:
        print("OK")
        sys.exit(0)

if __name__ == "__main__":
    run_suite_per_file()
