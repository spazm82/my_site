import streamlit as st



st.markdown('<meta name="referrer" content="no-referrer" />', unsafe_allow_html=True)

def go_streamlit():
    # Задаём название на вкладке Браузера
    st.set_page_config(
        page_title="Сайт музыканта и композитора Мезенцева Александра",
    )
    # Убираем "Сэндвич"-меню на вкладке
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.sidebar.header("""**Рад Вас приветствовать на моём сайте!**\nМеня зовут **Мезенцев Александр**. В своё свободное время я пишу музыку и песни, а мой
                      сценический псевдоним **spazm82**.\nКак песни, так и музыка пишется мной в разных жанрах. Настолько разных, что даже как-то объединить\nих по какому-то одному
                      направлению просто не возможно! От зубодоробительной смеси "тяжёлой" музыки, до миролюбивой "попсятинки".\nДобро пожаловать
                      в гости к **spazm82**, дорогой друг!""")

    # Раздел с кнопками на карточки музыканта
    col_butt1, col_butt2, col_butt3 = st.columns(3)
    with col_butt1:
        st.link_button("Карточка музыканта на VK", url="https://vk.ru/artist/spazm82", icon=":material/recommend:")
    with col_butt2:
        st.link_button("Карточка музыканта на Яндекс.Музыка", url="https://music.yandex.ru/artist/25824937", icon=":material/recommend:")
    with col_butt3:
        st.link_button("Карточка музыканта на 4beat", url="https://4beat.ru/id13934", icon=":material/recommend:")
    # Ссылка на радио LP
    st.link_button("Радио LP где можно заказать мои релизы к прослушиванию", url="https://radio.lp-media.ru/", icon=":material/radio:")

    st.divider()

    # Раздел с фото
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo/8318.jpg")
    with col2:
        st.image("photo/8320.jpg")

    st.divider()

    # Раздел с музыкой
    with st.container():
        st.image("photo/1.jpg")
        yandex_disk_url_1 = "https://disk.yandex.ru/d/kS37UZEjHnA7Jg"
        direct_audio_url_1 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_1}"
        st.audio(direct_audio_url_1, format="audio/mpeg")

        st.image("photo/2.jpg")
        yandex_disk_url_2 = "https://disk.yandex.ru/d/ZrVmO0c002IC_Q"
        direct_audio_url_2 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_2}"
        st.audio(direct_audio_url_2, format="audio/mpeg")

        st.image("photo/3.jpg")
        yandex_disk_url_3 = "https://disk.yandex.ru/d/ekp-e6qfEQoeVA"
        direct_audio_url_3 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_3}"
        st.audio(direct_audio_url_3, format="audio/mpeg")

        st.image("photo/4.jpg")
        yandex_disk_url_4 = "https://disk.yandex.ru/d/oWc_cEhxYabZtA"
        direct_audio_url_4 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_4}"
        st.audio(direct_audio_url_4, format="audio/mpeg")

        st.image("photo/5.jpg")
        yandex_disk_url_5 = "https://disk.yandex.ru/d/yKf5IFXCDGK0jA"
        direct_audio_url_5 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_5}"
        st.audio(direct_audio_url_5, format="audio/mpeg")

        st.image("photo/6.jpg")
        yandex_disk_url_6 = "https://disk.yandex.ru/d/BaXC8oNIPwCOqA"
        direct_audio_url_6 = f"https://getfile.dokpub.com/yandex/get/{yandex_disk_url_6}"
        st.audio(direct_audio_url_6, format="audio/mpeg")


go_streamlit()
