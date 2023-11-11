import os, glob, re, warnings
import argparse

from html_ssi.classes import PathType

# Parser for CLI params
parser = argparse.ArgumentParser(description="Script to add server side include functionality to HTML files.")
parser.add_argument("-s", "--source", help="source directory (must container folder called '_includes' for the files to be included)", required=True, type=PathType(exists=True, type='dir'))
parser.add_argument("-d", "--destination", help="destination directory", required=True, type=PathType(exists=True, type='dir'))
args = parser.parse_args()

include_str_exp = r'\<!-- %include%\s.*\s\-->'
include_file_exp = r'(?<=\<!-- %include%\s)(.*)(?=\s\-->)'
include_dir = '_includes/'

# for each file, find all include statments
# iterate through include statements and replace w/ contents from corresponding file, if it exists, otherwise skip & log error

for sourcefile in glob.iglob(vars(args)["source"] + '**/*.html', recursive=True):
	if include_dir in sourcefile:
		continue
	with open(sourcefile) as file:
		s = file.read()
		includes = re.findall(include_str_exp, s)
		for include in includes:
			i = re.findall(include_file_exp, include)[0]
			print(">>> " + sourcefile + " < " + "_includes/" + i)
			try:
				f = open(vars(args)["source"] + include_dir + i).read()
			except Exception as e:
				print(">>>" + sourcefile + " is attempting to include file that cannot be opened\n", e)
			s = s.replace(include, f)
	with open(vars(args)["destination"] + os.path.basename(sourcefile), "w") as file:
		file.write(s)