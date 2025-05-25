# database/mongo.py
import streamlit as st
from pymongo import MongoClient

DB = "autohalle"
COLL = "cars"
CONN_STR = st.secrets["mongodb"]["mongoURI"]

def connect():
    try:
        return MongoClient(CONN_STR)
    except Exception as e:
        st.error(f"Fehler bei der Verbindung zur Datenbank: {e}")
        return None

def fetch_items():
    client = connect()
    if client:
        return list(client[DB][COLL].find())
    return []

def add_new_document(doc):
    client = connect()
    if client:
        client[DB][COLL].insert_one(doc)
