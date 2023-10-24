""" Build priority queue to handle real time tasks. It is assumed that all tasks arrive at same time. The 
attributes of tasks are task-id, priority and execution time. Compute waiting time, turnaround 
time for each job. It is treated that 10 is maximum priority and 1 is least priority.Include time range"""



import heapq
class Task:
    def __init__(self, task_id, priority, execution_time,arrival_time,deadline):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.arrival_time=arrival_time
        self.deadline = deadline

class maxHeap:
    def __init__(self, tasks=[]):
        self.data = tasks
        self._buildHeap()
        self.time=0
        self.start_time = None
        self.end_time = None
    
    def getCount(self):
        return len(self.data)
    def _parent(self,idx):
        return (idx-1)//2
    def _lchild(Self,idx):
        return (2*idx+1)
    def _rchild(self,idx):
        return (2*idx+2)
    def _swap(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]
    def _buildHeap(self):
        length=len(self.data)
        start=(length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap(idx,length)
    
    def _upHeap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j].priority > self.data[parent].priority:
            self._swap(j, parent)
            self._upHeap(parent)

    def _downHeap(self, idx, length):
        if self._lchild(idx) < length:
            left = self._lchild(idx)
            bigChild = left
            if self._rchild(idx) < length:
                right = self._rchild(idx)
                if self.data[right].priority > self.data[left].priority:
                    bigChild = right
            if self.data[bigChild].priority > self.data[idx].priority:
                self._swap(bigChild, idx)
                self._downHeap(bigChild, length)
    
    def addTask(self, task):
        if self.start_time <= task.arrival_time <= self.end_time:
            self.data.append(task)
            self._upHeap(len(self.data) - 1)
    
    def getHighestPriorityTask(self):
        return self.data[0]
    
    
    def set_schedule_time(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    
    def get_schedule(self):
        if self.start_time is None or self.end_time is None:
            return []

        self.time = self.start_time
        scheduled_tasks = []

        while not self.isEmpty() and self.time < self.end_time:
            task = self.getHighestPriorityTask()

            if self.time + task.execution_time <= task.deadline:
                task.turnaround_time = self.time + task.execution_time
                task.waiting_time = task.turnaround_time - task.execution_time
                self.time = task.turnaround_time
                scheduled_tasks.append(task)
            else:
                print(f"Missed the deadline Task ID={task.task_id}")

            
            
            self.data.pop(0)
        return scheduled_tasks
    
    def isEmpty(self):
        return len(self.data) == 0

# Create Task objects with task ID, priority, execution time, arrival time, and deadline
task1 = Task(1, 5, 3, 8, 0)
task2 = Task(2, 8, 4, 12, 2)
task3 = Task(3, 3, 2, 10, 3)
task4 = Task(4, 10, 5, 15, 5)
task5 = Task(5, 9, 15, 20, 7)

# Create a maxHeap and add tasks
task_queue = maxHeap()
task_queue.set_schedule_time(0,20) 
task_queue.addTask(task1)
task_queue.addTask(task2)
task_queue.addTask(task3)
task_queue.addTask(task4)


 


scheduled_tasks = task_queue.get_schedule()

for task in scheduled_tasks:
    print(f"Task ID={task.task_id}, Priority={task.priority}, Waiting Time={task.waiting_time}, Turnaround Time={task.turnaround_time}")








