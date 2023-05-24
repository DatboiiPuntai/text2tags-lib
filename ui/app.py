import gradio as gr
from text2tags import TaggerLlama

model = TaggerLlama()


def predict(caption, max_tokens, temperature, top_k, top_p, repeat_penalty):
    tags = model.predict_tags(caption, max_tokens=max_tokens, temperature=temperature,
                              top_k=top_k, top_p=top_p, repeat_penalty=repeat_penalty)
    return ', '.join(tags)


demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(label="Caption"),
        gr.Slider(0, 256, step=16, value=128, label='max_tokens'),
        gr.Slider(0, 2, step=0.1, value=0.8, label='temperature'),
        gr.Slider(0, 100, step=5, value=40, label='top_k'),
        gr.Slider(0, 2, step=0.05, value=0.95, label='top_p'),
        gr.Slider(0, 5, step=0.1, value=1.1, label='repeat_penalty'),
    ],
    outputs="text",
    title="Text2Tags",
    description="### Enter a caption to extract danbooru tags from it.",
    examples=[
        ["Minato Aqua from hololive with pink and blue twintails in a blue maid outfit"],
    ],
    allow_flagging="never"
)

demo.launch()
