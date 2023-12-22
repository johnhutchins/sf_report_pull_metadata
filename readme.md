## Steps to get all report meta data:

- Run getFolders.apex anonymously to generate the file
- Search for the file in the global search to find it and download it
- Save file to a location you can reference in your Python script
- Run the python script to generate the xml
- Use the XML to update package.xml in the org directory
  eg. 
`<types>
    <members>Report Folder Name/Report_Unique_Name</members>
    <members>Report Folder Name/Another_Report_Unique_Name</members>
    ...
    <name>Report>
<types>`

- Run sfdx force:source:retrieve -x manifest/package.xml -u yourSandboxAlias    


## TODO update python script to remove the "root" element
