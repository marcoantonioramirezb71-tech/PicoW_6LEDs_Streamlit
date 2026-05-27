import streamlit as st

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="Control 6 LEDs Pico W",
    layout="centered"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.main{
    background-color:#EAEAEA;
}

.block-container{
    max-width:900px;
    padding-top:1rem;
}

.titulo{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#008080;
}

.subtitulo{
    text-align:center;
    font-size:18px;
}

.panel{
    background:white;
    padding:25px;
    border-radius:15px;
    border:1px solid #BDBDBD;
}

.led_on{
    width:60px;
    height:60px;
    border-radius:50%;
    background-color:#00FF00;
    margin:auto;
    box-shadow:0px 0px 20px #00FF00;
}

.led_off{
    width:60px;
    height:60px;
    border-radius:50%;
    background-color:#404040;
    margin:auto;
}

.estado{
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ==========================================
# VARIABLES SESSION
# ==========================================

if "leds" not in st.session_state:

    st.session_state.leds=[0]*6

# ==========================================
# TITULO
# ==========================================

st.markdown(
    """
    <div class='titulo'>
    Raspberry Pi Pico W
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitulo'>
    Control de 6 LEDs
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

# ==========================================
# PANEL
# ==========================================

st.markdown(
    "<div class='panel'>",
    unsafe_allow_html=True
)

# ==========================================
# LEDS
# ==========================================

for i in range(6):

    col1,col2,col3=st.columns([1,1,1])

    with col1:

        st.markdown(
            f"### LED {i}"
        )

    with col2:

        if st.session_state.leds[i]:

            st.markdown(
                "<div class='led_on'></div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                "<div class='led_off'></div>",
                unsafe_allow_html=True
            )

    with col3:

        c1,c2=st.columns(2)

        with c1:

            if st.button(
                "ON",
                key=f"on{i}"
            ):

                st.session_state.leds[i]=1

        with c2:

            if st.button(
                "OFF",
                key=f"off{i}"
            ):

                st.session_state.leds[i]=0

    estado="ENCENDIDO" if st.session_state.leds[i] else "APAGADO"

    st.markdown(
        f"""
        <div class='estado'>
        {estado}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

# ==========================================
# BOTONES GENERALES
# ==========================================

a,b=st.columns(2)

with a:

    if st.button(
        "ENCENDER TODOS"
    ):

        st.session_state.leds=[1]*6

        st.rerun()

with b:

    if st.button(
        "APAGAR TODOS"
    ):

        st.session_state.leds=[0]*6

        st.rerun()

st.markdown(
    "</div>",
    unsafe_allow_html=True
)