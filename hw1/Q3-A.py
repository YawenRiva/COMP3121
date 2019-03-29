# there are total N people in the array
while (after we ask about everyone, its (n-1) times because the 
        last person doesnt need to answer the question)
    initially i = 0, and j = 1
    if person[i] knows person[i+j]
        person[i] is not celebrity
        keep asking, i++
    elif person[i] doesnt know person[i+j]
        person[i] might be celebrity
        keep asking about the person after
        j++
# after we ask everyone, there's one person left, A
# we need to make sure that the person doesnt know anyone
# because celebrity doesnt know anyone
while (n-1) {
    if person[A] knows anyone
        then person[A] is not celebrity
        theres no celebrity in this party
    else
        then we need to check if everyone knows A
        because everyone knows celebrity
        if everyone which is (n-1) people knows A
            then A is celebrity
        else A is not celebrity
}

