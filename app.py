import streamlit as st
import requests

# ==========================================
# IP PICO W
# ==========================================

PICO_IP="192.168.1.50"

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Pico W LEDs"
)

# ==========================================
# SESSION
# ==========================================

if "leds" not in st.session_state:

    st.session_state.leds=[0]*6

# ==========================================
# TITULO
# ==========================================

st.title(
    "Control LEDs Raspberry Pi Pico W"
)

# ==========================================
# LEDS
# ==========================================

for i in range(6):

    st.subheader(f"LED {i}")

    c1,c2=st.columns(2)

    # ======================================
    # ON
    # ======================================

    with c1:

        if st.button(
            f"ON {i}"
        ):

            try:

                requests.get(
                    f"http://{PICO_IP}/led{i}/on"
                )

                st.session_state.leds[i]=1

            except:

                st.error(
                    "Error conexión Pico W"
                )

    # ======================================
    # OFF
    # ======================================

    with c2:

        if st.button(
            f"OFF {i}"
        ):

            try:

                requests.get(
                    f"http://{PICO_IP}/led{i}/off"
                )

                st.session_state.leds[i]=0

            except:

                st.error(
                    "Error conexión Pico W"
                )

    estado="ON" if st.session_state.leds[i] else "OFF"

    st.write(
        "Estado:",
        estado
    )