import numpy as np
import streamlit as st
import base64
from GimmeSomeJazz import GimmeSomeJazz
from GimmeSomeJazzGifs import GimmeSomeJazzGifs


DATASET = 'dataset/library.json'


st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="🎙️Gimme Somme Jazz!",
    page_icon="🎙️"
)
left_column, right_column = st.beta_columns(2)
left_column.write("# I'm your jazz coach")
left_column.write("Feeding you with the best of jazz")
button = left_column.button("Gimme some jazz!", "new")

gifer = GimmeSomeJazzGifs("LIVDSRZULELA")
trainer = GimmeSomeJazz(DATASET)

if button:
    desc = trainer.draw()
    gif = gifer.draw()
    left_column.write(desc, unsafe_allow_html=True)
    right_column.image(gif, width=400, use_column_width='always')
    right_column.write("[link to TenorGif](%s)" % gif)
