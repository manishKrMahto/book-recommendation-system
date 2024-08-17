# Book Recommendation System

This project is a Book Recommendation System that uses collaborative filtering to recommend books based on user ratings. The system also showcases the top 50 trending books based on average ratings. The project is built using **Python, pandas, scikit-learn, and Streamlit** for the web interface.

## Features

- **Top 50 Trending Books:** Displays the top 50 books based on their average ratings.
- **Book Recommendation:** Recommends similar books based on a selected book using collaborative filtering (cosine similarity).

## Datasets

The system uses two main datasets:
- **Books.csv:** Contains book information such as ISBN, title, author, and image URLs.
- **Ratings.csv:** Contains user ratings for various books.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/manishKrMahto/book-recommendation-system.git
   cd book-recommendation-system
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the dataset files are in the correct path as specified in the code.**

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. The web interface will provide two main options:
   - **Top 50 Trending Books:** View the most popular books based on average ratings.
   - **Book Recommendation:** Select a book to get recommendations for similar books.

## Implementation Details

### 1. **Data Loading and Preprocessing**
   - Datasets are loaded using pandas.
   - Books and ratings are merged to create a unified dataset.
   - Users who have given more than 100 ratings and books with more than 50 ratings are filtered for better recommendations.

### 2. **Top 50 Trending Books**
   - Books are ranked based on their average ratings.
   - The top 50 books are displayed along with their title, author, and a medium-sized image.

### 3. **Collaborative Filtering**
   - A pivot table is created with books as rows and users as columns, where the cell values represent the ratings.
   - Cosine similarity is calculated between books to find similar ones.
   - The system recommends books that are most similar to the selected book.

### 4. **Streamlit Web Interface**
   - **show_trending_books:** Displays the top 50 trending books with images and ratings.
   - **recommend_books:** Recommends books similar to the selected book.

## Known Issues

- Some images might fail to load due to restrictions on certain URLs. ***(status code = 403)***

## Reference

- **YouTube Video by CampusX (Nitish Singh Sir):** [Building a Book Recommendation System](https://www.youtube.com/watch?v=1YoD0fg3_EM&t=3243s)
