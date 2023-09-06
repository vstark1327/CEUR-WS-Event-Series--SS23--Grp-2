from query.query_events import WikidataEvents
from query.query_series import WikidataEventSeries
from query.query_proceedings import WikidataProceedings
from matching.event_series import OpenAISeriesMatcher
from matching.proceedings import OpenAIProceedingsMatcher

if __name__ == "__main__":
    events = WikidataEvents()
    events.query()

    event_series = WikidataEventSeries()
    event_series.query()

    proceedings = WikidataProceedings()
    proceedings.query()

    series_matcher = OpenAISeriesMatcher()
    series_matcher.compare_results()

    proceeding_matcher = OpenAIProceedingsMatcher()
    print(proceeding_matcher.extracted_texts)
