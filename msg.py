import time
import json

actions = ['wakeup', 'sleep']

def get_time_str():
    now_time = time.time()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))
    print(now_time)
    print(localtime)
    return localtime


def create_msg(time, action):
    index = get_index()
    msg = {}
    msg['index'] = index
    msg['time'] = time
    msg['action'] = action
    return json.dumps(msg)


def add_msg(msg):
    with open('./msg.txt', 'a') as f:

        f.write(msg)
        f.write("\n")
    pass


def get_index():
    index = 0
    with open('./msg.txt', 'r') as f:

        while True:
            msg = f.readline()
            if not msg:
                break
            if msg == "\n":
                continue
            #print(msg)
            msg_json = json.loads(msg)
            index = msg_json['index'] + 1
    return index


def main():

    add_msg(create_msg("2021-01-26 13:10:00", "sleep"))
    #time.sleep(10)
    add_msg(create_msg("2021-01-26 13:30:00", "wakeup"))



if __name__ == '__main__':
    main()
    # print(__name__)
