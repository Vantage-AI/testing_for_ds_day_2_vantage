import pytest
import requests  # type: ignore
from _pytest.monkeypatch import MonkeyPatch

from dishwashers.data import parse_duration, scrape_duration_from_recipe_page
from tests.generate_test_data import DUMMY_RECIPE_PAGE_PATH


def test_scrape_duration_from_recipe_page(monkeypatch: MonkeyPatch) -> None:
    class MockRequestsGet:
        def __init__(self, url: str):
            with open(DUMMY_RECIPE_PAGE_PATH) as f:
                self.content = "".join(f.readlines())

    monkeypatch.setattr(requests, "get", MockRequestsGet)
    duration = scrape_duration_from_recipe_page(url="")
    assert duration == "20 min. bereiden"


# -- Exercise 1 --
# The previous test doesn't cover every line of scrape_duration_from_recipe_page(). Find out with
# ```pytest --cov dishwashers tests\test_data.py``` which lines of that function are not covered. Write a test for them.


# -- Exercise 2 --
# Above, requests.get was replaced with the contents of tests/test_data/dummy_recipe_page.txt. Therefor the test is
# repeatable and doesn't require an internet connection. A worse solution is caching the recipe page, but for learning
# purposes let's implement it anyway. Write a test for scrape_duration_from_recipe_page() that still replaces
# requests.get, but know with a cached version of the webpage that it retrieved from the internet.


# -- Exercise 3 --
# Besides full line coverage, we want to make sure that a function works for all realistic inputs. Make sure that both
# of these reasons are satisfied by adding parameter values to the next test.
# 1) Cover all code from both retrieve_first_number() and parse_duration().
# 2) For realistic inputs have a look at a few recipe pages from the data.
@pytest.mark.parametrize("text, expected",
                         [("1 uur", 60)])
def test_parse_duration(text: str, expected: int) -> None:
    assert parse_duration(text) == expected
