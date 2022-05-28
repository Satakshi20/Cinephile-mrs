import pickle
import streamlit as st
import requests
import pandas as pd


#Website configuration
st.set_page_config(
     page_title="Cinephile",
     page_icon="❄",
     layout="wide",
     initial_sidebar_state="collapsed",
)

page_bg_img = '''
          <style>
                .stApp {
            background-image: url("https://media.istockphoto.com/photos/gray-and-red-speed-abstract-technology-background-picture-id1219543826?b=1&k=20&m=1219543826&s=170667a&w=0&h=Ef94L2JpxXupPMkEiAbFsPniEeRDLxKfGVq-KT2sDkg=");
            background-size: cover;
          }
          </style>
          '''

st.markdown(page_bg_img, unsafe_allow_html=True)



def fetch_poster (id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []


    for i in distances[1:8]:
        # fetch the movie poster
        id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters



col1, mid = st.columns([1,1])
with col1:
     st.image('logo_website.png', width=300)


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie = st.selectbox(
      "Type or select a movie from the dropdown",
       movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

        with col6:
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
            with col7:
                st.text(recommended_movie_names[6])
                st.image(recommended_movie_posters[6])


# ---- CONTACT SECTION ----
with st.container():
    st.write("---")
    st.header("Contact")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/satakshisingh360@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    # Using local CSS File

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")



# ---- ABOUT SECTION----
with st.container():
    st.write("---")
    st.header("About")
    st.write("This website is made by **Satakshi Singh** under the mentorship of Microsoft.")




