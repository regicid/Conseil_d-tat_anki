import pandas as pd
import genanki
import numpy as np

for td_number in range(15):
  tableau = pd.read_excel("tonio_clean.xlsx",sheet_name=4+td_number,header=None)
  my_deck = genanki.Deck(
    1234,
    'TD1')
  my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
      {'name': 'Question'},
      {'name': 'Answer'},
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
      },
    ])

  for i in range(len(tableau.index)):
    if tableau.iloc[i,:3].isna().sum()<3 and tableau.iloc[i,3:4].isna().sum()==0:
      my_note = genanki.Note(
      model=my_model,
      fields=[str(tableau.iloc[i,0]) + ", " + str(tableau.iloc[i,1]) + ", " + str(tableau.iloc[i,2]), tableau.iloc[i,3]])
      my_deck.add_note(my_note)
      print(i)

  genanki.Package(my_deck).write_to_file('td_' + str(td_number+1)+'.apkg')