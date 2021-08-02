class Queue:
    def __init__(self,n):
        self.q = [0 for i in range(n)]
        self.full_size = n
        self.q_size = 0
        self.f_idx = 0
        self.b_idx = 0

    def size(self):
        return self.q_size

    def empty(self):
        if self.q_size == 0:
            return 1
        return 0

    def front(self):
        if self.empty() == 1:
            return -1
        return self.q[self.f_idx]

    def back(self):
        if self.empty() == 1:
            return -1
        return self.q[self.b_idx-1]

    def push(self,x):
        if self.q_size == self.full_size:
            print(-1)
            return 
        self.q[self.b_idx] = x
        self.b_idx = (self.b_idx + 1) % self.full_size
        self.q_size += 1

    def pop(self):
        if self.q_size == 0:
            return -1
        temp = self.q[self.f_idx]
        self.f_idx = (self.f_idx + 1) % self.full_size
        self.q_size -= 1
        return temp

def run_cmd_with_queue(command, queue_obj):
    cmd_type = command[0]

    if cmd_type == "push":
        _, num = command
        queue_obj.push(int(num))
    elif cmd_type == "pop":
        print(queue_obj.pop())

    elif cmd_type == "size":
        print(queue_obj.size())

    elif cmd_type == "empty":
        print(queue_obj.empty())

    elif cmd_type == "front":
        print(queue_obj.front())

    elif cmd_type == "back":
        print(queue_obj.back())
    

n = int(input())  # q_size
queue_obj = Queue(n)

N = int(input())  # 실행횟수

for _ in range(N):
    run_cmd_with_queue(input().split(), queue_obj)