from random import choice
topic = ["computer system", "CPU", "Memory", "languages", "starwars", "interview", "pros and cons", "self-portraint", "algorithm", "Places", "HTML", "HTML5", "pay-as-you-throw", "cool-green-cities", "tortoies"]
with open("topics.txt", "a+") as file:
    file.seek(0)
    read_topic = [i for i in file.readlines()]
    topics = choice(topic)
    if len(read_topic) == len(topic):
        exit(0)
    while topics+"\n" in read_topic:
        topics = choice(topic)
    else:
        file.writelines(topics+"\n")
        print(f"Ripeti -> {topics}")
