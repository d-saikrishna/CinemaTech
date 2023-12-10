# CinemaTech
Exploring the intersection of Film Making and Technology

## Shot division

Every script should be broken down into shots. This is generally done by the director-cinematographer together.

If the script is written in a certain format, we can attempt to create a template that makes the discussion between director and cinematographer simpler.

Script format:
1. Every paragraph should be one shot. Paragraph can be a single line as well.

Ideal:
1. The resulting shot division should be the optimum one. If all the shots are captured, essentially all the actions are captured without any duplication. Director can ofcourse choose duplication on sets for other purposes.

Props:

One of the variables required in the shot_divison template is the `props` variable. It is basically the list of properties used in each shot.
I am assuming that a property is nothing but a `noun` present in the sentence. So, I will search for them using NLP. Ofcourse, this gives me all unneccessary nouns (Proper nouns etc) - which I can filter later. I think it did a decent job.

For this, I used spaCy - English Language model.
```
pip install spacy
python -m spacy download en_core_web_sm
```