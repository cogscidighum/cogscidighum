# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#CogSciDigHum
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

import streamlit as st
from streamlit.logger import get_logger
from gradio_client import Client
import gradio as gr

LOGGER = get_logger(__name__)
    
def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.write("# Welcome to CogSciDigHum! 👋")

    client = Client("https://osaaso-ytscrap.hf.space/")
    result = client.predict(
				"https://youtu.be/vQUCSHUlN-k?si=FfIsODGjJDzIHOAS",	# str in 'link' Textbox component
				api_name="/predict"
    )
    print("The talk by Rob West on Altruism has viewcounts of ", result)

    st.sidebar.header("The talk by Rob West on Altruism has viewcounts of : " + str(result))
    st.title("The talk by Rob West on Altruism has viewcounts of : " + str(result))

    st.markdown(
        """
    The Video: 
    
    :pencil: [Open](https://youtu.be/vQUCSHUlN-k?si=FfIsODGjJDzIHOAS)    
    """
    )
    st.markdown(
        """
    What you can do with this:
    
    * get youtube views!

    """
    )

    st.sidebar.success("demo to come...")

    st.markdown(
        """
        **👈**

    """
    )


if __name__ == "__main__":
    run()
