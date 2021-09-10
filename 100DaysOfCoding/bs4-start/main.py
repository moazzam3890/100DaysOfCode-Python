from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
texts = [article_tag.getText() for article_tag in articles]
links = [article_tag.get("href") for article_tag in articles]
upvotes = [int(upvotes.string.split()[0]) for upvotes in soup.find_all(name="span", class_="score")]

highest_votes = max(upvotes)
highest_index = upvotes.index(highest_votes)
print(highest_votes)
# print(highest_index)
article_name = texts[highest_index]
article_link = links[highest_index]
print(article_name)
print(article_link)
# print(texts)
# print(links)
# print(upvotes)


list_of_span_tags = soup.find_all(name="span", class_="score")
# print(list_of_span_tags)
points_list = []
for value in list_of_span_tags:
    # print(value.string)
    points = value.string
    points_list.append(points)

# with open("website.html") as file:
#     data = file.read()
# # Creating a soup from data from file.
# soup = BeautifulSoup(data, "html.parser")
# # printing title tag.
# print(soup.title)
# # printing name of title tag.
# print(soup.title.name)
# # print data inside title tag.
# print(soup.title.string)
# # formatting soup.
# print(soup.prettify())
# # printing all anchor tags.
# print(soup.a)
# # printing all lists.
# print(soup.li)
# # returning all anchor tags in a list
# all_anchors = soup.find_all(name="a")
# # looping through anchor tags lists.
# for tag in all_anchors:
#     # printing content inside anchor tag.
#     print(tag.getText())
#     # printing link inside anchor tag.
#     print(tag.get("href"))
# # returning h1 tan with id name.
# heading1 = soup.find(name="h1", id="name")
# print(heading1)
# # returning h3 tag with class heading,
# heading3 = soup.find(name="h3", class_="heading")
# print(heading3)
# # returning all tags with id name.
# h1 = soup.select_one(selector="#name")
# print(h1)
# # returning all tags with class heading.
# h3 = soup.select(selector=".heading")
# print(h3)
# # returning all anchor tags inside p (paragraph)
# a_inside_p = soup.select(selector="p a")
# print(a_inside_p)
