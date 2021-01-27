import matplotlib.pyplot as plt
import json


def draw_HP():
    x = []
    y = []
    y0 = []
    yc1 = []
    yc2 = []

    with open('./HP.txt', 'r') as f:
        while True:
            msg_json = f.readline()
            if not msg_json:
                break
            if msg_json == "\n":
                print("Get empty line")
                continue
            msg = json.loads(msg_json)
            # print(msg)

            #以时间字符串为x轴
            x.append(msg["time"][5:-3])
            #以时间戳为x轴
            #x.append(msg["time_stamp"] / 3600)

            y.append(msg["HP"])
            if msg["change"] > 0:
                yc1.append(msg["change"])
                yc2.append(0)
            else:
                yc1.append(0)
                yc2.append(msg["change"])
            y0.append(0)


    fig = plt.figure()
    fig.subplots_adjust(bottom=0.2)


    plt.bar(x, yc1, color="blue", label='+', alpha=0.8)
    plt.bar(x, yc2, color="red", label='-', alpha=0.8)
    plt.plot(x, y, c='black', label='HP')
    plt.plot(x, y0, c='black')

    for i in range(len(y)):
        if y[i] > 0:
            plt.text(x[i], y[i] + 1, ' %s' %round(y[i],3), ha='left', color = "black", fontsize=12)
        else :
            plt.text(x[i], y[i] + 1, ' %s' %round(y[i],3), ha='left', color = "black", fontsize=12)

    for i in range(len(yc1)):
        if yc1[i] != 0:
            plt.text(x[i], yc1[i]/2, '%s' %round(yc1[i],3), ha='center', color = "black", fontsize=8)

    for i in range(len(yc2)):
        if yc2[i] != 0:
            plt.text(x[i], yc2[i]/2, '%s' %round(yc2[i],3), ha='center', color = "black", fontsize=8)

    plt.title('Dead Point')
    plt.xlabel('Date')
    plt.ylabel('HP')
    plt.xticks(rotation=60)

    plt.legend()

    # plt.grid()
    plt.show()
