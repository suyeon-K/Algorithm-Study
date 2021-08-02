class Queue:
    def __init__(self, n):
        self.array = [None for _ in range(n)]
        self.f_idx = 0
        self.b_idx = 0
        self.q_size = n
        self.q_empty = True

    def push(self, num):

        if self.is_empty():
            self.q_empty = False
        elif self.is_full():
            print(-1)
            return

        self.array[self.b_idx] = num
        self.b_idx = (self.b_idx + 1) % self.q_size
        

    def pop(self):
        
        if self.is_empty():
            return -1
        
        pop_val = self.array[self.f_idx]
        self.f_idx = (self.f_idx + 1) % self.q_size

        if self.f_idx == self.b_idx:
            self.q_empty = True

        return pop_val


    def size(self):
        if self.f_idx == self.b_idx:
            if self.is_empty():
                return 0
            else:
                return self.q_size
        elif self.f_idx < self.b_idx:
            return self.b_idx - self.f_idx
        else:
            return self.b_idx - self.f_idx + self.q_size


    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0

    def front(self):
        if self.is_empty():
            return -1

        return self.array[self.f_idx]

    def back(self):
        if self.is_empty():
            return -1
        
        return self.array[self.b_idx-1]

    # 내부 도움 함수
    def is_empty(self):
        return self.q_empty

    def is_full(self):
        return self.size() == (self.q_size)


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