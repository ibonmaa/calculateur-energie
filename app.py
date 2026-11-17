
import streamlit as st

st.title("Calculateur énergétique")
st.write("Calcul des obligations énergétiques et des sanctions")

# Une seule fonction pour les deux carburants
def resultat(fossile: float, ENR: float, energie: str):
    if energie == "Gazole":
        taux = 9.5
    elif energie == "Essence":
        taux = 9.7

    tarif = 40

    gj = ((taux * fossile / 100) - ENR) * 3.3
    gwh = gj / 3600
    sanction = gwh * tarif

    return gwh, gj, sanction


# Choisir le carburant
energie = st.selectbox(
    "Choisissez le carburant :",
    ["Gazole", "Essence"]
)

# Entrer les valeurs
fossile = st.number_input(
    "Volume fossile (hL) :",
    min_value=0.0,
    value=0.0
)

ENR = st.number_input(
    "Volume ENR (hL) :",
    min_value=0.0,
    value=0.0
)

# Calcul
if st.button("Calculer"):
    gwh, gj, prix = resultat(fossile, ENR, energie)

    st.subheader("Résultats")

    st.write(f"Carburant : {energie}")
    st.write(f"Quantité restante : {gj:.2f} GJ")
    st.write(f"Quantité restante : {gwh:.2f} GWh")
    st.write(f"Montant de la sanction : {prix:.2f} €")
