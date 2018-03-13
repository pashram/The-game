from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    while True:
        next = raw_input(">")
        num = check_number(next)
        if num == True:
            how_much = float(next)

            if how_much <= 50:
                print "Nice, you're not greedy, you win!"
                exit(0)
            else:
                dead("You greedy bastard!")
        else:
            print "Man, learn to type a number."

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead ("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input(">")

    if "left" in next:
        bear_room()
    elif "right" in next:
        cthulhu_room()
    else:
        dead("You stuble around the room until you starve.")

def check_number(x):
    """This function takes a string and returns 'True' only
    if it is a number."""

    length = len(x)
    count = 0
    dot_count = 0
    for i in x:
        for a in range(10):
            if i == str(a):
                count += 1
                break
            elif i == ".":
                count += 1
                dot_count += 1
                break

    if length == count and dot_count <= 1 and count != dot_count:
        result = True
    else:
        result = False
    #print "length = %r; count = %r; dot count = %r" % (length, count, dot_count)
    return result




start()
