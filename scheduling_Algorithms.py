class FirstComeFirstServe:  #pag pinili yung 1
    def processData(self, no_of_processes):
        data = []
        for i in range(no_of_processes):
            temp = []
            process_id = (f"P{str(i + 1)}")
            while True:
                try:
                    arrival_time = int(input(f"Enter Arrival Time for Process [{process_id}]: "))
                    if arrival_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            while True:
                try:
                    burst_time = int(input(f"Enter Burst Time for Process [{process_id}]: "))
                    print("_____________________________________________________")
                    if burst_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue

            temp.extend([process_id, arrival_time, burst_time])
            data.append(temp)
        FirstComeFirstServe.schedulingProcess(self, data)

    def schedulingProcess(self, data):
        data.sort(key=lambda x: x[1])

        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(data)):
            if s_time < data[i][1]:
                s_time = data[i][1]
            start_time.append(s_time)
            s_time = s_time + data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            data[i].append(e_time)
        TurnAroundTime = FirstComeFirstServe.Cal_TAT(self, data)
        WaitingTime = FirstComeFirstServe.Cal_WT(self, data)
        FirstComeFirstServe.printData(self, data, TurnAroundTime, WaitingTime)

    def Cal_TAT(self, data):
        total_turnaround_time = 0
        for i in range(len(data)):
            turnaround_time = data[i][3] - data[i][1]                  # turnaround_time = completion_time - arrival_time
            total_turnaround_time = total_turnaround_time + turnaround_time
            data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(data)            # average_turnaround_time = total_turnaround_time / Processes

        return average_turnaround_time

    def Cal_WT(self, data):
        total_waiting_time = 0
        for i in range(len(data)):
            waiting_time = data[i][4] - data[i][2]                   # waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time + waiting_time
            data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(data)                # average_waiting_time = total_waiting_time / Processes

        return average_waiting_time

    def printData(self, data, average_turnaround_time, average_waiting_time): #printing turnaroundtime and waiting time
        print("----------------------------------------------------------------------------------------")
        print("Process_ID\t  Arrival_Time  Burst_Time\t  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(data)):
            for j in range(len(data[i])):
                print(data[i][j], end="				")
            print()
        print("_____________________________________________________")
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("_____________________________________________________")
        while True:
            restart = input("\nMain Menu?[y/n]: ")
            if restart == 'Y' or restart == 'y':
                main()
            elif restart == 'N' or restart == 'n':
                exit()
            else:
                print("Error. Please type 'Y' for 'YES and 'N' for 'NO' ")
class ShortestJobFirst: #Pagpinili yung 2

    def processData(self, processes):
        data = []
        for i in range(processes):
            temp = []
            process_id = (f"P{str(i + 1)}")
            while True:
                try:
                    arrival_time = int(input(f"Enter Arrival Time for Process [{process_id}]: "))
                    if arrival_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            while True:
                try:
                    burst_time = int(input(f"Enter Burst Time for Process [{process_id}]: "))
                    print("_____________________________________________________")
                    if burst_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            temp.extend([process_id, arrival_time, burst_time, 0, burst_time])
            data.append(temp)
        ShortestJobFirst.scheduling(self, data)


    def scheduling(self, data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        data.sort(key=lambda x: x[4]) #magsosort depende sa burst
        data.sort(key=lambda x: x[0]) #magsosort depende sa process id
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(data)):
                if data[i][1] <= s_time and data[i][3] == 0:
                    temp.extend([data[i][0], data[i][1], data[i][2], data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif data[i][3] == 0:
                    temp.extend([data[i][0], data[i][1], data[i][2], data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2]) #magsosort depende sa burst
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for p in range(len(data)):
                    if data[p][0] == ready_queue[0][0]:
                        break
                data[p][2] = data[p][2] - 1
                if data[p][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    data[p][3] = 1
                    data[p].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for p in range(len(data)):
                    if data[p][0] == normal_queue[0][0]:
                        break
                data[p][2] = data[p][2] - 1
                if data[p][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    data[p][3] = 1
                    data[p].append(e_time)
        t_time = ShortestJobFirst.Cal_TAT(self, data)
        w_time = ShortestJobFirst.Cal_WT(self, data)
        ShortestJobFirst.printData(self, data, t_time, w_time, sequence_of_process)

    def Cal_TAT(self, data):
        total_turnaround_time = 0
        for i in range(len(data)):
            turnaround_time = data[i][5] - data[i][1]                               #turnaround_time = completion_time - arrival_time
            total_turnaround_time = total_turnaround_time + turnaround_time
            data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(data)                         #average_turnaround_time = total_turnaround_time / processes
        return average_turnaround_time

    def Cal_WT(self, data):
        total_waiting_time = 0
        for i in range(len(data)):
            waiting_time = data[i][6] - data[i][4]                               #waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time + waiting_time
            data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(data)#average_waiting_time = total_waiting_time / processes
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        for i in range(0, len(process_data)):
            process_data[i].pop(2)
            process_data[i].pop(2)
        process_data.sort(key=lambda x: x[0])
        print("----------------------------------------------------------------------------------------")
        print("Process_ID\t  Arrival_Time  Burst_Time\t  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="				")
            print()
        print("_____________________________________________________")
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("_____________________________________________________")
        while True:
            restart = input("\nMain Menu?[y/n]: ")
            if restart == 'Y' or restart == 'y':
                main()
            elif restart == 'N' or restart == 'n':
                exit()
            else:
                print("Error. Please type 'Y' for 'YES and 'N' for 'NO' ")
class Priority: #pagpinili yung 3

    def processData(self, processes):
        data = []
        for i in range(processes):
            temporary = []
            process_id = (f"P{str(i + 1)}")
            while True:
                try:
                    arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
                    if arrival_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            while True:
                try:
                    burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
                    if burst_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            while True:
                try:
                    priority = int(input(f"Enter Priority for Process {process_id}: "))
                    print("_____________________________________________________")
                    if priority < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            temporary.extend([process_id, arrival_time, burst_time, priority, 0, burst_time])
            data.append(temporary)
        Priority.schedulingProcess(self, data)

    def schedulingProcess(self, data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        data.sort(key=lambda x: x[1]) #Sort processes according to the Arrival Time
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(data)):
                if data[i][1] <= s_time and data[i][4] == 0:
                    temp.extend([data[i][0], data[i][1], data[i][2], data[i][3],
                                 data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif data[i][4] == 0:
                    temp.extend([data[i][0], data[i][1], data[i][2], data[i][4],
                                 data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(data)):
                    if data[k][0] == ready_queue[0][0]:
                        break
                data[k][2] = data[k][2] - 1
                if data[k][2] == 0:       #if burst time is zero, it means process is completed
                    data[k][4] = 1
                    data[k].append(e_time)
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(data)):
                    if data[k][0] == normal_queue[0][0]:
                        break
                data[k][2] = data[k][2] - 1
                if data[k][2] == 0:        #if burst time is zero, it means process is completed
                    data[k][4] = 1
                    data[k].append(e_time)
        t_time = Priority.Cal_TAT(self, data)
        w_time = Priority.Cal_WT(self, data)
        Priority.printData(self, data, t_time, w_time, sequence_of_process)

    def Cal_TAT(self, data):
        total_turnaround_time = 0
        for i in range(len(data)):
            turnaround_time = data[i][6] - data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(data)
        return average_turnaround_time

    def Cal_WT(self, data):
        total_waiting_time = 0
        for i in range(len(data)):
            waiting_time = data[i][7] - data[i][5]  #waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time + waiting_time
            data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(data) #average_waiting_time = total_waiting_time / processes
        return average_waiting_time

    def printData(self, data, average_turnaround_time, average_waiting_time, sequence_of_process):
        data.sort(key=lambda x: x[0])
        for i in range(0, len(data)):
            data[i].pop(2)
            data[i].pop(3)
        print("---------------------------------------------------------------------------------------------------------")
        print("Process_ID  Arrival_Time    Priority       Burst_Time    Completion_Time   Turnaround_Time   Waiting_Time")
        for i in range(len(data)):
            for j in range(len(data[i])):
                print(data[i][j], end="				")
            print()
        print("_____________________________________________________")
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("_____________________________________________________")
        while True:
            restart = input("\nMain Menu?[y/n]: ")
            if restart == 'Y' or restart == 'y':
                main()
            elif restart == 'N' or restart == 'n':
                exit()
            else:
                print("Error. Please type 'Y' for 'YES and 'N' for 'NO' ")
class RoundRobin:

    def processData(self, no_of_processes):
        data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = (f"P{str(i + 1)}")
            while True:
                try:
                    arrival_time = int(input(f"Enter Arrival Time for Process [{process_id}]: "))
                    if arrival_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue
            while True:
                try:
                    burst_time = int(input(f"Enter Burst Time for Process [{process_id}]: "))
                    print("_____________________________________________________")
                    if burst_time < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cant accept negative Number and special character, Please try again..")
                    continue

            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            data.append(temporary)

        Quantum = int(input("Enter Quantum: "))

        RoundRobin.schedulingProcess(self, data, Quantum)

    def schedulingProcess(self, data, Quantum):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        data.sort(key=lambda x: x[1]) #Sort processes according to the Arrival Time
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(data)):
                if data[i][1] <= s_time and data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:                  #checks that the next process is not a part of ready_queue
                        for k in range(len(ready_queue)):
                            if data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:                           #loop adds a process to the ready_queue only if it is not already present in it
                        temp.extend([data[i][0], data[i][1], data[i][2], data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:    #loop makes sure that the recently executed process is appended at the end of ready_queue
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                elif data[i][3] == 0:
                    temp.extend([data[i][0], data[i][1], data[i][2], data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > Quantum: #If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    start_time.append(s_time)
                    s_time = s_time + Quantum
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == ready_queue[0][0]:
                            break
                    data[j][2] = data[j][2] - Quantum
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= Quantum:  #If a process has a remaining burst time less than or equal to time quantum, it will complete its execution
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == ready_queue[0][0]:
                            break
                    data[j][2] = 0
                    data[j][3] = 1
                    data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > Quantum: #f process has remaining burst time greater than the time quantum, it will execute for a time period equal to time slice and then switch
                    start_time.append(s_time)
                    s_time = s_time + Quantum
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == normal_queue[0][0]:
                            break
                    data[j][2] = data[j][2] - Quantum
                elif normal_queue[0][2] <= Quantum: #If a process has a remaining burst time less than or equal to time quantum, it will complete its execution
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == normal_queue[0][0]:
                            break
                    data[j][2] = 0
                    data[j][3] = 1
                    data[j].append(e_time)
        t_time = RoundRobin.Cal_TAT(self, data)
        w_time = RoundRobin.Cal_WT(self, data)
        RoundRobin.printData(self, data, t_time, w_time, executed_process)

    def Cal_TAT(self, data):
        total_turnaround_time = 0
        for i in range(len(data)):
            turnaround_time = data[i][5] - data[i][1] #turnaround_time = completion_time - arrival_time
            total_turnaround_time = total_turnaround_time + turnaround_time
            data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(data) #average_turnaround_time = total_turnaround_time / processes
        return average_turnaround_time

    def Cal_WT(self, data):
        total_waiting_time = 0
        for i in range(len(data)):
            waiting_time = data[i][6] - data[i][4] #waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time + waiting_time
            data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(data) #average_waiting_time = total_waiting_time / processes
        return average_waiting_time

    def printData(self, data, average_turnaround_time, average_waiting_time, executed_process):
        data.sort(key=lambda x: x[0])
        for i in range(0, len(data)):
            data[i].pop(2)
            data[i].pop(2)
        print(
            "Process_ID  Arrival_Time  Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(data)):
            for j in range(len(data[i])):
                print(data[i][j], end="				")
            print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("_____________________________________________________")
        while True:
            restart = input("\nMain Menu?[y/n]: ")
            if restart == 'Y' or restart == 'y':
                main()
            elif restart == 'N' or restart == 'n':
                exit()
            else:
                print("Error. Please type 'Y' for 'YES and 'N' for 'NO' ")
'''
main menu for scheduling algorithm
'''
def main():
    print("====Simple Process Scheduling====")
    print("[1]First Come First Serve")
    print("[2]Shortest Job First{Pre-emptive}")
    print("[3]Priority{Pre-emptive}")
    print("[4]Round Robin")
    print("[5]Quit")
    while True:
        try:
            print("_____________________________________________________")
            Scheduler = int(input("Choose Algorithm: "))
            print("_____________________________________________________")
            if Scheduler == 1:
                while True:
                    try:
                        Processes = int(input("Enter number of processes: "))
                        print("_____________________________________________________")
                        if Processes <= 0:
                            print("No Data to be Process.")
                            raise ValueError
                        break
                    except ValueError:
                        print("_____________________________________________________")
                        print("please input  positive integer only..")
                        continue
                fcfs = FirstComeFirstServe()
                fcfs.processData(Processes)
            elif Scheduler == 2:
                while True:
                    try:
                        Processes = int(input("Enter number of processes: "))
                        print("_____________________________________________________")
                        if Processes <= 0:
                            print("No Data to be Process.")
                            raise ValueError
                        break
                    except ValueError:
                        print("_____________________________________________________")
                        print("please input  positive integer only..")
                        continue
                sjf = ShortestJobFirst()
                sjf.processData(Processes)
            elif Scheduler == 3:
                while True:
                    try:
                        Processes = int(input("Enter number of processes: "))
                        print("_____________________________________________________")
                        if Processes <= 0:
                            print("No Data to be Process.")
                            raise ValueError
                        break
                    except ValueError:
                        print("_____________________________________________________")
                        print("please input  positive integer only..")
                        continue
                priority = Priority()
                priority.processData(Processes)
            elif Scheduler == 4:
                while True:
                    try:
                        Processes = int(input("Enter number of processes: "))
                        print("_____________________________________________________")
                        if Processes <= 0:
                            print("No Data to be Process.")
                            raise ValueError
                        break
                    except ValueError:
                        print("_____________________________________________________")
                        print("please input  positive integer only..")
                        continue
                rr = RoundRobin()
                rr.processData(Processes)
            elif Scheduler == 5:
                while True:
                    restart = input("\nExit?[y/n]: ")
                    if restart == 'Y' or restart == 'y':
                        exit()
                    elif restart == 'N' or restart == 'n':
                        main()
                    else:
                        print("Error. Please type 'Y' for 'YES and 'N' for 'NO' ")
            else:
                print("Choose 1-5 only....")
        except ValueError:
            print("_____________________________________________________")
            print("please input integer only..")
            continue
main()