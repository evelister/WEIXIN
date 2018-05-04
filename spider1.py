import itchat
import pandas
import jieba
from wordcloud import WordCloud

def weixin():
    itchat.login()
    friends = itchat.get_friends(update=True)
    df_friends = pandas.DataFrame(friends)
    signatures = df_friends.Signature
    text = ' '.join(signatures)
    wordlist = jieba.cut(text, cut_all=True)
    wordlists = ' '.join(wordlist)
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(wordlists)

    wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2, font_path='simhei.ttf').generate(wordlists)
    wordcloud.to_file('weixin.png')

def main():
    weixin()

if __name__ == "__main__":
    main()