print('Hello, World!')
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file_to_sed", dest="file_to_sed", default="manifest\\package.xml",
                    help="File to edit")
parser.add_argument("-o", "--orig_string", dest="orig_string", default="PLACE_HOLDER",
                    help="What string to replace")
parser.add_argument("-n", "--new_string", dest="new_string", default="HelloWorld.cls",
                    help="The new string to set")

args = parser.parse_args()
with open(args.file_to_sed,'r') as file:
    filedata = file.read()
    filedata = filedata.replace(args.orig_string, args.new_string)
with open(args.file_to_sed,'w') as file:
    file.write(filedata)