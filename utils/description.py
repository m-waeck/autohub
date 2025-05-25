# services/description.py

def create_message(car_model, car_year, car_specials):
    message = (
        f"Beschreibe das Auto {car_model} aus dem Jahr {car_year} in einem kurzen Fließtext auf Deutsch. "
        f"Der Text soll maximal 8 Sätze enthalten, positiv klingen und die Vorteile des Autos hervorheben. "
        f"Erwähne nicht das Baujahr. Verwende nicht immer die gleichen Formulierungen, "
        f"aber achte darauf, dass der Text verständlich bleibt."
    )
    if car_specials:
        message += f" Beachte folgende Besonderheiten und gehe darauf ein: {car_specials}"
    return message
