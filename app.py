# src/app.py

import streamlit as st
from datetime import datetime

from config import DEFAULT_AI_MODEL, MODEL_CONFIG, IMAGE_PATH
from database.mongo import fetch_items, add_new_document
from utils.description import create_message


def main():
    st.sidebar.header("Projekt von Marvin Wäcker")
    st.sidebar.markdown("[GitHub](https://github.com/m-waeck)")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/marvin-waecker/)")

    selected_model = st.sidebar.radio("Sprachmodell auswählen", list(MODEL_CONFIG.keys()), index=DEFAULT_AI_MODEL)
    model_data = MODEL_CONFIG.get(selected_model)

    if not model_data:
        st.error("Ungültiges Modell.")
        return

    get_response = model_data["func"]
    api_key = st.secrets[model_data["secret_section"]]["key"]
    ai_model = model_data["model"]

    st.image(IMAGE_PATH)
    st.title("Text-Generierung mittels KI")
    st.write((f"Mit diesem Tool lassen sich Texte generieren, die von einer KI geschrieben wurden "
              f"und in wenigen Sätzen ein bestimmtes Auto beschreiben."))
    st.markdown("<br>", unsafe_allow_html=True)

    st.header("Beschreibungstext generieren")
    car_model = st.text_input("Modelbezeichnung:", "Fiat Multipla")
    car_year = st.text_input("Baujahr:", "2001")
    car_specials = st.text_input("Besonderheiten:", "Keine")

    if st.button("Generieren"):
        car_descr = ""
        word_count = 999
        print(f"Generating description using model {ai_model} for {car_model} ({car_year})...")
        while word_count > 160:
            prompt = create_message(car_model, car_year, None if car_specials == "Keine" else car_specials)
            car_descr = get_response(prompt, False, api_key, ai_model)
            word_count = len(car_descr.split())
            print(f"Text generated with {word_count} words.")

        now = datetime.now()
        add_new_document({
            "date": now.strftime('%d-%m-%Y'),
            "time": now.strftime('%H:%M:%S'),
            "model": car_model,
            "year": int(car_year),
            "specials": None if car_specials == "Keine" else car_specials,
            "descr": car_descr,
            "ai_model": ai_model
        })

    items = fetch_items()
    if items:
        st.header("Generierte Beschreibungen")
        for i, car in enumerate(reversed(items)):
            if i > 9: break
            ad_title = f"{car['model']}, Baujahr: {car['year']}"
            st.subheader(ad_title)
            car_readable_ai_model_name = next((key for key, value in MODEL_CONFIG.items() if value['model'] == car['ai_model']), "Unbekannt")
            st.write(f"{car['date']}  |  {car['time']} Uhr  |  {car_readable_ai_model_name}")
            st.write(car["descr"])
            if car["specials"]:
                st.write(f"Besonderheiten: {car['specials']}")
    else:
        st.warning("Keine Fahrzeuge gefunden.")

if __name__ == "__main__":
    main()
