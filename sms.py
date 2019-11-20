"""'sms.py' This program is a sms simulation program using a class called SMSmessage
This class receives three variables namely:
    1. has_been_read - a bool for whether the user read a sms or not.
    2. message_text - for the receiving of a text message sent by the user.
    3. from_number - for the receiving of the number from which the text message comes.
The class holds various functions that return results based on user input. In short,
the program can send, receive, read, get, mark and delete sms's from a number.
"""
# An SMS Simulation


class SMSmessage():  # class definition
    """'class SMSmessage' This is a class for the defining of three variables in
    the class, has_been_read, message_text, from_number"""

    # initialise the class through the constructor
    def __init__(self, has_been_read, message_text, from_number):
        # set the parameters
        self.has_been_read = has_been_read
        self.message_text = message_text
        self.from_number = from_number

    def mark_as_read(self):
        """'MarkAsRead()' a function for changing the bool value of a sms read to True'"""
        userinput2 = int(
            input("Which message would you like to mark as read? 1/2/3... "))
        # for changing the correct bool the user value must be decreased by 1
        i_user = userinput2 - 1
        SMSSTORE[i_user][0] = True  # change the sms to read.
        print("That sms: " + SMSSTORE[i_user][1] + " is now marked as read")
        # print(SMSSTORE) - Checkpoint print if needed

    def add_sms(self):
        """'add_sms()' a function that adds as a list the new sms with properties to the SMSSTORE"""
        new1 = self.from_number = input("Please enter your number: ")
        new2 = self.message_text = input("Please enter your text message.: ")
        # must add the bool for new messages as unread through False
        new3 = self.has_been_read = False
        newsms = [new3, new2, new1]  # set new list
        SMSSTORE.append(newsms)  # append it to the SMSSTORE

    def get_count(self):
        """'get_count()' a function for counting the amount of messages in the SMSSTORE"""
        length = len(SMSSTORE)
        return length  # return the count

    def get_message(self):
        """'get_message()' a function that returns the message of the sms the user chose"""
        userinput = int(input("Which message would you like to get?: "))
        n_user = userinput - 1
        print("The message for that sms is: " + SMSSTORE[n_user][1])

    def get_unread(self):
        """'get_unread()' this function returns the unread messages"""
        print("The unread messages are: ")
        for message in SMSSTORE:
            if False in message:
                print(str(SMSSTORE.index(message) + 1), "✉️ " + message[2])

    def remove(self):
        """'remove()' this function will remove an sms the user chose from the list printed
        with number indexing"""
        userinput = input("Do you want to remove a sms? Y / N: ")
        remove_sms = userinput.upper()
        if remove_sms == "Y":
            if SMSSTORE == []:  # if the list is empty print that their are no more messages.
                print("You have no more messages in the inbox")
            else:
                which_one = int(
                    input("Which sms would you like to delete? 1/2/3...? "))
                # for correct removal from the list the user input must be offset neg. by one
                removelist = SMSSTORE[which_one - 1]
                SMSSTORE.remove(removelist)  # remove the sms from the list
                # for a new list create a for loop that now iterates through the newly created list
                print("The new sms list is: ")
                for smsnewl in SMSSTORE:
                    # print the new list
                    print(SMSSTORE.index(smsnewl) + 1, "✉️ " + smsnewl[2])
        # else just print "okay" for breaking out of the function
        else:
            print("Okay")


# the list for storing all the sms messages in
SMSSTORE = []
# set an empty variable that holds the user response.
USERCHOICE = ""
# create a while loop with nested conditions that will call funtions
# from the class based on the user response
while USERCHOICE != "quit":
    USERCHOICE = input(
        "What would you like to do - read/send/mark/delete/quit? ")
    # if the user wants to read the messages create a for loop
    if USERCHOICE == "read":
        for sms in SMSSTORE:  # print a list of all the sms's in the inbox
            print(SMSSTORE.index(sms) + 1, "✉️ " + sms[2])
        print(str(SMSmessage.get_count(self=SMSmessage)) +
              " messages in the inbox.")  # print a count of the total amount of sms's in the list
        # list the unread messages
        SMSmessage.get_unread(self=SMSmessage)
        # through this function ask the user which message they would like to read
        SMSmessage.get_message(self=SMSmessage)
        # after the previous list the unread messages again
    elif USERCHOICE == "delete":
        for sms in SMSSTORE:  # print a list of all the sms's inbox
            print(SMSSTORE.index(sms) + 1, "✉️ " + sms[2])
        SMSmessage.remove(self=SMSmessage)
        # print a new count of messages in the inbox
        print(str(SMSmessage.get_count(self=SMSmessage)) +
              " messages now in the inbox.")
    # if the user wants to send call the add_sms function
    elif USERCHOICE == "send":
        SMSmessage.add_sms(self=SMSmessage)
    # if the user wants to mark a message as read
    elif USERCHOICE == "mark":
        SMSmessage.get_unread(self=SMSmessage)
        SMSmessage.mark_as_read(self=SMSmessage)
    # if the user wants to quit the print "Goodbye"
    elif USERCHOICE == "quit":
        print("Goodbye")
    # for incorrect input
    else:
        print("Oops - incorrect input")
