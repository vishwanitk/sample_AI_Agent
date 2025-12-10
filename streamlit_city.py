#!/usr/bin/env python
# coding: utf-8

# In[84]:


import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import getpass


# In[86]:


st.set_page_config(page_title="City One-Word Describer", page_icon="🌎")

st.title("🌆 One-Word City Describer")
st.write("Type any city name and I will describe it in **one word**.")


# In[88]:


api_key = "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"

if not api_key:
    st.info("Please enter your Groq API Key to continue.")
    st.stop()


# In[90]:


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key

)


# In[92]:


prompt = PromptTemplate(
    input_variables=["city"],
    template="In ONE word only, describe the city {city}. Output just the single word and explain why you chose to that word for that city"
)


# In[96]:


#llm.invoke("tell about Berlin")


# In[98]:


city_name = st.text_input("Type city name:")


# In[100]:


if st.button("Describe"):
    if city_name.strip() == "":
        st.error("Please enter a valid city name.")
    else:
        chain = prompt | llm
        response = chain.invoke({"city": city_name}).content

        st.success(f"**One-word description for {city_name}: {response}")
        #st.markdown(f"### 🏷️ {response.content.strip()}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




