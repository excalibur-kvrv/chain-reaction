## Chain Reaction AI

An AI that will help in winning the game of chain reaction, this is based on mini-max algorithm.

### Rules:-
- There can be N number of players, each player is assigned a unique color for distinction. where N >= 2
- A player picks a position on the board, that will result in incrementation of the value at that position.
- On incrementation 3 senarios are possible for a player:-
    - Hijack another position(Occupied by another player).
    - Take another position.
    - Increment value held by you at a particular position.
- Increment behaviour:-
    - If your position to be incremented is a non edge position, if value is 3, on incrementation, your current     position becomes 0, and immediate neighbors(LRTD) will get incremented by +1, this can also result in hijacking, and recursive.
    - If your position is an edge:-
        - If your position is the edge of a row and coloumn, immediate 2 neighbors, will get incremented by 1.
        - If you position is an edge of a row or a coloumn, 3 immediate neighbors are incremented by 1  
- Goal is to hijack all players until only 1 is left.
