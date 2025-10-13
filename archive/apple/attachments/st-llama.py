import streamlit as st
from llama_cpp import Llama

# Main app
st.write("# Llama-70B demo 🧠")

# Replace with local llama model
#llm = Llama(model_path='/Users/ammarh/j595/llama.cpp/models/llama-2/llama-2-13b-chat.ggmlv3.q4_0.bin')
llm = Llama(model_path='/Users/local/Source/llama.cpp/models/llama2_70b/llama-2-70b-chat.ggmlv3.q4_0.bin', n_gqa=8)

form = st.form("search_form")
searchtext = form.text_area('Query', 'Ask Llama a question')
confidence = form.slider("Confidence", min_value=0.65, max_value=0.90, value=0.75)
generate_ans = form.checkbox('Summarize')
# Now add a submit button to the form:
submit = form.form_submit_button("Submit")

if submit:
    with st.spinner('Wait for it...'):
        session_variables = {}
        session_variables['searchtext'] = searchtext
        session_variables['confidence'] = confidence
        session_variables['generate_ans'] = generate_ans

        out = llm.create_completion(searchtext)

        txt = out['choices'][0]['text']

        st.write(f"Llama response: {txt}")
        st.json(out)
