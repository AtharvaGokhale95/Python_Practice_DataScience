select 
    CASE                            
        WHEN G.Grade >= 8 THEN S.Name              -- The case condition only returns 1 column, so we only consider name here
        ELSE NULL
    END AS Name, 
    G.Grade, 
    S.Marks
from Students S
JOIN Grades G
    ON S.Marks between G.Min_Mark and G.Max_Mark
Order by        
    G.Grade DESC,
    CASE                                            -- Because all the rows don't have a Name column, we need to use the case condition also in ORDER BY 
        WHEN G.Grade >= 8 THEN S.Name
        ELSE NULL
    END ASC,
    CASE
        WHEN G.Grade < 8 THEN S.Marks
        ELSE NULL
    END ASC