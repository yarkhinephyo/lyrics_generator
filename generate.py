
import pronouncing
import pickle
import random
import os


def get_random_rhymes(keylist, n):

  completed = False

  while not completed:
    count = 1
    keyword = random.choice(keylist)
    returnlist = [keyword]
    rhymedset = set(pronouncing.rhymes(keyword)) #Unordered SET
    for word in rhymedset:
      if word in keylist and word != keyword:
        count += 1
        returnlist.append(word)
      if count == n: #Only when sufficient rhymes are found, the results are returned
        completed = True
        break

  return tuple(returnlist)


def generate_one_line(reverse_dict_1, reverse_dict_2, endword, maxlength):

  text_list = [endword]
  word_one = None
  word_two = endword

  for i in range(maxlength):
    tmp1 = word_two

    if (word_one, word_two) in reverse_dict_2:
      tmp2 = random.choice(reverse_dict_2[(word_one, word_two)])
    elif word_two in reverse_dict_1: #If not found in dict_2, search in dict_1
      tmp2 = random.choice(reverse_dict_1[word_two])
    else: #If no list of following words is found, chose a random word
      tmp2 = random.choice(list(reverse_dict_1.keys()))
    
    if tmp2 == "#": 
      break #BREAK if EOL

    word_two = tmp2
    word_one = tmp1
    text_list.insert(0, word_two)
  
  return (" ".join(text_list)).capitalize()


def get_reverse_dicts(genre):
  return pickle.load(open(os.path.join('static', genre + '_reverse_dicts.pkl'),'rb'))


def get_generated_song(genre, numOfLines, maxlength, n):

  reverse_dicts = get_reverse_dicts(genre)

  reverse_dict_1 = reverse_dicts['unigram'] #One word
  reverse_dict_2 = reverse_dicts['bigram'] #Two word pairs

  keylist = list(reverse_dict_1.keys())

  line_list, endwords = [], []

  for i in range(numOfLines//n):
    rhymeTuple = get_random_rhymes(keylist, n) #Get rhymed pairs/ triples/ quadruples etc
    endwords.extend(rhymeTuple)

  for i in range(len(endwords)):
    newline = generate_one_line(reverse_dict_1, reverse_dict_2, endwords[i], maxlength)
    line_list.append(newline)

  return "\n".join(line_list)


# print(get_generated_song('Hip-Hop', 10, 7, 2))