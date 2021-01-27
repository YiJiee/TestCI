import os, sys, getopt, string
'''
Loops through the entire folder of ci_test and finds all .txt files and evaluate them.
Will raise exception if passing rate is less than the specified threshold.
'''
TOTAL_TEST_CASES = 0
PASSED_TEST_CASES = 0
PASS_RATE = 0
def usage():
    print("Please specify the passing rate (float) using the -p flag for the evaluation to exit with status code 0.")
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:")
    for opt, arg in opts:
        if opt == '-p':
            PASS_RATE = float(arg)
except:
    usage()
    sys.exit(1)

if PASS_RATE > 1 or PASS_RATE < 0:
    print("-p passing rate param must be between 0 and 1")
    sys.exit(1)

for file_path in os.listdir():
    filename, file_extension = os.path.splitext(file_path)
    if file_extension != ".txt":
        continue
    
    with open(file_path) as f:
        lines = f.readlines()
        lines = [l for l in lines if 'answer: ' in l]

        for i in range(0, len(lines), 2):
            my_answer = lines[i].strip().split(":")[-1]
            cor_answer = lines[i + 1].strip().split(":")[-1]
            if my_answer == cor_answer:
                PASSED_TEST_CASES += 1
            TOTAL_TEST_CASES += 1

if TOTAL_TEST_CASES != 0:
    print("Total test cases: {}, passed test cases: {}, passing rate: {}".format(TOTAL_TEST_CASES, PASSED_TEST_CASES, PASSED_TEST_CASES / TOTAL_TEST_CASES))

if TOTAL_TEST_CASES != 0 and (PASSED_TEST_CASES / TOTAL_TEST_CASES) >= PASS_RATE:
    sys.exit(0)
else:
    sys.exit(1)
    