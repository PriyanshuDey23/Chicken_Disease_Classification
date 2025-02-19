# 🐔 Chicken Disease Classification


![Chicken Disease Classification](https://raw.githubusercontent.com/PriyanshuDey23/Chicken_Disease_Classification/main/output.jpg)


## 📌 Project Overview
The **Chicken Disease Classification** project aims to predict whether a chicken is **Healthy** or affected by **Coccidiosis** using deep learning techniques. This model leverages **VGG16** in **Keras** for high-accuracy image classification.

## 🚀 Features
- Utilizes **VGG16** as a feature extractor with transfer learning.
- Efficient classification of **Healthy** vs **Coccidiosis-affected** chickens.
- End-to-end pipeline management with **DVC**.
- Streamlit-based web application for easy interaction.
- Modular and scalable codebase following best software practices.

---

## 🔧 Workflow

### **1️⃣ Configuration & Setup**
1. **Update `config.yaml`** - Define paths, hyperparameters, and other configurations.
2. **Update `secrets.yaml` (Optional)** - Store sensitive information securely.
3. **Update `params.yaml`** - Set model training parameters.

### **2️⃣ Implementation**
4. **Update the entity** - Define the entity structure.
5. **Update the configuration manager (`src/config`)** - Manage configurations dynamically.
6. **Update the components** - Implement the data pipeline, preprocessing, and model training.
7. **Update the pipeline** - Integrate components into an end-to-end training pipeline.
8. **Update `main.py`** - Define execution flow and orchestrate all components.
9. **Update `dvc.yaml`** - Track pipeline stages and dependencies using **DVC**.

---

## 🛠 How to Run?

### **📥 Step 1: Clone the Repository**
```bash
https://github.com/PriyanshuDey23/Chicken_Disease_Classification.git
```

### **🐍 Step 2: Create & Activate a Conda Environment**
```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### **📦 Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🚀 Step 4: Run the Application**
#### **Backend**
```bash
python app.py
```

#### **Frontend**
```bash
streamlit run streamlit_app.py
```

---

## 🔄 DVC Commands

To manage version control for datasets and models:
1. **Initialize DVC**
   ```bash
   dvc init
   ```
2. **Run the pipeline**
   ```bash
   dvc repro
   ```
3. **Visualize pipeline dependencies**
   ```bash
   dvc dag
   ```

---

## 📜 License
This project is open-source and available under the **MIT License**.



