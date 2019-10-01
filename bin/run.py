import os
import sys

#Adding the project path to the sys.path
current_file = os.path.abspath(__file__)
project_home = os.sep.join(current_file.split(os.sep)[:-2])
if project_home in sys.path:
    sys.path.remove(project_home)
sys.path.append(project_home)

import libs.common.log as log
import libs.common.config as cfg
import libs.common.filerw as filerw

#log.init()
#log.debug("I m in")

class Run():
    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = None

def main():
    #Reading command line arguments and feeding in the config
    import argparse
    parser = argparse.ArgumentParser(description="Provide correct arguments")
    parser.add_argument("-test", type=str, help="Name of the test to run")
    parser.add_argument("-suite", type=str, help="Name of the suite to run")
    parser.add_argument("-project", type=str, help="Name of the project to run")
    parser.add_argument("-testlist", type=str, help="To check available testcases in a particular suite")
    parser.add_argument("-suitelist", type=str, help="To check available suites in a particular project")
    parser.add_argument("-loglevel", type=str, default='WARNING', help="To set the loglevel, any one of DEBUG/INFO/ERROR/WARNING/CRITICAL")
    parser.add_argument("-setup", type=str, help="Provide the name of the setup to run the test")
    parser.add_argument("-product", type=str, help="Provide the name of the product")
    parser.add_argument("--projectlist", action='store_true', help="To check available projects")
    parser.add_argument("--verbose", action='store_true', help="Set the verbose mode")

    args = parser.parse_args()

    if args.projectlist:
        files = filerw.get_files_from_dir(cfg.PROJ_DIR)
        if len(files) != 0 :
            print("-------Available projects----------")
            for filename in files:
                print(filename.split('.')[0])
            print("-----------------------------------")
        else:
            print("No project available to run, please create one")
        sys.exit(1)

    if args.suitelist != None:
        lines = filerw.get_content_in_lines(cfg.PROJ_DIR + os.sep + args.suitelist + '.ini')
        if lines != []:
            print("Suites in project \"{}\" are".format(args.suitelist))
            for line in lines:
                if 'suites' in line:
                    suites = line.split(':')[1].strip().split(',')
                    for suite in suites:
                        print(suite.strip())
        else:
            print("Project ini file is not correct, please fix it")
        sys.exit(1)

    if args.test == None and args.suite == None and args.project == None:
        print("Test/suite/project must be present as one the arguments")
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()