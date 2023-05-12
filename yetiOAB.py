import os
import sys
import argparse
import gradio as gr
from src.user import user
from src.bot import bot

def main(debug, share, image_width, image_height, openai_api):
    openai.api_key = openai_api

    with gr.Blocks(theme='Monochrome') as demo:
        gr.Markdown("# Oracle of All Beings `v.0.0.1`")
        gr.Markdown("## Please select the text box and press the `Enter` Key")
        chatbot = gr.Chatbot(label="Oracle of All Beings")
        with gr.Row():
            txt = gr.Textbox(show_label=False, value="Begin", placeholder="Press Enter to Start").style(container=False)

        txt.submit(user, [txt, chatbot], [txt, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        txt.submit(None, None, txt, _js="() => {''}")
    demo.queue()
    demo.launch(debug=debug, share=share)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Oracle of All Beings')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--share', action='store_true', help='Enable sharing mode')
    parser.add_argument('--width', type=int, default=720, help='Image width')
    parser.add_argument('--height', type=int, default=720, help='Image height')
    parser.add_argument('--api', type=str, required=True, help='OpenAI API key')

    args = parser.parse_args()

    main(args.debug, args.share, args.width, args.height, args.api)
