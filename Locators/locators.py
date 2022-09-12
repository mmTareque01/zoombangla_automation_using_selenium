from selenium.webdriver.common.by import By


class Locators:
    # ----------{ home page }----------#
    url = 'https://zoombangla.com/'
    home_page_title = 'Home - ZoomBangla'
    # home page => search box
    search_icon_xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/a'
    search_box_xpath =  '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/form/input'
    seacrh_button_xpath =  '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/form/button'

    # home page => sub domain
    news_subdomain_xpat = '//*[@id="menu-item-541"]/a'
    shop_subdomain_xpat = '//*[@id="menu-item-542"]/a'
    video_subdomain_xpat = '//*[@id="menu-item-543"]/a'
    answer_subdomain_xpat = '//*[@id="menu-item-544"]/a'
    jobs_subdomain_xpat = '//*[@id="menu-item-545"]/a'
    travel_subdomain_xpat = '//*[@id="menu-item-546"]/a'

    # home page => social media
    facebook = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/a[1]'
    twitter = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/a[2]'
    youtube = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/a[3]'
    instagram = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/a[4]'

    # home page => footer
    contact_us_xpath = '//*[@id="block-5"]/div/a[2]'

    # ----------{ contact page }----------#

    name_input_field_xpath =  '//*[@id="wpforms-1542-field_0"]'
    email_input_field_xpath =  '//*[@id="wpforms-1542-field_1"]'
    subject_input_field_xpath ='//*[@id="wpforms-1542-field_3"]'
    message_input_field_xpath =  '//*[@id="wpforms-1542-field_2"]'
    submit_button_xpath =  '//*[@id="wpforms-submit-1542"]'
    # map_xpath =  '//*[@id="mapDiv"]/div/div/div[2]'
    map_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[4]/div/div[2]/section/div/div[2]/div/div/div/iframe'
    form_submit_confirmation_button =  "wpforms-confirmation-1542"

    # ----------{ video page }----------#
    video_xpath = '//*[@id="menu-item-543"]'
    video_card_tag = 'article'
    load_more_videos_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[2]/div/div/section/div/div/div/div/div/div/div[2]/div[2]/a'
    video_search_icon_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/a'
    video_search_input_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/form/input'
    video_search_button_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/form/button'
    error_comments = 'https://video.zoombangla.com/wp-comments-post.php'
    #
    video_link_xpath = (By.XPATH, '//*[@id="menu-item-543"]')
    comment_name_xpath = ''
    comment_email_xpath = ''
    comment_text_xpath = ''
    comment_website_xpath = ''
    comment_submit_button = ''

    add_dismiss_button = '//*[@id="dismiss-button"]'
    add_iframe_1 = 'aswift_12'
    add_iframe_2 = 'ad_iframe'
    author_id = 'author'
    email_id = 'email'
    url_id = 'url'
    comment_id = 'comment'
    submit_button_id = 'submit'
