###It will access the file named story.txt as in read mode.
with open("story.txt","r") as f:
    story=f.read()

words=set()###set is used not to use the word second time.
### "words" is used to store unique braket words
start_of_word=-1
target_start="<"
target_end=">"
###It iterates to the last word by using enumerate
for i,char in enumerate(story):
    if char ==target_start:
        start_of_word=i
        
    ###extracts the words from the story to words
    if char == target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
        

###user defined words will be added in the story
answers={}
for word in words:
    answer=input("Enter a word for "+word+": ")
    answers[word]=answer
    
for word in words:
    story=story.replace(word,answers[word])
    
print(story)