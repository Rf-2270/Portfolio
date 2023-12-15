import sys

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        return

    cat_visits = 0
    other_cats = 0
    total_time_in_minutes = 0

    min_duration = float('inf')
    max_duration = float('-inf')

    for line in lines:
        if line.strip() == 'END':
            break

        cat_info, start_time, end_time = line.strip().split(',')


        if cat_info == 'OURS':
            start_time, end_time = int(start_time), int(end_time)

            visit_duration = end_time - start_time
            total_time_in_minutes += visit_duration
            cat_visits += 1
            min_duration = min(min_duration, visit_duration)
            max_duration = max(max_duration, visit_duration)
        elif cat_info == 'THEIRS':
            other_cats += 1

    if cat_visits == 0:
        average_duration = 0
    else:
        average_duration = total_time_in_minutes // cat_visits

    total_hours = total_time_in_minutes // 60
    total_minutes = total_time_in_minutes % 60

    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}\n")
    print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
    print(f"Average Visit Length: {average_duration} Minutes")
    print(f"Longest Visit:        {max_duration} Minutes")
    print(f"Shortest Visit:       {min_duration} Minutes\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        log_file_path = sys.argv[1]
        analyze_cat_shelter_log(log_file_path)
