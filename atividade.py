
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geobr

gdf_estados = geobr.read_state()
gdf_municipios = geobr.read_municipality()

st.title('atividade proxima aula')

cidades = gdf_municipios['name_muni']
select = st.multiselect('Escolha os municipios ', cidades)

# GDF
fig, mapa = plt.subplots()

idx = gdf_municipios[gdf_municipios['name_muni'].isin(select)]
idx.plot(ax=mapa, color="b", alpha=1)
estados = gdf_estados[gdf_estados['abbrev_state'].isin(idx['abbrev_state'])]
estados.plot(ax=mapa, color='b', alpha=0.5)
 
st.pyplot(fig)
