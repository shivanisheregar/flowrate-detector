def calculate_flow_rate(volume_ml, time_sec):

    if time_sec == 0:
        return 0

    return volume_ml / time_sec
