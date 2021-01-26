import time
import json

"""
首先正常人睡8小时，活动16小时，保持生命平衡
8s = 16w
假设人类可以满负荷活动32小时猝死
即 100HP = 32w
w = 25/8 = 3.125 (HP/hour) 
s = 2w = 25/4 = 6.25(HP/hour)
"""

# 醒着掉血
def HP_cost(interval):
    # 每小时消耗HP：
    cost_unit = 3.125

    cost = - interval * cost_unit / 3600
    return int(cost)


# 睡觉回血
def HP_recover(exist):
    # 每小时恢复HP：

    recover_unit = 6.25
    recover = exist * recover_unit / 3600
    return int(recover)


def HP_calculate():
    HP_list = []

    with open('./analyse.txt', 'r') as f:
        while True:
            msg_json = f.readline()
            if not msg_json:
                break
            if msg_json == "\n":
                print("Get empty line")
                continue

            msg = json.loads(msg_json)
            # print(msg)

            # init
            if msg['index'] == 0:
                continue
            elif msg['index'] == 1:
                HP_init = {}
                HP_init["flag"] = "Begin"
                HP_init["index"] = 0
                HP_init["HP"] = 100
                HP_init["change"] = 100
                HP_init["time_stamp"] = msg['end_stamp']
                HP_init["time"] = msg['end']
                HP_list.append(HP_init)
            else:
                HP_start = {}
                HP_start["index"] = len(HP_list)
                HP_start["change"] = HP_cost(msg['interval'])
                HP_start["HP"] = HP_list[len(
                    HP_list) - 1]["HP"] + HP_start["change"]
                HP_start["time_stamp"] = msg['start_stamp']
                HP_start["time"] = msg['start']
                HP_list.append(HP_start)

                HP_end = {}
                HP_end["index"] = len(HP_list)
                HP_end["change"] = HP_recover(msg['exist'])
                HP_end["HP"] = HP_list[len(
                    HP_list) - 1]["HP"] + HP_end["change"]
                if HP_end["HP"] > 100:
                    HP_end["HP"] = 100
                HP_end["time_stamp"] = msg['end_stamp']
                HP_end["time"] = msg['end']
                HP_list.append(HP_end)

        # 和现在时间比较
        HP_now = {}
        HP_now["flag"] = "Now"
        HP_now["time_stamp"] = int(time.time())
        HP_now["time"] = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(HP_now["time_stamp"]))
        last_interval = HP_now["time_stamp"] - \
            HP_list[len(HP_list) - 1]["time_stamp"]
        HP_now["index"] = len(HP_list)
        HP_now["change"] = HP_cost(last_interval)
        HP_now["HP"] = HP_list[len(HP_list) - 1]["HP"] + HP_now["change"]
        HP_list.append(HP_now)
        print(HP_now)

    return HP_list


def create_HP_file():
    # print(HP_calculate())
    with open('./HP.txt', 'w') as f:
        for HP in HP_calculate():
            analyse_line = json.dumps(HP)
            f.write(analyse_line)
            f.write("\n")
    pass
