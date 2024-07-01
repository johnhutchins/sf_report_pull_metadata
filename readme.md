# Important: make sure that inside vscode we search and filter out anything other than reports

## Steps to get all report meta data:

- Run getFolders.apex anonymously to generate the file
- Search for the file in the global search to find it and download it
- Download the file and save to a location you can reference in your Python script
- Run the python script to generate the xml
- Remove the <root> element from the generated XML (issue should be logged and fixed eventually)
- Add a <name>Report</name> element at the bottom of the generated XML (issue should be logged and fixed eventually)
- Use the XML to update package.xml in the org directory
- Right click on package.xml and "Retrieve source from org"

## TODO update python script to remove the "root" element
