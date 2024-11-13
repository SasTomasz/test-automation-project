from src.search_result_page import SearchResultPage

def test_search_returns_warning_to_logout_user(driver, main_page):
    main_page.go_to_main_page()
    main_page.check_the_page_is_ready()
    main_page.fill_search_field("automation")
    main_page.click_search_button()

    results_page = SearchResultPage(driver)
    results_page.check_page_is_ready()
    warning = results_page.get_search_warning()

    assert warning == "Must be logged in to use global search", "There was no proper text in the webpage"
