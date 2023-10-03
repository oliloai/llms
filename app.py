import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from models.model_openai import ModelOPENAI
from models.model_llama2 import ModelLLAMA2
from models.model_stablelm import ModelStableLM
from models.model_palm2 import ModelPalM2

from init import init_styles, olilo_info


def main():
    
    init_styles()
    olilo_info()

    prompt = st.text_area("Enter your prompt:", placeholder= "Type here...")

    run_button = st.button("Ask Models")

    progress = st.progress(0)
    
    models = [ModelOPENAI(), ModelLLAMA2(), ModelStableLM(), ModelPalM2()]
    # Create columns
    cols = st.columns(len(models))

    for i,  model in enumerate(models):
        cols[i].caption(f"LLM #{i+1} ready...")

    if run_button:
        if prompt == "":
            st.toast("Please enter a prompt", icon='🎉')
        else:
            st.snow()
            with st.spinner("Processing..."):
                
                # Create a thread pool for parallel execution
                with ThreadPoolExecutor() as executor:                    
                    # Start the threads for each model
                    futures = [executor.submit(model.interact, prompt) for model in models]
                    # Retrieve and display the results
                    for i, future in enumerate(as_completed(futures)):
                        progress.progress((i+1)/len(models))
                        cols[i].write(future.result(), unsafe_allow_html=True)

            st.balloons()

    st.sidebar.divider()
    st.sidebar.subheader("Supported LLMS")

    for model in models:
        st.sidebar.write(model.getName())
      

if __name__ == "__main__":
    main()
