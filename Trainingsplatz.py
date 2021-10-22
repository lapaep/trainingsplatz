from kaggle_environments import make, evaluate
# pip install kaggle_environments
# pip install requests

'''Trainingsplatz zum testen der programmierten Bots.'''

def Testspiel(submission):

    # Erstellen des Spieles und Angabe der spielenden Submissions
    env = make("halite", debug=True)
    env.run([submission, "random", "random", "random"])

    # Rendern des Spielablaufes und Ausgabe als html-Datei
    out = env.render(mode="html")
    f = open('wiederholung.html','w')
    f.write(out)
    f.close
    print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


def Evaluation(submission):
    # Fehler? Zurzeit wird 5 mal das gleiche Spiel wiederholt
    agents = [submission, "random", "random", "random"]
    rewards = evaluate("halite",agents,num_episodes=5,debug = True)
    print(rewards)



# Load an agent from a file.
agent = "submission.py"

Testspiel(agent)