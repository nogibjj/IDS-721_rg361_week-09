import streamlit as st
import requests

# from transformers import pipeline

# # Initializing the pipeline for the model
# pipe = pipeline("text2text-generation", model="grammarly/coedit-large")


# # To process the input and get the output
# def query(dropdown_value, textinput_value):
#     prompt = dropdown_value + ": " + textinput_value
#     try:
#         return pipe(prompt, max_new_tokens=50)[0]["generated_text"]
#     except:  # noqa
#         return "Sorry, there was an error. Please try again."


API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": "Bearer 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"}


def query(dropdown_value, textinput_value):

    prompt = dropdown_value + ": " + textinput_value
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()[0]["generated_text"]
    except:  # noqa
        return "Sorry, there was an error. Please try again."


# defining the streamlit app
def main():
    st.title("Sentence Rewriter")
    st.write("This app rewrites sentences based on the user's choice.")

    # Create a dropdown menu
    dropdown_value = st.selectbox(
        "What would you like to do?",
        [
            "Fix the grammar",
            "Make this text coherent",
            "Rewrite to make this easier to understand",
            "Paraphrase this",
            "Write this more formally",
            "Write in a more neutral way",
        ],
    )

    # Create a text input
    textinput_value = st.text_area("Enter your sentence here:")
    if st.button("Submit"):
        with st.spinner("Rewriting..."):
            output = query(dropdown_value, textinput_value)
        st.write(output)


if __name__ == "__main__":
    main()
