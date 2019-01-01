# Processes in Linux Systems

## Getting information about running processes:

### The _top_ command:

In linux systems we can have a view of wha processes are running by executing the `top` command in the terminal.

> This command is "real-time". You can see the list is not static, it changes. That's because the `top` lists in real-time the processes that are running in your machine.
If you open a new application, you can see it begin add to the processes list.

Each entry in this list is a process. In the columns you can see information about each process. The most relevant information are:
1. The **PID** number (an unique ID for that process). The PID is used to manage the process;
2. The **USER** that's running the application;
	- This is the “effective” username (which maps to an user ID) of the user who started the process.
	- Linux assigns a real user ID and an effective user ID to processes.
	- The effective user ID allows a process to act on behalf of another user. (For example, a non-root user can elevate to root in order to install a package.)
4. _PR_ and _NI_ are values related to the process scheduling system:
	- The **PR** field shows the scheduling priority of the process from the perspective of the kernel. 
	- The **NI** field shows the “nice” value of a process. The nice value affects the priority of a process.
5. _VIRT_, _RES_, _SHR_ and _%MEM_ fields are related with memory consumption.
	- **VIRT** is the total amount of memory consumed by a process. This includes the program’s code, the data stored by the process in memory, as well as any regions of memory that have been swapped to the disk;
	- **RES** is the memory consumed by the process in RAM;
	- And **%MEM** expresses this value as a percentage of the total RAM available. Finally, “SHR” is the amount of memory shared with other processes.
6. **S** value shows the process state in the single-letter form (a process may be in various states).
	-  The status of the task which can be one of:
		- D = uninterruptible sleep
		- R = running
		- S = sleeping
		- T = stopped by job control signal
		- t = stopped by debugger during trace
		- Z = zombie

7. **TIME+** is the total CPU time used by the process since it started, precise to the hundredths of a second.
8. The **COMMAND** column shows the command name associated whit the process.

### The _ps_ commands:

Theres also the `ps` command. The `ps` (i.e., process status) command is also used to provide information about the currently running processes.

> While the `top` command is mostly used interactively, `ps` is designed for non-interactive use (scripts, extracting some information with shell pipelines etc.)

While `top` allows you to display all processes statistics continuously, the `ps` gives you a **single snapshot of the running active processes** (statical).

> From the _man ps_: "By default, ps selects all processes with the same effective user ID (euid=EUID) as the current user and associated with the same terminal as the invoker.
It displays the process ID (pid=PID), the terminal associated with the process (tname=TTY), the cumulated CPU time in [DD-]hh:mm:ss format (time=TIME), and the executable name (ucmd=CMD).

That means the `ps` command without any arguments, displays processes for the current shell and same effective user ID.

You can use the `-A` or `-e` flag to select all processes. 
It's also possible to list all processes and their status and resource usage using `ps aux`.

> Basically, the `aux` means: a = show processes for all users; u = display the process's user/owner; x = also show processes not attached to a terminal

Typically, the `ps aux` and `ps -A`commands are used like this:

```
$ ps aux | grep [PROCESS YOU'RE LOOKING FOR]

or

$ ps -A | grep [PROCESS YOU'RE LOOKING FOR]
```

Now, if you're looking for an determined PID, you can use the `pgrep` command.

### The _pgrep_ command:

 Using the `preg` command, you can look up or signal processes based on name and other attributes. The _pgrep_ looks through the currently running processes and lists the process IDs which match the selection. Use it like this:

```
$ pgrep _COMMAND-NAME_
```

There can be more than one process associated with a single _COMMAND_ field value. Therefore, the `pgrep` can return a list of PID.

Analogous to the `pgrep` command, theres the `pkill` command that will end all running processes that are associated the same _COMMAND_ name. (We will see an exemple about this soon).

## Managing processes:

### The _kill_ command:

The name is pretty much intuitive for this one. The `kill` command sends a signal to a process using its PID.
The syntax for the command is:

```
$ kill [options] <pid> [...]
```

There are more then 30 different signals send to a process using `kill`. You can list all possible signal by running:

```
$ kill -L
```
This will list signal names in a nice table.

The signal can be specified by using its name or number. The default signal for kill is TERM.


