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

