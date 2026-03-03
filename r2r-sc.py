from adc_plot import plot_voltage_vs_time
from adc_plot import plot_sampling_period_hist
import time
from r2r_adc import R2R_ADC

def main():
    dac_range = 3.30
    compare_time = 0.0001

    voltage_values = []
    time_values = []
    duration = 3.0

    adc = R2R_ADC(dac_range, compare_time)

    try:
        start_time = time.time()

        while time.time() - start_time < duration:
            voltage = adc.get_sc_voltage()

            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)

            time.sleep(0.05)

        plot_voltage_vs_time(time_values, voltage_values, dac_range)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()

if __name__ == "__main__":
    main()