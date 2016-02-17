# Chapter 2 Review Questions
Name: Mounika Madireddy
Course: 5143 Operating Systems
Date: 17 Feb 2016


## 1.What are three objectives of an OS design?
**The three main objectives of an OS design are:**

1. _Convenience_: An operating system should make the computer more convienient to use.
2. _Efficiency_: An operating system should allow the computer resources to be used efficiently.
3. _Ability to evolve_:An opearing system should be constructed in such a way to permit the effective development for testing, and for introduction of new systems with out interfering with the system.

## What is the kernel of an OS?
**_Kernel_** is the computer program that manages the input requests and output requests from a software and translates them into data processing instructions for CPU.

## What is multiprogramming?
**_Multiprogramming_** is an approach to resource management. In multiprogramming system when one program is waiting for I/O ,there is another program ready to utilize the CPU, so as to acheive maximum efficiency.

## What is a process?
A program in execution is known as a **_process_** (or)  process is defined as an entity that is assigned and executed on a processor.
## How is the execution context of a process used by the OS?
Operating system uses process control block (PCB) for execution of a process. All the information needed to manage that particular process is kept in process control block.
## List and briefly explain five storage management responsibilities of a typical OS?
The five storage management responsibilities of a typical OS is:

1. **Process isolation**: It is the segregation of a different processes to prevent them from accessing memory space they do not own.This can be done by providing privilige levels to certain programs and restricting the memory that they use.
2. **Automatic allocation and management**: memory should be allocated dynamically for the programs and user must know the memory limitations and  OS can  acheive efficiency by assigning memory to jobs only as needed.
3. **Support of modular programming**: OS should provide flexibility for the programmers to define, create ,destroy and alter the size of the module dynamically.
4. **Protection and access control**:  Sharing of memory between programs creates the potential of one program for accessing the memory space of another program ,which is threatens the integrity of programs,so the OS should allow only the portions of memory to be accessible in various ways by various users.
5. **Long term storage**: Many programs needed to be stored for further usage even after the computer shutdowns so it has be stored for further usage.

## Explain the distinction between a real address and a virtual address?
**Real address** tells us where exactly a program is stored in main memory.

**virtual address** is a reference to access the program in main memory.

## Describe the round-robin scheduling technique?
**Round robin scheduling** : It is scheduling algorithm used by the CPU during process execution, preemption is added to switch among processes.A small unit of time known as time slice is defined.All processes in this algorithm are placed in a circular queue also known as ready queue. By using this algorithm the CPU make sures that time slices are assigned to each process and each process is executed for fixed interval of time without any priority.

## Explain the difference between a monolithic kernel and a microkernel?
1. In **_monolithic kernel_** OS is provided with large kernels including scheduling,file system,drives and memory management and it is implemented in a single process.
2.  whereas **_micro kerenel_** assigns only a few functions to kernel inlcuding inter process communication(IPC) and basic scheduling and remaining other functions are assigned to servers.

## What is multithreading?
**_Multithreading_** is a technique in which a process executing the application is  divided into sub tasks known as threads that can run concurrently.The OS handles the resources to individual threads and switches these allocations from one running thread to another.This gives the apperance that all the threads are running at same time.

## List the key design issues for an SMP operating system?
The key design issues for an SMP operating systems are:

* simultaenous concurrent process or threads.
* Synchronization
* Memory management
* scheduling
* Reliability and fault tolerance 
