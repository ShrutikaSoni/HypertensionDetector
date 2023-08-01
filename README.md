# Hypertension Detector

## Project Description

High blood pressure, also known as hypertension, usually develops over time and can be caused by unhealthy lifestyle choices, such as lack of regular physical activity. Certain health conditions like diabetes and obesity can also increase the risk of developing high blood pressure. The "Hypertension Detector" project aims to control hypertension and prevent cardiovascular diseases by predicting hypertension risks and reducing mortality.

## Objective

The primary objective of the "Hypertension Detector" is to empower individuals and healthcare professionals to take proactive measures against hypertension. By utilizing the power of machine learning, specifically the widely used Random Forest algorithm, we aim to achieve accurate predictions and early detection of hypertension risks.

## Algorithm: Random Forest

Random Forest is a popular supervised machine learning algorithm that combines the outputs of multiple decision trees to reach a single result. Its ease of use and flexibility make it suitable for both classification and regression problems, and it has been widely adopted in various fields.

## Performance Analysis

We conducted performance analysis by testing five ML algorithms with different balancing techniques. Additionally, we compared the performance of the medical protocol currently used in screening programs. The results revealed that Random Forest exhibited interesting performances (0.818 sensitivity - 0.629 specificity) compared to medical protocols (0.906 sensitivity - 0.230 specificity).

## Conclusion

The ML models in the "Hypertension Detector" project demonstrated excellent performance in predicting hypertension and its associated factors. By implementing the models on an open-source platform, we can scale the application to reach millions of people, enabling early self-screening for hypertension. Addressing hypertension is crucial, especially for the elderly population, as it is associated with a higher risk of cardiovascular morbidity and mortality. Reducing blood pressure values through early detection can lead to improved health outcomes and decreased risks of related health issues.

## Technologies Used

- GUI Framework: Django, Bootstrap
- Languages: Python, HTML/CSS, JavaScript
- Implemented Libraries: Pandas, Sklearn

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/ShrutikaSoni/HypertensionDetector.git
```

2. Change into the project directory:

```bash
cd HypertensionDetector
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Access the web-app locally:

Open your web browser and go to `http://localhost:8000/`
