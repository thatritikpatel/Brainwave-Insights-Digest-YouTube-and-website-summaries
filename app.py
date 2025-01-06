import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


import requests
from bs4 import BeautifulSoup
from langchain.schema import Document  
from langchain.text_splitter import CharacterTextSplitter  


class CustomURLTextLoader:
    def __init__(self, url: str):
        self.url = url

    def load(self):
        """
        Fetches the webpage, parses the HTML, and returns a document with plain text content.
        """
        try:
            # Step 1: Fetch the webpage
            response = requests.get(self.url)
            response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)
            
            # Step 2: Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 3: Extract the main content (you may want to target specific elements)
            main_content = soup.find('div', class_='article-content')  # Adjust based on actual structure

            # If no specific content area is found, extract all text
            if not main_content:
                page_text = soup.get_text(separator="\n", strip=True)
            else:
                page_text = main_content.get_text(separator="\n", strip=True)

            # Step 4: Return the text as a LangChain Document
            return [Document(page_content=page_text)]
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []


## sstreamlit APP
st.set_page_config(page_title="Brainwave Insights Digest: YouTube and website summaries", page_icon="🦜")
st.title("🦜 Brainwave Insights Digest: YouTube and website summaries")
st.subheader('Please enter the URL you would like summarized.')



## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")


prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YouTube or Website"):
    ## Gemma Model USsing Groq API
    llm =ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the API key to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or a website URL.")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data

                if "youtube.com" in generic_url:
                    # loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                    loader=YoutubeLoader.from_youtube_url(generic_url)

                else:
                    loader = CustomURLTextLoader(generic_url)


                docs=loader.load()

                ## Chain For Summarization
                # print(docs)
                
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")
                    