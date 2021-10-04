import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import re
from dateutil import parser

main_df = pd.read_excel('29sep.xlsx', sheet_name='Sheet1')
ex_df = main_df[['NAME', 'Twitter']]
ex_df = ex_df.dropna(subset=['Twitter', 'NAME'])
# ex_df = ex_df.head(2)

listOfWords = ["Synopsis", "Vegan/plant based athlete", "Improved athletic performance",
               "Dairy and link to hormonal cancers", "environmental impact of diet",
               "dairy industry influence/marketing", "Switch for good", "Dairy-free", "dairyfree", "vegan",
               "plant-based", "non-dairy", "vegan athletes", "plant-based athletes", "lactose intolerance",
               "dairy sensitivity", "food sensitivity", "athlete nutrition", "Dotsie Bausch", "vegan Olympians",
               "vegan cheese", "nondairy milk", "inflammation", "workout recovery", "exercise recovery", "dairy-free",
               "how to go dairy-free", "dairy-free alternatives", "oat milk", "lactose intolerance",
               "am I lactose intolerant?", "will going plant-based help me lose weight?", "do I need more calcium?",
               "vegan athlete", "am I allergic to dairy", "best plant-based cheeses", "dairy vs soy",
               "dairy-free recipes", "dairy-free meal plan", "Dairy cows suffering", "plant milk protein",
               "best protein to build muscle", "Vegan diet deficiencies", "Where do we get B12",
               "Difference between dairy allergy and lactose intolerance", "Vegan athletes didn't start vegan",
               "Is milk or meat worse for you", "Do vegans need to take many supplements",
               "What is ethically sourced meat/dairy", "Eating meat and climate change", "What foods can I grow myself",
               "Side effects of going vegan", "Is vegan high carb", "Dairy-free nutrition", "Dairy-free recipes",
               "Dairy alternatives", "Cows milk alternatives", "Dairy pros and cons", "Non-dairy foods",
               "Dairy is bad for you", "Side-effects of milk", "Dairy health risk", "Dairy and health", "Ditch dairy",
               "Plant-based", "Healthy food", "Athletic performance", "No whey", "Dairy causes inflammation",
               "Inflammatory markers", "Dietary racism", "Improve health", "Improve the world", "Dairy-free athlete",
               "Dairy-free Olympian", "Dairy-free products", "Dairy-free companies", "Dairy allergies",
               "Milk allergies", "Dairy avoidance", "Milk avoidance"]

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
driver.maximize_window()

# open the webpage
driver.get("https://twitter.com/login")
time.sleep(5)


def i_flow_login():
    while "i/flow" in driver.current_url:
        time.sleep(5)

        check = driver.find_element_by_xpath(
            "(//div[@class='css-1dbjc4n r-1n7yuxj'])").text

        if 'first enter your phone' in check:
            username = driver.find_element_by_xpath(
                "(//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj "
                "r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu'])")
            username.click()
            time.sleep(5)
            username.send_keys('swapnilukey2251995@gmail.com')
            username.send_keys(Keys.ENTER)

        if 'There was unusual login activity' in check:
            username = driver.find_element_by_xpath(
                "(//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj "
                "r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu'])")
            username.click()
            time.sleep(5)
            username.send_keys('itsswaky')
            username.send_keys(Keys.ENTER)

        if 'Enter your password' in check:
            password = driver.find_element_by_xpath(
                "(//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj "
                "r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu'])")
            password.clear()
            password.send_keys('Sw@pnil2251995')
            time.sleep(5)
            password.send_keys(Keys.ENTER)
            time.sleep(5)


def login():
    # target username
    time.sleep(5)
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[username_or_email]']")))
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[password]']")))

    # enter username and password
    username.clear()
    username.send_keys('swapnilukey.sss@gmail.com')
    password.clear()
    password.send_keys('r(<#q#/TAT4*NsC')
    # r(<#q#/TAT4*NsC       swapnilukey.sss@gmail.com       @SwapnilUkey16
    # SwapnilUkey13       WysGz9uNXeJDema
    time.sleep(5)
    password.send_keys(Keys.ENTER)


if "i/flow" in driver.current_url:
    time.sleep(5)
    i_flow_login()
else:
    time.sleep(5)
    login()

# open new window with execute_script()
time.sleep(10)
driver.execute_script("window.open('');")
time.sleep(5)

# switch to new window with switch_to.window()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)


def profile_data():
    name_of_lead = driver.find_element_by_xpath("(//div[@class='css-1dbjc4n r-6gpygo r-14gqq1x'])").text.replace('\n',
                                                                                                                 ' ')

    intro_lead = driver.find_element_by_xpath("(//div[@class='css-1dbjc4n r-1adg3ll r-6gpygo'])").text.replace('\n',
                                                                                                               ' ')

    loc_lead = driver.find_elements_by_xpath("(//div[@class='css-1dbjc4n r-1adg3ll r-6gpygo'])")[-1].text.replace('\n',
                                                                                                                  ' ')

    follower_lead = driver.find_elements_by_xpath("(//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj'])")[
        -1].text.replace('\n', ' ')

    return tuple((name_of_lead, intro_lead, loc_lead, follower_lead))


def move_scroll_reply():
    replay_in_list = []
    while True:
        time.sleep(4)
        replay_in_list.append(post_replay_text_scrap())
        page_ht_bef = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        page_ht_aft = driver.execute_script("return document.body.scrollHeight")
        replay_in_list.append(post_replay_text_scrap())

        if page_ht_bef == page_ht_aft:
            break

        post_date_lead = driver.find_elements_by_xpath("(//time)")[-1].text.replace('\n', ' ')

        date = parser.parse(post_date_lead)
        today = date.today()
        delta = (today - date).days

        if delta > 365:
            break
    return replay_in_list


def move_scroll():
    a_in_list = []
    while True:
        time.sleep(6)
        a_in_list.append(temp_a_list())
        page_ht_bef = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)
        page_ht_aft = driver.execute_script("return document.body.scrollHeight")
        a_in_list.append(temp_a_list())
        # print(a_in_list)
        if page_ht_bef == page_ht_aft:
            break

        post_date_lead = driver.find_elements_by_xpath("(//time)")[-1].text.replace('\n', ' ')

        date = parser.parse(post_date_lead)
        today = date.today()
        delta = (today - date).days

        if delta > 365:
            break

    return a_in_list


def in_bet_login_click():
    time.sleep(5)
    finder_login_btn = driver.find_element_by_xpath(
        "(//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'])")
    finder_login_btn.click()

    time.sleep(5)
    if "i/flow" in driver.current_url:
        time.sleep(5)
        i_flow_login()
    else:
        time.sleep(5)
        login()

    pass

    return True


def in_between_login():
    time.sleep(5)
    try:
        finder_login_pop = driver.find_element_by_xpath(
            "(//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep r-rthrr5'])").text.replace('\n', ' ')
        if 'Don’t miss what’s happening People on Twitter' in finder_login_pop:
            in_bet_login_click()
    except:
        pass

    return True


def temp_a_list():
    posts_links = []
    try:
        time.sleep(3)
        posts_lead_links = driver.find_elements_by_xpath(
            "(//a[@class='css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0'])")
        for links in posts_lead_links:
            posts_links.append(links.get_attribute('href'))
    except:
        pass
    return posts_links


# posts_lead_links = driver.find_element_by_tag_name("section").text.replace('\n', ' ')


def post_text_scrap():
    posts_lead = []
    try:
        posts_lead = driver.find_element_by_tag_name("article").text.replace('\n', ' ')
    except:
        pass
    return posts_lead


def post_replay_text_scrap():
    replay_list = []
    try:
        replay_list = driver.find_element_by_tag_name("section").text.replace('\n', ' ')
    except:
        pass
    return replay_list


post_scrap = []
replay_scrap = []

pro_data = []
name = []
twitter = []

for (l, n) in zip(ex_df.Twitter, ex_df.NAME):
    try:
        print(l + ' link with name : ' + n + ' Is Starting')
        driver.get(l)
        # driver.get('https://twitter.com/katyared')
        time.sleep(5)
        link_of_post = move_scroll()
        link_of_post1 = [item for elem in link_of_post for item in elem]
        link_of_post1 = list(set(link_of_post1))

        if not link_of_post1:
            in_between_login()

            driver.get(l)
            time.sleep(5)
            link_of_post = move_scroll()
            link_of_post1 = [item for elem in link_of_post for item in elem]
            link_of_post1 = list(set(link_of_post1))

        elif link_of_post1:
            name.append(n)
            twitter.append(l)
            pro_data.append(profile_data())
            dummy_post = []
            dummy_reply = []
            count = 0
            for d_l in link_of_post1:
                count = count + 1
                print(str(count) + ' out of : ' + str(len(link_of_post1)))

                time.sleep(5)
                driver.get(d_l)

                time.sleep(5)
                post_ = post_text_scrap()
                print(post_)

                reply_ = move_scroll_reply()
                reply_ = [item for elem in reply_ for item in elem]
                reply_ = list(set(reply_))
                print(reply_)

                dummy_post.append(post_)
                dummy_reply.append(reply_)

            post_scrap.append(dummy_post)
            replay_scrap.append(dummy_reply)

        else:
            pass

    except:
        pass

dum_tup = zip(name, twitter, pro_data, post_scrap, replay_scrap)
df_primary_scrape = pd.DataFrame(dum_tup, columns=['name', 'twitter', 'pro_data', 'article', 'reply'])

df_primary_scrape.reply = df_primary_scrape.reply.values.flatten()
df_primary_scrape.article = df_primary_scrape.article.values.flatten()

df_primary_scrape['reply'] = df_primary_scrape['reply'].agg(lambda x: ','.join(map(str, x))).str.strip('[^A-Za-z0-9]+')
df_primary_scrape['article'] = df_primary_scrape['article'].agg(lambda x: ','.join(map(str, x))).str.strip(
    '[^A-Za-z0-9]+')
df_primary_scrape['pro_data'] = df_primary_scrape['pro_data'].astype(str).str.strip('[^A-Za-z0-9]+')

df_primary_scrape['reply'] = df_primary_scrape['reply'].str.lower()
df_primary_scrape['article'] = df_primary_scrape['article'].str.lower()
df_primary_scrape['pro_data'] = df_primary_scrape['pro_data'].str.lower()

df_primary_scrape['combine'] = df_primary_scrape['reply'] + " " + df_primary_scrape['article'] + " " + \
                               df_primary_scrape['pro_data']

listOfWords = [x.lower() for x in listOfWords]

for i in listOfWords:
    df_primary_scrape[f'{i}'] = df_primary_scrape['combine'].map(lambda x: x.count(f'{i}'))

df_primary_scrape = df_primary_scrape.applymap(lambda x: x.encode('unicode_escape').
                                               decode('utf-8') if isinstance(x, str) else x)
#
# Excel_convertor = pd.ExcelWriter(f'{int(time.time())}KeywordHits.xlsx')
# df_primary_scrape.to_excel(Excel_convertor, index=False)
# Excel_convertor.save()
#
# file_name = str(time.time())
# df_primary_scrape.to_csv(f'{str(int(time.time()))}KeywordHits.csv')

