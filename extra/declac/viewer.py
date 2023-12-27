import dcalc

def create_list(*args, **kwargs):
    angle_list = []

    for i, value in enumerate(args):
        name = f"Point_{i + 1}"
        answer = dcalc.deg_to_gms(value)
        angle_str = f"{name}: {answer}"
        angle_list.append(angle_str)

    for name, value in kwargs.items():
        answer = dcalc.deg_to_gms(value)
        angle_str = f"{name}: {answer}"
        angle_list.append(angle_str)
    
    return angle_list


angles_result = create_list(30.5, 45.75, Point_3=60.0)

print(angles_result)
