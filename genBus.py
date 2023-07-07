import uuid
import yaml
from datetime import datetime
from lxml import etree

# Read YAML file
with open('business_rule.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Load the JavaScript from the file
with open(data['script'], 'r') as f:
    js_code = f.read()

# Create a unique sys_id
sys_id = uuid.uuid4().hex

# Create root element
root = etree.Element('record_update', sys_domain="global", table="sys_script")

# Create business rule element
br_element = etree.SubElement(root, 'sys_script', action="INSERT_OR_UPDATE")

# Add child elements
for key, value in data.items():
    if key != 'script':
        etree.SubElement(br_element, key).text = str(value).lower()
    else:
        # Handling the script tag and its CDATA separately
        script_element = etree.SubElement(br_element, key)
        script_element.text = etree.CDATA(js_code)

# Add additional fields
etree.SubElement(br_element, 'sys_created_by').text = 'admin'
etree.SubElement(br_element, 'sys_created_on').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
etree.SubElement(br_element, 'sys_id').text = sys_id
etree.SubElement(br_element, 'sys_updated_by').text = 'admin'
etree.SubElement(br_element, 'sys_updated_on').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Generate XML string
xml_str = etree.tostring(root, pretty_print=True).decode()

# Write XML to file
with open('sys_update_xml.xml', 'w') as f:
    f.write(xml_str)

print('XML file has been generated.')
