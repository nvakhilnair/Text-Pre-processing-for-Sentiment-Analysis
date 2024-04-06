import itertools
import json
import re

from textblob import TextBlob


class ProcessText:
    def __init__(self) -> None:
        self.apostrophe_mapping = self.load_json_file("apostrophe.json")
        self.slang_mapping = self.load_json_file("slangs.json")
        self.stopwords_list = self.load_json_file("stopwords.json").get("stopword", {})
        self.html_tags_regex = re.compile("<[^>]*>")
        self.urls_regex = re.compile(r"https?://(?:www\.)?\w+\.\w+(?:/\S*)?")
        self.emoji_regex = re.compile(
            "[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]"
        )
        self.punctuation_regex = re.compile(r"[^\w\s]")
        self.split_attached_regex = re.compile("[A-Za-z][^A-Z]*")
        self.interjections = str.split(
            "Yuck,Ew,Aw,Ouch,Oh,Ah,Ugh,Phew,Phooey,Yum,Yippee,Ack,Blah,Brr,Eek,Uh-huh,Boo,Hm,Gee,Gosh,Whoa,Yahoo,Bah,Hmph,Yowza,Aha,Gadzooks,Pish,Huzzah,Woot,Gada bing,Zowie,Boo hoo,Drat,Duh,Er,Fooey,Gah,Ha,Ick,Geez,Meh,Mmm,Oof,Pfft,Psst,Tsk tsk,Um,okk,hmm,mmm,yepp,eee,hehehe,hehe,yaa,haa",
            ",",
        )
        self.whitespace_regex = re.compile(r"\s+")

    async def clean_text(self, uncleaned_text, auto_corrector):

        # Convert to lowercase
        uncleaned_text = uncleaned_text.lower()

        # Remove HTML tags
        uncleaned_text = self.html_tags_regex.sub(r"", uncleaned_text)

        # Removing URLS
        uncleaned_text = self.urls_regex.sub(r"", uncleaned_text)

        # Removing emoji's
        uncleaned_text = self.emoji_regex.sub(r"", uncleaned_text)

        # Removing punctuation
        uncleaned_text = self.punctuation_regex.sub(r"", uncleaned_text)

        # Split attached words
        uncleaned_text = " ".join(self.split_attached_regex.findall(uncleaned_text))

        # Replace apostrophe with the respective mapping
        uncleaned_words = uncleaned_text.split(" ")
        uncleaned_text = " ".join(
            [
                (
                    self.apostrophe_mapping[word]
                    if word in self.apostrophe_mapping
                    else word
                )
                for word in uncleaned_words
            ]
        )

        # Replace slangs with the respective mapping
        uncleaned_words = uncleaned_text.split(" ")
        uncleaned_text = " ".join(
            [
                self.slang_mapping[word] if word in self.slang_mapping else word
                for word in uncleaned_words
            ]
        )

        # standardizing words by 2 words
        uncleaned_text = "".join(
            "".join(s)[:2] for _, s in itertools.groupby(uncleaned_text)
        )

        # Remove interjunctions
        uncleaned_words = uncleaned_text.split(" ")
        uncleaned_text = " ".join(
            [word for word in uncleaned_words if word not in self.interjections]
        )

        # Removing Stopwords
        uncleaned_words = uncleaned_text.split(" ")
        uncleaned_text = " ".join(
            [word for word in uncleaned_words if word not in self.stopwords_list]
        )

        # Spelling corrector
        if auto_corrector:
            text = str(TextBlob(uncleaned_text).correct())

        # Removing whitspaces
        uncleaned_text = self.whitespace_regex.sub(r" ", uncleaned_text)
        cleaned_text = uncleaned_text.strip()

        return cleaned_text

    def load_json_file(self, file_name):
        file_name = r"./static/data/" + file_name
        with open(file_name, "r") as f:
            json_data = json.load(f)
        return json_data
