import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('daily_calories.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the table for daily calorie intake based on height and weight
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_calories (
        id INTEGER PRIMARY KEY,
        height REAL,
        weight REAL,
        daily_calorie INTEGER
    )
''')

# Example data
example_data = [
    (1, 140, 45),   # Height: 140 cm, Weight: 45 kg
    (2, 145, 50),   # Height: 145 cm, Weight: 50 kg
    (3, 147, 48),   # Height: 147 cm, Weight: 48 kg
    (4, 150, 50),   # Height: 150 cm, Weight: 50 kg
    (5, 154, 52),   # Height: 154 cm, Weight: 52 kg
    (6, 155, 55),   # Height: 155 cm, Weight: 55 kg
    (7, 156, 54),   # Height: 156 cm, Weight: 54 kg
    (8, 159, 56),   # Height: 159 cm, Weight: 56 kg
    (9, 160, 60),   # Height: 160 cm, Weight: 60 kg
    (10, 162, 58),  # Height: 162 cm, Weight: 58 kg
    (11, 163, 60),  # Height: 163 cm, Weight: 60 kg
    (12, 165, 64),  # Height: 165 cm, Weight: 64 kg
    (13, 165, 65),  # Height: 165 cm, Weight: 65 kg
    (14, 168, 62),  # Height: 168 cm, Weight: 62 kg
    (15, 170, 66),  # Height: 170 cm, Weight: 66 kg
    (16, 170, 70),  # Height: 170 cm, Weight: 70 kg
    (17, 172, 68),  # Height: 172 cm, Weight: 68 kg
    (18, 174, 70),  # Height: 174 cm, Weight: 70 kg
    (19, 175, 75),  # Height: 175 cm, Weight: 75 kg
    (20, 177, 74),  # Height: 177 cm, Weight: 74 kg
    (21, 178, 72),  # Height: 178 cm, Weight: 72 kg
    (22, 180, 78),  # Height: 180 cm, Weight: 78 kg
    (23, 180, 80),  # Height: 180 cm, Weight: 80 kg
    (24, 182, 76),  # Height: 182 cm, Weight: 76 kg
    (25, 184, 80),  # Height: 184 cm, Weight: 80 kg
    (26, 185, 85),  # Height: 185 cm, Weight: 85 kg
    (27, 187, 82),  # Height: 187 cm, Weight: 82 kg
    (28, 188, 86),  # Height: 188 cm, Weight: 86 kg
    (29, 190, 88),  # Height: 190 cm, Weight: 88 kg
    (30, 195, 90)   # Height: 195 cm, Weight: 90 kg
]

# Populate the daily_calories table with example data
for data in example_data:
    # Example formula for calculating daily calories (just for demonstration)
    height, weight = data[1], data[2]
    daily_calorie = int((10 * weight) + (6.25 * height) - (5 * 25) + 5)  # Example formula, you may adjust this
    cursor.execute('''
        INSERT INTO daily_calories (height, weight, daily_calorie) 
        VALUES (?, ?, ?)
    ''', (height, weight, daily_calorie))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
