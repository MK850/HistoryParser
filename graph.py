import HistoryParser
import matplotlib.pyplot as plt
import numpy as np

def main():
    visit_count=HistoryParser.web_value
    max_visit=max(visit_count)

    y=HistoryParser.web_key

    #  bar plot으로 나타낼 데이터 입력
    models = ['Visit Count']
    yticks = y
    data = {'Visit Count':visit_count }

    #  matplotlib의 figure 및 axis 설정
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))  # 1x1 figure matrix 생성, 가로(7인치)x세로(5인치) 크기지정
    colors = ['salmon']
    height = 0.2

    # bar 그리기
    for i, model in enumerate(models):
        pos = compute_pos(yticks, height, i, models)
        bar = ax.barh(pos, data[model], height=height *2, label=model, color=colors[i])
        present_width(ax, bar)  # bar너비 출력

    # x축 세부설정
    ax.set_xlim([0, max_visit+1])
    ax.xaxis.set_tick_params(labelsize=10)
    ax.set_xlabel('Visit Count', fontsize=14)

    # y축 세부설정
    ax.set_yticks(range(len(yticks)))
    ax.set_yticklabels(yticks, fontsize=8)
    ax.set_ylabel('Web Site', fontsize=14)

    # 범례
    box = ax.get_position()  # 범례를 그래프상자 밖에 그리기위해 상자크기를 조절
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True, ncol=1)

    # 7. 보조선(눈금선)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)

    # 8. 그래프 저장 & 출력
    plt.savefig('ex_barhplot.png', format='png', dpi=300)
    plt.show()


def compute_pos(yticks, height, i, models):
    index = np.arange(len(yticks))
    n = len(models)
    correction = i - 0.5 * (n - 1)
    return index + height * correction


def present_width(ax, bar):
    for rect in bar:
        witdh = rect.get_width()
        posx = witdh * 1.01
        posy = rect.get_y() + rect.get_height() * 0.5
        ax.text(posx, posy, '%d' % witdh, rotation=0, ha='left', va='center')

if __name__ == '__main__':
    main()

