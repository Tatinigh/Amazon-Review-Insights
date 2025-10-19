# 📊 Amazon Review Insights

An interactive dashboard for visualizing and analyzing customer sentiment from Amazon reviews.

---

## ✨ Features

This dashboard provides a comprehensive Exploratory Data Analysis (EDA) of customer feedback:

* **📈 Key Metrics (KPIs):** At-a-glance view of:
    * Total Reviews
    * Positive Sentiment (%)
    * Negative Sentiment (%)
    * Neutral Sentiment (%)
* **Sentiment Distribution:** A donut chart showing the overall sentiment breakdown.
* **Rating Distribution:** A bar chart visualizing the count for each star rating (1 to 5).
* **☁️ Word Cloud:** A visual representation of the most frequently used words in the reviews.

---

## 🚀 How to Run

1.  **Clone the repository (or download the files).**
2.  **Open your terminal** and navigate to the project directory:
    ```bash
    cd path/to/amazon-reviews
    ```
3.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas plotly wordcloud matplotlib
    ```
4.  **Run the Streamlit app:**
    * (If `streamlit` command is in your path)
        ```bash
        streamlit run "dashboard.py"
        ```
    * (If not, run as a Python module - recommended)
        ```bash
        python -m streamlit run "dashboard.py"
        ```
5.  The app will automatically open in your web browser!

---

## 🛠️ Technologies Used

* **Streamlit:** For creating and serving the web app.
* **Pandas:** For data manipulation and analysis.
* **Plotly Express:** For creating interactive charts (pie & bar).
* **WordCloud:** For generating the word cloud.
* **Matplotlib:** For displaying the word cloud plot.