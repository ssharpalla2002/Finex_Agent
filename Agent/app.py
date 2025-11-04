import streamlit as st
from langchain_core.messages import HumanMessage
from RAG_Agent import rag_agent 

st.set_page_config(page_title="Stock Market Assistant", page_icon="📈")

st.title("Stock Market AI Agent")
st.markdown("Ask any questions about the stock market performance")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Your question:", placeholder="What does the report say about NASDAQ?")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            messages = [HumanMessage(content=question)]
            result = rag_agent.invoke({"messages": messages})
            answer = result['messages'][-1].content
            st.session_state.history.append((question, answer))
    else:
        st.warning("Please enter a question.")

if st.session_state.history:
    st.markdown("### Chat History")
    for q, a in reversed(st.session_state.history):
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")