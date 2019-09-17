# PWSA-Matching-Algorithm-in-Python
This project was one carried out during a 2-week python programming workshop held in 2018 at the University of Ibadan and Organized by the PWSA (Programming Worshop for Scientists in Africa)

This project mirrors the selection process for Youth Corps Menmbers for the compulsory one-year National Youth Service in Nigeria

The National Youth Service Corps (NYSC) is an organization set up by the Nigerian government
to involve the country’s graduates in the development of the country. Since 1973 graduates of
universities and later polytechnics have been required to take part in the NYSC program for one
year. Have you ever wondered how the allocation of corp members is being carried out by the
NYSC administrative? Given the number of students that need to be allocated in each batch,
can you estimate how long it will take if this allocation process is done manually, or the amount
of human resources that would be expended? Obviously, a lot! To save time and resources, the
Director General (DG) of NYSC has approached you as a mathematician and programmer to help
design an automated system that can be used to efficiently allocate corps members to one of the
36 states in Nigeria, based on their choices.
What you will be provided
A dataset containing the following:
(i) information of corp members C = fc1; c2; : : : ; c1000g,
(ii) six list of states that each ci 2 C would like to be assigned to, ranked according to order of
preference (that is, first choice, second choice, and so on).
You have also been told that the maximum number of corp members that can be allocated to each
state is 30. For clarification, each line in the txt file is read  as follows: Corp member 1 prefers Adamawa to Niger, and she prefers Niger to Zamfara, and so on.. Corp member 2 prefers Benue to Borno, and she prefers Borno to Katsina, and so on..
What you are required to do
You are expected to implement a program that will
1. take the preferences of these youth corps into consideration,
2. assign each of them to only one of the states that appear on her list,
3. without exceeding the maximum capacity of the states.
First, imagine you want to solve this problem with pencil and paper, how would you go about it?
Whatever set of instructions you come up with on paper is what we refer to as algorithms. Next,
your aim is to communicate this algorithm to the computer in a language that it understands,which is where the Python programming language comes in. 

The goal: Using the skills you have
acquired in the past few days: (i) read in the data in Python using a most suitable data structure,
(ii) implement your algorithm, (iii) run this algorithm on the data set you’ve just read, and finally
(iv) output your solution, which will inform the DG’s decision on which state to allocate each corps
member.
