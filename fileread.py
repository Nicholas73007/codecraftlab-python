#Written by Nicholas.

myfile = open("C:\Users\student\Desktop\Pygame1\myfile.txt","r");
highscore = myfile.readline();
#print(myfile.read());
#myfile.seek(25,0)
#print(myfile.read());
#print(myfile.tell());
# print (line)
#myfile.write("*Howdey i'm Flowey! Flowey The Flower You must be new to the underground, aren't cha'? looks like little ol' me will have to show yall how things work down here");
#myfile.close();
print("the current high score is" +  highscore);
flag = True
score = 0
while flag:
        inp = raw_input()
        if inp.isalpha() :
                flag = False
        else:
                score  += 1
myfile.close()
myfile = open("C:\Users\student\Desktop\myfile.txt", "w");

if score > int (highscore):
        myfile.write(str(score))
        myfile.close()
        print("the current highscore is"  +  str(score))
        print("your score is " + str(score))
myfile.close()

