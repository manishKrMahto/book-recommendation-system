import streamlit as st 
import pickle 
import pandas as pd
import numpy as np

# unpickling the objects
top_50_books = pickle.load(open('top_50_books.pkl' , 'rb'))
pivot_table = pickle.load(open('pivot_table.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))
books = pickle.load(open('books.pkl' , 'rb'))


def show_trending_books():
    st.header('Top 50 books')

    index = 0 # to iterate top_50_books index
    for row in range(10):  # for 10 rows
        col = st.columns(5) # in each row their is 5 columns

        # displaying the details ...
        for i in range (5):
            col[i].image(top_50_books.iloc[index]['Image-URL-M'])
            col[i].write(f'Title : {top_50_books.iloc[index]['Book-Title']}')
            col[i].write(f'Writer : {top_50_books.iloc[index]['Book-Author']}')
            col[i].write(f'Avg Rating : {round(top_50_books.iloc[index]['Avg-Rating'] , 2)}')
            index = index + 1


def recommend_books(book_name):
  index = np.where(pivot_table.index == book_name)[0][0] # fatchine index of given movie

  # creating a empty dataframe to concat each book details and return it 
  book_to_recommend = pd.DataFrame( columns = ['Book-Title' , 'Book-Author' , 'Image-URL-M'])

  # fetching top 6 close books of given books
  for movie_index in sorted(list(enumerate(similarity[index])) , reverse = True , key = lambda x : x[1])[1:6]:
    book_name = pivot_table.index[movie_index[0]]  # got book name

    # from book name fatching all the details 
    temp = books[books['Book-Title'] == book_name].drop_duplicates(subset='Book-Title')[['Book-Title' , 'Book-Author' , 'Image-URL-M']]

    # concating the book into empty dataframe
    book_to_recommend = pd.concat((book_to_recommend , temp))
  
  return book_to_recommend



def book_recommendation_option ():
    book_name = st.selectbox('Choose book' , pivot_table.index)
    # st.write(book_name)

    recommend = st.button('Recommend')

    if recommend:
        books_to_recommend = recommend_books(book_name)
  
        col = st.columns(5) 
        index = 0
        for i in range (5):
            col[i].image(books_to_recommend.iloc[index]['Image-URL-M'])
            col[i].write(f'Title : {books_to_recommend.iloc[index]['Book-Title']}')
            col[i].write(f'Writer : {books_to_recommend.iloc[index]['Book-Author']}')
            index = index + 1


if __name__ == '__main__':
    st.title("Book Recommendation System")
    st.warning('Here some Image is Failed to Load')

    status = st.selectbox("select option" ,('Top 50 Trending books' , 'Book Recommendation'))

    # st.write(status)
    if status  == 'Top 50 Trending books':
        show_trending_books()
    else :
        book_recommendation_option()