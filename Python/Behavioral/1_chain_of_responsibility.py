"""
Every piece of code must do one, and only one, thing.
"""


class ContentFilter:
    """This class accepts different filters each one
    filtering only by one specific thing."""
    def __init__(self, filters=None):
        self._filters = list()
        if filters:
            self._filters += filters

    def filter(self, content):
        for _filter in self._filters:
            content = _filter(content)
        return content


# def main():
#     content = "Some text"
#     content_filter = ContentFilter([
#         offensive_filter,
#         ads_filter,
#         harassment_video_filter])
#     filtered_content = content_filter.filter(content)
#
# if __name__ == '__main__':
#     main()
