# 🌟 Brainwave Insights Digest: YouTube and Website Summaries

## 📖 Overview

**Brainwave Insights Digest** is a powerful and user-friendly tool designed to summarize YouTube videos and web pages, enabling users to quickly glean key insights without spending hours consuming long-form content. Built with cutting-edge language models and an intuitive interface, it offers a seamless experience for extracting meaningful information from digital content.

---

## Video Demo

Here's a video demo of the project:

https://github.com/user-attachments/assets/13fd7b00-d0b6-42a3-ad2b-be7461f140ab

---

## 🤔 Why This Project Exists

In today's digital age, we are inundated with information, from lengthy YouTube videos to comprehensive website articles. However, time is limited, and it can be challenging to extract relevant insights efficiently. **Brainwave Insights Digest** aims to solve this problem by:

- ⏳ Reducing the time spent on consuming content while retaining key takeaways.
- 🧠 Providing a concise and accurate summary of vast and diverse information sources.
- 🚀 Empowering users to focus on decision-making rather than content processing.

---

## 🛠️ What It Does

This tool:

1. 🎥 Extracts and summarizes content from YouTube videos.
2. 🌐 Summarizes articles and web pages from URLs.
3. 🤖 Leverages advanced natural language processing models to ensure accurate and human-like summaries.
4. ✅ Validates user-provided links to prevent errors or invalid inputs.

---

## ⚙️ How It Works

### Key Components

1. **🔗 Input Validation**:
   - Ensures that user-provided YouTube links and URLs are valid using the `validators` library.

2. **📄 Content Extraction**:
   - Uses `YoutubeLoader` to retrieve transcripts from YouTube videos.
   - Uses `UnstructuredURLLoader` to scrape and parse content from websites.

3. **📝 Summarization**:
   - Employs the `load_summarize_chain` function from LangChain to summarize the content effectively.
   - Utilizes the `ChatGroq` LLM (`llama-3.3-70b-versatile`) for high-quality and context-aware summaries.

4. **💻 Frontend Interface**:
   - Built with `Streamlit` to provide a clean, interactive, and easy-to-use UI.

### Workflow

1. User inputs a YouTube URL or website link.
2. The tool validates the input.
3. Content is extracted from the source (video transcript or webpage text).
4. The summarization model processes the content.
5. The summary is displayed on the user interface.

### Code Snippet

```python
import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
import requests
from bs4 import BeautifulSoup
from langchain.schema import Document

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Streamlit UI
st.title("Brainwave Insights Digest")
input_url = st.text_input("Enter a YouTube URL or website link:")

if validators.url(input_url):
    if "youtube.com" in input_url:
        loader = YoutubeLoader(input_url)
    else:
        loader = UnstructuredURLLoader(urls=[input_url])

    docs = loader.load()
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)
    st.write("## Summary")
    st.write(summary)
else:
    st.error("Invalid URL. Please enter a valid link.")
```

---

## 🎯 Advantages

- ⏱️ **Time Efficiency**: Saves users hours by condensing content into concise summaries.
- 🖱️ **User-Friendly**: Easy-to-use interface built with Streamlit.
- 🔄 **Versatile Content Support**: Handles both video and text-based content seamlessly.
- 📊 **Accurate Insights**: Powered by a robust LLM for reliable summarization.

---

## 🛑 Problems It Solves

- **🌀 Information Overload**: Reduces cognitive load by distilling vast amounts of content into actionable insights.
- **⏳ Limited Time**: Helps professionals, students, and researchers stay informed without consuming excessive time.
- **🔍 Content Accessibility**: Extracts meaningful information even from dense or verbose sources.

---

## ✅ Benefits

- 📈 Enhances productivity by allowing users to process more content in less time.
- 💡 Improves decision-making by focusing on key points.
- 📚 Facilitates learning and research with quick summaries of educational materials.

---

## 🚀 Future Enhancements

1. 🌍 **Multilingual Support**:
   - Enable summaries for content in multiple languages.

2. 🔍 **Topic-Based Summarization**:
   - Allow users to request summaries focused on specific topics or questions.

3. 🤝 **Integration with Other Platforms**:
   - Add support for additional content platforms like Twitter, LinkedIn, and blogs.

4. 🧠 **Enhanced Summarization Techniques**:
   - Incorporate more advanced models or ensemble methods for greater precision.

5. 📱 **Mobile App**:
   - Develop a mobile application for on-the-go usage.

6. 🛠️ **Personalized Summaries**:
   - Tailor summaries based on user preferences and past interactions.

---

## 🌈 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/username/brainwave-insights-digest.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Input a YouTube URL or website link to get started!

---

## 🤝 Contributing

We welcome contributions! If you have suggestions, ideas, or bug reports, please:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## ✨ Conclusion

**Brainwave Insights Digest** revolutionizes the way we consume digital content by delivering fast, accurate, and concise summaries. Whether you are a busy professional, a student, or just someone curious about the world, this tool helps you make the most of your time while staying informed.

Feel free to ⭐ star this repository, share it with others, and contribute to its growth!

---

## 📧 Contact

For any queries or suggestions, feel free to reach out at 

- Ritik Patel - [https://www.linkedin.com/in/thatritikpatel/]
- Project Link: [https://github.com/thatritikpatel/Brainwave-Insights-Digest-YouTube-and-website-summaries]