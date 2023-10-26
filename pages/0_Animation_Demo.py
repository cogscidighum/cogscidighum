# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from gradio_client import client 

def animation_demo(): #-> None:
    client = Client("https://osaaso-ytscrap.hf.space/")
    result = client.predict(
				"https://youtu.be/vQUCSHUlN-k?si=FfIsODGjJDzIHOAS",	# str in 'link' Textbox component
				api_name="/predict"
    )
    print("The talk by Rob West on Altruism has viewcounts of ", result)

    st.sidebar.header("The talk by Rob West on Altruism has viewcounts of : " + str(result))
    st.title("The talk by Rob West on Altruism has viewcounts of : " + str(result))


    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Animation Demo", page_icon="📹")
st.markdown("# Animation Demo")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""


)

animation_demo()

show_code(animation_demo)
