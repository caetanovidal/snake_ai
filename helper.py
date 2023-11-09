import matplotlib.pyplot as plt
import matplotlib
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)


def save_record(record):
    file_name = 'model/record.txt'

    with open(file_name, 'w') as f:
        f.write(str(record))

def load_record():
    file_name = 'model/record.txt'

    try:
        with open(file_name, 'r') as f:
            record = int(f.read())
    except FileNotFoundError:
        record = 0
    
    return record