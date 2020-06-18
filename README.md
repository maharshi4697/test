# Postman_Assignment
Maharshi Chattopadhyay's Postman Assignment


Pre-Requisites:
1. Docker.
2. Docker-Compose.

A.Steps to run code:
1. Clone the repo.
2. Run the build_run.sh.
3. Once Python code, is run successfully, you'll get a message. Press Ctrl+c on the keyboard.
4. Postgres #, will open.
5. Copy Commands from Top Ten Query.txt to see top 10 products with the same name.
6. When done, use '\q' to exit from the Postgres Instance.
7. Run stop.sh to stop containers.


B. Details of all the tables.

No. of Tables : 3.
1.Staging Table, no of rows: 500,000.
2.Final Table, no of rows: 466,693.
3.Agg Table, no of rows: 212,660.

Staging Table and Final Table will be created on running the shell script.
For the Agg table, query is provided in the Top Ten Query.txt ( Can be automated upon requirement.)

Staging Table: ( Rows as per csv, input using String.io to reduce time and memory utilization .)

    name            sku                     description
    Bryce Jones    lay-raise-best-end    Art community floor adult your single type. Per back community former stock thing.
    John Robinson    cup-return-guess    Produce successful hot tree past action young song. Himself then tax eye little last state vote. Country down list that speech economy leave.
    Theresa Taylor    step-onto    Choice should lead budget task. Author best mention. Often stuff professional today allow after door instead. Model seat fear evidence. Now sing opportunity feeling no season show.
    Roger Huerta    citizen-some-middle    Important fight wrong position fine. Friend song interview glass pay. Organization possible just.
    John Buckley    term-important    Alone maybe education risk despite way. Want benefit manage financial story term must. Former wife activity firm example later. Black win rest ask.
    Tiffany Johnson    do-many-avoid    Born tree wind. Boy marriage begin value. Record health laugh ask under notice federal. Hard lose need sell treatment. Certain throw executive front late. Because truth risk.
    Roy Golden DDS    help-return-art    Pm daughter thousand. Process eat employee have they example past. Increase author water. Magazine child mention start.
    David Wright    listen-enough-check    Under its near. Necessary education game everybody. Hospital upon suffer year discussion south government nothing. Knowledge race population exist against must wear level. Coach girl situation.
    Anthony Burch    anyone-executive    I lose positive manage reason option. Crime structure space both traditional teacher that.
    Lauren Smith    grow-we-decide-job    Smile yet fear society theory help. Rather thing language skill since heart across wait. According ask them government or.


Final Table: ( Columns sorted, Primary Key Brought First, Indexing applied on 'sku' and Duplicates Removed. )

    sku                    name                 description
    a-above-its-focus    Jennifer Lambert    Go audience old. Law main federal area myself. Leave various leave discover consumer hotel. Safe fall up compare plant affect stuff.
    a-act-spring-camera    Vicki Barber    Difference compare society best structure democratic team machine. Administration item light among. Each when capital condition election miss defense. Left after treat listen law girl.
    a-adult-situation    Candace Francis    Fine month cold age teach all factor brother. Table edge believe garden recently. Project both claim positive minute country night form. Site personal to able point of growth.
    a-age-make-picture    Bailey Irwin    Gun necessary knowledge human leave. Thank his drop which go long. Shoulder our yet fact smile. Speech campaign charge value. Gun approach nothing physical mind.
    american-around    Amanda Rhodes DVM    Cup statement fund debate court. Husband night to.
    a-agent-although    Lance Baker    Speak ok executive bed central we. Carry machine before read represent. Direction Mrs compare data. Authority car stock different. Call until start quickly remain. Four fly measure their.
    a-agree-job-hour    Jason Smith    Choose recognize usually support memory production. Reality provide picture central. Charge discussion also save huge light eat. Religious agree too edge great concern way. Ok fine affect.
    ability-argue-white    Carly Brown    Necessary ready energy expect physical protect example.
    ability-care-bank    Joyce Santos    Themselves kind thought. Pretty resource interesting finish concern better little.
    a-agree-list    Randall Miller    Again same share option no best who. Wear my create ahead third vote drop or. Author body teacher each star fight. Military final character dinner child. American office set include soon.


Agg Table: ( T op 10 products, with the same names. Derived from final table.)

    Top 10 names   No. of products
    Michael Smith    231
    Michael Johnson    175
    Robert Smith    156
    Christopher Smith    150
    David Smith    149
    John Smith    144
    James Smith    142
    Michael Williams    141
    Jennifer Smith    138
    Michael Brown    133

C.Points Achieved:
1. Code Follows Concept of OOPS. (1 Main Class,3 Helper Classes)
2. Support for regular non-blocking parallel ingestion. (500k rows takes less than 90 secs to insert into table.) (CSV split into 100k rows and run simultaneously to verify non-blocking parallel ingestion.)
3. Support for updating existing products. ( For Current CSV, last entry of each sku is considered. For new CSV, on conflict command implemented in Postgres.)
4. All Product Details ingested into table (Maharshi_Postman.Products). (Schema Name and Table Name can be updated in Configurations.txt)
5. Aggregated Table Query available in Top Ten Query.txt. Can be copy pasted and used as is, in terminal if configuration file is not changed.

D.Points Not Achieved:
N/A

E. If Given More Days:

1. Add Django Framework, for front-end support.
2. New CSV and Configuration file can be inserted via front-end instead of placing it in the path.
