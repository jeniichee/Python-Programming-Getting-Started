"""
Questions:
"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
"Are encoding and encryption the same? - Yes/No":
"Is it possible to decrypt a message without a key? - Yes/No":
"Is it possible to decode a message without a key? - Yes/No":
"Is a hashed message supposed to be un-hashed? - Yes/No":
"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
"Is MD5 a secured hashing algorithm? - Yes/No":
"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
"""

def welcome_assignment_answers(question):

    if (
        question
        == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    ):
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif (
        question
        == "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    ):
        answer = "0d0df7d1ec81507a43e1d6d3b50f831c5ef2de5d3b12687b2fd4637c76492f59"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif (
        question
        == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    ):
        answer = 5
    elif (
        question
        == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    ):
        answer = 3
    else:
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answer


if __name__ == "__main__":
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
