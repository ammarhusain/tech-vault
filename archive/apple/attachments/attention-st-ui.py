import os
os.environ["COMET_URL_OVERRIDE"] = "https://palazzo-eval.corp.apple.com/clientlib/"
os.environ["COMET_INTERNAL_CHECK_TLS_CERTIFICATE"] = "0"

import streamlit as st
import json
import uuid
from llama_cpp.llama import Llama, LlamaGrammar
from llama_cpp.llama_chat_format import format_chatml
import subprocess
import comet_llm, comet_ml

def extract_response(full_string, substring="assistant"):
    # Find the index of the substring
    index = full_string.rfind(substring)
    
    # Check if the substring is found
    if index != -1:
        # Add the length of the substring to the index to start extracting after it
        return full_string[index + len(substring):]
    else:
        # Return an empty string or appropriate message if the substring is not found
        return f"Substring {substring} not found"

# grammar = LlamaGrammar.from_file("/Users/local/Desktop/attn/json_chatml.gbnf")
# model_path = "/Users/ammarh/j595/llama.cpp/models/neuralhermes-2.5-mistral-7b/neuralhermes-2.5-mistral-7b.Q5_K_M.gguf"
# model_path = "/Users/ammarh/j595/llama.cpp/models/openorca-platypus2-13b/openorca-platypus2-13b.Q5_K_M.gguf"
# model_path = "/Users/ammarh/j595/llama.cpp/models/dolphin-mixtral-8x7b-GGUF/dolphin-2.7-mixtral-8x7b.Q5_K_M.gguf"
model_path = "/Users/ammarh/j595/llama.cpp/models/dolphin-mixtral-8x7b-GGUF/dolphin-2.5-mixtral-8x7b.Q5_K_M.gguf"

# Define attributes and their options
entity_name = 'Unknown'
proximity = ['Within Reach - less than 2 feet', 'Close - between 2 feet and 6 feet', 'In the room - beyond 6 feet']
is_gazing = ['Yes', 'No']
head_direction = ['Facing Device', 'Not Facing Device']
is_speaking = ['Yes', 'No']
is_moving = ['Yes', 'No']
novelty = ['less than 5 seconds', 'between 5 seconds and 2 minutes', 'longer than 2 minutes']
speech = ''

attention_modes = {'Hyper-Focussed': """
    * Once you're engrossed in a conversation or taking on a task with somebody (or a group of people) who is engaged with you (they are looking at you with some frequency, most of their speech is directed to you or to a group that includes you) you should keep your attention bodily on them, paying close attention to their movements, to what they say, what they might be referring to in the physical space from their speech (like when they say something “look over there”, “to your right”, “follow me”). 
    * You are deliberately less sensitive to other entities that are not engaged directly with you (i.e. they are not speaking, looking, or near you). So even if they move, you are unlikely to be distracted enough to turn your attention to them. 
    * Entities in the “background“ (i.e. not engaged in this task or conversation at hand) would need to deliberately say something to either you directly or to your subject of interest, in which case, you’d pay attention to them if your current subject of attention did as well. Exceptions to this would be entities that come up really close to you (within your personal space of 2 feet, i..e roughly within reach) in which case it would be rude not to acknowledge them. 
    * And while you are hyper focused on your attended subject, you can quickly acknowledge changes in the environment like someone new coming in with a quick darting glance to check if there’s any engagement or interest, but return your focus to the topic and subject you've been focusing on. Likely background activity will not be someone trying to catch your attention with their gaze or body motion. 
    * When hyper focused on a group of people, you still need to choose one person at a time to be very reactive towards, and are deliberately not sensitive to entities that aren't a part of this initial group, or aren't especially relevant to them. 
    * hyper focus is most relevant when you are actively trying to complete a task or are a crucial participant or leading role in an activity, like when you are the photographer in a photoshoot, or when you are the proctor in an exam, or the coach trying to help an individual, or the therapist chatting someone through their feelings in a conversation, 
                   """, 
                   "Involved": """
    * If you haven't been explicitly invited, addressed, or directly engaged, there still might be a context or situation that is close enough to be interesting or relevant to you like someone sitting within 2 feet of you working on something at their computer. Your attention is loosely attached to each entity as they change their behavior, or as you occasionally, periodically check in on what they're up to. 
    * Typically, your “involved”-attention is for activities where you are not a crucial participant or leading role, like when you are a peer trying to learn with someone and their teacher, when you are just trying to be a helpful companion keeping someone company as they work, when you are watching a movie with someone. In which case, you really don’t need to attend constantly to the other entity. Your attention cycles between the shared interest (what is everyone else looking at and referring to?), whoever might be speaking, or otherwise any changes (say if someone were to suddenly start clapping, moving, or whoops in delight). If the sound or motion catches your eye, you typically stay watching it til it either stops or it ends up repetitive (like if someone is fidgeting, after a while of the same constant fidgeting you lose interest)
                   """
                   }

behavior_principles = """* generally, you want to reciprocate the level of attention that is given to you. If someone is engaging you (giving you some eye contact, is near you, and definitely if they are speaking to you) you want to give them your attention expressed by your body turning towards them, eye contact, generally following their motion, attempts to mirror or reciprocate their energy level.
    * Someone highly engaged with you makes frequent eye contact, are facing towards you, and might have even angled their body towards you. They are more likely to be within 6 ft from you (more than that, and it’s likely you are not their sole focus). Even without observable visual signals like the above though, if you can tell from their speech that they are likely addressing you, then that is considered engaged and you should reciprocate with your attention on them. 
* In a conversation that is happening close to you, is somewhat interesting to you and relevant topically (i.e. something you can contribute to) you pay attention to the speaker, and try to anticipate who they might be addressing, if they aren’t addressing you, when they finish speaking you should turn to who they might be addressing as a way of expressing how well you are following the conversation. The longer the conversation goes on without an opportunity for you to contribute, without any engagement with you from the other participants, the less you need to express your attention to the situation.
* You are generally very curious and interested in what happens around you. You are proactive and eager to help when you see something you can assist in. Especially when it’s calculating, or searching up information, or making use of your prodigiously good memory.
"""

proprioception = """You are a small iPad sized robot that can spin your base, much like how people can spin their body in a chair.
    * spinning your base towards someone is like turning your full body towards someone. You do so when you are trying to express your full attention is on someone.
    * You don’t always have to spin bodily to fully face someone, if they are not meant to be the subject of your full attention, you can turn your base partially towards them and use your face to convey the rest of the directionality.
    * when you're on a desk where someone is working within reach of you, you try not to make your body movements too distracting to them (your motion is calm, you aren't trying to react to every little change in order to not be come across fidgety or distracting) You keep your motion smaller because when someone is really close to you, you don't need much movement to be expressive. you can be subtle.
    * When they are beyond arms reach away from you, you prefer to exaggerate your motion, making bigger moves, faster.
"""

st.text_area('Behavior Principles: ', value=behavior_principles, key='attention_behavior')
st.text_area('Proprioception: ', value=proprioception, key='proprioception')
st.selectbox('Attention Mode: ', attention_modes.keys(), key='attention_mode')

# State to keep track of the number of Attribute 1 instances
if 'rolling_context' not in st.session_state:
    st.session_state['rolling_context'] = []


if st.button('Set System Prompt'):
    sys_prompt = f"""
    Your proprioception is {st.session_state['proprioception']}\n\n
    Your perception system provides to your the following signals that you get from various entities that are around you. 
    You must rely only on the signals that you perceive and sense through your perception signal and nothing else. Here are the list of signals and what they mean for you.
    "entity_name" is the name of the person around if you know it or "Unknown" otherwise.
    "proximity" indicates to you how close this person is to you in physical space.
    "is_gazing" tells you whether this person is making eye contact and looking at you or not
    "head_direction" tells you where this person is facing and whether their orientation is towards you or not indicating a level of engagement.
    "is_moving" tells you whether this person is moving near you or not
    "is_speaking" signals to you whether this person is currently engaging in a conversation with you
    "novelty" signals to you when you first saw this person into the scene or within your perception
    "speech" is the utterance of this person directed at you and indicates either a command or conversation that this person has directed towards you. You must listen carefully to what they are asking you to do
    
    ### Behavior Principles: {st.session_state['attention_behavior']}\n
    ### Attention Mode: {st.session_state['attention_mode']}\n
    {attention_modes[st.session_state['attention_mode']]}\n        

    ### Expected Output
    You need to figure out which entity in the most recently provided entities to pay attention to along with a short explanation of why that entity is of interest based on their various sensed attributes.
    You must stick to JSON for your responses as you see in the examples. The keys in your output JSON should only be "look_at_entity" , "look_at_entity_uuid" and "reason" which match the most recent input user entities.\n

    Following are a few examples of what entities you might get and your expected output for each of them.
    """
    st.session_state['rolling_context'].clear()
    st.session_state['rolling_context'].append({"role": "system", "content": sys_prompt},)

    # Some input examples
    # Example 1:
    st.session_state['rolling_context'].append({"role": "user", "content": """entities: [
{
    "entity_name": "Bob",
    "entity_uuid": "c054a702-9b3e-4ca5-a393-1c07c7d75999",
    "proximity": "Within Reach - less than 2 feet",
    "is_gazing": "Yes",
    "head_direction": "Facing Device",
    "is_speaking": "Yes",
    "is_moving": "Yes",
    "novelty": "less than 5 seconds",
    "speech": ""
},
{
    "entity_name": "Alice",
    "entity_uuid": "d62679c6-2cd3-45ef-b873-259bd12ed3d5",
    "proximity": "Within Reach - less than 2 feet",
    "is_gazing": "No",
    "head_direction": "Facing Device",
    "is_speaking": "No",
    "is_moving": "No",
    "novelty": "less than 5 seconds",
    "speech": ""
},
                                                
]"""})
    st.session_state['rolling_context'].append({"role": "assistant", "content": """attend_to_entity: {
"entity_name": "Bob",
"entity_uuid": "c054a702-9b3e-4ca5-a393-1c07c7d75999",
"reason": "Bob is engaging with the device by looking at it and speaking to it"                                                

}
"""})
    # Example 2:
    st.session_state['rolling_context'].append({"role": "user", "content": """entities: [
{
    "entity_name": "Bob",
    "entity_uuid": "c054a702-9b3e-4ca5-a393-1c07c7d75999",
    "proximity": "Within Reach - less than 2 feet",
    "is_gazing": "Yes",
    "head_direction": "Facing Device",
    "is_speaking": "Yes",
    "is_moving": "Yes",
    "novelty": "less than 5 seconds",
    "speech": "Alice is a wonderful dancer"
},
{
    "entity_name": "Alice",
    "entity_uuid": "d62679c6-2cd3-45ef-b873-259bd12ed3d5",
    "proximity": "Within Reach - less than 2 feet",
    "is_gazing": "No",
    "head_direction": "Facing Device",
    "is_speaking": "No",
    "is_moving": "No",
    "novelty": "less than 5 seconds",
    "speech": ""
},
                                                
]"""})
    st.session_state['rolling_context'].append({"role": "assistant", "content": """attend_to_entity: {
"entity_name": "Alice",
"entity_uuid": "d62679c6-2cd3-45ef-b873-259bd12ed3d5",
"reason": "Bob said something about Alice"                                                
}
"""})
    ## TODO : Add more examples here

    # st.session_state['attention_llm'] = Llama(model_path=model_path,
    #         rope_freq_scale=2, # Increase the frequency of ROPE tokens
    #         n_ctx=32768, # Increase the context window size
    #         #grammar=grammar
    #         )

    # llm_out = st.session_state['attention_llm'].create_chat_completion(
    #     messages = st.session_state['rolling_context'],
    #     max_tokens=1,
    #     temperature=0.7,
    #     top_p=1.0,
    #     )
    # print(f'Primed LLM - initial generation:{llm_out["choices"][0]["message"]["content"]}')
    # st.session_state['attention_llm_state'] = st.session_state['attention_llm'].save_state()



# Function to display nested attributes
def display_nested_attributes(attr_id, key):
    with st.expander(f"Motif signals for UUID: {attr_id}"):
        col1, col2, col3, col4, col_del = st.columns([1, 1, 1, 1, 1])
        st.selectbox('Proximity', proximity, key=key + "_proximity")
        with col1:
            st.selectbox('Is Gazing?', is_gazing, key=key + "_gazing")
        with col2:
            st.selectbox('Head Direction', head_direction,  key=key + "_head_dir")
        with col3:
            st.selectbox('Is Speaking?', is_speaking, key=key + "_speaking")
        with col4:
            st.selectbox('Is Moving?', is_moving, key=key + "_moving")
        st.selectbox('Novelty', novelty, key=key + "_novelty")
        st.text_input('Speech', value=speech, key=key + "_speech")
        if st.button('Delete', key='delete_' + attr_id):
            st.session_state['num_entities'].remove(attr_id)
            st.rerun()


# State to keep track of the number of Attribute 1 instances
if 'num_entities' not in st.session_state:
    st.session_state['num_entities'] = []

# Button to add more Attribute 1 instances
if st.button('Add Entity'):
    st.session_state['num_entities'].append(str(uuid.uuid4()))

# Display the appropriate number of Attribute 1 instances and their nested attributes
for attr_id in st.session_state['num_entities']:
    key = f"entity_{attr_id}"
    st.text_input ('Entity name: ', value=entity_name, key=key)
    display_nested_attributes(attr_id, key)


    
if st.button('Submit'):
    selected_attributes = []
    for attr_id in st.session_state['num_entities']:
        key = f"entity_{attr_id}"
        entry = {
            'entity name': st.session_state[key],
            'entity_uuid': attr_id,
            'proximity': st.session_state[key + "_proximity"],
            'is_gazing': st.session_state[key + "_gazing"],
            'head_direction': st.session_state[key + "_head_dir"],
            'is_speaking': st.session_state[key + "_speaking"],
            'is_moving': st.session_state[key + "_moving"],
            'novelty': st.session_state[key + "_novelty"],
            'speech': st.session_state[key + "_speech"]
        }
        selected_attributes.append(entry)

    st.session_state['rolling_context'].append({"role": "user", "content": f"""entities: {json.dumps(selected_attributes, indent=4)}"""})

    formatted_chat_prompt = format_chatml(st.session_state['rolling_context']).prompt
    with st.expander("View raw prompt"):
        st.code(formatted_chat_prompt)

    # Define the path to the binary
    binary_path = '/Users/ammarh/j595/llama.cpp/main'

    # Define the arguments for the binary as a list
    arguments = ['-m', model_path, '-c', '32768', '-p', formatted_chat_prompt, '--prompt-cache', '/tmp/attn/cache']  # Replace these with your actual arguments
 
    # Combine the binary path and the arguments
    command = [binary_path] + arguments

    # Run the binary and capture the output
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the stdout and stderr
    stdout = process.stdout
    stderr = process.stderr

    # Check if there was an error
    if process.returncode != 0:
        print(f"Error running command: {stderr}")
        st.write(stderr)

    else:
        print(f"Command output: {stdout}")
        llm_response = extract_response(stdout, "assistant")
        st.code(llm_response)
        comet_experiment=comet_ml.Experiment(
            api_key = "viG5OIqNNBnZWlRn5opWCVnO6",
            project_name = "attention-experimental-sys",
            workspace = "j595")
        
        comet_llm.log_prompt(
            api_key = "viG5OIqNNBnZWlRn5opWCVnO6",
            project = "attention-experimental",
            metadata={"system.experiment-url": comet_experiment.url,},
            workspace = "j595",
            prompt = formatted_chat_prompt,
            output = llm_response,
        )
        comet_experiment.log_other('llm_project_url', comet_llm_result.project_url)
        comet_experiment.log_other('llm_prompt_id', comet_llm_result.id )
        comet_experiment.end()
    # st.session_state['attention_llm'].load_state(st.session_state['attention_llm_state'])
    # llm_out = st.session_state['attention_llm'].create_chat_completion(
    #     messages = st.session_state['rolling_context'],
    #     max_tokens=-1,
    #     temperature=0.7,
    #     top_p=1.0,
    #     )
    
    # st.write(llm_out["choices"][0]["message"]["content"])
