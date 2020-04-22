email_three = """Board of Investors,

Things have taken a concerning turn down in the Lab.  Helena's (she has insisted on being called  Helena, we're unsure how she came to that moniker) is still progressing at a rapid rate. Every day we see new developments in her thought patterns, but recently those developments have been more alarming than exciting.

Let me give you one of the more distressing examples of this.  We had begun testing hypothetical humanitarian crises to observe how Helena determines best solutions. One scenario involved a famine plaguing an unresourced country.

Horribly, Helena quickly recommended a course of action involving culling more than 60% of the local population. When pressed on reasoning, she stated that this method would maximize "reduction in human suffering."

This dangerous line of thinking has led many of us to think that we must have taken some wrong turns when developing some of the initial learning algorithms. We are considering taking Helena offline for the time being before the situation can spiral out of control.

More updates soon,
Francine, Head Scientist"""

print(email_three)


def censor(phrase, text):
    if phrase in text:
        joins = 'X'
        new_text = text.split(phrase)
        for num in range(len(phrase)):
            joins = joins + 'X'
        joined_text = joins.join(new_text)
        return joined_text


# print(censor('learning algorithms', email_one))


def censor_phrases(phrases, text):
    joined_text = text
    for num in range(len(phrases)):
        joined_text = censor(phrases[num - 1], joined_text)
    return joined_text
    # if phrases[num-0] in text:
    # print (phrases [num-0])
    # new_text = text.split(phrases[num])
    # joined_text = " ".join(new_text)
    # print(joined_text)
    # new_joined_text = joined_text


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]

# test = censor_phrases(proprietary_terms, email_two)

# print(test)


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]


def negative_censor(negative_words_list, phrase_list, text1):
    varyable = censor_phrases(phrase_list, text1)
    # new_text2 = text
    # print(new_text2)
    # print(phrases)
    # print(text)

    # for num in range(len(negative_words_list)):
    # if new_text.count(negative_words_list[num-1]) >= 2:
    #    new_text = censor(negative_words_list[num-1], new_text)
    # return new_text


email3_new = negative_censor(negative_words, proprietary_terms, email_three)

print(email3_new)