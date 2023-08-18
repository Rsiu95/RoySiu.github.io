from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_list = response.text
soup = BeautifulSoup(movie_list, "html.parser")

movies = []
movie_title = soup.find_all(name = "h3", class_="title")
for movie in movie_title:
    movies.append(movie.getText())
movies = movies[::-1]
print(movies)

with open("./Udemy 100 Days of Code/Day 45/movies.txt", "w", encoding = "utf-8") as movie_data:
    for movie in movies:
        movie_data.write(movie + "\n")

# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')

# article_titles = []
# article_links = []
# for article_tag in soup.find_all(name="span", class_="titleline"):
#     article_titles.append(article_tag.getText())
#     article_links.append(article_tag.find("a")["href"])

# article_upvotes = []
# for article in soup.find_all(name="td", class_="subtext"):
#     if article.span.find(class_="score") is None:
#         article_upvotes.append(0)
#     else:
#         article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# max_points_index = article_upvotes.index(max(article_upvotes))
# print(
#     f"{article_titles[max_points_index]}, "
#     f"{article_upvotes[max_points_index]} points, "
#     f"available at: {article_links[max_points_index]}."
# )


# with open('./Udemy 100 Days of Code/Day 45/website.html', encoding = 'utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup)
# for tag in soup.find_all("a"):
#     print(tag.get("href"))

# heading = soup.find(name = "h1", id = "name")
# print(heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#")

# headings = soup.select(".heading")