class LogSystem:

    def __init__(self):
        self.time_position_dict = {"Year": 0, "Month": 1,
                                   "Day": 2, "Hour": 3, 
                                   "Minute": 4, "Second": 5}
        self.logs = {}

    def put(self, id, timestamp):
        self.logs[timestamp] = id

    def retrieve(self, s, e, gra):
        retrieve_logs = []
        need_length = self.time_position_dict[gra] + 1
        actual_s = self.decode_timestamp(s, need_length)
        actual_e = self.decode_timestamp(e, need_length)
        for timestamp in self.logs.keys():
            log_time = self.decode_timestamp(timestamp, need_length)
            if actual_s <= log_time and log_time <= actual_e:
                retrieve_logs.append(self.logs[timestamp])
        return retrieve_logs

    def decode_timestamp(self, timestamp, length):
        decoded_time = int("".join(timestamp.split(":")[0:length]))
        return decoded_time


if __name__ == "__main__":
    log_system = LogSystem()
    log_system.put(1, "2017:01:01:23:59:59")
    log_system.put(2, "2017:01:01:22:59:59")
    log_system.put(3, "2016:01:01:00:00:00")
    res = log_system.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00",
    "Hour")
    print(res)

