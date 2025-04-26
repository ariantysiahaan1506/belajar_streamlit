import numpy as np
import streamlit as st
import pandas as pd


def tampilkan_tentang_saya():
    st.markdown("*My name* is **Arianty Siahaan** ***Data Analyst Enthuasiast***.")
    st.markdown("\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''I am a Biostatistician with specialized 
    expertise in data analysis. With proven 
    experience in data entry, cleaning, merging, 
    analysis, storytelling, and action planning. I have contributed to impactful initiatives at reputable organizations, including BKKBN, Yayasan KNCV Indonesia, Dinas Kesehatan DKI Jakarta, and Save the Children Indonesia. Passionate about the field of data, I bring 4+ years of experience as a Data Officer/Analyst, specializing in managing and analyzing large datasets to generate actionable insights. I am proficient in tools such as Python, SQL, Power BI, Tableau, Excel, SPSS, STATA, and QGIS, with a strong ability to transform complex data into meaningful outcomes. Highly motivated and adaptable, I thrive in collaborative environments with diverse teams, leveraging data to solve real-world problems and drive positive change..
    '''
    st.markdown(multi)