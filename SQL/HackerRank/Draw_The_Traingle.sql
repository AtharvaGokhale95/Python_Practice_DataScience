-- Using Recursive CTE
With Recursive pattern(row_number) as (
    -- Anchor member: Base Query - The Starting point
    select 20

    UNION ALL
    -- Recursive Member - Repeatedly runs on the output of the previous result
    select row_number - 1
    from pattern
    where row_number > 1 -- This is the logic to stop the recursive member
)
-- The CTE generates the numbers from 20 -> 1

-- Now select query to print * char for 20 times
select REPEAT('* ', row_number) 
from pattern 


-- Output:
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * *
* * * * * * * * * * * * * *
* * * * * * * * * * * * *
* * * * * * * * * * * *
* * * * * * * * * * *
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*


With Recursive pattern(row_number) as (
    -- Base Query
    select 1
    UNION ALL
    -- Recursive query
    select row_number + 1
    from pattern
    where row_number < 20
)

select REPEAT('* ', row_number)
from pattern