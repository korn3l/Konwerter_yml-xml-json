import argparse
import os
import json
import yaml
import xmltodict

parser = argparse.ArgumentParser(description='XML, JSON, YML Converter!')

parser.add_argument('input_file', type=str, help='Input file.')
parser.add_argument('output_file', type=str, help='Output file.')

arguments = parser.parse_args()

if not os.path.isfile(arguments.input_file):
    print(f"Input file: {arguments.input_file} is invalid")
else:
    print(f"Input file: {arguments.input_file} is valid :-)")

input_ex = arguments.input_file.split('.')[-1]
input_ex = input_ex.lower()

output_ex = arguments.output_file.split('.')[-1]
output_ex = output_ex.lower()

if input_ex == 'json':
    with open(arguments.input_file, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print('Invalid format', str(e))
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
    with open(arguments.output_file, 'w') as file_xml:
        xml_data = xmltodict.unparse({'root': data}, pretty=True)
        file_xml.write(xml_data)


def json_yaml():
    with open(arguments.output_file, 'w') as file:
        yaml.dump(data, file, indent=4)


def yaml_json():
    with open(arguments.output_file, 'w') as file:
        json.dump(data, file, indent=4)


def yaml_xml():
    with open(arguments.output_file, 'w') as file_xml:
        xml_data = xmltodict.unparse(data, pretty=True)
        file_xml.write(xml_data)


def xml_json():
    jdata = json.dumps(data, indent=4)
    with open(arguments.output_file, "w") as file_json:
        file_json.write(jdata)


def xml_yaml():
    ydata = yaml.dump(data, indent=4)
    with open(arguments.output_file, "w") as file_yaml:
        file_yaml.write(ydata)


if input_ex == output_ex:
    same_ex()

elif input_ex == 'json':
    if output_ex == 'yml':
        print("You are converting: json -> yml")
        json_yaml()

    elif output_ex == 'xml':
        print("You are converting: json -> xml")
        json_xml()

elif input_ex == 'yml':
    if output_ex == 'json':
        print("You are converting yaml -> json")
        yaml_json()

    elif output_ex == 'xml':
        print("You are converting yaml -> xml")
        yaml_xml()

elif input_ex == 'xml':
    if output_ex == 'json':
        print("You are converting xml -> json")
        xml_json()

    elif output_ex == 'yml':
        print("You are converting xml -> yaml")
        xml_yaml()

else:
    print("Something gone wrong...")
