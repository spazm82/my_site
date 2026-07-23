import streamlit as st



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
                      сценический псевдоним **spazm82**.\nКак песни, так имузыка пишется мной в разных жанрах. Настолько разных, что даже как-то объединить\nих по 
                      одному жанру и поджанрам просто не возможно! От зубодоробительной смеси "тяжёлых" направлений музыки, до миролюбивой "попсятинки".\nДобро пожаловать
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
        st.image("photo/155.jpg")
    with col2:
        st.image("photo/18.jpg")

    st.divider()

    # Раздел с музыкой
    with st.container():
        st.write("**Я не с тобою:**")
        st.audio("audio/spazm82 - Я не с тобою.mp3", format="audio/mp3", 
                 sample_rate=None, loop=False, autoplay=False)
        st.write("**Прямой дорогой в Ад:**")
        st.audio("audio/Прямой дорогой в Ад.mp3", format="audio/mp3", 
                 sample_rate=None, loop=False, autoplay=False)
        st.write("**Час расплаты:**")
        st.audio("audio/Час расплаты.mp3", format="audio/mp3",
                 sample_rate=None, loop=False, autoplay=False)
        st.write("**Последний рубеж:**")
        st.audio("audio/Последний рубеж(Инструментал).mp3", format="audio/mp3", 
                 sample_rate=None, loop=False, autoplay=False)
        st.write("**Неизбежно:**")
        st.audio("audio/Неизбежно.mp3", format="audio/mp3",
                 sample_rate=None, loop=False, autoplay=False)
        st.write("**Крылья бездорожья:**")
        st.audio("audio/Крылья бездорожья.mp3", format="audio/mp3",
                 sample_rate=None, loop=False, autoplay=False)


go_streamlit()
