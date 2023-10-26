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

LOGGER = get_logger(__name__)
    
def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    from gradio_client import Client

    client = Client("https://osaaso-ytscrap.hf.space/")
    result = client.predict(
				"https://www.youtube.com/watch?v=prt9D90BvFI",	# str in 'link' Textbox component
				api_name="/predict"
    )
    print("The talk by Rob West on Altruism has viewcounts of ", result)

    st.sidebar.header("The talk by Rob West on Altruism has viewcounts of : "+ str(result))
    st.title(str(result))

    st.markdown(
        """
    Welcome 
    
    :pencil: [Open](https://www.youtube.com/watch?v=prt9D90BvFI)    
    """
    )
    st.image("img/demo.gif")
    st.markdown(
        """
    What you can do with this:
    
    * get views

    """
    )
    st.write("# Welcome to CogSciDigHum! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
