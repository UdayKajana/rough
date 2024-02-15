from faker import Faker
import pandas as pd
fake = Faker()
for it in range(1,50,1):
    data = {
        'Employee ID': [fake.random_int(min=1000, max=9999) for _ in range(80000)],
        'Name': [fake.name() for _ in range(80000)],
        'Email': [fake.email() for _ in range(80000)],
        'Phone Number': [fake.phone_number() for _ in range(80000)],
        'Department': [fake.random_element(elements=('IT', 'HR', 'Finance', 'Marketing')) for _ in range(80000)],
        'Age': [fake.random_int(min=20, max=60) for _ in range(80000)],
        'Gender': [fake.random_element(elements=('Male', 'Female')) for _ in range(80000)],
        'Salary': [fake.random_int(min=30000, max=180000) for _ in range(80000)],
        'Location': [fake.city() for _ in range(80000)]
    }
    df = pd.DataFrame(data)
    df.to_csv("synthetic_data1/syn_emp_data{}.csv".format(it), index=False)
