def step_function(a):
    if(a >= 1):
        return 1
    
    return 0


def calculate_accuracy(result, expected):
    if len(expected) > len(result):
        return -1
    
    response = []
    for i in range(len(result)):
        res = expected[i] - result[i]
        response.append(res)

    return response


def update_weight(weigth, learn_rate, input_data, err):
    return weigth + (learn_rate * input_data * err)


def process(input_data):
    result = []

    for i in input_data:
        res = (i["x1"] * i["weight1"]) + (i["x2"] * i["weight2"])
        result.append(step_function(res))

    return result


input_data = [
    {
        "x1": 0, "weight1": 0,
        "x2": 0, "weight2": 0,
    },
    {
        "x1": 0, "weight1": 0,
        "x2": 1, "weight2": 0,
    },
    {
        "x1": 1, "weight1": 0,
        "x2": 0, "weight2": 0,
    },
    {
        "x1": 1, "weight1": 0,
        "x2": 1, "weight2": 0,
    },
]

expected = [0, 0, 0, 1]

result_1 = process(input_data)
print("Result => ", result_1)
print("Expected => ", expected)
print(calculate_accuracy(result_1, expected))
print("Accuracy =>", calculate_accuracy(result_1, expected))
print(update_weight(0, 0.1, 1, 25))
print()

print("After update weight")
input_data = [
    {
        "x1": 0, "weight1": 0.5,
        "x2": 0, "weight2": 0.5,
    },
    {
        "x1": 0, "weight1": 0.5,
        "x2": 1, "weight2": 0.5,
    },
    {
        "x1": 1, "weight1": 0.5,
        "x2": 0, "weight2": 0.5,
    },
    {
        "x1": 1, "weight1": 0.5,
        "x2": 1, "weight2": 0.5,
    },
]
result_1 = process(input_data)
print("Result => ", result_1)
print("Expected => ", expected)
print("Accuracy =>", calculate_accuracy(result_1, expected))
