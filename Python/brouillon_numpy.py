import numpy as np

egg_carton1 = np.array(
    [[0.89, 0.90, 0.83, 0.89, 0.97, 0.98], [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]]
)

egg_carton2 = np.array(
    [[0.89, 0.95, 0.84, 0.92, 0.94, 0.93], [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]]
)

egg_carton3 = np.array(
    [[0.83, 0.95, 0.89, 0.54, 0.37, 0.92], [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]]
)


print(np.average(egg_carton1))
print(np.average(egg_carton2))
print(np.average(egg_carton3))

stats = np.array([6, 5, 25, 10, 5])


steps = np.array([[50, 51, 54, 59, 59, 53, 54, 51], [45, 50, 38, 44, 40, 46, 43, 39]])

print(
    f"Max: {np.max(steps)}\nMin: {np.min(steps)}\nSum: {np.sum(steps)}\nAverage: {np.average(steps)}"
)


month_results = np.array(
    [
        56,
        100,
        33,
        0,
        45,
        45,
        46,
        34,
        89,
        180,
        60,
        45,
        45,
        44,
        46,
        45,
        0,
        0,
        15,
        90,
        301,
        197,
        20,
        60,
        45,
        45,
        42,
        45,
    ]
)
print(month_results.shape)
week_results = month_results.reshape(7, 4)
print(week_results)
# ==============================================================================
comet = np.arange(1986, 3000, 75)
# =========================================================# axis = 0: each column
# axis = 1: each row


passengers = np.array(
    [
        [1, 0, 3, 22],
        [2, 1, 1, 38],
        [3, 1, 3, 26],
        [4, 1, 1, 35],
        [5, 0, 3, 35],
        [6, 0, 3, 18],
        [7, 0, 1, 54],
        [8, 0, 3, 2],
        [9, 1, 3, 27],
        [10, 1, 2, 14],
        [11, 1, 3, 4],
        [12, 1, 1, 58],
        [13, 0, 3, 20],
        [14, 0, 3, 39],
        [15, 0, 3, 14],
        [16, 1, 2, 55],
        [17, 0, 3, 2],
        [18, 1, 2, 12],
        [19, 0, 3, 31],
        [20, 1, 3, 8],
        [21, 0, 2, 35],
        [22, 1, 2, 34],
        [23, 1, 3, 15],
        [24, 1, 1, 28],
        [25, 0, 3, 8],
        [26, 1, 3, 38],
        [27, 0, 3, 2],
        [28, 0, 1, 1],
        [29, 1, 3, 5],
        [30, 0, 3, 18],
        [31, 0, 1, 40],
        [32, 1, 1, 70],
        [33, 1, 3, 33],
        [34, 0, 2, 66],
        [35, 0, 1, 28],
        [36, 0, 1, 42],
        [37, 1, 3, 5],
        [38, 0, 3, 18],
        [39, 0, 3, 18],
        [40, 1, 3, 14],
        [41, 0, 3, 40],
        [42, 0, 2, 27],
        [43, 0, 3, 29],
        [44, 1, 2, 0],
        [45, 1, 3, 19],
        [46, 0, 3, 33],
        [47, 0, 3, 14],
        [48, 1, 3, 22],
        [49, 0, 3, 41],
        [50, 0, 3, 18],
    ]
)


print(
    f"Array shape: {passengers.shape}\nAverage age of the passengers: {np.average(passengers,axis = 0)[3]}\nOldest passenger: {np.max(passengers,axis = 0)[3]}\nYoungest passenger: {np.min(passengers,axis = 0)[3]}\nSurvival rate: {np.average(passengers,axis=0)[1]*100}\nSurvival rate based on passenger class:   "
)
