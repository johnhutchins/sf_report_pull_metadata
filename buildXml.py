import pandas as pd
import xml.etree.ElementTree as ET

# Load the JSON file into a DataFrame
json_file_path = 'ReportFolderData.json'
df = pd.read_json(json_file_path)

# Create a list to hold the XML strings
xml_elements = []

# Iterate over the rows in the DataFrame and create the XML structure
for index, row in df.iterrows():
    member_element = ET.Element('members')
    member_element.text = f"{row['folderName']}/{row['reportDeveloperName']}"
    # Convert each element to string and add it to the list
    xml_string = ET.tostring(member_element, encoding='unicode')
    xml_elements.append(xml_string)

# Join the XML strings with line breaks
tree_string_with_breaks = '\n'.join(xml_elements)

# Write the formatted XML string to a file
output_xml_path = 'FormattedStringsOutput.xml'
with open(output_xml_path, 'w') as xml_file:
    xml_file.write(tree_string_with_breaks)

print(f"Formatted XML strings with line breaks written to {output_xml_path}")

