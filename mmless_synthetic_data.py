from faker import Faker
import pandas as pd

# Initialize Faker generator150712
fake = Faker()

# Generate synthetic data
for it in range(10):
    data = {
        'Employee ID': [fake.random_int(min=1000, max=9999) for _ in range(20000)],
        'Name': [fake.name() for _ in range(20000)],
        'Email': [fake.email() for _ in range(20000)],
        'Phone Number': [fake.phone_number() for _ in range(20000)],
        'Department': [fake.random_element(elements=('IT', 'HR', 'Finance', 'Marketing')) for _ in range(20000)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save data to CSV file
    df.to_csv("synthetic_employee_data{}.csv".format(it), index=False)
