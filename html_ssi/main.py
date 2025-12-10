import os, glob, re, warnings
import argparse

from html_ssi.classes import PathType

# Parser for CLI params
parser = argparse.ArgumentParser(description="Script to add server side include functionality to HTML files.")
parser.add_argument("source", help="source directory (must container folder called '_includes' for the files to be included)", type=PathType(exists=True, type='dir'))
parser.add_argument("destination", help="destination directory", type=PathType(exists=True, type='dir'))
args = parser.parse_args()

include_str_exp = r'\<!-- %include%\s.*\s\-->'
include_file_exp = r'(?<=\<!-- %include%\s)(.*)(?=\s\-->)'
include_dir = '_includes/'

# for each file, find all include statments
# iterate through include statements and replace w/ contents from corresponding file, if it exists, otherwise skip & log error

for sourcefile in glob.iglob(os.path.join(vars(args)["source"], '**/*.html'), recursive=True):
	if include_dir in sourcefile:
		continue
	with open(sourcefile) as file:
		s = file.read()
		includes = re.findall(include_str_exp, s)
		for include in includes:
			i = re.findall(include_file_exp, include)[0]
			print(">>> " + sourcefile + " < " + "_includes/" + i)
			try:
				include_path = os.path.join(vars(args)["source"], include_dir, i)
				f = open(include_path).read()
				s = s.replace(include, f)
			except Exception as e:
				print(">>>" + sourcefile + " is attempting to include file that cannot be opened\n", e)
	relative_path = os.path.relpath(sourcefile, vars(args)["source"])
	dest_path = os.path.join(vars(args)["destination"], relative_path)
	os.makedirs(os.path.dirname(dest_path), exist_ok=True)
	with open(dest_path, "w") as file:
		file.write(s)