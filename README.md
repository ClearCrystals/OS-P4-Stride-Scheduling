# Stride Scheduling for xv6
In this project, I put in a new scheduler into xv6. It is called a stride scheduler, and the algorithm is described in Figure 1 in this paperLinks to an external site..

The objectives for this project:

To gain further knowledge of a real kernel, xv6.
To familiarize myself with a scheduler.
To change that scheduler to implement a new algorithm - stride scheduling

## Stride Scheduling
The basic idea in stride scheduling is the following:

Each process is assigned tickets, and the stride is inversely proportional to the number of tickets assigned, specifically calculated as stride = max_stride / tickets, where max_stride is the maximum stride, which is a constant number.
Each process has a pass value, which starts from the stride and is incremented by the stride every time the process executes for a time slot
The scheduler schedules a runnable process with the minimum pass value to run in the next time slot.
For example:

Max stride = 12, tickets for processes: A: 3, B: 2:

stride(A) = 12/3 = 4, stride(B) = 12/2 = 6

Initial values for pass(A) = 4, pass(B) = 6

Process A has a lower pass value, so it will be first chosen for scheduling. After process A runs for 1 time slot, the pass values will be

pass(A) = 4 (initial) + 4 (stride(A)) = 8 pass(B) = 6

Now process B has the lower pass value and will be chosen for scheduling in the next time slot and so on.

After a while

If process A executes 5 time slots, pass(A) = 4 (initial) + 4 * 5 (stride(A) * slots) = 24

If process B executes 5 time slots, pass(B) = 6 (initial) + 6 * 5 (stride(A) * slots) = 36

Implementation/setup details
Set CPUS := 1 in the Makefile to see the effect of scheduling on a single CPU
The max_stride value should be greater than max tickets allocated to any process and preferably divisble by ticket values for getting more accurate strides (assuming an integer max_stride)
If the number of tickets is changed while a process is executing, we update the tickets, stride, but not the pass value. So, the updated tickets will not reflect immediately in actual scheduling due to the existing pass values.
We will not test for a dynamic allocation of tickets, since the algorithm is meant to handle a static allocation
Details
Need two new system calls to implement this scheduler. The first is int settickets(int number), which sets the number of tickets of the calling process. By default, each process should get one ticket; calling this routine makes it such that a process can raise the number of tickets it receives, and thus receive a higher proportion of CPU cycles. This routine should return 0 if successful, and -1 otherwise (if, for example, the caller passes in a number less than one).

The second is int getpinfo(struct pstat *). This routine (detailed below) returns information about all running processes, including how many times each process has been chosen to run and the process ID of each process. Can use this system call to build a variant of the command line program ps, which can then be called to see what is going on. The structure pstat is defined below; note, cannot change this structure, and must use it exactly as is. This routine should return 0 if successful, and -1 otherwise (if, for example, a bad or NULL pointer is passed into the kernel).

Most of the code for the scheduler is quite localized and can be found in proc.c; the associated header file, proc.h is also quite useful to examine. To change the scheduler, not much needs to be done; study its control flow and then try some small changes.

Good examples of how to pass arguments into the kernel are found in existing system calls. In particular, follow the path of read(), which will lead to sys_read(), which will show how to use argptr() (and related calls) to obtain a pointer that has been passed into the kernel. Note how careful the kernel is with pointers passed from user space -- they are a security threat(!), and thus must be checked very carefully before usage.

Need to assign tickets to a process when it is created. Specifically, A child process inherits the same number of tickets as its parents. Thus, if the parent has 10 tickets and has a stride of 2, and calls fork() to create a child process, the child should also get 10 tickets, will have stride 2, and its pass value starts from its stride value (2). The first process - init starts with 1 ticket, and stride of max_stride, and pass value of max_stride. The pass value of a process is never reset for the purposes of this project.

To run the tests:

1. Navigate to the base directory of the xv6 code
2. From that directory, execute the runtests executable in this directory
  Like:  ~cs537-1/tests/P4/runtests

The output from runtests will indicate which tests that have passed and which that have failed (if any)

For more options available while testing, run '.../runtests -h'
