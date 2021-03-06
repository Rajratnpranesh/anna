

##########
#lIBRARIES
##########

import streamlit as st
import streamlit.components.v1 as components
from gensim.summarization import summarize
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
import readtime
import textstat

########
#HEADER
#######

st.set_page_config(page_title="Anne", page_icon=":smiley:", layout="wide")

st.markdown("<h4 style='text-align: center; color:grey;'>Your AI homework buddy</h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Generate. Summarize. Paraphrase. Measure.</h1>", unsafe_allow_html=True)
st.write('')

#"""
#[![Star](https://img.shields.io/github/stars/dlopezyse/Synthia.svg?logo=github&style=social)](https://gitHub.com/dlopezyse/Synthia)
#&nbsp[![Follow](https://img.shields.io/twitter/follow/lopezyse?style=social)](https://www.twitter.com/lopezyse)
#"""
st.write('')
st.write(':point_left: Using the menu at left, please select a task for Anna (click on > if closed).')

st.markdown('___')

#########
#SIDEBAR
########

st.sidebar.header('Pick one task :bulb:')
nav = st.sidebar.radio('',['Generate text', 'Summarize text', 'Paraphrase text', 'Measure text'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

#ABOUT
######
expander = st.sidebar.beta_expander('About Anne')
expander.write("Anne is your AI teacher who is here to help you with your daily homework. Whether you are in a school or college, Anna can help you to get your work done easily and quickly. Anna is still learning and growing, therefore your feedbacks can help us to understand your needs and improvr Anna. Please reach out to us and share your thoughts about Anna :smiley:. [LinkedIn] (https://www.linkedin.com/in/raj-ratn-pranesh-382155172/) and [Website] (https://rajratnpranesh.github.io/)")


#######
#PAGES
######

#GENERATE
#########

# if nav == 'Generate text':
#     st.markdown("<h3 style='text-align: left; color:#F63366;'><b>Generate Text<b></h3>", unsafe_allow_html=True)
#     st.text('')

#     input_ge = st.text_area("Type in some words, and we will create something for you", max_chars=500, value="The future of humanity will depend on")

#     if st.button('Create text'):
#         if input_ge =='':
#             st.error('Please enter some words')
#         else:
#             with st.spinner('Wait for it...'):
#                 result = input_ge.title()
#                 from transformers import GPT2LMHeadModel, GPT2Tokenizer
#                 tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#                 model = GPT2LMHeadModel.from_pretrained('gpt2')
#                 inputs = tokenizer.encode(result, return_tensors='pt')
#                 outputs = model.generate(inputs, max_length=200, do_sample=True)
#                 text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#                 st.write(text)

#     st.markdown('___') 
    
#     components.html(
#                         """
#                         <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Meet ANNA, your AI homework buddy @PraneshRatn" data-url="https://rajratnpranesh.github.io/" data-hashtags="AI,Education,MachineLearning,Anna" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#                         """,
#                         )
        
#-----------------------------------------

#SUMMARIZE
##########

# if nav == 'Summarize text':
#     st.markdown("<h3 style='text-align: left; color:#F63366;'><b>Summarize Text<b></h3>", unsafe_allow_html=True)
#     st.text('')
    
#     input_su = st.text_area("Write some text or copy & paste so we can summarize it (minimum = 1000 characters)", max_chars=5000)

#     if st.button('Summarize'):
#         if input_su =='':
#             st.error('Please enter some text')
#         elif len(input_su) < 1000:
#             st.error('Please enter a larger text')
#         else:
#             with st.spinner('Wait for it...'):
#                 st.success(summarize(input_su, word_count=50, ratio=0.05))

#     st.markdown('___')

#     components.html(
#                         """
#                         <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Meet ANNA, your AI homework buddy @PraneshRatn" data-url="https://rajratnpranesh.github.io/" data-hashtags="AI,Education,MachineLearning,Anna" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#                         """,
#                         )

#-----------------------------------------

#PARAPHRASE
###########

# if nav == 'Paraphrase text':
#     st.markdown("<h3 style='text-align: left; color:#F63366;'><b>Paraphrase Text<b></h3>", unsafe_allow_html=True)
#     st.text('')
    
#     input_pa = st.text_area("Write some text or copy & paste so we can paraphrase it", max_chars=5000)

#     if st.button('Paraphrase'):
#         if input_pa =='':
#             st.error('Please enter some text')
#         else:
#             with st.spinner('Wait for it...'):
#                 translator = Translator()
#                 mid = translator.translate(input_pa, dest="fr").text
#                 mid2 = translator.translate(mid, dest="de").text
#                 back = translator.translate(mid2, dest="en").text
#                 st.write(back)

#     st.markdown('___')

#     components.html(
#                         """
#                         <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Meet ANNA, your AI homework buddy @PraneshRatn" data-url="https://rajratnpranesh.github.io/" data-hashtags="AI,Education,MachineLearning,Anna" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#                         """,
#                         )

#-----------------------------------------
   
#MEASURE
########
       
if nav == 'Measure text':
    st.markdown("<h3 style='text-align: left; color:#F63366;'><b>Measure Text<b></h3>", unsafe_allow_html=True)
    st.text('')

    input_me = st.text_area("Input some text in English, and scroll down to analyze it", max_chars=5000)

    if st.button('Measure'):
        if input_me =='':
            st.error('Please enter some text')
        elif len(input_me) < 500:
            st.error('Please enter a larger text')
        else:
            with st.spinner('Wait for it...'):
                nltk.download('punkt')
                rt = readtime.of_text(input_me)
                tc = textstat.flesch_reading_ease(input_me)
                tokenized_words = word_tokenize(input_me)
                lr = len(set(tokenized_words)) / len(tokenized_words)
                lr = round(lr,2)
                st.text('Reading Time')
                st.write(rt)
                st.text('Text Complexity (score from 0 (hard to read), to 100 (easy to read))')
                st.write(tc)
                st.text('Lexical Richness (distinct words over total number of words)')
                st.write(lr)

    st.markdown('___') 
    
    components.html(
                        """
                        <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Meet ANNA, your AI homework buddy @PraneshRatn" data-url="https://rajratnpranesh.github.io/" data-hashtags="AI,Education,MachineLearning,Anna" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                        """,
                        )

####################################
