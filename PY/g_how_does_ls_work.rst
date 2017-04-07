How does ``ls`` work?
---------------------

I wanted to be really able to explain to a fair amount of detail how
does the program :command:`ls` actually work right from the moment you
type the command name and hit ENTER. What goes on in user space and
and in kernel space? This is my attempt and what I have learned so far
on Linux (Fedora 19, 3.x kernel).

How does the shell find the location of 'ls' ?
==============================================

In user space, the location of :command:`ls` is first searched in the locations
in ``PATH``. We can see the search by placing break points at the key
locations in BASH's source code::

    (gdb) b search_for_command
    Breakpoint 1 at 0x4661d0: file findcmd.c, line 303.
    (gdb) run -c ls
    Starting program: /home/gene/work/linux_system_experiments/how-does-ls-work/sources/bash/./bash -c ls

    Breakpoint 1, search_for_command (pathname=0x6f42b8 "ls") at findcmd.c:303
    303     {
    Missing separate debuginfos, use: debuginfo-install ncurses-libs-5.9-11.20130511.fc19.x86_64
    (gdb) bt
    #0  search_for_command (pathname=0x6f42b8 "ls") at findcmd.c:303
    #1  0x0000000000430c68 in execute_disk_command (cmdflags=64, fds_to_close=0x6fe6a8, async=0, pipe_out=-1, pipe_in=-1, command_line=0x6f42c8 "ls", 
    redirects=0x0, words=<optimized out>) at execute_cmd.c:4668
    #2  execute_simple_command (simple_command=<optimized out>, pipe_in=-1, pipe_out=-1, async=<optimized out>, fds_to_close=0x6fe6a8) at execute_cmd.c:3990
    #3  0x000000000043247e in execute_command_internal (command=0x6fe588, asynchronous=0, pipe_in=-1, pipe_out=-1, fds_to_close=0x6fe6a8) at execute_cmd.c:735
    #4  0x000000000046fe8b in parse_and_execute (string=<optimized out>, from_file=from_file@entry=0x4a7799 "-c", flags=flags@entry=4) at evalstring.c:319
    #5  0x000000000041d72a in run_one_command (command=<optimized out>) at shell.c:1315
    #6  0x000000000041c506 in main (argc=3, argv=0x7fffffffdc38, env=0x7fffffffdc58) at shell.c:688

As you can see from the line #0 above, the argument, ``pathname``
refers to the string ``ls`` which now has to be searched in the
locations specified by the user's ``PATH`` variable::

    (gdb) b find_user_command_in_path
    Breakpoint 2 at 0x465ed0: file findcmd.c, line 552.
    (gdb) cont
    Continuing.

    Breakpoint 2, find_user_command_in_path (name=0x6f42b8 "ls", 
    path_list=0x6f7008 "/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/bin:/usr/games:/usr/local/sbin:/usr/sbin:/home/gene/.local/bin:/home/gene/bin", flags=36) at findcmd.c:552
    552     {
    (gdb) bt
    #0  find_user_command_in_path (name=0x6f42b8 "ls", 
    path_list=0x6f7008 "/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/bin:/usr/games:/usr/local/sbin:/usr/sbin:/home/gene/.local/bin:/home/gene/bin", flags=36) at findcmd.c:552
    #1  0x0000000000466220 in find_user_command_internal (flags=36, name=0x6f42b8 "ls") at findcmd.c:268
    #2  find_user_command (name=0x6f42b8 "ls") at findcmd.c:213
    #3  search_for_command (pathname=0x6f42b8 "ls") at findcmd.c:354
    #4  0x0000000000430c68 in execute_disk_command (cmdflags=64, fds_to_close=0x6fe6a8, async=0, pipe_out=-1, pipe_in=-1, command_line=0x6f42c8 "ls", 
    redirects=0x0, words=<optimized out>) at execute_cmd.c:4668
    #5  execute_simple_command (simple_command=<optimized out>, pipe_in=-1, pipe_out=-1, async=<optimized out>, fds_to_close=0x6fe6a8) at execute_cmd.c:3990
    #6  0x000000000043247e in execute_command_internal (command=0x6fe588, asynchronous=0, pipe_in=-1, pipe_out=-1, fds_to_close=0x6fe6a8) at execute_cmd.c:735
    #7  0x000000000046fe8b in parse_and_execute (string=<optimized out>, from_file=from_file@entry=0x4a7799 "-c", flags=flags@entry=4) at evalstring.c:319
    #8  0x000000000041d72a in run_one_command (command=<optimized out>) at shell.c:1315
    #9  0x000000000041c506 in main (argc=3, argv=0x7fffffffdc38, env=0x7fffffffdc58) at shell.c:688

From the above backtrace we can see that ``search_for_command()``
calls ``find_user_command()`` and eventually
``find_user_command_in_path`` is called (most likely, because
the call to ``find_user_command_internal()`` fails, since :command:`ls` is an
external command). The ``find_user_command_in_path()`` function calls
the ``find_in_path_element()`` function for each of the locations
specifiied in the ``PATH`` variable, unless it finds the correct
location for the executable file corresponding to the command
:command:`ls`. The following gdb session illustrates this::

    (gdb) b find_in_path_element
    Breakpoint 3 at 0x465d10: file findcmd.c, line 467.
    (gdb) cont
    Continuing.

    Breakpoint 3, find_in_path_element (name=name@entry=0x6f42b8 "ls", path=path@entry=0x6fea08 "/usr/lib64/qt-3.3/bin", flags=flags@entry=36, 
    dotinfop=dotinfop@entry=0x7fffffffd750, name_len=<optimized out>) at findcmd.c:467
    467     find_in_path_element (name, path, flags, name_len, dotinfop)
    (gdb) bt
    #0  find_in_path_element (name=name@entry=0x6f42b8 "ls", path=path@entry=0x6fea08 "/usr/lib64/qt-3.3/bin", flags=flags@entry=36, 
    dotinfop=dotinfop@entry=0x7fffffffd750, name_len=<optimized out>) at findcmd.c:467
    #1  0x0000000000465fd0 in find_user_command_in_path (name=0x6f42b8 "ls", 
         path_list=0x6f7008 "/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/bin:/usr/games:/usr/local/sbin:/usr/sbin:/home/gene/.local/bin:/home/gene/bin", flags=36) at findcmd.c:586
    #2  0x0000000000466220 in find_user_command_internal (flags=36, name=0x6f42b8 "ls") at findcmd.c:268
    #3  find_user_command (name=0x6f42b8 "ls") at findcmd.c:213
    #4  search_for_command (pathname=0x6f42b8 "ls") at findcmd.c:354
    #5  0x0000000000430c68 in execute_disk_command (cmdflags=64, fds_to_close=0x6fe6a8, async=0, pipe_out=-1, pipe_in=-1, command_line=0x6f42c8 "ls", 
    redirects=0x0, words=<optimized out>) at execute_cmd.c:4668
    #6  execute_simple_command (simple_command=<optimized out>, pipe_in=-1, pipe_out=-1, async=<optimized out>, fds_to_close=0x6fe6a8) at execute_cmd.c:3990
    #7  0x000000000043247e in execute_command_internal (command=0x6fe588, asynchronous=0, pipe_in=-1, pipe_out=-1, fds_to_close=0x6fe6a8) at execute_cmd.c:735
    #8  0x000000000046fe8b in parse_and_execute (string=<optimized out>, from_file=from_file@entry=0x4a7799 "-c", flags=flags@entry=4) at evalstring.c:319
    #9  0x000000000041d72a in run_one_command (command=<optimized out>) at shell.c:1315
    #10 0x000000000041c506 in main (argc=3, argv=0x7fffffffdc38, env=0x7fffffffdc58) at shell.c:688

    (gdb) cont
    Continuing.

    Breakpoint 3, find_in_path_element (name=name@entry=0x6f42b8 "ls", path=path@entry=0x6fe948 "/usr/lib64/ccache", flags=flags@entry=36, 
           dotinfop=dotinfop@entry=0x7fffffffd750, name_len=<optimized out>) at findcmd.c:467
    467     find_in_path_element (name, path, flags, name_len, dotinfop)
    (gdb) cont
    Continuing.

    Breakpoint 3, find_in_path_element (name=name@entry=0x6f42b8 "ls", path=path@entry=0x6fe948 "/usr/local/bin", flags=flags@entry=36, 
    dotinfop=dotinfop@entry=0x7fffffffd750, name_len=<optimized out>) at findcmd.c:467
    467     find_in_path_element (name, path, flags, name_len, dotinfop)
    (gdb) cont
    Continuing.

    Breakpoint 3, find_in_path_element (name=name@entry=0x6f42b8 "ls", path=path@entry=0x6fe948 "/usr/bin", flags=flags@entry=36, 
    dotinfop=dotinfop@entry=0x7fffffffd750, name_len=<optimized out>) at findcmd.c:467
    467     find_in_path_element (name, path, flags, name_len, dotinfop)
    (gdb) 

    Continuing.
    process 15253 is executing new program: /usr/bin/ls

And finally it, finds :file:`/usr/bin/ls` and calls ``execve()`` with
to execute the command (More on this in the next section). The
``stat()`` system call is used to check the existence of an executable
:command:`ls` in the above locations. This is a snippet of the calls
to ``stat()``::

    stat("/usr/lib64/qt-3.3/bin/ls", 0x7fff8c535c40) = -1 ENOENT (No such
    file or directory)
    stat("/usr/lib64/ccache/ls", 0x7fff8c535c40) = -1 ENOENT (No such file
    or directory)
    stat("/usr/local/bin/ls", 0x7fff8c535c40) = -1 ENOENT (No such file or
    directory)
    stat("/usr/bin/ls", {st_mode=S_IFREG|0755, st_size=120232, ...}) = 0
    stat("/usr/bin/ls", {st_mode=S_IFREG|0755, st_size=120232, ...}) = 0


So far, BASH has found out the location of the executable
corresponding to the command :command:`ls`. To get to this point, the
filesystem had to be traversed at the locations in ``PATH``. Let us
dive into the kernel space to see how this is being done. We will use
the following ``SystemTap`` script to trace the call and return from
the function ``vfs_fstatat()`` in the file ``fs/stat.c``::

    probe kernel.function("vfs_fstatat@fs/stat.c").call
    {
        # we are only interested in calls to vfs_fstatat() from "bash"
        # assuming that only one user is using "bash" to execute "ls"
        if(execname() == "bash")
            printf("%s -> %s %s\n", thread_indent(-1), probefunc(), kernel_string($filename)); 
    }

    probe kernel.function("vfs_fstatat@fs/stat.c").return
    {
        # same as above
        if(execname() == "bash")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }

    probe timer.ms(300000)
    {
        exit() 
    }

The ``stat()`` system call is defined as follows::

    SYSCALL_DEFINE2(stat, const char __user *, filename, struct __old_kernel_stat __user *, statbuf)
    {
        struct kstat stat;
        int error;

        error = vfs_stat(filename, &stat);
        if (error)
                return error;

        return cp_old_stat(&stat, statbuf);

    }

The ``vfs_stat()`` function in turn is defined as follows::

    int vfs_stat(const char __user *name, struct kstat *stat)
    {
        return vfs_fstatat(AT_FDCWD, name, stat, 0);
    }

Hence, we trace the call and return from the ``vfs_fstatat()``
function which has the following prototype::

    int vfs_fstatat(int dfd, const char __user *filename, struct kstat
    *stat, int flag)

The parameter, ``filename`` is what we are interested in here. When
you run the SystemTap script, you will see the following lines::

    # stap find_ls.stp

    Pass 1: parsed user script and 110 library script(s) using
    221520virt/38768res/3072shr/36596data kb, in 120usr/20sys/142real ms.
    Pass 2: analyzed script: 3 probe(s), 16 function(s), 4 embed(s), 2
    global(s) using 432420virt/92908res/4344shr/91140data kb, in
    340usr/410sys/752real ms.
    Pass 3: translated to C into
    "/tmp/stap10Um7s/stap_3647789271d0793b6962cabaec032633_5961_src.c"
    using 429960virt/95976res/7532shr/91140data kb, in
    110usr/170sys/284real ms.
    Pass 4: compiled C into
    "stap_3647789271d0793b6962cabaec032633_5961.ko" in
    2510usr/340sys/2707real ms.
    Pass 5: starting run.

Now, execute the :command:`ls` command in another terminal window, you
should see these lines in the SystemTap window::

    741 bash(18259): -> vfs_fstatat /usr/lib64/qt-3.3/bin/ls
    754 bash(18259): <- SYSC_newstat
    762 bash(18259): -> vfs_fstatat /usr/lib64/ccache/ls
    772 bash(18259): <- SYSC_newstat
    780 bash(18259): -> vfs_fstatat /usr/local/bin/ls
    790 bash(18259): <- SYSC_newstat
    797 bash(18259): -> vfs_fstatat /usr/bin/ls

Note that each of these ``vfs_fstatat()`` calls also results in accessing
the underlying filesystem (traversing the directories, and files - a
topic which we explore in some detail in the third section, since that
is similar to how the kernel enables :command:`ls` to do what it does).

At this stage, we have a fairly reasonable idea of what happens in
user space and kernel space so that the location of the program that the
:command:`ls` corresponds to is found. Now, we are ready to see how
the executable binary is executed.

How does the shell execute the command?
=======================================

A call to ``execve()`` is made, which is a system call, defined as
follows::

    SYSCALL_DEFINE3(execve,
                   const char __user *, filename,
                   const char __user *const __user *, argv,
                   const char __user *const __user *, envp)
    {
        struct filename *path = getname(filename);
        int error = PTR_ERR(path);
        if (!IS_ERR(path)) {
                error = do_execve(path->name, argv, envp);
                putname(path);
        }
        return error; 
    }

Effectively, it is the ``do_execve()`` function which does the
work. It has the following prototype::

    static int do_execve_common(const char *filename,
                                struct user_arg_ptr argv,
                                struct user_arg_ptr envp)

Using the following SystemTap script, we place a probe at this function::

    # TODO: find a way to get access to the argv and argp
    probe kernel.function("do_execve@fs/exec.c")
    {
        if(execname() == "bash")
        printf("%s -> %s %s\n", thread_indent(1), probefunc(), kernel_string($filename));
    }

    probe timer.ms(30000)
    {
        exit()
    }

Run this script and execute :command:`ls` in another terminal window
and you will see::

    0 bash(26013): -> SyS_execve /usr/bin/ls

There is a bunch of other things that needs to be done before the
binary ``/usr/bin/ls`` is executed - the program has to be read from
the disk, it's binary format needs to be found and the appropriate
handling code needs to be invoked which will read the binary into
memory. The following SystemTap script probes at some of the key
functions which allows us to observe how the :file:`/usr/bin/ls`
binary is loaded into memory::

    # TODO: find a way to get access to the argv and argp
    probe kernel.function("do_execve_common@fs/exec.c")
    {
        if(execname() == "bash")
            printf("%s %s\n", probefunc(), kernel_string($filename)); 
    }

    probe kernel.function("search_binary_handler@fs/exec.c").call
    {
        if(execname() == "bash")
            printf("%s -> %s Executable: %s Interpreter: %s\n", thread_indent(1), probefunc(), kernel_string($bprm->filename),  kernel_string($bprm->interp));
    }

    probe kernel.function("search_binary_handler@fs/exec.c").return
    {
        if(execname() == "bash")
            printf("%s <- %s \n", thread_indent(-1), probefunc());
    }

    probe kernel.function("open_exec@fs/exec.c").call
    {
        if(execname() == "bash")
            printf("%s -> %s %s\n", thread_indent(1), probefunc(), kernel_string($name));
    }

    probe kernel.function("open_exec@fs/exec.c").return
    {
        if(execname() == "bash")
            printf("%s <- %s \n", thread_indent(-1), probefunc());
    }

    probe kernel.function("load_elf_binary@fs/binfmt_elf.c").call
    {
        if(execname() == "bash")
            printf("%s %s: Executable: %s Interpreter: %s\n", thread_indent(1), probefunc(), kernel_string($bprm->filename),  kernel_string($bprm->interp));
    }

    probe timer.ms(30000)
    {
        exit();
    }

Run the SystemTap script and execute :command:`ls` in another window
and you will see the following in the SystemTap window::

    do_execve_common.isra.24 /bin/ls
         0 bash(7988): -> open_exec /bin/ls
         25 bash(7988): <- do_execve_common.isra.24 
         0 bash(7988): -> search_binary_handler Executable: /bin/ls Interpreter: /bin/ls
         14 bash(7988):  load_elf_binary: Executable: /bin/ls Interpreter: /bin/ls
         27 bash(7988):   -> open_exec /lib64/ld-linux-x86-64.so.2
         54 bash(7988):   <- load_elf_binary 


The ``search_binary_handler()`` function iterates the list of
currently supported binary formats and once it finds that the
executable is a supported format, proceeds to call the appropriate
function to load the binary which is the function
``load_elf_binary()`` in this case. This becomes quite interesting
when we execute a script with a ``#!`` (I have some experiments which
I hope to share in a next article). Also, note how the glibc loader is
also being opened, since :file:`/usr/bin/ls` dynamically loads ``glibc``
into memory. To see how things are different when you compile a program
statically, let's consider this C program::

    # include <stdio.h>

    int main(int argc, char **argv)
    {
      printf("Hello World\n");
      return 0;
    }

Compile it with ``gcc -o simple simple.c`` and execute it while
keeping the above SystemTap script running. You will see the
following::

    do_execve_common.isra.24 ./simple
         0 bash(8102): -> open_exec ./simple
         20 bash(8102): <- do_execve_common.isra.24 
         0 bash(8102): -> search_binary_handler Executable: ./simple Interpreter: ./simple
         13 bash(8102):  load_elf_binary: Executable: ./simple Interpreter:./simple
         26 bash(8102):   -> open_exec /lib64/ld-linux-x86-64.so.2
         56 bash(8102):   <- load_elf_binary 


Now, compile the program, passin the ``-static`` flag to gcc as
``gcc -o simple_static simple.c -static`` and execute the program. You
will see the following output in SystemTap's window::

    do_execve_common.isra.24 ./simple_static
        0 bash(8119): -> open_exec ./simple_static
        23 bash(8119): <- do_execve_common.isra.24 
        0 bash(8119): -> search_binary_handler Executable:./simple_static Interpreter: ./simple_static
        20 bash(8119):  load_elf_binary: Executable: ./simple_static Interpreter: ./simple_static

In this case, you can see that the loader is not being opened any
more. After this, bunch of things such as setting up the memory areas,
copying over the arguments, etc need to happen. I haven't yet gained
sufficient clarity here to explain, so I will skip over it now.

How does ``ls`` do what it does?
================================

At this stage, the program is in memory and is ready to execute when
it gets a chance. So, how does :command:`ls` read the directories and files
from disk and what happens in the kernel space to make that happen?
This is what we focus on now. :command:`ls` uses ``readdir(3)``
function to read the directory contents which in turn invokes the
``getdents()`` system call defined as follows in :file:`fs/readdir.c`::

  SYSCALL_DEFINE3(getdents, unsigned int, fd, struct linux_dirent __user *, dirent, unsigned int,count)   

To summarize what we are looking to observe here is that the directory
entries are ready from the block device (the underlying filesystem), which
involves look up in the filesystem's inode table. My filesystem is
formatted with ``btrfs`` which is compiled as a kernel module and I
trace two functions from this module - ``btrfs_lookup_dentry()`` which I am
fairly certain is doing the look up and the ``btrfs_real_readdir()``
function which is reading the directory from the underlying block
device. 

Once a directory entry is read from the block device, the function
``filldir()`` in :file:`fs/readdir.c` is called (from the likes of
it as a callback function) where I believe the in-memory directory
entry is being created (This is not specific to the underlying
filesystem being ``btrfs`` - i have observed this with ``ext4`` too). 

The following SystemTap script traces the above functions in addition
to the ``vfs_write()`` function which finally writes the output to the terminal::

    probe module("btrfs").function("btrfs_lookup_dentry").call
    {
        if(execname() == "ls")
           printf("%s -> %s\n", thread_indent(1), probefunc());
    }

    probe module("btrfs").function("btrfs_lookup_dentry").return
    {
        if(execname() == "ls")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }

    probe module("btrfs").function("btrfs_real_readdir").call
    {
        if(execname() == "ls")    printf("%s -> %s\n", thread_indent(1), probefunc());
    } 

    probe module("btrfs").function("btrfs_real_readdir").return
    {
        if(execname() == "ls")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }

    # for ext4
    probe kernel.function("ext4_readdir@fs/ext4/dir.c").call
    {
        if(execname() == "ls")
            printf("%s -> %s\n", thread_indent(1), probefunc());
    }

    probe kernel.function("ext4_readdir@fs/ext4/dir.c").return
    {
        if(execname() == "ls")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }

    probe kernel.function("filldir@fs/readdir.c").call
    {
        if(execname() == "ls")
            printf("%s -> %s : %s\n", thread_indent(1), probefunc(), kernel_string($name));
    }

    probe kernel.function("filldir@fs/readdir.c").return
    {
        if(execname() == "ls")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }

    probe kernel.function("vfs_write@fs/read_write.c").call
    {
        if(execname() == "ls")
            printf("%s -> %s\n", thread_indent(1), probefunc());
    }

    probe kernel.function("vfs_write@fs/read_write.c").return
    {
        if(execname() == "ls")
            printf("%s <- %s\n", thread_indent(-1), probefunc());
    }


Run this SystemTap script and execute :command:`ls` in another
terminal window and you should see in the SystemTap window lines such
as these::

    0 ls(11381): -> btrfs_lookup_dentry
    32 ls(11381): <- btrfs_lookup
     0 ls(11381): -> btrfs_lookup_dentry
    15 ls(11381): <- btrfs_lookup
     0 ls(11381): -> btrfs_real_readdir
     5 ls(11381):  -> filldir : .
    11 ls(11381):  <- btrfs_real_readdir
    15 ls(11381):  -> filldir : ..
    18 ls(11381):  <- btrfs_real_readdir
    37 ls(11381):  -> filldir : sources�
    41 ls(11381):  <- btrfs_real_readdir
    46 ls(11381):  -> filldir : notes.rst
    50 ls(11381):  <- btrfs_real_readdir
    54 ls(11381):  -> filldir : ftrace_demo.c
    58 ls(11381):  <- btrfs_real_readdir
    63 ls(11381):  -> filldir : ftrace_demo.c
    .. 
    ..

    0 ls(11381): -> vfs_write
    31 ls(11381): <- sys_write
     0 ls(11381): -> vfs_write
    17 ls(11381): <- sys_write


The last few lines indicate the output of :command:`ls` being written
to the terminal.


See also
========

Some random links I came across while researching:

- http://www.cs.virginia.edu/~dww4s/articles/ld_linux.html
- http://www.win.tue.nl/~aeb/linux/vfs/trail-2.html
