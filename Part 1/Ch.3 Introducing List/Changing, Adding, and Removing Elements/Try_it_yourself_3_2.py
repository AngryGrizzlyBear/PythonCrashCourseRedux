# 3-4 Guest List: If you could invite anyone , living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you'd like to
# invite to dinner. Then use your list to print a list to each person, inviting them
# to dinner.

dinner_invitations = ['Monica', 'Avery', 'Brandon']

print(dinner_invitations[0] + ", You have been invited to dinner!")
print(dinner_invitations[1] + ", You have been invited to dinner!")
print(dinner_invitations[2] + ", You have been invited to dinner!")

# 3-5 Changing Guest List: You just heard that one of your guest can't make the dinner,
# so you need to send out a new set of invitations. You'll have to think of someone else
# to invite.
# Start with our program from Exersize 3-4. Add a print statement at the end
# of your program stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the name of the new person
# you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("Oh no! " + dinner_invitations[2] + " can't make it!" )

del dinner_invitations[2]
dinner_invitations.insert(2,'Rachel')

print(dinner_invitations[0] + ", You have been invited to dinner!")
print(dinner_invitations[1] + ", You have been invited to dinner!")
print(dinner_invitations[2] + ", You have been invited to dinner!")

# 3-6 More Guest: You just found a bigger dinner table, so now more space is available.
# Think of three more guest to invite to the dinner table.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end
# of your program informing that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the end of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print("\nI found a bigger table! I wish to invite more people!\n")

dinner_invitations.insert(0, 'Thomas')
dinner_invitations.insert(2, 'Stacy')
dinner_invitations.append('Marcus')


print(dinner_invitations[0] + ", You have been invited to dinner!")
print(dinner_invitations[1] + ", You have been invited to dinner!")
print(dinner_invitations[2] + ", You have been invited to dinner!")
print(dinner_invitations[3] + ", You have been invited to dinner!")
print(dinner_invitations[4] + ", You have been invited to dinner!")
print(dinner_invitations[5] + ", You have been invited to dinner!")

# Shrinking Guest List: You just found out that your new dinner table won't arrive
# in time for the dinner, and you have space for only two guest.
# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guest from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a message to that person
# letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make
# sure you actually have an empty list at the end of your program.

print("\nSorry everyone, but our new dinner table won't arrive in time for our event. I only"
      "have space for two people now.\n")
cancelled_invitations = dinner_invitations.pop(5)
print("Sorry, " + cancelled_invitations + " but I can no longer invite you to dinner.")
cancelled_invitations = dinner_invitations.pop(0)
print("Sorry, " + cancelled_invitations + " but I can no longer invite you to dinner.")
cancelled_invitations = dinner_invitations.pop(1)
print("Sorry, " + cancelled_invitations + " but I can no longer invite you to dinner.")
cancelled_invitations = dinner_invitations.pop(1)
print("Sorry, " + cancelled_invitations + " but I can no longer invite you to dinner.")


print("\nHey, " + dinner_invitations[0] + " you're still invited! Please come!")
print("Hey, " + dinner_invitations[1] + " you're still invited! Please come!")
print("\nI'm inviting " + str(len(dinner_invitations)) + " guest.")
del dinner_invitations[0]
del dinner_invitations[0]
print(dinner_invitations)
