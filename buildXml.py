import pandas as pd
import xml.etree.ElementTree as ET

# Load the JSON file into a DataFrame
json_file_path = 'ReportFolderData.json'
df = pd.read_json(json_file_path)

# Create the root element for the XML
root = ET.Element('root')

# Iterate over the rows in the DataFrame and create the XML structure
for index, row in df.iterrows():
    member_element = ET.SubElement(root, 'members')
    member_element.text = f"{row['folderName']}/{row['reportDeveloperName']}"

# Convert the ElementTree to a string and add line breaks
tree = ET.ElementTree(root)
tree_string = ET.tostring(root, encoding='unicode')

# Adding line breaks between members elements
tree_string_with_breaks = tree_string.replace('</members>', '</members>\n')

# Write the formatted XML string to a file
output_xml_path = 'FormattedStringsOutput.xml'
with open(output_xml_path, 'w') as xml_file:
    xml_file.write(tree_string_with_breaks)

print(f"Formatted XML strings with line breaks written to {output_xml_path}")
