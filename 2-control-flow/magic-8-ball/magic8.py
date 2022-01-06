import random

name = "Kabiru"
question = "Will I get PR to Canada this year?"
answer = ""
random_number = random.randint(1, 12)
#print(random_number)

if (len(name) > 1) and (len(question) > 1):
  if random_number == 1:
   answer = "Yes - definitely."
  elif random_number == 2:
   answer = "It is decidedly so."
  elif random_number == 3:
   answer = "Without a doubt."
  elif random_number == 4:
   answer = "Reply hazy, try again."
  elif random_number == 5:
   answer = "Ask again later."
  elif random_number == 6:
   answer = "Better not tell you now."
  elif random_number == 7:
   answer = "My sources say no."
  elif random_number == 8:
   answer = "Outlook not so good."
  elif random_number == 9:
   answer = "Very doubtful."
  elif random_number == 10:
   answer = "Jehovah has the final say."
  elif random_number == 11:
   answer = "Guess...?"
  elif random_number == 12:
   answer = "Let's see how it goes."
  else:
   answer = "Error"
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
elif len(question) < 1:
  print("You have not asked a question I can respond to. Please, ask me a question")
else:
  print("Question: " + question)
