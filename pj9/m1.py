import streamlit as st
st.set_page_config(page_title='',page_icon='question:', layout='wide')
title=st.empty()
title.title('Chọn con vật bạn thích')

col1,col2,col3,col4,col5=st.columns(5)
col1_2,col2_2=st.columns([3,1])
with col1:
    bt1=st.button('Chó sói')
with col2:
    bt2=st.button('Voi')
with col3:
    bt3=st.button('Đại bàng')
with col4:
    bt4=st.button('Cá voi')
with col5:
    bt5=st.button('Sư tử')
if bt1:
    title.title('Bạn đã chọn con chó sói')
    with col1_2:
        st.write('Âm thanh')
        st.audio('pj9/sound/sosi.mp3',format='mp3')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=RvxgZznvy9k&pp=ygUEc8OzaQ%3D%3D',format='mp4/video')
    with col2_2:    
        st.write('Hình ảnh')
        st.image('pj9/image/sosi.jpg')
if bt2:
    title.title('Bạn đã chọn con voi')
    with col1_2:
        st.write('Âm thanh')
        st.audio('pj9/sound/voi.mp3',format='mp3')
    
        st.write('Video')
        st.video('https://www.youtube.com/watch?v=-8Nt1BAG4Sc&pp=ygUDdm9p',format='mp4/video')
    with col2_2:    
        st.write('Hình ảnh')
        st.image('pj9/image/voi.jpg')
if bt3:
    title.title('Bạn đã chọn con đại bàng')
    with col1_2:
        st.write('Âm thanh')
        st.audio('pj9/sound/daibang.mp3',format='mp3')
        st.write('Video')
        st.video('https://www.youtube.com/watch?v=cSLrA3udmKo&pp=ygUMxJHhuqFpIGLDoG5n',format='mp4/video')
    with col2_2:    
        st.write('Hình ảnh')
        st.image('pj9/image/daibang.jpg')
if bt4:
    title.title('Bạn đã chọn con cá voi')
    with col1_2:
        st.write('Âm thanh')
        st.audio('pj9/sound/cavoi.mp3',format='mp3')
        st.write('Video')
        st.video('https://www.youtube.com/watch?v=e1pFMirzG8g&pp=ygUHY8OhIHZvaQ%3D%3D',format='mp4/video')
    with col2_2:    
        st.write('Hình ảnh')
        st.image('pj9/image/cavoi.jpg')
if bt5:
    title.title('Bạn đã chọn con sư tử')
    with col1_2:
        st.write('Âm thanh')
        st.audio('pj9/sound/sutu.mp3',format='mp3')
    
        st.write('Video')
        st.video('https://www.youtube.com/watch?v=oWc3_C4EtbQ&pp=ygUIc8awIHThu60%3D',format='mp4/video')
    with col2_2:    
        st.write('Hình ảnh')
        st.image('pj9/image/sutu.jpg')

