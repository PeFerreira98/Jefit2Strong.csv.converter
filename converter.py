import csv
from datetime import datetime

def create_weight_exercise(date, exercise_name, weight, reps, set_order):
    return {
        'Date': date,
        'Workout Name': 'Jefit',
        'Exercise Name': exercise_name,
        'Set Order': set_order,
        'Weight': weight,
        'Weight Unit': 'kg',
        'Reps': reps,
        'RPE': '',
        'Distance': '',
        'Distance Unit': '',
        'Seconds': '0',
        'Notes': '',
        'Workout Notes': '',
        'Workout Duration': '50m'
    }

def create_cardio_exercise(date, exercise_name, distance, seconds, set_order):
    return {
        'Date': date,
        'Workout Name': 'Jefit',
        'Exercise Name': exercise_name,
        'Set Order': set_order,
        'Weight': '',
        'Weight Unit': '',
        'Reps': '',
        'RPE': '',
        'Distance': distance,
        'Distance Unit': 'km',
        'Seconds': seconds,
        'Notes': '',
        'Workout Notes': '',
        'Workout Duration': '50m'
    }

def create_bweight_exercise(date, exercise_name, reps, set_order):
    return {
        'Date': date,
        'Workout Name': 'Jefit',
        'Exercise Name': exercise_name,
        'Set Order': set_order,
        'Weight': '',
        'Weight Unit': '',
        'Reps': reps,
        'RPE': '',
        'Distance': '',
        'Distance Unit': '',
        'Seconds': '0',
        'Notes': '',
        'Workout Notes': '',
        'Workout Duration': '50m'
    }

def build_weight_exercise(date, exercise_name, set_components, set_order):
    comp0 = set_components[0]
    comp1 = set_components[1] if len(set_components) > 1 else '1'
    return create_weight_exercise(date, exercise_name, comp0, comp1, set_order)

def build_cardio_exercise(date, exercise_name, set_components, set_order):
    comp0 = set_components[0] if int(set_components[0]) > 0 else ''
    comp1 = set_components[1] if len(set_components) > 1 else '1'
    return create_cardio_exercise(date, exercise_name, comp0, comp1, set_order)

def build_bweight_exercise(date, exercise_name, set_components, set_order):
    comp0 = set_components[0] 
    comp1 = set_components[1] if len(set_components) > 1 else '1'
    return create_bweight_exercise(date, exercise_name, comp1, set_order)

def convert_date(date):
    #datetime_object = datetime.strptime(date, '%d/%m/%Y %H:%M')
    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    return datetime_object.strftime('%Y-%m-%d %H:%M:%S')

def convert_exercise_name(exercise_name):
    alternative_exercisename_list = {'Ab Crunch Machine':'Crunch (Machine)', 'Abdominal Pendulum':'Crunch', 'Alternate Heel Touchers':'Crunch', 'Alternate Heel Touches':'Crunch', 'Barbell Bench Press':'Bench Press (Barbell)', 'Barbell Bent Over Row':'Bent Over Row (Barbell)', 'Barbell Bent-Over Row':'Bent Over Row (Barbell)', 'Barbell Close Grip Preacher Curl':'Preacher Curl (Barbell)', 'Barbell Curl':'Bicep Curl (Barbell)', 'Barbell Deadlift':'Deadlift (Barbell)', 'Barbell Decline Bench Press':'Decline Bench Press (Barbell)', 'Barbell EZ Bar Reverse Grip Curl':'Bicep Curl (Barbell)', 'Barbell Glute Bridge':'Hip Thrust (Barbell)', 'Barbell Hip Thrust':'Hip Thrust (Barbell)', 'Barbell Incline Bench Press':'Incline Bench Press (Barbell)', 'Barbell Incline Bench Row':'Incline Row (Barbell)', 'Barbell Lying Triceps Extension':'Triceps Extension (Barbell)', 'Barbell One Leg Squat':'Squat (Barbell)', 'Barbell Preacher Curl':'Preacher Curl (Barbell)', 'Barbell Reverse Curl':'Reverse Curl (Barbell)', 'Barbell Reverse Preacher Curls':'Preacher Curl (Barbell)', 'Barbell Seated Palms Up Wrist Curl':'Bicep Curl (Barbell)', 'Barbell Shoulder Press':'Shoulder Press (Barbell)', 'Barbell Shrug':'Shrug (Barbell)', 'Barbell Squat':'Squat (Barbell)', 'Barbell Standing Calf Raise':'Standing Calf Raise (Barbell)', 'Barbell Standing Wide Grip Biceps Curl':'Bicep Curl (Barbell)', 'Barbell Step Ups':'Step-up', 'Barbell Sumo Deadlift':'Sumo Deadlift (Barbell)', 'Barbell Triceps Extension':'Triceps Extension (Barbell)', 'Bench Dip':'Bench Dip', 'Bench Press Machine':'Bench Press (Smith Machine)', 'Bodyweight Standing Calf Raise':'Standing Calf Raise (Bodyweight)', 'Bridge':'Single Leg Bridge', 'Cable Close Grip Curl':'Bicep Curl (Cable)', 'Cable Cross Over':'Cable Crossover', 'Cable Elevated Rows':'Seated Row (Cable)', 'Cable Front Raise':'Front Raise (Cable)', 'Cable Inner Chest Crossover ':'Cable Crossover', 'Cable Inner Chest Press':'Bench Press (Cable)', 'Cable Lower Chest Raise':'Chest Raise (Cable)', 'Cable Mid Chest Crossovers':'Cable Crossover', 'Cable One Arm Lat Pulldown':'Lat Pulldown (Single Arm)', 'Cable Reverse Grip Triceps Pushdown':'Triceps Pushdown (Cable - Straight Bar)', 'Cable Rope Face Pull':'Face Pull (Cable)', 'Cable Rope Hammer Curls':'Hammer Curl (Cable)', 'Cable Rope Lat Pull Down':'Lat Pulldown (Cable)', 'Cable Rope Overhead Triceps Extension':'Triceps Extension (Cable)', 'Cable Rope Triceps Pushdown':'Triceps Pushdown (Cable - Straight Bar)', 'Cable Seated Row':'Seated Row (Cable)', 'Cable Standing Deltoid Raise':'Lateral Raise (Cable)', 'Cable Straight Arm Push Down':'Triceps Pushdown (Cable - Straight Bar)', 'Cable Triceps Pushdown':'Triceps Pushdown (Cable - Straight Bar)', 'Chin Up':'Chin Up', 'Close Grip Front Lat Pulldown':'Lat Pulldown (Machine)', 'Close Hand Pushup':'Push Up', 'Crunches':'Crunch', 'Crunches with Legs on an Exercise Ball':'Crunch', 'Dip':'Bench Dip', 'Dumbbell Alternate Bicep Curl':'Bicep Curl (Dumbbell)', 'Dumbbell Alternate Hammer Curl':'Hammer Curl (Dumbbell)', 'Dumbbell Alternate Incline Curl':'Incline Curl (Dumbbell)', 'Dumbbell Alternate Seated Curl':'Bicep Curl (Dumbbell)', 'Dumbbell Bench Press':'Bench Press (Dumbbell)', 'Dumbbell Bent Arm Pullover':'Pullover (Dumbbell)', 'Dumbbell Bent Over Reverse Fly':'Reverse Fly (Dumbbell)', 'Dumbbell Concentration Curls':'Concentration Curl (Dumbbell)', 'Dumbbell Deadlift':'Deadlift (Dumbbell)', 'Dumbbell Decline Bench Press':'Decline Bench Press (Dumbbell)', 'Dumbbell Fly':'Chest Fly (Dumbbell)', 'Dumbbell Front Raise':'Front Raise (Dumbbell)', 'Dumbbell Hammer Curl':'Hammer Curl (Dumbbell)', 'Dumbbell Hammer Curls':'Hammer Curl (Dumbbell)', 'Dumbbell Hamstring Curl':'Hammer Curl (Dumbbell)', 'Dumbbell Incline Bench Press':'Incline Bench Press (Dumbbell)', 'Dumbbell Incline Curl':'Incline Curl (Dumbbell)', 'Dumbbell Incline Fly':'Incline Chest Fly (Dumbbell)', 'Dumbbell Lateral Raise':'Lateral Raise (Dumbbell)', 'Dumbbell Lying Supine Two Arm Triceps Extension':'Triceps Extension (Dumbbell)', 'Dumbbell One Arm Preacher Curl':'Preacher Curl (Dumbbell)', 'Dumbbell One Arm Row':'Bent Over One Arm Row (Dumbbell)', 'Dumbbell One-Arm Row':'Bent Over One Arm Row (Dumbbell)', 'Dumbbell Palms Down Wrist Curl':'Seated Palms Up Wrist Curl (Dumbbell)', 'Dumbbell Palms In Bench Press':'Bench Press (Dumbbell)', 'Dumbbell Palms Up Wrist Curl':'Seated Palms Up Wrist Curl (Dumbbell)', 'Dumbbell Reverse Preacher Curl':'Reverse Curl (Dumbbell)', 'Dumbbell Seated Triceps Press':'Triceps Extension (Dumbbell)', 'Dumbbell Shoulder Press':'Arnold Press (Dumbbell)', 'Dumbbell Side Bend':'Side Bend (Dumbbell)', 'Dumbbell Standing Press':'Arnold Press (Dumbbell)', 'Dumbbell Standing Triceps Extension':'Triceps Extension (Dumbbell)', 'Dumbbell Straight Arm Pullover':'Pullover (Dumbbell)', 'Dumbbell Tricep Kickback':'Triceps Extension (Dumbbell)', 'Dumbell thruster':'Thruster (Kettlebell)', 'Dynamic plank':'Plank', 'EZ Bar Close Grip Curl':'Bicep Curl (Barbell)', 'EZ Bar Curl':'Bicep Curl (Barbell)', 'EZ Bar Tricep Extension':'Triceps Extension (Barbell)', 'EZ Bar Triceps Extension':'Triceps Extension (Barbell)', 'Glute Kickback':'Glute Kickback (Machine)', 'Glute Kickback ':'Glute Kickback (Machine)', 'Hack Squat':'Squat (Bodyweight)', 'Hanging Knee Raise':'Hanging Knee Raise', 'Hanging Leg Raise':'Hanging Leg Raise', 'Hollow Position':'V Up', 'Hyperextensions - Back Extensions':'Back Extension', 'Indoor Cycling':'Cycling (Indoor)', 'Inverted Row':'Inverted Row (Bodyweight)', 'Jackknife Sit up':'Jackknife Sit Up', 'Jackknife Sit-Up':'Jackknife Sit Up', 'Knee Hip Raise On Parallel Bars':'Hanging Knee Raise', 'Kneeling Squat':'Squat (Bodyweight)', 'Leg Extension':'Leg Extension (Machine)', 'Leg Extensions':'Leg Extension (Machine)', 'Leg Press':'Leg Press', 'Leg Raise':'Flat Leg Raise', 'Lying Leg Curls':'Lying Leg Curl (Machine)', 'Machine Ab Crunch':'Crunch (Machine)', 'Machine Back Extension':'Back Extension (Machine)', 'Machine Fly':'Chest Fly', 'Machine Inner Chest Press':'Chest Press (Machine)', 'Machine Shoulder Press':'Shoulder Press (Machine)', 'Mountain Climbers':'Mountain Climber', 'Plank':'Plank', 'Prisoner Squat':'Squat (Bodyweight)', 'Prone Leg Curls':'Lying Leg Curl (Machine)', 'Push Up':'Push Up', 'Reverse Crunch':'Reverse Crunch', 'Seated Calf Raise':'Seated Calf Raise (Machine)', 'Seated Leg Curl':'Seated Leg Curl (Machine)', 'Seated Machine Row':'Seated Row (Machine)', 'Side Bridge':'Single Leg Bridge', 'Side Jackknife':'Jackknife Sit Up', 'Single Bench Dip':'Bench Dip', 'Sit Up':'Sit Up', 'Smith Machine Leg Press':'Leg Press', 'Smith Machine Lunge':'Lunge (Barbell)', 'Smith Machine Overhead Shoulder Press':'Overhead Press (Smith Machine)', 'Smith Machine Reverse Calf Raises':'Standing Calf Raise (Smith Machine)', 'Smith Machine Shrug':'Shrug (Smith Machine)', 'Smith Machine Squat':'Squat (Smith Machine)', 'Smith Machine Upright Row':'Upright Row (Barbell)', 'Stationary Bike':'Cycling (Indoor)', 'Superman':'Superman', 'T Bar Row':'T Bar Row', 'Treadmill Running':'Running (Treadmill)', 'Weight Plate Front Raise':'Front Raise (Plate)', 'Weight Plate High Front Raise':'Front Raise (Plate)', 'Weight Plate Rotation':'Weighted Russian Twist', 'Weight Plate Russian Twist':'Weighted Russian Twist', 'Weight Plate Twist':'Weighted Russian Twist', 'Weighted Glute Kickback':'Glute Kickback (Machine)', 'Wide Grip Lat Pulldown':'Lat Pulldown (Machine)', 'Wide Grip Pulldown Behind The Neck':'Lat Pulldown (Machine)', 'Wide Grip Pulldown Behind the Neck':'Lat Pulldown (Machine)', 'Wide Hand Pushup':'Push Up'}
    try:
        return alternative_exercisename_list.get(exercise_name)
    except ValueError:
        print('FATAL ERROR! -> ValueError: ' + exercise_name)
        return exercise_name

def build_exercise(row, reader_headers, set_order, set_data):
    date = convert_date(row[reader_headers[7]])
    exercise_name = convert_exercise_name(row[reader_headers[9]])
    set_components = set_data.split('x')

    if exercise_name in ('Flat Leg Raise', 'Hip Thrust (Bodyweight)'):
        return build_bweight_exercise(date, exercise_name, set_components, set_order)

    if exercise_name in ('Cycling (Indoor)', 'Plank', 'Running (Treadmill)'):
        return build_cardio_exercise(date, exercise_name, set_components, set_order)

    if len(set_components) > 1 and set_components[0] != '0':
        return build_weight_exercise(date, exercise_name, set_components, set_order)
    
    if len(set_components) > 1:
        return build_bweight_exercise(date, exercise_name, set_components, set_order)
    
    return build_cardio_exercise(date, exercise_name, set_components, set_order)
    
def iterate_jefit_csv(reader, reader_headers):
    for row in reader:
        sets = row[reader_headers[4]].split(',')
        set_order = 0
        for i, set_data in enumerate(sets):
            if set_data != '0x0':
                set_order += 1
                yield build_exercise(row, reader_headers, set_order, set_data)

def process_jefit_unfiltered_file(jefit_filename, output_header, output_filename):
    with open(jefit_filename, mode='r') as jefit_csv, open(output_filename, mode='w', newline='') as output_csv:
        jefit_reader = csv.DictReader(jefit_csv, delimiter=',')
        jefit_reader_headers = jefit_reader.fieldnames
        writer = csv.DictWriter(output_csv, fieldnames=output_header, delimiter=';')
        writer.writeheader()
        for line in iterate_jefit_csv(jefit_reader, jefit_reader_headers):
            writer.writerow(line)

def append_to_file(strong_filename, output_header, output_filename):
    with open(strong_filename, mode='r') as input_csv:
        with open(output_filename, mode='a', newline='') as output_csv:
            reader = csv.DictReader(input_csv, delimiter=';')
            writer = csv.DictWriter(output_csv, fieldnames=output_header, delimiter=';')
            for line in reader:
                writer.writerow(line)

jefit_filename = 'jefitInput.csv'
strong_filename = 'strongInput.csv'
output_filename = 'output.csv'

output_header = ['Date', 'Workout Name', 'Exercise Name', 'Set Order', 'Weight', 'Weight Unit', 'Reps', 'RPE', 'Distance', 'Distance Unit', 'Seconds', 'Notes', 'Workout Notes', 'Workout Duration']

process_jefit_unfiltered_file(jefit_filename, output_header, output_filename)

append_to_file(strong_filename, output_header, output_filename)