log1 = """Jun  4 03:43:02 10.0.0.1 systemd: Removed slice user-0.slice.
Jun  4 03:43:02 10.0.0.2 systemd: Stopping user-0.slice.
Jun  4 03:50:01 10.0.0.3 systemd: Created slice user-0.slice.
Jun  4 03:50:01 10.0.0.4 systemd: Starting user-0.slice.
Jun  4 03:50:01 10.0.0.5 systemd: Started Session 879 of user root.
"""

log2 = """Jun  4 03:43:02 10.0.0.3 systemd: Removed slice user-0.slice.
Jun  4 03:43:02 10.0.0.4 systemd: Stopping user-0.slice.
Jun  4 03:50:01 10.0.0.5 systemd: Created slice user-0.slice.
Jun  4 03:50:01 10.0.0.6 systemd: Starting user-0.slice.
Jun  4 03:50:01 10.0.0.7 systemd: Started Session 879 of user root.
"""

ip_set_1 = set()
ip_set_2 = set()
hash_dict = {}

for log in [log1, log2]:
    for line in log.split("\n"):
        words = line.split(" ")
        #should be an regex checking IP
        if len(words) >4 : 
            ip = words[4]
        else:
            print("log entry missing IP:", words)
        print(ip)
        if log == log1:
            ip_set_1.add(ip)
        else:
            ip_set_2.add(ip)

for item in list(ip_set_1) + list(ip_set_2):
    if item not in hash_dict:
        hash_dict[item] = 1
    else:
        hash_dict[item] += 1
        if hash_dict[item] == 2:
           print("duplicate", item)

