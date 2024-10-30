# Poverty Analysis Web Application

## 📊 Overview
### Predicting Future Poverty Gaps and International Poverty Line Shortfall

Poverty is a persistent challenge affecting many countries globally. Understanding and forecasting poverty dynamics is critical for policymakers and development organizations to allocate resources effectively and design targeted interventions. This project focuses on predicting two key poverty metrics: the future **poverty gap** and the **international poverty line shortfall** for individual countries.

- **Poverty Gap**: Measures the average shortfall of the population from the poverty line, reflecting the depth of poverty.
- **International Poverty Line Shortfall**: Represents the total resources required to lift all individuals below the international poverty line (set at $2.15 per day in 2017 PPP) up to that line.

#### Why This Matters
Accurate predictions of these metrics are essential for:
- Anticipating resources needed to address poverty.
- Targeting interventions for the populations most at risk.
- Monitoring and improving the effectiveness of poverty alleviation programs.
- Informing long-term strategies aligned with global development goals like the UN Sustainable Development Goals.

#### Key Features
This project includes several innovative features:
- **Artificial Neural Networks (ANNs)**: This project employs sophisticated ANN architectures to model and forecast critical poverty indicators. By leveraging historical data on poverty headcount and headcount ratios, the model learns intricate patterns and relationships, enabling it to generate accurate predictions for various countries and timeframes.

- **Interactive Data Visualization**: The project includes intuitive graphical outputs that effectively communicate complex data insights. These visualizations allow users to easily identify and analyze poverty trends over time, facilitating a deeper understanding of the dynamics at play in different regions.

- **Custom Data Preprocessing Tools**: To ensure high-quality inputs for model training and prediction, the project incorporates tailored preprocessing steps. This includes filtering the dataset to focus on relevant variables, handling missing values, and feature engineering to create meaningful indicators from the raw data, enhancing the model's predictive power.

- **Dynamic Web Interface Using Streamlit**: A user-friendly, interactive web application is developed using Streamlit, allowing users to engage with the data directly. Users can select specific countries to view tailored predictions and corresponding graphs, making the insights more accessible and relatable.

- **Comprehensive Statistical Analysis**: The project features thorough statistical analysis to explore and quantify the relationships between various variables. This analysis not only informs the model's development but also helps in refining its accuracy by identifying key factors that influence poverty levels.

- **Real-World Dataset**: The entire project is grounded in a real-world dataset, which has been meticulously filtered and feature engineered to ensure relevance and accuracy. This robust dataset serves as the backbone for all modeling and prediction efforts, providing a credible foundation for the analysis.

#### Interactive Web App
An interactive web application, built using the **Streamlit** framework, allows users to visualize and analyze the results. Through a simple dropdown interface, users can select a country and explore graphs showing predicted poverty trends, helping to inform decision-making and policy planning.

By predicting future poverty gaps and the international poverty line shortfall, this project offers a valuable tool for understanding poverty and supporting efforts to reduce its impact globally.

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Dataset
A global dataset of poverty and inequality measures prepared by **Our World in Data** from the World Bank's **Poverty and Inequality Platform (PIP)** database.

To view the full codebook [click here]('https://github.com/SavyaSanchi-Sharma/Poverty-Prediction-Model/blob/main/Dataset/pip_codebook.csv') 


### Required Packages

#### Core Dependencies
- pandas - Data manipulation and analysis
- numpy - Numerical computations
- tensorflow - Machine learning and neural networks
- scikit-learn- Data Preprocessing and Feature Engineering
- matplotlib - Static data visualization
- seaborn - Statistical data visualization
- plotly - Interactive visualizations
- streamlit - Web application interface

#### Custom Packages
- Povert_Cleaning - Cleaning the dataset
- EDA_Poverty - Filtering Columns according to the goal
- graphs - All the graphs for visual analysis
- poverty_model1 - Artificial Neural Network Model to predict poverty gaps
- poverty_model2 - Artificial Neural Network Model to predict international poverty shortfall

**Note:** All these packages are available at [Custom Packages]('https://github.com/SavyaSanchi-Sharma/Poverty-Prediction-Model/tree/main/Web%20App/WebApp%20Packages')

#### Custom Trained Model and Encoders
You can get the trained models and encoder [here]('https://github.com/SavyaSanchi-Sharma/Poverty-Prediction-Model/tree/main/Web%20App/Trained%20Models%20and%20Encoder')

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone ['https://github.com/SavyaSanchi-Sharma/Poverty-Prediction-Model.git']
   cd [Poverty-Prediction-Model]
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Or install individually:
   ```bash
   pip install pandas numpy tensorflow matplotlib seaborn plotly streamlit
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 💻 Usage

### Running the Web Application
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`

## 🌍 Poverty Prediction Project Features Guide

## 1. Data Upload & Preprocessing 📊
- **Seamless Upload:** Effortlessly upload your dataset through a user-friendly interface, ensuring a smooth start to your analysis journey.
- **Dynamic Preprocessing:** Automatically apply cutting-edge preprocessing techniques to cleanse and prepare your data, making it ready for insightful analysis.
- **Statistics at a Glance:** Gain quick insights into your data with comprehensive statistics, helping you understand trends and anomalies before diving deeper.

## 2. Visualization 🎨
- **Interactive Charts:** Engage with your data like never before through dynamic, interactive charts that bring your findings to life and allow for exploratory analysis.
- **Statistical Plots:** Utilize a variety of statistical plots to illustrate key relationships and distributions within your data, making complex information easily digestible.
- **Geographic Visualizations:** Uncover geographical trends in poverty with stunning visualizations that highlight disparities and patterns across different regions.

## 3. Analysis 🔍
- **Poverty Metrics Calculation:** Calculate essential poverty metrics tailored to your specific interests, providing a clear picture of poverty levels and their implications.
- **Trend Analysis:** Analyze historical trends in poverty rates to identify patterns and inform future projections, ensuring that your insights are grounded in data.
- **Predictive Modeling:** Leverage advanced Artificial Neural Networks to build predictive models, forecasting future poverty gaps with unparalleled accuracy.

## 📊 Screenshots
[Add screenshots of your web application here]


## 🐛 Troubleshooting
Common issues and solutions:
1. Port already in use:
   ```bash
   streamlit run app.py --port [alternative-port]
   ```
2. Package conflicts:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

## 📫 Contact
[Your Name]
- GitHub: [@SavyaSanchi-Sharma]
- Email: [savyasanchisharma.official@gmail.com]

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
