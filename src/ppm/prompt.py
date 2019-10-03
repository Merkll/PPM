import sys

def cli_prompt(question, possible_answers=None, required=False, default=None):
  question_answered = False
  
  while not question_answered:
      default_answer = "({})".format(default) if default else ""
      possible_answer = " ? [" + "/".join(possible_answers) + "] : " if possible_answers else " : " 
      choice = input(question + default_answer + possible_answer).lower()
      if possible_answers and not choice in possible_answers:
        sys.stdout.write("Please respond with {}\n".format(possible_answers))
      else:
        question_answered = True
        return choice or default
      if not required: return default
            