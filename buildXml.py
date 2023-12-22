import pandas as pd
import xml.etree.ElementTree as ET

json_file_path = 'ReportFolderData.json'

df = pd.read_json(json_file_path)

root = ET.Element('root')

for index, row in df.iterrows():
    member_element = ET.SubElement(root, 'members')
    member_element.text = f"{row['folderName']}/{row['reportDeveloperName']}"

tree = ET.ElementTree(root)

output_xml_path = 'FormattedStringsOutput.xml'

tree.write(output_xml_path)

print(f"Formatted XML strings written to {output_xml_path}")