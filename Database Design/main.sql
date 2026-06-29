CREATE DATABASE BTD210_Asg2_4
GO
USE BTD210_Asg2_4
GO

CREATE TABLE FACULTY(
F_ID TINYINT PRIMARY KEY,
F_FNAME VARCHAR(255),
F_LNAME VARCHAR(255)
);
CREATE TABLE TERM(
S_CODE INT PRIMARY KEY,
S_SEASON VARCHAR(255),
S_YEAR INT
);
CREATE TABLE COURSE(
C_CODE VARCHAR(255) PRIMARY KEY,
C_TITLE VARCHAR(255),
S_SEMESTER TINYINT,
C_DESCRIPTION VARCHAR(1024),
C_METHOD VARCHAR(255),
C_HOURS INT,
C_WEEKS INT,
F_ID TINYINT,
FOREIGN KEY (F_ID) REFERENCES FACULTY
);
CREATE TABLE CLO(
CLO_ID TINYINT,
CLO_DESC VARCHAR(1024),
C_CODE VARCHAR(255)
PRIMARY KEY(CLO_ID,C_CODE),
FOREIGN KEY (C_CODE) REFERENCES COURSE
);
CREATE TABLE PLO(
PLO_ID TINYINT PRIMARY KEY CHECK(PLO_ID <=8),
PLO_DESC VARCHAR(255)
);
CREATE TABLE GA(
GA_ID TINYINT PRIMARY KEY CHECK(GA_ID<=12),
GA_DESC VARCHAR(255)
);
CREATE TABLE BOOK(
BOOK_ID TINYINT PRIMARY KEY,
BOOK_IDENTIFIER VARCHAR(255),
BOOK_PUBLISHER VARCHAR(255),
BOOK_TITLE VARCHAR(255),
C_CODE VARCHAR(255)
FOREIGN KEY (C_CODE) REFERENCES COURSE,
);
CREATE TABLE AUTHOR(
AUTHOR_ID TINYINT PRIMARY KEY,
AUTHOR_FNAME VARCHAR(255),
AUTHOR_LNAME VARCHAR(255)
);
CREATE TABLE PROGSATISFY(
C_CODE VARCHAR(255),
PLO_ID TINYINT,
PRIMARY KEY (C_CODE,PLO_ID),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (PLO_ID) REFERENCES PLO
);
CREATE TABLE GASATISFY(
C_CODE VARCHAR(255),
GA_ID TINYINT,
PRIMARY KEY (C_CODE,GA_ID),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (GA_ID) REFERENCES GA
);
CREATE TABLE PRNEED(
C_CODE VARCHAR(255),
PR_CODE VARCHAR(255),
PRIMARY KEY (C_CODE),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (PR_CODE) REFERENCES COURSE
);
CREATE TABLE CRNEED(
C_CODE VARCHAR(255),
CR_CODE VARCHAR(255),
PRIMARY KEY (C_CODE),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (CR_CODE) REFERENCES COURSE
);
CREATE TABLE FACEFFECT(
C_CODE VARCHAR(255),
F_ID TINYINT,
PRIMARY KEY (C_CODE,F_ID),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (F_ID) REFERENCES FACULTY
);
CREATE TABLE WRITING(
BOOK_ID TINYINT,
AUTHOR_ID TINYINT,
PRIMARY KEY (BOOK_ID,AUTHOR_ID),
FOREIGN KEY (BOOK_ID) REFERENCES BOOK,
FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR
);
CREATE TABLE TERMING(
C_CODE VARCHAR(255),
S_CODE INT,
PRIMARY KEY (C_CODE,S_CODE),
FOREIGN KEY (C_CODE) REFERENCES COURSE,
FOREIGN KEY (S_CODE) REFERENCES TERM
);

INSERT INTO FACULTY VALUES('1','Vida','Movahedi');
INSERT INTO FACULTY VALUES('2','Allan','Randall');
INSERT INTO FACULTY VALUES('3','Jacky','Lau');
INSERT INTO FACULTY VALUES('4','Kifah','Al-Ansari');
INSERT INTO FACULTY VALUES('5','Arif','Obaid');
INSERT INTO FACULTY VALUES('6','Ali','Sanaee');

INSERT INTO COURSE VALUES('BTD210','Database Design Principles', '3', 'This course introduces the principles of relational database design and use. 
Students learn a methodology for relational database design that uses Entity Relationship Diagrams and normalization of data. 
The design is then used to create a database schema, and to implement a database by using an introductory subset of SQL (Structured Query Language). 
Students also use SQL to perform query and data modification operations. A modern and a widely-used database server is used to host the database.', 
'LL', '4', '14', '1');
INSERT INTO COURSE VALUES('SEM305','Discrete Mathematics', '3', 'The mathematics of modern computer science is built almost entirely on discrete math. 
Students are introduced to discrete structures in order to formulate abstract concepts and techniques using the language of propositional and predicate logic and
set theory.', 'LL', '4', '14', '2');
INSERT INTO COURSE VALUES('SES250','Electromagnetics', '2', 'Students are introduced to electrostatics, magnetism and circuit theory with an emphasis on circuit and machine design. 
Electromagnetics is the foundation of all studies in electronics, wireless communications, and electrical machines. Electromagnetism is one of the four fundamental interactions (commonly called
forces) in nature, together with the strong interaction, the weak interaction, and gravitation.', 'LL', '6', '14', '3');
INSERT INTO COURSE VALUES('SEH300','Digital and Analog Circuits', '3', 'An introduction to the basic concepts of electricity, magnetism, electric circuits, and basic combinational and sequential digital circuits. 
Students develop an understanding of microprocessors and computer architecture in software driven hardware. DC and AC driven circuits, and digital circuits are studied in detail.
Fundamental electronic components are examined such as resistors, inductors, capacitors, diodes, transistors, operational amplifiers and digital logic gates.', 'LL', '4', '14', '4');
INSERT INTO COURSE VALUES('MEC110','Mechanics', '1', 'This course introduces the subject of statics. The study of particles and rigid bodies in equilibrium. 
Students study, and solve problems involving, the equilibrium of particles and rigid bodies in two and in three dimensions. In particular, they calculate the forces in the members of trusses and frames. 
They also learn to calculate the coordinates of the centroids of two-dimensional geometric figures as well as the centre of gravity of homogeneous solid bodies. 
Problems involving machines and equilibrium problems which include dry friction are studied as well.', 'LE', '6', '14', '3');

INSERT INTO CLO VALUES('1','Compose SQL to retrieve data from databases.','BTD210');
INSERT INTO CLO VALUES('2','Compose SQL to create and modify tables in databases.','BTD210');
INSERT INTO CLO VALUES('3','Prepare a physical relational database schema for specific business applications.','BTD210');
INSERT INTO CLO VALUES('4','Prepare a logical relational database schema for specific business applications.','BTD210');
INSERT INTO CLO VALUES('5','Compose an Entity Relationship Diagram for specific business applications.','BTD210');
INSERT INTO CLO VALUES('6','Re-organize data to third normal form.','BTD210');
INSERT INTO CLO VALUES('7','Distinguish the differences between relational, hierarchical and network databases.','BTD210');
INSERT INTO CLO VALUES('8','Differentiate between the basic functions of a Database Management System.','BTD210');
INSERT INTO CLO VALUES('9','Describe the responsibilities of a Database administrator in an organization.','BTD210');
INSERT INTO CLO VALUES('10','Compose such specialized material as Entity Relationship Diagrams, normalized database schemas and databases.','BTD210');

INSERT INTO CLO VALUES('1','Compare logical constructs and proofs to verify mathematical statements.','SEM305');
INSERT INTO CLO VALUES('2','Arrange sets as a building block for the types of objects considered in discrete mathematics.','SEM305');
INSERT INTO CLO VALUES('3','Construct matrices for mathematical transformations of physical systems.','SEM305');
INSERT INTO CLO VALUES('4','Classify algorithms according to growth to minimize computing time.','SEM305');
INSERT INTO CLO VALUES('5','Apply the principles of induction for mathematical proofs.','SEM305');
INSERT INTO CLO VALUES('6','Assemble graphs to show the relationships between objects.','SEM305');
INSERT INTO CLO VALUES('7','Construct trees to model computer algorithms.','SEM305');
INSERT INTO CLO VALUES('8','Design logic circuits using the principles of Boolean algebra.','SEM305');

INSERT INTO CLO VALUES('1','Examine electrostatic induction in machines for commercial applications.','SES250');
INSERT INTO CLO VALUES('2','Explore the role of electrical resistance in controlling current and voltage in hardware applications.','SES250');
INSERT INTO CLO VALUES('3','Apply magnetic induction to electric motors.','SES250');
INSERT INTO CLO VALUES('4','Connect the interaction between electric and magnetic fields in simple circuits.','SES250');
INSERT INTO CLO VALUES('5','Predict component current and voltage for various circuit configurations.','SES250');
INSERT INTO CLO VALUES('6','Design simple AC and DC circuits for electrical power transfer.','SES250');

INSERT INTO CLO VALUES('1','Apply engineering fundamentals to solve hardware problems.','SEH300');
INSERT INTO CLO VALUES('2','Connect the effect of moving electric and magnetic fields on circuits to protect against component damage and ensure correctness of operation.','SEH300');
INSERT INTO CLO VALUES('3','Employ the operating modes of analog electronic components for linear or non- linear operation.','SEH300');
INSERT INTO CLO VALUES('4','Design simple analog circuits for low power and high-power applications.','SEH300');
INSERT INTO CLO VALUES('5','Characterize digital components for combinational or sequential operation.','SEH300');
INSERT INTO CLO VALUES('6','Create simple digital circuits for synchronous or asynchronous applications.','SEH300');
INSERT INTO CLO VALUES('7','Design mixed analog and digital circuit design for interfacing to a computer.','SEH300');

INSERT INTO CLO VALUES('1','Calculate the resultant of a number of concurrent forces in two or three dimensions.','MEC110');
INSERT INTO CLO VALUES('2','Calculate the magnitude and direction of a force required to keep a given force system in equilibrium.','MEC110');
INSERT INTO CLO VALUES('3','Draw a free-body diagram of a particle acted on by forces and use the diagram as an aid to calculate the magnitudes and directions of the unknown force(s) if equilibrium is to be obtained.','MEC110');
INSERT INTO CLO VALUES('4','Use the concepts of moments and couples to calculate the single force and the single couple which is equivalent to a system of coplanar couples and/or non- concurrent forces.','MEC110');
INSERT INTO CLO VALUES('5','Define a rigid body and use free body diagrams to aid in solving for the unknown forces and/or couples required to maintain a two-dimensional rigid body in equilibrium.','MEC110');
INSERT INTO CLO VALUES('6','Calculate the coordinates of the centroids of plane areas and of the centers of gravity of homogeneous plates having uniform thickness. Calculate the magnitude and locate the line of action of that single force which is equivalent to a distributed load using the concept of the centroid of area.','MEC110');
INSERT INTO CLO VALUES('7','Calculate the magnitudes of the unknown forces acting in some or all of the members of a truss, machine or frame which is acted on by a number of external forces and /or couples and which is in equilibrium.','MEC110');
INSERT INTO CLO VALUES('8','Explain dry friction and use the equations of dry friction to solve the problems of statics equilibrium.','MEC110');

INSERT INTO PLO VALUES('1','Apply mathematics, natural sciences, and engineering fundamentals to solve engineering problems.');
INSERT INTO PLO VALUES('2','Create software engineering solutions that satisfy technical and business requirements.');
INSERT INTO PLO VALUES('3','Design an optimal solution using artificial intelligence, data mining, and machine learning tools for complex and open-ended problems.');
INSERT INTO PLO VALUES('4','Employ interpersonal, teambuilding, and leadership skills to solve problems independently and in diverse teams.');
INSERT INTO PLO VALUES('5','Communicate complex engineering problems and solutions to fellow software engineers and designers as well as non-technical audiences.');
INSERT INTO PLO VALUES('6','Act ethically and responsibly with public welfare and environmental protection as a guiding professional practice.');
INSERT INTO PLO VALUES('7','Plan and manage the scope, cost, timing, and quality of the project for success as defined by the project stakeholders.');
INSERT INTO PLO VALUES('8','Utilize investigative practices and self-awareness techniques to identify and pursue lifelong learning opportunities within their field of study and more broadly.');

INSERT INTO GA VALUES('1','Knowledge Base');
INSERT INTO GA VALUES('2','Problem Analysis');
INSERT INTO GA VALUES('3','Investigation');
INSERT INTO GA VALUES('4','Design');
INSERT INTO GA VALUES('5','Use of Engineering Tools');
INSERT INTO GA VALUES('6','Individual and Team Work');
INSERT INTO GA VALUES('7','Communication Skills');
INSERT INTO GA VALUES('8','Professionalism');
INSERT INTO GA VALUES('9','Impact on Society and the Environment');
INSERT INTO GA VALUES('10','Ethics and Equity');
INSERT INTO GA VALUES('11','Economics and Project Management');
INSERT INTO GA VALUES('12','Life-long Learning');

INSERT INTO BOOK VALUES('1','ISBN-10: 1305627482 ISBN-13: 9781305627482','Course Technology','Database Systems: Design, Implementation, & Management (12th Edition)','BTD210');
INSERT INTO BOOK VALUES('2','ISBN-10: 1260091996 ISBN-13: 978-1260091991','McGraw-Hill Education','Discrete Mathematics and Its Applications (8th Edition)','SEM305');
INSERT INTO BOOK VALUES('3','ISBN-10: 9781107014022 ISBN-13: 978-1107014022','Cambridge University Press','Electricity and Magnetism','SES250');
INSERT INTO BOOK VALUES('4','http://atomoptics-nas.uoregon.edu/~dsteck/teaching/electronics/electronics-notes.pdf','','Analog and Digital Electronics','SEH300');
INSERT INTO BOOK VALUES('5','ISBN: 9780072464788','McGraw-Hill','Mechanics for Engineers: Statics and Dynamics (5th Edition)','MEC110');

INSERT INTO AUTHOR VALUES('1','Carlos','Coronel');
INSERT INTO AUTHOR VALUES('2','Steven','Morris');
INSERT INTO AUTHOR VALUES('3','Kenneth','Rosen');
INSERT INTO AUTHOR VALUES('4','Edward','Purcell');
INSERT INTO AUTHOR VALUES('5','David','Morin');
INSERT INTO AUTHOR VALUES('6','Daniel','Steck');
INSERT INTO AUTHOR VALUES('7','Ferdinand','Beer');
INSERT INTO AUTHOR VALUES('8','Russell','Johnston');

INSERT INTO TERM VALUES('2231','Winter','2023');
INSERT INTO TERM VALUES('2234','Summer','2023');
INSERT INTO TERM VALUES('2237','Fall','2023');

INSERT INTO TERMING VALUES('BTD210','2237');
INSERT INTO TERMING VALUES('SEM305','2237');
INSERT INTO TERMING VALUES('SES250','2234');
INSERT INTO TERMING VALUES('SEH300','2237');
INSERT INTO TERMING VALUES('MEC110','2231');

INSERT INTO PROGSATISFY VALUES('BTD210','2');
INSERT INTO PROGSATISFY VALUES('BTD210','3');
INSERT INTO PROGSATISFY VALUES('SEM305','1');
INSERT INTO PROGSATISFY VALUES('SEM305','3');
INSERT INTO PROGSATISFY VALUES('SES250','1');
INSERT INTO PROGSATISFY VALUES('SEH300','1');
INSERT INTO PROGSATISFY VALUES('MEC110','1');

INSERT INTO GASATISFY VALUES('BTD210','1');
INSERT INTO GASATISFY VALUES('BTD210','2');
INSERT INTO GASATISFY VALUES('BTD210','4');
INSERT INTO GASATISFY VALUES('BTD210','5');
INSERT INTO GASATISFY VALUES('SEM305','1');
INSERT INTO GASATISFY VALUES('SES250','1');
INSERT INTO GASATISFY VALUES('SEH300','1');
INSERT INTO GASATISFY VALUES('SEH300','2');
INSERT INTO GASATISFY VALUES('SEH300','5');
INSERT INTO GASATISFY VALUES('MEC110','1');

INSERT INTO PRNEED VALUES('BTD210',NULL);
INSERT INTO PRNEED VALUES('SEM305',NULL);
INSERT INTO PRNEED VALUES('SES250','MEC110');
INSERT INTO PRNEED VALUES('SEH300','SES250');
INSERT INTO PRNEED VALUES('MEC110',NULL);

INSERT INTO CRNEED VALUES('BTD210',NULL);
INSERT INTO CRNEED VALUES('SEM305',NULL);
INSERT INTO CRNEED VALUES('SES250',NULL);
INSERT INTO CRNEED VALUES('SEH300','SEM305');
INSERT INTO CRNEED VALUES('MEC110',NULL);

INSERT INTO FACEFFECT VALUES('BTD210','1');
INSERT INTO FACEFFECT VALUES('SEM305','2');
INSERT INTO FACEFFECT VALUES('SES250','3');
INSERT INTO FACEFFECT VALUES('SES250','5');
INSERT INTO FACEFFECT VALUES('SEH300','4');
INSERT INTO FACEFFECT VALUES('SEH300','5');
INSERT INTO FACEFFECT VALUES('MEC110','3');
INSERT INTO FACEFFECT VALUES('MEC110','6');

INSERT INTO WRITING VALUES('1','1');
INSERT INTO WRITING VALUES('1','2');
INSERT INTO WRITING VALUES('2','3');
INSERT INTO WRITING VALUES('3','4');
INSERT INTO WRITING VALUES('3','5');
INSERT INTO WRITING VALUES('4','6');
INSERT INTO WRITING VALUES('5','7');
INSERT INTO WRITING VALUES('5','8');



-- 1- List the CLOs for BTD210.
SELECT CLO_DESC
FROM CLO
WHERE C_CODE = 'BTD210';



-- 2- List publishers for all textbooks of all courses.
SELECT DISTINCT BOOK_PUBLISHER
FROM BOOK;




-- 3- For all courses offered in 2237, list the course code, title, the name of the faculty who developed the course, and all faculty who are teaching the course.
SELECT C.C_CODE, C.C_TITLE,
       FDEV.F_FNAME + ' ' + FDEV.F_LNAME AS Developer,
       FTEACH.F_FNAME + ' ' + FTEACH.F_LNAME AS Instructor
FROM COURSE C
JOIN TERMING T ON C.C_CODE = T.C_CODE
LEFT JOIN FACULTY FDEV ON C.F_ID = FDEV.F_ID
LEFT JOIN FACEFFECT FE ON C.C_CODE = FE.C_CODE
LEFT JOIN FACULTY FTEACH ON FE.F_ID = FTEACH.F_ID
WHERE T.S_CODE = 2237;




-- 4- List the course code, course title and the textbook titles for courses that teach about 'SQL' (mentioned in their description or CLOs).
SELECT DISTINCT C.C_CODE, C.C_TITLE, B.BOOK_TITLE
FROM COURSE C
LEFT JOIN CLO CL ON C.C_CODE = CL.C_CODE
LEFT JOIN BOOK B ON C.C_CODE = B.C_CODE
WHERE LOWER(C.C_DESCRIPTION) LIKE '%sql%'
   OR LOWER(CL.CLO_DESC) LIKE '%sql%';





-- 5- Create a view that lists all course codes, course titles, their pre-reqs (code and title) and their co-reqs (code and title).
CREATE VIEW CourseDependencies AS
SELECT C.C_CODE,
       C.C_TITLE,

       PR.PR_CODE AS PREREQ_CODE,
       CPR.C_TITLE AS PREREQ_TITLE,

       CR.CR_CODE AS COREQ_CODE,
       CCR.C_TITLE AS COREQ_TITLE

FROM COURSE C
LEFT JOIN PRNEED PR ON C.C_CODE = PR.C_CODE
LEFT JOIN COURSE CPR ON PR.PR_CODE = CPR.C_CODE
LEFT JOIN CRNEED CR ON C.C_CODE = CR.C_CODE
LEFT JOIN COURSE CCR ON CR.CR_CODE = CCR.C_CODE;





-- 6- List all courses that do NOT have a laboratory component in their method of instruction.
SELECT C_CODE, C_TITLE
FROM COURSE
WHERE C_METHOD NOT LIKE '%LA%';




-- 7- What is the total number of hours of all courses in the program (only for samples entered)?
SELECT SUM(C_HOURS) AS Total_Hours
FROM COURSE;








-- 8- List all PLOs and the number of courses that teach each PLO.
SELECT P.PLO_ID, P.PLO_DESC, COUNT(PS.C_CODE) AS NumCourses
FROM PLO P
LEFT JOIN PROGSATISFY PS ON P.PLO_ID = PS.PLO_ID
GROUP BY P.PLO_ID, P.PLO_DESC;







-- 9- Which GA is taught in the highest number of courses? Show this GA and the number of courses it is taught in.
SELECT TOP 1 GA_ID, COUNT(*) AS NumCourses
FROM GASATISFY
GROUP BY GA_ID
ORDER BY COUNT(*) DESC;







-- 10- List all GAs and the highest semester they are taught in.
SELECT GA.GA_ID, GA.GA_DESC, MAX(C.S_SEMESTER) AS MaxSemester
FROM GA
JOIN GASATISFY GS ON GA.GA_ID = GS.GA_ID
JOIN COURSE C ON GS.C_CODE = C.C_CODE
GROUP BY GA.GA_ID, GA.GA_DESC;









-- 11- What is the minimum, maximum and average number of CLOs in courses.
SELECT MIN(cnt) AS MinCLO,
       MAX(cnt) AS MaxCLO,
       AVG(cnt * 1.0) AS AvgCLO
FROM (
    SELECT C_CODE, COUNT(*) AS cnt
    FROM CLO
    GROUP BY C_CODE
) AS X;







-- 12- Create a view named ‘DesignInCLO’ which lists course codes and the number of times the word 'design' is mentioned in the CLOs of each course (let’s call this column nDesign).
GO
CREATE VIEW DesignInCLO AS
SELECT C_CODE,
       SUM(CASE 
            WHEN LOWER(CLO_DESC) LIKE '%design%' 
            THEN 1 ELSE 0 
       END) AS nDesign
FROM CLO
GROUP BY C_CODE;
GO










-- 13- List course code, nDesign and whether the course is checked off for 'design' in GAs for all courses that nDesign is more than zero. Use DesignInCLO.
SELECT D.C_CODE, D.nDesign,
       CASE 
           WHEN EXISTS (
               SELECT 1 
               FROM GASATISFY GS
               JOIN GA ON GS.GA_ID = GA.GA_ID
               WHERE GS.C_CODE = D.C_CODE
               AND LOWER(GA.GA_DESC) LIKE '%design%'
           )
           THEN 'YES'
           ELSE 'NO'
       END AS Has_Design_GA
FROM DesignInCLO D
WHERE D.nDesign > 0;








-- 14- Calculate the percentage of CLOs per course that are at ‘APPLY’ level in Bloom’s taxonomy. Here, these would be CLOs that use one of these verbs: (Apply, Use, Implement, Demonstrate, Interpret, Execute, Solve, Calculate).
SELECT C_CODE,
       (SUM(CASE 
            WHEN LOWER(CLO_DESC) LIKE '%apply%' OR
                 LOWER(CLO_DESC) LIKE '%use%' OR
                 LOWER(CLO_DESC) LIKE '%implement%' OR
                 LOWER(CLO_DESC) LIKE '%demonstrate%' OR
                 LOWER(CLO_DESC) LIKE '%interpret%' OR
                 LOWER(CLO_DESC) LIKE '%execute%' OR
                 LOWER(CLO_DESC) LIKE '%solve%' OR
                 LOWER(CLO_DESC) LIKE '%calculate%'
            THEN 1 ELSE 0 END) * 100.0
        / COUNT(*)) AS Apply_Percentage
FROM CLO
GROUP BY C_CODE;





