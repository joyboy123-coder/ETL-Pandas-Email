# 📦 ETL + Pandas + Snowflake + Email Automation 🚀

Hey there! 👋  
This project is all about taking a messy CSV file with 50,000 rows 🐛, cleaning it up using **Pandas** 🧼, loading it into **Snowflake** ❄️, and then sending a fancy email report 📧 — all in one smooth flow!

---

## 🗃️ Data Folder

Inside the `data/` folder, you’ll find:

- **`raw_data/`** – holds the file `raw_data.csv` which has 50K messy rows. It’s the starting point for everything. 😬
- **`cleaned_data/`** – contains `cleaned_data.csv`, which starts out empty but gets filled with clean and shiny data after the ETL process. ✨✅

---

## 🛠️ ETL Magic in Action

In the `etl/` folder, we break down the ETL process:

- 🧲 **Extract** – pulls data from the raw CSV
- 🧽 **Transform** – cleans and processes the data using Pandas (say goodbye to dirty data!)
- 📤 **Load** – takes the cleaned data and pushes it into your Snowflake warehouse like a pro 💼

---

## ✉️ Email Time!

Once the data is cleaned and loaded, the project helps you send out an email report 📬  
You just pop in the receiver’s email address, and boom 💥 — they get the update in their inbox (or maybe the spam folder, lol 😅)

---

## 🖼️ Images Folder

The `images/` folder shows it all in action:

- Before & after cleaning the 50K rows 🧹
- Before & after loading into Snowflake ❄️📊
- A peek at how credentials are entered securely (don’t worry, yours won’t be exposed 👀)

---

## 🤖 What Happens Behind the Scenes

- You start the pipeline.
- It asks for your Snowflake credentials (see image examples, yours will be private 🔐)
- It extracts → transforms → loads the data into Snowflake 💪
- Then, you run the email script and enter the recipient's email 💌
- Within seconds, an email is sent 📫 (sometimes it plays hide-and-seek in the spam folder 👻)

---

## 💡 Why It’s Cool

- Cleans big messy data with ease 🛁
- Loads straight into a real data warehouse 🏢
- Sends reports automatically 💻➡️📧
- Easy to follow, super helpful for data engineering vibes 🔄

---

Built with ❤️ to make data cleaning, loading, and sharing a breeze!
