from rag_backend import ask_rag  

import gradio as gr

# =========================
# RAG CHAT FUNCTION (USE YOUR EXISTING RAG)
# =========================
def rag_chat(message, history):

    try:
        answer = ask_rag(message)
    except Exception as e:
        answer = f"❌ Error: {str(e)}"

    if history is None:
        history = []

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    return history, ""


# =========================
# BLUE THEME CSS
# =========================
custom_css = """
.gradio-container {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #021B79, #0575E6);
    color: white;
}

.chatbox {
    border-radius: 16px !important;
    overflow: hidden;
}

button {
    border-radius: 10px !important;
    background: linear-gradient(90deg, #0072ff, #00c6ff) !important;
    color: white !important;
    font-weight: bold !important;
}
"""


# =========================
# UI
# =========================
with gr.Blocks() as demo:

    gr.Markdown("""
    # TechProduct_RAG_System
    Ask anything about your product catalog (laptops, mobiles, etc.)
    """)

    chatbot = gr.Chatbot(height=500, elem_classes="chatbox")

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Ask: HP Victus price?",
            scale=8,
            container=False
        )
        send_btn = gr.Button("Send", scale=1)

    send_btn.click(
        rag_chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    msg.submit(
        rag_chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    gr.Button("🗑 Clear Chat").click(lambda: [], outputs=chatbot)


# =========================
# RUN
# =========================
if __name__ == "__main__":
    demo.launch(
        css=custom_css,
        theme=gr.themes.Soft(primary_hue="blue")
    )