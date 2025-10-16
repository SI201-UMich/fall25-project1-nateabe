#Nate Abraham
#1879 4472
#nateabra@umich.edu
#I worked alone
#I used GenAi to help me write my functions and fix errors when I was stuck


import csv

def read_csv_to_dict(filename):
  
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

data = read_csv_to_dict("crop_yield.csv")
print(data[0])    
print(len(data))  

def avg_rainfall_by_fertilizer(data):

    total_with = 0
    count_with = 0
    total_without = 0
    count_without = 0

    for row in data:
        rainfall = float(row["Rainfall_mm"])
        used = row["Fertilizer_Used"].strip().lower()

        if used == "true":
            total_with += rainfall
            count_with += 1
        else:
            total_without += rainfall
            count_without += 1

    avg_with = total_with / count_with
    avg_without = total_without / count_without 

    return {"true": avg_with, "false": avg_without}




def avg_yield_by_fertilizer(data):

    total_with = 0
    count_with = 0
    total_without = 0
    count_without = 0

    for row in data:
        yield_val = float(row["Yield_tons_per_hectare"])
        used = row["Fertilizer_Used"].strip().lower()

        if used == "true":
            total_with += yield_val
            count_with += 1
        else:
            total_without += yield_val
            count_without += 1

    avg_with = total_with / count_with
    avg_without = total_without / count_without

    return {"true": avg_with, "false": avg_without}

def write_results_to_file(rainfall_result, yield_result, filename="results.txt"):

    with open(filename, "w") as file:
        
        file.write("Agriculture Crop Yield Analysis Results\n")
        file.write("--------------------------------------\n")
        file.write(f"Average Rainfall (Fertilizer Used=True): {rainfall_result['true']:.2f} mm\n")
        file.write(f"Average Rainfall (Fertilizer Used=False): {rainfall_result['false']:.2f} mm\n\n")
        file.write(f"Average Yield (Fertilizer Used=True): {yield_result['true']:.2f} tons per hectare\n")
        file.write(f"Average Yield (Fertilizer Used=False): {yield_result['false']:.2f} tons per hectare\n")

def main():
    data = read_csv_to_dict("crop_yield.csv")

    rainfall_result = avg_rainfall_by_fertilizer(data)
    yield_result = avg_yield_by_fertilizer(data)

    write_results_to_file(rainfall_result, yield_result)

    print("Results written to results.txt")


def test_avg_yield_by_fertilizer():
    

    data1 = [
        {"Fertilizer_Used": "True", "Yield_tons_per_hectare": 4.0},
        {"Fertilizer_Used": "True", "Yield_tons_per_hectare": 6.0},
        {"Fertilizer_Used": "False", "Yield_tons_per_hectare": 2.0},
        {"Fertilizer_Used": "False", "Yield_tons_per_hectare": 4.0},
    ]
    result1 = avg_yield_by_fertilizer(data1)
    assert abs(result1["true"] - 5.0) < 1e-6
    assert abs(result1["false"] - 3.0) < 1e-6
    print("General Case 1 passed.")

    data2 = [
        {"Fertilizer_Used": "True", "Yield_tons_per_hectare": 8.0},
        {"Fertilizer_Used": "True", "Yield_tons_per_hectare": 12.0},
    ]
    result2 = avg_yield_by_fertilizer(data2)
    assert abs(result2["true"] - 10.0) < 1e-6
    assert result2["false"] == 0  
    print("General Case 2 passed.")

    data3 = []
    result3 = avg_yield_by_fertilizer(data3)
    assert result3 == {"true": 0, "false": 0}
    print("Edge Case 1 passed.")


    data4 = [
        {"Fertilizer_Used": "True", "Yield_tons_per_hectare": ""},
        {"Fertilizer_Used": "False", "Yield_tons_per_hectare": None},
    ]
    result4 = avg_yield_by_fertilizer(data4)
    assert result4 == {"true": 0, "false": 0}
    print("Edge Case 2 passed.")



def test_avg_rainfall_by_fertilizer():
    """Test avg_rainfall_by_fertilizer() with 4 cases: 2 general, 2 edge"""

    data1 = [
        {"Fertilizer_Used": "True", "Rainfall_mm": 100},
        {"Fertilizer_Used": "True", "Rainfall_mm": 120},
        {"Fertilizer_Used": "False", "Rainfall_mm": 80},
        {"Fertilizer_Used": "False", "Rainfall_mm": 60},
    ]
    result1 = avg_rainfall_by_fertilizer(data1)
    assert abs(result1["true"] - 110) < 1e-6
    assert abs(result1["false"] - 70) < 1e-6
    print("General Case 1 passed.")


    data2 = [
        {"Fertilizer_Used": "True", "Rainfall_mm": 200},
        {"Fertilizer_Used": "False", "Rainfall_mm": 100},
    ]
    result2 = avg_rainfall_by_fertilizer(data2)
    assert abs(result2["true"] - 200) < 1e-6
    assert abs(result2["false"] - 100) < 1e-6
    print("General Case 2 passed.")

    data3 = []
    result3 = avg_rainfall_by_fertilizer(data3)
    assert result3 == {"true": 0, "false": 0}
    print("Edge Case 1 passed.")

    data4 = [
        {"Fertilizer_Used": "True", "Rainfall_mm": ""},
        {"Fertilizer_Used": "False", "Rainfall_mm": None},
    ]
    result4 = avg_rainfall_by_fertilizer(data4)
    assert result4 == {"true": 0, "false": 0}
    print("Edge Case 2 passed.")



if __name__ == "__main__":
    main()
