import xlsxwriter
import pandas as pd
import math
import numpy as np

# Read xlsx file into data frame that Python can recognize.
data_file = pd.read_excel('finals.xlsx')
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet1 = workbook.add_worksheet()


def calculate_weighted_value(subject_option):
    # Process columns one by one and find the max value considering NaN as possible elements.
    options = ['Chinese_rank', 'Math_rank', 'Physics_rank', 'Chemistry_rank',
               'Biology_rank', 'English_rank', 'Geology_rank', 'Politics_rank', 'History_rank']
    subject = data_file[options[subject_option]].tolist()
    m = np.nanmax(subject)

    # Assign weighted value of a specific subject to each student according to their percentile rank.
    weighted_value = []
    for i in subject:
        if math.isnan(i):
            weighted_value.append(0)
        elif i / m <= 0.06:
            weighted_value.append(0.95)
        else:
            n = (i / m) - 0.06
            rank = (n - n % 0.047) / 0.047
            if rank < 18:
                value = round(0.9 - rank * 0.05, 2)
            elif rank == 18:
                value = 0.03
            elif rank == 19:
                value = 0.02
            else:
                value = 0
            weighted_value.append(value)
    return weighted_value


# Write weighted values into another workbook.
col = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', ]
for k in range(9):
    lines_k = calculate_weighted_value(k)
    worksheet1.write_column(col[k], lines_k)
workbook.close()
