class Solution:
    def kill_process(self, pid, ppid, kill):
        children_of_ppid = {}
        for i, id in enumerate(ppid):
            if children_of_ppid.get(id, 0):
                children_of_ppid[id].append(pid[i])
            else:
                children_of_ppid[id] = [pid[i]]

        queue = [kill]
        killed_pids = []
        while len(queue) > 0:
            current_kill = queue.pop()
            killed_pids.append(current_kill)
            queue.extend(children_of_ppid.get(current_kill, []))

        return killed_pids
            

if __name__ == "__main__":
    pid = [1, 3, 10, 5]
    ppid = [9,9,9,9]
    kill = 9
    killed_pids = Solution().kill_process(pid, ppid, kill)
    print(killed_pids)
