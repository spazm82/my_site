import streamlit as st



RELEASES = [{'photo': "photo/1.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/kS37UZEjHnA7Jg",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/Vc04a",
             'icon_button': "🎵"},
             {'photo': "photo/2.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/ZrVmO0c002IC_Q",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/VOIBM",
             'icon_button': "🎵"},
             {'photo': "photo/3.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/ekp-e6qfEQoeVA",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/uc3qM",
             'icon_button': "🎵"},
             {'photo': "photo/4.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/oWc_cEhxYabZtA",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/LYSJX",
             'icon_button': "🎵"},
             {'photo': "photo/5.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/yKf5IFXCDGK0jA",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/pFjS1",
             'icon_button': "🎵"},
             {'photo': "photo/6.jpg",
             'audio_ya_link': "https://disk.yandex.ru/d/BaXC8oNIPwCOqA",
             'format_audio': "audio/mpeg",
             'button_name': "Слушать на стриминговых площадках",
             'url_button': "https://band.link/xp6Oi",
             'icon_button': "🎵"},
            ]

PHOTO_PRE = ["photo/8318.jpg", "photo/8320.jpg"]
PHOTO_POST = ["photo/18.jpeg", "photo/15.jpeg"]
BUTTONS_SOC = [["Карточка музыканта на VK", "https://vk.ru/artist/spazm82", ":material/recommend:"],
                ["Карточка музыканта на Яндекс.Музыка", "https://music.yandex.ru/artist/25824937", ":material/recommend:"],
                ["Карточка музыканта на 4beat", "https://4beat.ru/id13934", ":material/recommend:"]
            ]
BUTTONS_FRIENDS = [["VK замечательного фотографа Евгения Фазлеева", "https://vk.ru/club185811187", ":material/recommend:"],
                   ["Организация концертов Live Progect | Миасс", "https://vk.ru/liveproject_miass", ":material/recommend:"]    
                ]

st.markdown('<meta name="referrer" content="no-referrer" />', unsafe_allow_html=True)

def releases(photo: str, audio_ya_link: str, format_audio: str, 
              button_name: str, url_button: str, icon_button: str):
    st.image(photo)
    #direct_audio_url = f"https://getfile.dokpub.com/yandex/get/{audio_ya_link}"
    #st.audio(direct_audio_url, format=format_audio)
    st.link_button(button_name, url=url_button, icon=icon_button)

def photos(photo_list: list):
    col1, col2 = st.columns(2)
    with col1:
        st.image(photo_list[0])
    with col2:
        st.image(photo_list[1])

def buttons(button_list: list):
  for chek_list in button_list:
        if len(chek_list) == 3:
            col1, col2, col3 = st.columns(3)
            for buttons in chek_list:
                with col1:
                    st.link_button(buttons[0][0], url=buttons[0][1], icon=buttons[0][2])
                with col2:
                    st.link_button(buttons[1][0], url=buttons[1][1], icon=buttons[1][2])
                with col3:
                    st.link_button(buttons[2][0], url=buttons[2][1], icon=buttons[2][2])
        elif len(chek_list) == 2:
            col1, col2 = st.columns(2)
            for buttons in chek_list:
                with col1:
                    st.link_button(buttons[0][0], url=buttons[0][1], icon=buttons[0][2])
                with col2:
                    st.link_button(buttons[1][0], url=buttons[1][1], icon=buttons[1][2])
        else:
            st.link_button(button_list[0], url=button_list[1], icon=button_list[2])

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
    buttons(BUTTONS_SOC)
    # Ссылка на радио LP
    buttons([["Радио LP где можно заказать мои релизы к прослушиванию", "https://radio.lp-media.ru/", ":material/radio:"]])
    st.divider()

    # Раздел с фото
    photos(PHOTO_PRE)
    st.divider()

    # Раздел с музыкой
    with st.container():
        for releas in RELEASES:
            releases(releas['photo'], releas['audio_ya_link'],
            releas['format_audio'], releas['button_name'],
            releas['url_button'], releas['icon_button'])

            st.divider()
        
        st.image("photo/7.jpg")
        st.write("Выходит 03 августа 2026.")
        st.link_button("Можно сделать пресейв, чтобы точно не пропустить выход релиза!",
                        url="https://band.link/Sj9uI",
                        icon="🎵"
                    )

        st.divider()

    # Раздел с фото
    photos(PHOTO_POST)
    st.divider()

    # Раздел на ссылки друзей
    buttons(BUTTONS_FRIENDS)


go_streamlit()
