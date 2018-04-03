# 01 - Assembly Language

## What we were instructed to do:

> Using Assembly Language, create a mulitiplication program for **xComputer**

## What I did:

> Using Assembly Language, created a calculator that could handle addition, subtraction, mulitiplication, division, and exponential operations. It can also handle all negatives, with one bug listed in the exponential area below.

## How to run this project

* Begin by cloning or downloading the entire *CS_230* repository from GitHub.
* Make sure you have the JRE (Java Runtime Enviroment) installed.
    * Open Command Prompt on Windows or Terminal on Mac.
    * Type `java --version` and press **Enter**.
    * If you see a version number, you have the JRE installed
    * If not, go here to download it: [JRE Download](http://www.oracle.com/technetwork/java/javase/downloads/jre10-downloads-4417026.html)
* Open the *CS_230* folder on your machine, find the *01 - Assembly Language* folder, and open it.
* Double click *xComputer.jar* to run it. 
* Click **Load File**
* Browse to the *01 - Assembly Language* folder, open it, and select the *Total Challenge* file. 
* Click **Open**.
* Follow the instructions in the code.
    * Step 1: Choose a math operation to perform.
    * Step 2: Enter that choice next to `choice: `, in place of the holder code of `data`.
    * Step 3: Enter two number values to perform the math operations on.
* Click **Translate**.
* Select your speed to run at. For almost immediate operation, select **Fastest Speed**.
* Make sure the dropdown on the right is set to **Integers**.
* Click **Run**.
* View your results in the right side panel.
    * Addition: The top number is your sum.
    * Subtraction: The top number is your difference.
    * Mulitplication: The top number is your product.
    * Division: The top number is your quotient, the second is the numberator to the remainder, and the third is the denominator to the remainder. The remainder is not reduced.
    * Exponents:
        * Positives: The top number is your answer.
        * Negatives: The top number is 0. The second is the numerator to the answer, the third is the denominator to the answer. 
            > There is a known bug in which a negative number to a negative exponent sometimes results in both the numerator and denomiator. This is due to the inherent difficulty in displaying an answer in this format. This was the best I could do at the time.
* To make changes and re-run the program:
    * Select **Total Challenge** from the top dropdown.
    * Make your changes.
    * Click **Translate**.
    * Click Run.

## Summary 
This project was very interesting for as a first assignment. I enjoyed the problem solving involved at this low level programming. I hope you enjoyed this project, check out my other projects to see the unique twists I made with each assignment.
