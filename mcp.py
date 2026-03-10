from mcp3021_dravier import MCP3021
from adc_plot import plot_voltage_vs_time
from adc_plot import plot_sampling_period_hist
import time

def main():
    duration = 3

    voltage_values = []
    time_values = []

    adc = MCP3021(5.2)

    try:
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_voltage()

            time_values.append(time.time() - start_time)
            voltage_values.append(voltage)

        plot_voltage_vs_time(time_values, voltage_values, 5.2)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()

if __name__     == "__main__":
    main()