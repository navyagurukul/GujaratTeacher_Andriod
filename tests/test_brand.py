"""ES Teacher brand check: the suite must be driving the English Shiksha Teacher
(Gujarat) app, not EG Teacher. The two builds share code and copy, so the theme
colour is what tells them apart (utils/theme.py) — checked on the login screen
and again on the home dashboard after login."""
import pytest

from config import settings
from data.test_data import TEACHER_MOBILE
from pages.login_page import LoginPage
from utils import theme

ES_PACKAGE = "com.OritSciencesPrivateLimited.EnglishGurukul.englishshikshateacher"


@pytest.mark.sanity
@pytest.mark.smoke
def test_app_under_test_is_es_teacher(driver):
    assert settings.APP_PACKAGE == ES_PACKAGE, (
        f"suite is configured for {settings.APP_PACKAGE}, not ES Teacher"
    )
    assert driver.current_package == ES_PACKAGE, (
        f"foreground app is {driver.current_package}, not ES Teacher"
    )


@pytest.mark.sanity
@pytest.mark.smoke
def test_theme_is_es_teacher(driver):
    login = LoginPage(driver)
    assert login.is_loaded(), "Login screen did not show 'Sign in to continue'"
    brand, rgb = theme.detect(driver)
    assert brand == theme.ES, (
        f"login screen theme is {rgb} ({brand or 'unknown'}), expected the ES "
        f"Teacher blue ~{theme.ES_PRIMARY}, not the EG brown ~{theme.EG_PRIMARY}"
    )

    home = login.login_or_register(TEACHER_MOBILE)
    assert home.is_loaded(), "Home dashboard ('Welcome!') did not load after login"
    brand, rgb = theme.detect(driver)
    assert brand == theme.ES, (
        f"home dashboard theme is {rgb} ({brand or 'unknown'}), expected the ES "
        f"Teacher blue ~{theme.ES_PRIMARY}"
    )
