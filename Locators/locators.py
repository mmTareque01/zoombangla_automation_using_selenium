class Locators:
    # ----------{ home page }----------#
    url = 'https://zoombangla.com/'
    home_page_title = 'Home - ZoomBangla'
    # home page => search box
    search_icon_xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/a'
    search_box_xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/form/input'
    seacrh_button_xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/form/button'

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
    # "//*[@id="dismiss-button"]/div/span"

    # '//*[@id="block-5"]/div/a[2]'
    # '//*[@id="block-5"]/div/a[2]'

    # ----------{ contact page }----------#

    name_input_field_xpath = '//*[@id="wpforms-1542-field_0"]'
    email_input_field_xpath = '//*[@id="wpforms-1542-field_1"]'
    subject_input_field_xpath = '//*[@id="wpforms-1542-field_3"]'
    message_input_field_xpath = '//*[@id="wpforms-1542-field_2"]'
    submit_button_xpath = '//*[@id="wpforms-submit-1542"]'
    map_xpath = '//*[@id="mapDiv"]/div/div/div[2]'

    # ----------{ video page }----------#
    video_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[2]/div/div/section/div/div/div/div/div/div/div[1]/div[1]/div/article'
    load_more_videos_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[2]/div/div/section/div/div/div/div/div/div/div[2]/div[2]/a'
    video_search_icon_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/a'
    video_search_input_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/form/input'
    video_search_button_xpath = '/html/body/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/form/button'
    error_comments = 'https://video.zoombangla.com/wp-comments-post.php'
    #
    video_link_xpath = '/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[2]/div/div/section/div/div/div/div/div/div/div[1]/div[1]/div/article[4]'
    comment_name_xpath = ''
    comment_email_xpath = ''
    comment_text_xpath = ''
    comment_website_xpath = ''
    comment_submit_button = ''
