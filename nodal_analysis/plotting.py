import matplotlib.pyplot as plt


def create_plot(VLP, IPR, Q):
    plt.plot(Q, [VLP.production(q) for q in Q], label='VLP')
    plt.plot(Q, [IPR.production(q) for q in Q], label='IPR')
    plt.title('Узловой анализ')
    plt.xlabel('Дебит')
    plt.ylabel('Давление')
    plt.legend()
    plt.grid()
    plt.show()
    