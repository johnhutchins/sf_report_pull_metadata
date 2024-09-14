# Important: make sure that inside vscode we search and filter out anything other than reports

## Steps to get all report meta data:

- Run getFolders.apex anonymously to generate the file
- Search for the file in the global search to find it and download it
- Save file to a location you can reference in your Python script
- Run the python script to generate the xml
- Remove the <root> element from the generated XML (issue should be logged and fixed eventually)
- Add a <name>Report</name> element at the bottom of the generated XML (issue should be logged and fixed eventually)
- Use the XML to update package.xml in the org directory
  eg.
  `<types>
    <members>Report Folder Name/Report_Unique_Name</members>
    <members>Report Folder Name/Another_Report_Unique_Name</members>
    ...
    <name>Report></name>
<types>`

- Run sfdx force:source:retrieve -x manifest/package.xml -u yourSandboxAlias
