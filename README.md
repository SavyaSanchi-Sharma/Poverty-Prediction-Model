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
[List your custom packages here with brief descriptions]

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd [your-project-name]
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
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

### Features Guide
1. Data Upload & Preprocessing
   - Upload your dataset
   - Apply preprocessing techniques
   - View data statistics

2. Visualization
   - Interactive charts
   - Statistical plots
   - Geographic visualizations

3. Analysis
   - Poverty metrics calculation
   - Trend analysis
   - Predictive modeling

## 📁 Project Structure
```
project/
├── app.py                  # Main Streamlit application
├── data/                   # Data directory
│   ├── raw/               # Raw data files
│   └── processed/         # Processed data files
├── src/                   # Source code
│   ├── preprocessing/     # Data preprocessing modules
│   ├── visualization/     # Visualization modules
│   ├── analysis/         # Analysis modules
│   └── utils/            # Utility functions
├── models/               # Trained models
├── requirements.txt      # Project dependencies
├── LICENSE              
└── README.md
```

## 📊 Screenshots
[Add screenshots of your web application here]

## 🔧 Configuration
The application can be configured through the following environment variables:
```bash
PORT=8501  # Default Streamlit port
```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -am 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Submit a Pull Request

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
- GitHub: [@yourusername]
- Email: [your.email@example.com]

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Requirements
To install all required packages, run:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas numpy tensorflow matplotlib seaborn plotly streamlit
```

Python Version: 3.8 or higher

### Dependency List
```
pandas>=1.5.0
numpy>=1.21.0
tensorflow>=2.10.0
matplotlib>=3.5.0
seaborn>=0.12.0
plotly>=5.10.0
streamlit>=1.20.0
```

[Add any specific version requirements for your custom packages]

---
Created with by [Your Name]