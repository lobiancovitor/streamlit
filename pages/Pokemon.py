import requests
import streamlit as st

st.header("Pokemon")

pokemons = ["charizard", "eevee", "snorlax", "garchomp", "lucario"]
pokemon = st.selectbox("Select a Pokemon", pokemons)

if pokemon:
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()
    for img in r["sprites"].values():
        if img is not None:
            if str(img)[-4:] == ".png":
                st.image(img)
