# Sunfish Algorithm
The sunfish algorithm run's in a loop **simulating a chess game**. The algorithm is used for the robotic arm's moves. He his the opponent to defeat. 

## Communication between Arduino, Rasberry Pie and Open CR(Robot)
We added a communication function called enterPos() replacing the input function in the original code. For our project demonstration we decided to implement puzzle to shorten the games. We use the Pyserial library to facilitate the communication between the arduino and the raspberry pi. We receive a string of the format a2a4 with the first two character being the initial position of the piece and the last two being his finale position. 

The string is used by the algorithm to send back another string of the same format representing the movement made by the arms. We also needed a way to know if a white piece was present in the finale scare of the arm's movement. The algorithm transform our move in number from 21 to 98. 

![image](https://user-images.githubusercontent.com/71843193/160680176-392b78ee-92e2-4ca8-9787-a3f8a7ec6e34.png)

We created a list with the position of the white piece called boardblanc, since we don't need to know where are each different piece we decided to use boolean in the list where the index represent the position on the board. We use this list when we send the arm move to the function to control the arm. We also added function to change the string sent by the algorithm to integer. We use the function analyseboardalphab() to interprete the alphabetical character and return a int. We use the function analyseboardint to interprete the numerical character and return a int that we can add to the other int to have the unique interger representing the square where the position is. 

## LED in Sunfish algorithm
The function to control the LED is also in the rasberry pi. We use the pins 17 for red, 27 for green and 22 for blue. We use the library RPi.GPIO to control the LED.  The setLedRGB() function is used to setup LED when you start the board. We have the ledRGB() function used to select the mode we want to be in. We have listed the different mode of the LED in the [instruction manual](https://github.com/ClanDesDindesLibres2/.github/blob/main/Instructions_Manual_ChessBras.docx) of the game.
