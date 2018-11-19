# CS454_Final_Project

STEPS:
    1) Generate a DFA M within the language "" with K states
    2) Score DFA M via string with length k and correct function, so that score(M) = ( |correct(M,k)|  / 2^k )
    3) Create a copy of DFA M into DFA L and do a local change to L
    4) Score DFA L via string with length k and correct function, so that score(L) = ( |correct(M,k)|  / 2k )
    5) Compare the scores of DFA M & L, if (M <= L) then choose L as the winner and copy into M, also 
        reset local change for DFA.  Else M wins so keep it and advance to the state that will be locally changed next
    6) Repeat steps 3-5 till the most optimal DFA has been generated

Done:
    -Build DFA (with specified states)
    -print standard format & interprut
    -Local Change
    -random DFA 
    -function to test a given string in the DFA
    
To Do:
    -Refine building of DFA with a specified language given to us for the problem
    -Read and code the Scoring method that is talked about in the Majority document sent by Ravi
    -Code a function to generate 20 DFAs, with 7 states, and pick one at random (Kinda done with 
        the random function: give it a number K and it will generate a random DFA with K states, check
        to see if it is refined enough to be s )
    -Comparing scores function, between two DFAs (original DFA score M vs locally changed DFA score L)
        and when winner has been decided (DFA M score <= DFA L score), if the DFA that won is the original
        DFA call local change but increment the state that is getting changed.  However if the new locally 
        changed DFA has won, then do the change at inital starting state.
    -Function to read in file(s) containing the DFAs with and without scores
    -Categorize the files into DFA0,1,...,n.txt for every DFA with specified format and SDFA0,1,...,n.txt 
        for every DFA with specified format and score from program.  When DFA scored, store in file? with 
        global number incrementing every time a file is created.
    
    
