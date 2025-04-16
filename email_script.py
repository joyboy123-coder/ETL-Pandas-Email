import smtplib
from email.message import EmailMessage

# 1. Setup email details
sender = 'vamsikandregula537@gmail.com'  # Replace with your email
receiver = input('Enter Reciever email : ')     # Replace with recipient email
subject = '✅ ETL Report: Cleaned ETL Data load to snowflake'

body = """
Hey Mate,

ETL pipeline completed successfully.

Summary of the cleaned file:
- Total Rows after cleaning: 47835
- Columns: ['First_Name', 'Last_Name', 'Age', 'Email', 'Salary', 'Region', 'City']

- Null values after cleaning:
    First_Name     0
    Last_Name      0
    Age            0
    Email          0
    Salary         0
    Region         0
    City           0

Cleaning done:
- Removed 100 duplicate rows
- Filled missing values in 'Region' column
- Converted 'Age' to int data type and 'Salary' to Float data type and rounded to two decimals
- Ensured no nulls present After Cleaning

Cleaned file attached ➕📎

Regards,
Vamsi
"""

# 2. Create the email message
msg = EmailMessage()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.set_content(body)

# 3. Attach the cleaned CSV file
with open('data/cleaned_data/cleaned_data.csv', 'rb') as file:
    msg.add_attachment(
        file.read(),
        maintype='application',
        subtype='octet-stream',
        filename='cleaned_data.csv'
    )

# 4. Send the email using Gmail SMTP with SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, 'vgncqbakmfslnsem')  # Replace with your Gmail app password
    smtp.send_message(msg)

print("✅ Email sent successfully!")
