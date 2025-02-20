from gtts import gTTS
import os
from langchain_groq import ChatGroq
soccer=str(input("enter your Groq Api key: "))
llm=ChatGroq(temperature=0.3,groq_api_key=soccer,model_name="llama-3.3-70b-versatile")
def translate():
  a=str(input("enter target indic language: "))
  b=str(input("enter phrase: "))
  messages = [
    (
        "system",
        f"You are a helpful assistant that translates English to {a}. Simply translate the user sentence. Don't write anything in english",
    ),
    ("human", b),
  ]
  ai_msg = llm.invoke(messages)
  print(ai_msg.content)
  mytext = ai_msg.content
  audio(mytext,a)
def audio(mytext,a):
  choice=str(input("do you want to hear audio? Enter 'Yes' or 'No': "))
  if choice=="Yes":
    print("Audio file saved as 'welcome.mp3'.")
    language = 'en'
    myobj = gTTS(text=mytext,tld="co.in", lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")
  elif choice=="No":
    print(f"It is wonderful that you can understand {a}.")
  else:
    print("No such option exists.")
def Transliterate():
  a=str(input("enter the language you want to transcribe to: "))
  b=str(input("enter phrase: "))
  mess=[("system",f"you are a helpful assistant that converts text from english to {a}.Simply convert the text to the correct Script. Don't translate it. Don't write anything else."),("human",b)]
  t=llm.invoke(mess)
  print(t.content)
  audio(t.content,a)
def Define():
  a=str(input("enter the language of the word/phrase you want definition of: "))
  b=str(input("enter phrase: "))
  mess=[("system",f"you are a helpful assistant that converts text from english to {a}.Simply convert the text to the correct Script. Don't translate it. Don't write anything else."),("human",b)]
  t=llm.invoke(mess)
  messy=[("system",f"you are a helpful assistant that explains meaning of {t.content}. Output should be in the english language"),("human",t.content)]
  l=llm.invoke(messy)
  print(l.content)
  audio(t.content,a)
def main():
  print("Welcome!")
  print("To translate indic langauges, enter a: ")
  print("To covert english text to indic script, enter b: ")
  print("To covert define a word in an Indic Language, enter c: ")
  choice=str(input("enter choice: "))
  if choice=="a":
    translate()
  elif choice=="b":
    Transliterate()
  elif choice=="c":
    Define()
  else:
    print("No such option exists.")
main()
