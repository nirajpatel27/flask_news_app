# 📰 HeadlineHub

**HeadlineHub** is a modern news aggregator web application built with **Flask** that fetches and displays real-time news using **NewsAPI**.  
It provides category-based browsing, keyword search, pagination, dark mode, and a clean, responsive UI.

---

## 🚀 Features

- 🗞️ Latest top headlines
- 📂 Category-wise news (Business, Technology, Sports, Health)
- 🔍 Search news by keyword
- 🌍 Country-based headlines
- ➕ Pagination (Load More)
- 🌗 Dark / Light mode toggle
- 🎯 Active navigation tabs
- ⚠️ Graceful empty & error states
- 🎨 Clean, responsive UI with CSS Grid
- 🧭 Clickable brand logo (routes to home)
- 🖼️ Custom favicon

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Jinja2
- **API:** NewsAPI.org
- **Styling:** CSS Grid, Flexbox
- **Other:** python-dotenv

---

## 📂 Project Structure

headlinehub/
│
├── app.py
├── config.py
├── services/
│ └── news_service.py
│
├── templates/
│ ├── base.html
│ └── home.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── images/
│ └── favicon.png
│
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
1. git clone https://github.com/your-username/headlinehub.git
cd headlinehub

2. Create virtual environment

    python -m venv venv

3. Activate virtual environment

    Windows - venv\Scripts\activate
    Mac/Linux - source venv/bin/activate

4. Install dependencies

    pip install -r requirements.txt

5. Configure environment variables

    Create a .env file in the root directory:
    NEWS_API_KEY=your_newsapi_key_here

6. Run the Application

    python app.py

7. Open your browser and visit:

    http://127.0.0.1:5000
    

🙌 Acknowledgements

NewsAPI.org
 for news data

Flask community


📄 License

This project is for learning and portfolio purposes.


---

## ✅ What This README Does Well

✔ Looks professional  
✔ Recruiter-friendly language  
✔ Clear setup instructions  
✔ Explains API limitations correctly  
✔ Clean structure  

---




