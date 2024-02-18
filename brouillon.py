""""""""""""





""""""""""""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly as px
import joblib
from PIL import Image
import base64
import plotly.graph_objects as go
import plotly.express as px
import altair as alt
from forex_python.converter import CurrencyRates

# Récupération du taux d'échange
# Créer une instance de CurrencyRates
devise_currency = CurrencyRates()

# Obtenir le taux de change de l'USD vers l'EUR
def usd_to_eur():
    exchange_rate = devise_currency.get_rate('USD', 'EUR')
    return exchange_rate



st.set_page_config(
    page_title="CryptoCourse Coin",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
 
# Inclure les styles CSS personnalisés
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Chargez l'image de votre logo
logo = Image.open("img/cc_logo.png")

st.title("CyptoCoin Course")
st.subheader("Application web pour la prédiction du cours du Bitcoin")



# Affichez l'image dans votre application Streamlit
st.sidebar.image(logo, width=120)

# st.title("CryptoCoin Course")
# st.subheader("Application de prédiction du cours du Bitcoin")

# # # Chargement du modèle
# model = joblib.load(filename="crypto_course.joblib")

# btc_data = joblib.load(filename="btc_dataset.joblib")
# prediction = joblib.load(filename="prediction.joblib")

# new_df = pd.DataFrame(data = btc_data.loc[prediction.iloc[0].index:prediction.iloc[-1].index]['Close'], index=btc_data.index)

# # st.write(prediction)












# # Ouvrez l'image
# image = Image.open('cc_logo.png')

# # Affichez l'image dans la barre latérale (qui est à gauche par défaut)
# st.sidebar.image(image, use_column_width=True)




# # Fonction pour obtenir la base64 d'un fichier
# # def get_base64_of_bin_file(bin_file):
# #     with open(bin_file, 'rb') as f:
# #         data = f.read()
# #     return base64.b64encode(data).decode()

# # # Fonction pour construire le balisage pour l'image
# # def build_markup_for_image(png_file):
# #     binary_string = get_base64_of_bin_file(png_file)
# #     return """
# #     <style>
# #     .reportview-container .main .block-container {
# #         position: relative;
# #     }
# #     .reportview-container .main .block-container::before {
# #         content: '';
# #         position: absolute;
# #         top: 2px;
# #         left: 2px;
# #         background: url("data:image/png;base64,%s");
# #         background-repeat: no-repeat;
# #         width: 20px;  /* Ajustez la largeur de l'image */
# #         height: 100px;  /* Ajustez la hauteur de l'image */
# #     }
# #     </style>
# #     """ % binary_string

# # # Fonction pour ajouter l'image
# # def add_image(png_file):
# #     image_markup = build_markup_for_image(png_file)
# #     st.markdown(image_markup, unsafe_allow_html=True)

# # # Utilisez la fonction pour ajouter une image locale
# # add_image("cc_logo.png")


# # Création d'un objet Figure
# fig = go.Figure()

# # Ajout de la première série
# fig.add_trace(go.Scatter(
#     x=btc_data.index,  # Dates en abscisse
#     y=new_df['Close'],  # Valeurs de la première série
#     mode='lines',
#     name='Valeurs vraies'
# ))

# # Ajout de la deuxième série
# fig.add_trace(go.Scatter(
#     x=btc_data.index,  # Dates en abscisse
#     y=prediction['Close'],  # Valeurs de la deuxième série
#     mode='lines',
#     name='Valeurs prédites'
# ))

# # Affichage du graphique
# fig.show()

# Chargement des données
# Remplacez ceci par le chargement de vos propres données


# Carte (si les données contiennent des informations de localisation)
# st.header('Carte')

# st.map(df)

import streamlit as st

# Define the custom CSS
dropdown_style = """
<style>
div[role="listbox"] ul {
    background-color: #f2f2f2;
    color: blue;
    font-size: 16px;
}
</style>
"""

# Apply the custom CSS to the dropdown menu
st.markdown(dropdown_style, unsafe_allow_html=True)

# Create the dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an option", options)
st.write("You selected: ", selected_option)



import streamlit as st

# Définir le texte à afficher
texte_déroulant = """
<span style="color: green">Le titre</span> : Ceci est le texte que vous pouvez dérouler en cliquant sur la flèche.
"""

# Utiliser st.expander pour créer une flèche déroulante
with st.sidebar.expander("Cours du Bitcoin"):
    st.markdown(texte_déroulant, unsafe_allow_html=True)


with st.expander("Titre du conteneur"):
    df = pd.read_csv('BTC-USD_complet.csv')
    df['Date'] = pd.to_datetime(df['Date'],)

    # Titre de l'application
    st.title('Mon Tableau de Bord')

    # Affichage des données brutes
    st.header('Données Brutes')
    st.write(df)

    # Histogramme
    st.header('Histogramme')
    # hist_values = st.sidebar.slider('Sélectionnez la plage de l\'histogramme', int(df['Date'].min()), int(df['Date'].max()), int((df['Date'].min())), int(df['Date'].max()))
    hist_bins = st.sidebar.number_input('Nombre de bacs', 5, 50, 20)
    selected_column = st.sidebar.selectbox('Sélectionnez une colonne', df.columns)
    # st.hist(df[selected_column], bins=hist_bins, range=hist_values)

    # Diagramme de dispersion
    st.header('Diagramme de Dispersion')
    x_axis = st.selectbox('Sélectionnez la variable pour l\'axe des x', df.columns)
    y_axis = st.selectbox('Sélectionnez la variable pour l\'axe des y', df.columns)
    st.plotly_chart(px.scatter(df, x=x_axis, y=y_axis))


# Utiliser st.markdown() avec du HTML pour changer la couleur du texte
st.markdown('', unsafe_allow_html=True)



# Utiliser st.write() pour placer les checkboxes sur une même ligne
st.write("Sélectionnez les options:")
st.write((st.checkbox("Option 1"), st.checkbox("Option 2"), st.checkbox("Option 3")))


