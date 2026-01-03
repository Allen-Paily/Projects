# Traffic Light

Simple circuit to demonstrate a simplified 4 way traffic light system. Utilizes 74 series ic chips including and, or, and binary counter chips. 

There are 4 lanes: lane 1 and 3 are parallel and lanes 2 and 4 are parallel. 

```
                  | 1 | 3 |
                  |   |   |
                  |   |   |
       ___________|   |   |___________
       2                              2
       -----------         -----------
       4                              4   
       ___________         ___________
                  | 1 | 3 |
                  |   |   |
                  |   |   |
                  |   |   | 
```
For simplicity we will ignore left turn and right turn lights.

6 states are needed for a 4 way traffic light stop:

State 1: Lane 1 and 3 are green and lane 2 and 4 are red <br>
State 2: Lane 1 and 3 are yellow and lane 2 and 4 are red <br>
State 3: Lane 1 and 3 are red and lane 2 and 4 are red <br>
State 4: Lane 1 and 3 are red and lane 2 and 4 are green <br>
State 5: Lane 1 and 3 are red and lane 2 and 4 are yellow <br>
State 6: Lane 1 and 3 are red and lane 2 and 4 are red <br>

We can then use a 74ls163 binary counter to count from 0-5 to represent these 6 states.
For each state we can use combinatinal logic to turn on the desired light.

We will call the red, green, and yellow lights that guide lanes 1 and 3 r1, g1, and y1 respectively  <br>
We will call the red, green, and yellow lights that guide lanes 2 and 4 r2, g2, and y2 respectively <br>
States 1-6 will be 0-5 in binary <br>

G1 is only on when the state is 000 <br>
Y1 is only on when the state is 010 <br>
R1 is on when the state is 010, 011, 100, or 101 <br>
G2 is only on when the state is 011 <br>
Y2 is only on when the state is 100 <br>
R2 is on when the state is 101, 000, 001, or 010 <br>

Using this information we can use AND and OR gates to turn on each light depending on the state of the binary counter.

Click [here](https://drive.google.com/drive/folders/1OTGpsSs9fFLDPTIjZPYxCcqT3BRqG7x6) for video
