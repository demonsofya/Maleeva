from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    
    plt.title("Зависимость напряжения АЦП от времени", fontsize = 14)
    plt.xlabel("Время (с)", fontsize = 12)
    plt.ylabel("Напряжение (В)", fontsize = 12)

    if time:
        plt.xlim(0, max(time))
    plt.ylim(0, max_voltage * 1.1)

    plt.grid(True, alpha = 0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)

    plt.title("Распределение периодов измерений", fontsize = 14)
    plt.xlabel("Период измерения (с)", fontsize = 12)
    plt.ylabel("Количество измерений", fontsize = 12)   

    plt.xlim(0, 0.1)
    plt.grid(True, alpha = 0.3)

    plt.tight_layout()
    plt.show()
