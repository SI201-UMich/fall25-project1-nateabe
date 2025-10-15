import csv

def read_csv_to_dict(filename):
    """Reads a CSV file and returns a list of dictionaries."""
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

data = read_csv_to_dict("crop_yield.csv")
print(len(data))  # Number of rows
print(data[0])    # First entry

def avg_rainfall_by_fertilizer(data):
    """Returns average rainfall for fertilizer used and not used."""
    total_with = 0
    count_with = 0
    total_without = 0
    count_without = 0

    for row in data:
        rainfall = float(row["Rainfall_mm"])
        used = row["Fertilizer_Used"].strip().lower()

        if used == "yes":
            total_with += rainfall
            count_with += 1
        else:
            total_without += rainfall
            count_without += 1

    avg_with = total_with / count_with if count_with else 0
    avg_without = total_without / count_without if count_without else 0

    return avg_with, avg_without

def avg_yield_by_fertilizer(data):
    """Returns average yield for fertilizer used and not used."""
    total_with = 0
    count_with = 0
    total_without = 0
    count_without = 0

    for row in data:
        yield_val = float(row["Yield_tons_per_h"])
        used = row["Fertilizer_Used"].strip().lower()

        if used == "yes":
            total_with += yield_val
            count_with += 1
        else:
            total_without += yield_val
            count_without += 1

    avg_with = total_with / count_with if count_with else 0
    avg_without = total_without / count_without if count_without else 0

    return avg_with, avg_without
def write_results_to_file(rainfall_result, yield_result, filename="results.txt"):
    """Writes the analysis results to a text file."""
    with open(filename, "w") as file:
        file.write("Crop Yield Data Analysis\n")
        file.write("=========================\n\n")
        file.write(f"Average Rainfall (Fertilizer Used): {rainfall_result[0]:.2f} mm\n")
        file.write(f"Average Rainfall (No Fertilizer): {rainfall_result[1]:.2f} mm\n\n")
        file.write(f"Average Yield (Fertilizer Used): {yield_result[0]:.2f} tons/ha\n")
        file.write(f"Average Yield (No Fertilizer): {yield_result[1]:.2f} tons/ha\n")
