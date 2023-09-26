# General Tips

## How to create a command alias on Windows 10

1. Open a text file and add the command; e.g.,

	```start C:\"Program Files"\Docker\Docker\"Docker Desktop.exe" &```

1. Save the file using the following naming convention: `command-name.cmd`; e.g., *start-docker.cmd*

1. Copy the file into your C:\Windows\System32 folder.

1. Open a command prompt and run the command; e.g., `start-docker`

**Note**: For running in Git Bash, run full command name; e.g., `start-docker.cmd`


## How to find files with specific text on a Linux server

### Using `grep` to search within files:

#### $ `grep "150495" *.yaml`
Returns the content within the file.
```
1679640069.yaml:      id: 150495
1679656314.yaml:      id: 150495
```
#### $ `grep "150495" *.yaml -l`
Returns a list of files.
```
1679640069.yaml
1679656314.yaml
```
#### $ `grep -l "150495" *.yaml | xargs ls -l`
Returns a list of files with file info.
```
-rw-r--r--. 1 abcdefgh abcdefgh 792 Mar 23 23:41 1679640069.yaml
-rw-r--r--. 1 abcdefgh abcdefgh 792 Mar 24 04:12 1679656314.yaml
```

### Using `find` to search file names:
Source: [10 ways to use the Linux find command](https://www.redhat.com/sysadmin/linux-find-command)

#### $ `find . -name '*314*'`
```
./logs/1666260314.log
./logs/1666314721.log
./logs/1667173141.log
./logs/1668073146.log
./logs/1668314461.log
```

##### $ `find . -name "*40069*" | xargs -d '\n' stat -c "%-25n %y"`
```
./logs/1677400690.log     2023-02-26 00:38:15.632853000 -0800
./logs/1679640069.log     2023-03-23 23:44:14.618391000 -0700
./1679640069.yaml         2023-03-23 23:41:13.630507000 -0700
```
