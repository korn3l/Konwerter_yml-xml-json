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
	    print("Invalid file format!", str(e))
	    exit(1)

elif input_ex == "yml":
    with open(arguments.input_file, 'r') as file:
	try:
	    data = yaml.safe_load(file)

	except Exception as e:
	    print("Failed to read the file!", str(e))
	    exit(1)

elif input_ex == "xml":
    try:
	with open(arguments.input_file) as file_xml:
	    data = xmltodict.parse(file_xml.read())
    except xmltodict.ExpatError as e:
	print("Invalid file format.", str(e))
	exit(1)


def same_ex():
    print("Format of input and output files is the same")
    exit(1)


def json_xml():
    file_xml = open(arguments.output_file, "w")
    xmltodict.unparse(data, output=file_xml, pretty=True)
    file_xml.close()


def json_yaml():
    with open(arguments.output_file, 'w') as file:
	yaml.dump(data, file, indent=4)


def yaml_json():
    with open(arguments.output_file, 'w') as file:
	json.dump(data, file, indent=4)


def yaml_xml():
    xml_file = open(arguments.output_file, "w")
    xmltodict.unparse(data, output=xml_file, pretty=True)
    xml_file.close()


def xml_json():
    jdata = json.dumps(data, indent=4)
    with open(arguments.output_file, "w") as file_json:
	file_json.write(jdata)
	file_json.close()


def xml_yaml():
    ydata = yaml.dump(data, indent=4)
    with open(arguments.output_file, "w") as file_yaml:
	file_yaml.write(ydata)
	file_yaml.close()
