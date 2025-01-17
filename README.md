# The Aggressive Cow Problem
Given the problem laid out in Assessment_Brief_TASK-A I have identified three main stages I intended to go though three stages to tackle the problem. 

1. Determine the business logic to apply to the problem. 
2. Write unit tests. The breif suggests two functions and we may only add a couple more to apply our business logic so the aim will be for 100 coverage on tests. 
3. Write and analyse the python code. 

## Business Logic
Based on the assement breifing these are the business assumptions which I have made and will be followed during the deveopment stage. 

- All stall postions are positve and zero indexed.
- If all cows cannot be placed or user input is invalid the program will use a set of error codes. For these we will use negative numbers as we don't expect to recieve negative stall coordintes (See table 1.1).
- When a single stall coordinate is passed in this isn't sufficent to calculte a max min distance so return an error.
- If the number of cows exceeds the number of stalls then return an error. 
- We know only one cow can be placed per stall. If the input contains the same stall coordinate twice then we should return an error. 

### Error Codes
| Error Condition | Error Code | Error Message |
| ----------- | ----------- | ----------- |
| More cows than stalls | -1 | Cows exceeds stalls. |
| Duplicate stall coordinates | -2 | Duplicate stall coordinates have been input. |
| A single stall is passed in | -3 | Unable to calculate distance with a single stall |
| A negative stall coordinate is given. | -4 | Negative stall coordinates are not permitted. |

Table 1.1
## Unit tests


## Code analysis

