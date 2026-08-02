import xml.etree.ElementTree as ET

tree = ET.parse("reports/regression.xml")
root = tree.getroot()

# If root is <testsuites>, get the first testsuite
if root.tag == "testsuites":
    suite = root.find("testsuite")
else:
    suite = root

tests = int(suite.attrib.get("tests", 0))
failures = int(suite.attrib.get("failures", 0))
errors = int(suite.attrib.get("errors", 0))
skipped = int(suite.attrib.get("skipped", 0))
passed = tests - failures - errors - skipped

print("=" * 40)
print("QUALITY GATE SUMMARY")
print("=" * 40)
print(f"Total Tests : {tests}")
print(f"Passed      : {passed}")
print(f"Failures    : {failures}")
print(f"Errors      : {errors}")
print(f"Skipped     : {skipped}")

if failures == 0 and errors == 0:
    print("\nRegression : PASS")
    print("Release Decision : APPROVED")
else:
    print("\nRegression : FAIL")
    print("Release Decision : BLOCKED")