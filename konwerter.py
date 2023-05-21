import argparse
import os
import json
import yaml
import xmltodict

parser = argparse.ArgumentParser(description='XML, JSON, YML Converter!')

parser.add_argument('input_file', type=str, help='Input file.')
parser.add_argument('output_file', type=str, help='Output file.')

arguments = parser.parse_args()

if not (os.path.isfile(arguments.input_file)):
    print(f"Input file: {arguments.input_file} is invalid")
else:
    print(f"Input file: {arguments.input_file} is valid :-)")

input_ex = arguments.input_file.split('.')[-1]
input_ex = input_ex.lower()

if input_ex == 'json':
    with open(arguments.input_file, 'r') as file:
        try:
	    data = json.load(file)
	except json.JSONDecodeError as e:
	    print("Invalid filr format!", str(e))
	    exit(1)


def same_ex():
    print("Format of input and output files is the same")
    exit(1)


def json_xml():
    file_xml = open(arguments.output_file, "w")
    xmltodict.unparse(data, output=xml_file, pretty=True)
    file_xml.close()


def json_yaml():
    with open(arguments.output_file, 'w') as file:
	yaml.dump(data, file, indent=4)
