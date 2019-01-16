# Administrative privileges 

## User Classes:

For each file, there are three classes of users that specify the levels of security:

- **user** : The file or directory owner, which is usually the user who created the file. The owner of a file can decide who has the right to read it, to write to it (make changes to it), or, if it is a command, to execute it.
- **group** : Members of a group.
- **others** : All other users who are not the file owner or group owner.

Only the owner of the file or root can assign or modify file permissions.

***

Theses are some **commands that alow you to have root permissions or change to other users**:
- `sudo`: Stands for _super-user do_. By using this command you have the root (super-user) previleges
- `su [USERNAME]`: Is the _switch user_ command. This command is supposed to be used with the user-name you want to switch to.
- `sudo su`: Switches to the root user. Which has all the previleges.

## Adding removing users:

Is very simple to add a new user:

```
$ sudo adduser _new-user-name_
```

Now you just need to fill in the user info (or leave it blank).

> Experiment switching to the new user (using `su`) and running a command with sudo.

The new user may not be a _sudoer_. That means that this user won't be able to run commands with _sudo_.
_To allow a new user to run a sudo command you'll need to access to an user that is a sudoer._

To make the new user a sudoer, `su` to an user that is a sudoer and run the command:

```
$ sudo adduser _new-user_ sudo
```

This will make _"new-user"_ a sudoer, by adding it to the sudo group.

Notice that to **add an user** and to **add an user to a gruop** we run the exect same `adduser` command.
But adding a second argument to the `adduser` will add that user to the group. 

In the a very similar manner, you can use the `deluser` command to remove users. Check the _man deluser_.
## File permissions and ownership:

### Ownship:

By typing the `$ ls -l` command, we can list the files in a directory and see its permissions and owners:

```
-rw-rw-r-- 1 username usergroup 335 dez 28 17:21 'Textfile.txt'
-rw-rw-r-- 1 root root 335 dez 28 17:21 Random_File
```

Note the _"-rw-rw-r-- 1 username usergruop"_ at the begging of the first file. This tells us the **permissions** and the **ownership** the file. 
In the example above, the first file is owned by the user "username", and belongs to the group "usergroup".
For the second file, we can see it is owned by the "root" user, and belongs to the "root" group.

It's possible to change a file ownership using the `chown` command. Suppose we want to change the ownership of the second file, we can do as such:
```
$ sudo chown newuser:newgroup Random_File
```
_Here we use the sudo to start the command because the file its owned by root, therefore we can't change it's properties from our regular user._

Alternatively, you can set owner and group separately:

``` 
$ chown newuser filename
$ chgrp group filename

```

### Permission:

Check the  _"-rw-rw-r--"_ at every file for the permission info, it follows this pattern:

 `-[OWNER PERMISSION]-[GROUP PERMISSION]-[PUBLIC PERMISSION]--`

In Linux, there are total of nine mode bits that set the basic access permissions.
The first three bits set the permissions for the owner of the file.
The next three bits set the permissions for the members of the file’s group.
The last three bits set the permissions for everyone else on the system.

And each letter is a different permission:
- `r` — read access
- `w` — write access
- `x` — execute access

Therefore, for the first file the permissions are _"-rw-rw-r--"_:
- The owner can read and write (rw).
- Any user in the _usergroup_ can read and write.
- Any public user can only read (r).

We can also change the permisson of a **file** using the `chmod` command. But to do so we must know that each permission setting can be represented by a numerical value:
- `r` = 4
- `w` = 2
- `x` = 1
- `-` = 0
_When these values are added together, the total is used to set specific permissions._
_For example, if you want read and write permissions, you would have a value of 4 + 2 = 6 (r + w = rw)_ 
_if want read, write, and execute permissions: 4 + 2 + 1 = 7 (r + w + x = rwx)_

Suppose we want to change the permission for the second file listed above, we can do as such:
```
$ sudo chmod 644 Random_File
```
_Again, we use the sudo to start the command because the file its owned by root._

Here is a list of some common settings, numerical values and their meanings:

|Setting|Numerical|Meaning|
|:---:|:---:|:---|
|-rw-------|(600)|Only the owner has read and write permissions.|
|-rw-r--r--|(644)|Only the owner has read and write permissions; the group and others have read only.|
|-rwx------|(700)|Only the owner has read, write, and execute permissions.|
|-rwxr-xr-x|(755)|The owner has read, write, and execute permissions; the group and others have only read and execute.|
|-rwx--x--x|(711)|The owner has read, write, and execute permissions; the group and others have only execute.|
|-rw-rw-rw-|(666)|Everyone can read and write to the file. (Be careful with these permissions.)|
|-rwxrwxrwx|(777)|Everyone can read, write, and execute. (Again, this permissions setting can be hazardous.)|

If we run both the `chown` and `chmod` on the _Random_File_, as exemplified above, and then the `ls -l` command again, the result would be:

```
-rw-rw-r-- 1 username usergroup 335 dez 28 17:21 'Textfile.txt'
-rw-r-r-- 1 newuser newgroup 335 dez 28 17:21 Random_File
```

***

Do note that the text above is about the `chmod` and `chown` commands for single files, but changing the permisson and ownship of a directory are pratically the same.

See the `ls -l` command with directories listed:

```
-rw-rw-r-- 1 username usergroup 335 dez 28 17:21 'Textfile.txt'
-rw-rw-r-- 1 root root 335 dez 28 17:21 Random_File
drwxr-xr-x  4 ubuntu ubuntu     4096 set  6 08:38  Programs
drwxr-xr-x 12 root root     4096 dez 27 20:15  Projects
```
Note the _Programs_ and the _Projects_ directories listed above. Both directories permission starts with the `d` characterer.
This is the special permissions flag, and there are a bunch of theses, here are some:

- `-`: no special permissions
- `d`: directory
- `l`: The file or directory is a symbolic link
- `s`: This indicated the setuid/setgid permissions.
- `t`: This indicates the sticky bit permissions.

When using `chmod` and `chown` for directories, its possible to change the permisson only for the folder - but not the the files inside said directory.
To do so just run the command normaly (this will change only the permision for the folder):

```
$ sudo chmod 755 ./Programs
```

If you wish to change the ownship or permission for the directory and all files that are inside of it, you can use the same `chmod` or `chown` command, just add the `-R` (for recurssive) flag to the command:

```
$ sudo chown -R newuser:newgroup ./Programs
```
_This will change the ownship for the folder and every file inside of it_


But be aware that changing the ownship or permisson for a folder and its files can be riscky, because some system files do need to be own by the root user and are expected to have determinaded permisson to be executed or read.


Have you notice that directories also have the `x` (execute) permission? That's because directories need to be executable for user to open them. 

When applying permissions to directories on Linux, the permission bits have different meanings than on regular files.

- The read bit allows the affected user to list the files within the directory
- The write bit allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes
- The execute bit allows the affected user to enter the directory, and access files and directories inside

