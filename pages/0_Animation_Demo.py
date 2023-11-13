from gradio_client import Client
client = Client("https://cogsphere-acogsphere.hf.space/")

from python_actr import *
log=log()

class RPSChoice(Model):
    choice=None
    font='Arial 20'
    waiting=True

    def start(self):
        self.visible=True
        self.text=self.instructions
    
    def choose(self,option):
        if not self.waiting: return
        if option not in ['rock','paper','scissors']: return
        self.choice=option
        self.visible=False
        self.waiting=False

        # check to see if both players have made a choice
        if self.parent.choice1.choice is not None and self.parent.choice2.choice is not None:
            self.parent.determine_winner()            

    def reset(self):
        self.text=self.instructions
        self.waiting=True
        self.visible=True
        self.choice=None


class RockPaperScissors(Model):
    choice1=RPSChoice(x=0.5,y=0.2,instructions='Choose: Rock(1) Paper(2) Scissors(3)')
    choice2=RPSChoice(x=0.5,y=0.8,instructions='Choose: Rock(Z) Paper(X) Scissors(C)')

    result=Model(x=0.5,y=0.5,visible=False)

    score1=Model(text=0,x=0.9,y=0.1)
    score2=Model(text=0,x=0.9,y=0.9)

    trials=0

    def key_pressed(self,key):
        if key=='1': self.choice1.choose('rock')
        if key=='2': self.choice1.choose('paper')
        if key=='3': self.choice1.choose('scissors')
        
        if key=='z': self.choice2.choose('rock')
        if key=='x': self.choice2.choose('paper')
        if key=='c': self.choice2.choose('scissors')

    def determine_winner(self):
        self.choice1.text=self.choice1.choice
        self.choice2.text=self.choice2.choice
        self.choice1.visible=True
        self.choice2.visible=True

        c1=self.choice1.choice
        c2=self.choice2.choice
        if c1==c2:
            self.result.text="Tie!"
        elif (c1=='rock' and c2=='scissors') or (c1=='paper' and c2=='rock') or (c1=='scissors' and c2=='paper'):
            self.result.text="Player 1 wins!"
            self.score1.text+=1
        else:
            self.result.text="Player 2 wins!"
            self.score2.text+=1
        self.result.visible=True
            

        yield 1

        self.result.visible=False
        
        self.choice1.reset()
        self.choice2.reset()

        self.trials+=1
        if self.trials>=100:
            scora=self.score1.text
            scorb=self.score2.text
            result = client.predict(
		"ACT-R RPS"
        "100",		
		"Model 1: " + str(scora) + " Model 2: " + str(scorb),
		fn_index=0)
            log.score1=self.score1.text
            log.score2=self.score2.text
            self.stop()
        

#from ccm.lib.actr import *
class ProceduralPlayer(ACTR):
    goal=Buffer()
    goal.set('play rps')

    def play_rock(goal='play rps',choice='waiting:True'):
        choice.choose('rock')
    def play_paper(goal='play rps',choice='waiting:True'):
        choice.choose('paper')
    def play_scissors(goal='play rps',choice='waiting:True'):
        choice.choose('scissors')

#env=RockPaperScissors()
#env.model1=ProceduralPlayer()
#env.model1.choice=env.choice1
#env.model2=ProceduralPlayer()
#env.model2.choice=env.choice2
#env.run()
#log_data = env.log
#return log_data[0]['score1']

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


def animation_demo() -> None:

    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
    separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

    # Non-interactive elements return a placeholder to their location
    # in the app. Here we're storing progress_bar to update it later.
    progress_bar = st.sidebar.progress(0)

    # These two elements will be filled in later, so we create a placeholder
    # for them using st.empty()
    frame_text = st.sidebar.empty()
    image = st.empty()

    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        # Here were setting value for these two elements.
        progress_bar.progress(frame_num)
        frame_text.text("Frame %i/100" % (frame_num + 1))

        # Performing some fractal wizardry.
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M: Any = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # Update the image placeholder by calling the image() function on it.
        image.image(1.0 - (N / N.max()), use_column_width=True)

    # We clear elements by calling empty on them.
    progress_bar.empty()
    frame_text.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Animation Demo ASN", page_icon="📹")
st.markdown("# Animation Demo")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)

animation_demo()

show_code(animation_demo)
