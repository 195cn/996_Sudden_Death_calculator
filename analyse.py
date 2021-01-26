
import time
import json

# 统计每一对【开始:结束】


def collect_cycle(start_act, end_act):
    last_start_msg = ""
    last_end_msg = ""
    cycle_list = []
    index = 0
    interval = 0

    # 读单行事件
    with open('./msg.txt', 'r') as f:
        while True:
            cycle_flag = True
            msg_json = f.readline()
            if not msg_json:
                break
            if msg_json == "\n":
                print("Get empty line")
                continue

            msg = json.loads(msg_json)
            #print(msg)

            # 默认首条录入为开始行为
            if msg['action'] == start_act:
                #print("Get start action")
                last_start_msg = msg
                cycle_flag = True

            # 录入开始行为后检测结束行为
            if msg['action'] == end_act and cycle_flag == True:
                #print("Get end action")
                # 首条结束行为，无间隔
                if index == 0:
                    interval = 0

                # 非首条结束行为，last_end_msg保存上一条结束行为，last_start_msg为本次开始行为。

                else:
                    # 计算上一条结束到本次开始的时间戳差
                    timeArray_start = time.strptime(
                        last_start_msg['time'], "%Y-%m-%d %H:%M:%S")
                    timeStamp_start = int(time.mktime(timeArray_start))
                    timeArray_end = time.strptime(
                        last_end_msg['time'], "%Y-%m-%d %H:%M:%S")
                    timeStamp_end = int(time.mktime(timeArray_end))
                    interval = timeStamp_start - timeStamp_end

                # 更新为本次结束行为
                last_end_msg = msg

                # 计算本次开始到本次结束的时间戳差
                timeArray_start = time.strptime(
                    last_start_msg['time'], "%Y-%m-%d %H:%M:%S")
                timeStamp_start = int(time.mktime(timeArray_start))
                timeArray_end = time.strptime(
                    last_end_msg['time'], "%Y-%m-%d %H:%M:%S")
                timeStamp_end = int(time.mktime(timeArray_end))
                exist_time = timeStamp_end - timeStamp_start

                cycle_msg = {}
                cycle_msg["index"] = index
                cycle_msg["type"] = start_act + ":" + end_act
                cycle_msg["start"] = last_start_msg['time']
                cycle_msg["start_stamp"] = timeStamp_start
                cycle_msg["end"] = last_end_msg['time']
                cycle_msg["end_stamp"] = timeStamp_end
                cycle_msg["exist"] = exist_time
                cycle_msg["interval"] = interval

                cycle_list.append(cycle_msg)

                index += 1

    # print(cycle_list)

    with open('./analyse.txt', 'w') as f:
        for cycle in cycle_list:
            analyse_line = json.dumps(cycle)
            f.write(analyse_line)
            f.write("\n")

    return


def create_analyse_file():
    collect_cycle("sleep", "wakeup")
    pass
