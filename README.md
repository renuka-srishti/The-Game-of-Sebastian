#### This repository contains assignment given by Prof. David Crandall during the Elements of Artificial Intelligence Spring 2021 class.

# The Game of Sebastian

## Introduction

Sebastian is a one-player game of luck and skill. Each turn has four steps:
- The player rolls five dice.
- The player inspects the dice and chooses any subset (including none or all) and rolls them.
- The player inspects the dice again again choose any subset and rolls them.
- The player must assign the outcome to exactly one category on their score card, depending on which five dice are showing after the third roll.

Goal is to achieve as high an average score as possible.

Players can choose which category to fill at the end of each turn, but each category may be filled only once per game. A player can also choose to assign a roll to a category that does not match the requirements, but then a zero is entered into that category.

## Approach

  1. We are using **expectimax** algorithm to find the best combination of move to maximize the score.
 
    ```
      def expectimax(self, dice, scorecard):
  
    ```
    
   2. We are processing one layer. We initially executed our program for 2 layers but it was expensive and results were similar to layer 1 so decided to go with layer 1 only.
   3. We are calling **expectimax** algorithm for first and second roll as follows:
   
         1. Caculating best move for all possible combinations of rerolls that can happen with all dice combinations as follows:
         
            Finding the score for each category possible for current dice pattern.
              
                  ````
                    def calculate_score_for_dice(self, dice_value, scorecard):
                  ````
                  
                  
         2. This will give you a dictionary with all the possible categories for the current dice pattern and their corresponding score. This dictionary will                   be used to find the maximum score.
         
         3. Using the above dictionary, now we will find out the possible category with maximum score:
   
            ````
              calculate_max_score
        
            ````
      
        4. So this way, we get the possible category with maximum score.
        
        5. Once we have the all max scores, we can get the best move with max score.
        
   4. In third roll, we will fit the best category which will give the max score.
        ````
          def fit_in_category(self, dice, scorecard):
          
        ````

## Problems we faced
1. How many layers to execute for the game of Sebastian.

   We finalized after testing for both layers
   
2. What is the best way to find the max score.

   So best way is to apply expectimax by assigning all possible categories to all possible dice combination and whichever gives the max score will be the best move.
   
   
 ## Output:
 Our program is returning mean score always more than 200. <br/>
 One output we got as follows: <br/>
    Final score: 165 <br/>
    Min/max/mean: 132 317 214.04 <br/>