from awsome.main import AWSomeApp


class TestAWSome:
    def test_title(self):
        assert AWSomeApp.TITLE == "AWSome"
