# 💳 Credit Score Risk Classifier

A lightweight machine learning pipeline that classifies customers into credit risk categories — Low, Medium, and High — based on synthetic financial data. It also demonstrates AWS S3 integration by uploading input and output files to a cloud bucket.

---

## 🚀 Features

- Simulates customer credit-related financial data
- Classifies risk using credit score thresholds
- Trains a Random Forest classifier on features
- Generates a classification report on predictions
- Uploads input and output files to AWS S3 bucket

---

## 🧰 Technologies Used

- Python 3.x
- pandas
- numpy
- scikit-learn
- boto3
- Jupyter Notebook

---

## 🛠️ How to Run

1. Clone this repo:
```bash
git clone https://github.com/YourUsername/credit-score-classifier.git
cd credit-score-classifier
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up AWS CLI (if not done yet):
```bash
aws configure
```

4. Open and run the notebook:
```bash
cd notebook
jupyter notebook credit_score_classifier.ipynb
```

⚠️ Don't forget to set your `bucket_name` in the notebook:
```python
bucket_name = 'shrushti-credit-bucket'
```

---

## 📂 Folder Structure

```
credit-score-classifier/
├── data/
│   └── credit_data.csv
├── output/
│   └── risk_predictions.csv
├── notebook/
│   └── credit_score_classifier.ipynb
├── Credit_Score_Classifier_Final_Report.docx
├── README.md
└── requirements.txt
```

---

## 👩‍💻 Author

**Shrushti Wable**  
[GitHub](https://github.com/ShrushtiCodes)