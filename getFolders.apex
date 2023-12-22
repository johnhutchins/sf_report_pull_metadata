public class FolderReport {
    public String folderName;
    public String reportDeveloperName;

    public FolderReport(String folderName, String reportDeveloperName) {
        this.folderName = folderName;
        this.reportDeveloperName = reportDeveloperName;
    }
}

Map<Id, String> folderNames = new Map<Id, String>();

for (Folder folder : [SELECT Id, Name FROM Folder WHERE Type = 'Report']) {
    folderNames.put(folder.Id, folder.Name);
}

List<FolderReport> folderReportsList = new List<FolderReport>();
for (Report report : [SELECT Id, Name, DeveloperName, OwnerId FROM Report]) {
    if (folderNames.containsKey(report.OwnerId)) {
        folderReportsList.add(new FolderReport(folderNames.get(report.OwnerId), report.DeveloperName));
    }
}

String jsonOutput = JSON.serialize(folderReportsList);

ContentVersion newFile = new ContentVersion();
newFile.Title = 'ReportFolderData';
newFile.PathOnClient = 'ReportFolderData.json';
newFile.VersionData = Blob.valueOf(jsonOutput);
newFile.Origin = 'H';
insert newFile;

System.debug('JSON file created: ' + newFile.Id);
