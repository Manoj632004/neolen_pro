from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = "sk-"
def main():
    st.set_page_config(page_title="home")
    st.header("UPLOAD FILE")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")#,accept_multiple_files=True

    if csv_file is not None:
        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question based on your file: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                try:
                    st.write(agent.run(user_question))
                except:
                    st.write("unable to answer!")


if __name__ == "__main__":
    main()
