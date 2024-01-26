# 0x05. Processes and signals

## General

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Tasks

* 0. What is my PID - file `0-what-is-my-pid`
Write a Bash script that displays its own PID
* 1. List your processes - file `1-list_your_processes`
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy

* 2. Show your Bash PID - file `2-show_your_bash_pid`
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009

* 3. Show your Bash PID made easy - file `3-show_your_bash_pid_made_easy`
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

You cannot use ps
