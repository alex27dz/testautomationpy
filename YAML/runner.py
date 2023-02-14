import os
import argparse


parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-b", "--browser", help = "Pass in a browser #optional - default: chrome")
parser.add_argument("-tn", "--test_name", help = "Pass in testfile name", required=True)
parser.add_argument("-rn", "--report_name", help = "Pass in reportfile name", default="unittestresult" )
parser.add_argument("-d", "--directory", help = "Pass in report file directory", default=os.getcwd())

args = parser.parse_args()

testStr = ("tests/"+(args.test_name))

browser = (" --browser " + args.browser)

jUnitReport = (args.directory + "/" + args.report_name + ".xml")

htmlReport = (args.directory + "/" + args.report_name + ".html")

reportingStr = " --junitxml=" + jUnitReport + " --html=" + htmlReport +" --self-contained-html"

print("python -m pytest " + testStr + browser + reportingStr + "")

os.system("python -m pytest " + testStr + browser + reportingStr + "") 

