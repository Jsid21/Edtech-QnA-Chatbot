# 📚 EdTech QnA Chatbot  

An AI-powered chatbot for answering frequently asked questions related to EdTech platforms. This chatbot utilizes **LangChain**, **FAISS**, and **Google Generative AI** (Gemini) to provide accurate responses based on a predefined FAQ dataset.

---

## 🚀 Features  
- Uses **Google Generative AI (Gemini-1.5-Flash)** for natural language understanding.  
- Implements **FAISS (Facebook AI Similarity Search)** for efficient question retrieval.  
- Loads data from a CSV file (`edtechData.csv`) containing user queries and responses.  
- Provides a **Streamlit-based UI** for user-friendly interaction.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** (for UI)  
- **LangChain** (for document processing)  
- **FAISS** (for vector-based retrieval)  
- **Google Generative AI** (Gemini)  

---
## 🔧 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Jsid21/Edtech-QnA-Chatbot.git
cd Edtech-QnA-Chatbot
```
### 2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Set Up API Keys
Create a `.env` file and add your Google API Key:
```ini
GOOGLE_API_KEY=your_google_api_key_here
```

### 4️⃣ Prepare the Vector Database
Run the script to process the CSV data and generate FAISS embeddings:
``` bash
python langchain_helper.py
```
### 5️⃣ Run the Streamlit App
``` bash
streamlit run app.py
```
