# RoboticArm_ChessBoard_PI
The chess algorithm is based from the [Sunfish Chess Algorithm](https://github.com/ClanDesDindesLibres2/RoboticArm_ChessBoard_PI/tree/main/sunfish-master#introduction) the decision making of the algorithm was not touch by our team. We needed a decision making algorithm in our project to be able to play against the robotic arm. We added function in the code to communicate with an arduino mega 2560 ([Arduino's code](https://github.com/ClanDesDindesLibres2/ChessBoard_Arduino)) using a raspberry Pi 4 and to send the movement needed to an Open CR board.

The sunfish algorithm run in a loop simulating a chess game, we added a communication function called enterPos() replacing the input function in the original code. For our project demonstration we decided to start the game with some premove already made. We use the Pyserial library to facilitate the communication between the arduino and the raspberry pi. We receive a string of the format a2a4 with the first two character being the initial position of the piece and the last two being his finale position. 

The string is used by the algorithm to send back another string of the same format representing the movement made by the arms. We also needed a way to know if a white piece was present in the finale scare of the arm's movement. The algorithm transform our move in number from 21 to 98. 
![image](https://user-images.githubusercontent.com/71843193/160680176-392b78ee-92e2-4ca8-9787-a3f8a7ec6e34.png)


We created a list with the position of the white piece called boardblanc, since we don't need to know where are each different piece we decided to use
