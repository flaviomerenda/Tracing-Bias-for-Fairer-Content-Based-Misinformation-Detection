import pandas as pd

from itertools import chain

import spacy

from preprocess import preprocess_data


def get_frequencies(
    data_df: pd.DataFrame,
    nlp: spacy.lang
) -> pd.DataFrame:
    
    preproc_df = preprocess_data(data_df, "text")

    flat_preproc_df = list(chain(*preproc_df))

    stopwords = nlp.Defaults.stop_words

    non_stopwords = []
    found_stopwords = []

    # Check whether the word is not in the stopwords list
    for token in flat_preproc_df:
        if token.lower() not in stopwords:
            non_stopwords.append(token)
        else: 
            found_stopwords.append(token)

    freq_df = pd.DataFrame(non_stopwords, columns=["tokens"])
    freq_df = freq_df\
        .groupby("tokens")\
        .size()\
        .sort_values(ascending=False)\
        .reset_index(name="count")

    return freq_df


def get_proportions(freq_df: pd.DataFrame) -> pd.DataFrame:

    # Calculate relative frequency with respect to total
    freq_df["proportion"] = freq_df["count"] / float(sum(freq_df["count"]))

    return freq_df.sort_values(by="count", ascending=False)


def get_stats(data_df: pd.DataFrame) -> pd.DataFrame:
    data_df["title_length"] = data_df["text"]\
        .apply(lambda x: len(x))

    data_df["word_count"] = data_df["text"]\
        .apply(lambda x: len(str(x).split(" ")))

    data_df["char_count"] = data_df["text"]\
        .apply(lambda x: sum(len(word) for word in str(x).split(" ")))

    data_df["sentence_count"] = data_df["text"]\
        .apply(lambda x: len(str(x).split(".")))

    data_df["avg_word_length"] = \
        data_df["char_count"] / data_df["word_count"]

    data_df["avg_sentence_lenght"] = \
        data_df["word_count"] / data_df["sentence_count"]

    return data_df
