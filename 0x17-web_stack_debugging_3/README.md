0x17. Web stack debugging #3
DevOps
SysAdmin
Scripting
Debugging


Concepts

For this project, we expect you to look at these concepts:

    Web Server
    Web stack debugging


Requirements
General

    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp
    Files will be checked with Puppet v3.4
Tasks
0. Strace is your friend
mandatory

Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

    strace can attach to a current running process
    You can use tmux to run strace in one window and curl in another one

Requirements:

    Your 0-strace_is_your_friend.pp file must contain Puppet code
    You can use whatever Puppet resource type you want for you fix
