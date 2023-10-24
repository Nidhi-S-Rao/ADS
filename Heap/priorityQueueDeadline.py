""" Build priority queue to handle real time tasks. It is assumed that all tasks arrive at same time. The 
attributes of tasks are task-id, priority and execution time. Compute waiting time, turnaround 
time for each job. It is treated that 10 is maximum priority and 1 is least priority.Include deadline for each job"""


class Task:
    def __init__(self, task_id, priority, execution_time,deadline):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.deadline = deadline

class maxHeap:
    def __init__(self, tasks=[]):
        self.data = tasks
        self._buildHeap()
        self.time=0
    
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
        self.data.append(task)
        self._upHeap(len(self.data) - 1)
    
    def getHighestPriorityTask(self):
        return self.data[0]
    
    def executeTask(self):
        task = self.data[0]
        if self.time + task.execution_time <= task.deadline:
            task.turnaround_time = self.time 
            task.waiting_time = task.turnaround_time - task.execution_time
            self.time+=task.execution_time
        else:
            print("Missed the deadline")
        self._swap(0, len(self.data) - 1)
        self.data.pop()
        self._downHeap(0, len(self.data))
        
        return task

    def isEmpty(self):
        return len(self.data) == 0





task1 = Task(1, 5, 3, 8)
task2 = Task(2, 8, 4, 12)
task3 = Task(3, 3, 2, 10)
task4 = Task(4, 10, 5, 15)


task_queue = maxHeap()
task_queue.addTask(task1)
task_queue.addTask(task2)
task_queue.addTask(task3)
task_queue.addTask(task4)


highest_priority_task = task_queue.getHighestPriorityTask()
print(f"Highest Priority Task: Task ID={highest_priority_task.task_id}, Priority={highest_priority_task.priority}")


while not task_queue.isEmpty():
    current_task = task_queue.executeTask()
    print(f"Task ID={current_task.task_id},Waiting Time={current_task.waiting_time},Turnaround Time={current_task.turnaround_time} ")
   