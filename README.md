# backup_tool
Back up some files and folders to a back up folder named with date and time, 
it can also choose compression options.

## How to use?
- Click on the "Backup to" button to select the backup destination folder,  
- Then drag the files/folders to be backed up in program window,  
- Select one or more files, right-click, for more options,  
- You can set compress and remove from the list,  
- After setting up, click the "Start Backup" button,  
- A new backup folder will be created under the backup destination folder, 
  named with current date and time,  
- As long as it is backed up once, the content settings of the list will 
  be remembered later.

## Which operating systems are supported？
This program can be package to an executable file through pyinstaller.  
On windows will package to a .exe file, and on MacOS will package to a .app.  
I test it passed on Windows 10 and MacOS Bigsur.

## Release Note:
Version 1.0.1  
- Multi language support English and Simplified Chinese.  
- Fix Compressed file permission issue, will be show a message warning.  
- UI optimize.  

Version 1.0.0  
- Only supports Simplified Chinese interface.  
