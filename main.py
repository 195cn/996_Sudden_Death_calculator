import HP
import analyse
import draw




def main():
    analyse.create_analyse_file()
    HP.create_HP_file()
    draw.draw_HP()
    pass

if __name__ == '__main__':
    main()
    # print(__name__)