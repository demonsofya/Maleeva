import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time
from adc_plot import plot_sampling_period_hist

if __name__ == "__main__":
    dac_range = 3.30
    compare_time = 0.01
    duration = 8

    adc = R2R_ADC(dac_range, compare_time)
    
    voltage_values = []
    time_values = []

    try:
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_sar_voltage()

            time_values.append(time.time() - start_time)
            voltage_values.append(voltage)

        plot_voltage_vs_time(time_values, voltage_values, dac_range)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()