class Person:
    """
    Represents a person in the social network.
    """

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # prevent duplicate friendships
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """
    Represents the social network graph.
    """

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            missing = person1_name if person1_name not in self.people else person2_name
            print(f"Friendship not created. {missing} doesn't exist!")
            return

        p1 = self.people[person1_name]
        p2 = self.people[person2_name]

        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self):
        for person in self.people.values():
            friends = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friends)}")


# -------- TEST NETWORK --------

network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# duplicate test
network.add_person("Alex")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # error test
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

print("\nSOCIAL NETWORK\n")
network.print_network()


"""
Design Memo

A graph is the best structure for representing a social network because relationships between users are naturally modeled as connections between nodes. In this program, each person is a node and friendships are bidirectional edges, allowing relationships to be mutual and dynamic.

A list would not work well because it cannot directly represent relationships without nested structures, making searches inefficient. A tree structure is also not appropriate because trees enforce a hierarchy with parent-child relationships, while social networks are many-to-many and non-hierarchical.

Using an adjacency list allows efficient storage and performance. Adding a person takes constant time, and adding a friendship only requires updating two lists. Printing the network requires iterating through all users and their friendships, which is linear relative to the size of the network.

One trade-off is that preventing duplicate friendships requires checking a person’s friend list, which takes linear time. However, this keeps the structure simple and memory efficient.

Overall, graphs provide the flexibility and realism needed to model real-world social relationships.
"""