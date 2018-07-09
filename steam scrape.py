from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

my_url = "https://store.steampowered.com/tags/en/Massively%20Multiplayer/"

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

new_release = page_soup.find("div", id = "NewReleasesRows")
contents = new_release.findAll("a")
for content in contents:
        nm = content.findAll("div", {"class":"tab_item_name"})
        name = nm[0].text
        disc = content.findAll("div", {"class":"discount_final_price"})
        discount = disc[0].text
        print("Name :"+name)
        print("Discount Price :"+discount)
        print("Tags :", end = " ")
        tags = content.findAll("span", {"class":"top_tag"})
        for each in tags:
                print(each.text, end = " ")

        print("\n")
