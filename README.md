# Data Analytics Final Report 

### By David Blessent

## Project Summary

I was tasked with deciding if any changes needed to be make at the cafeteria at my college. I conducted a survey and got results back from 125 of the students who attend my college. 

The recommendations I am hoping to pass along to the cafeteria boss are as follows:

1)	How health conscious are your students?
2)	Have students’ eating habits changed since they came to college?  For those who said habits got worse, what were the top two most reported changes?  For those who said habits got better, what were the top two most reported changes?  
3)	If you offered ethnic food in your cafeteria, would students be likely to eat it?  If so, what is the most popular cuisine?
4)	You’d also like to offer some comfort foods for your students.  What are the 5 most popular comfort foods?
5)	You also want to bring some nostalgia to your cafeteria.  What were your students top 5 childhood favorites?
6)	Should you offer fruit in the cafeteria?
7)	Should you offer vegetables in the cafeteria?
8)	Based on the student’s ideal diet, what other changes would you recommend?
9)	Do enough students live on campus who would come to your cafeteria?
10)	Based on what your students are willing to pay for a meal out, how should your price your meals?

## Approach

For the most part I followed the tried and true Murach's approach. Due to the scale of this project, I decided to split it into multiple notebooks files. The first file `J1_data_cleaner.ipynb` is responsible for the initial exploration and cleaning of the data. I'm sure there are a lot of things I missed on the cleaning (trying to be time-conscious), but I had a lot of fun doing this. I took the experience I've gained at work writing php iterations for dynamic database seeders my front-end components use for the data they use to try automate as much of the process as I can. 

I took the numeric columns one at a time and checked the mean median and mode. Most of the time the median and mode were the same, so I applied the median value to replace all null values. I then took at deeper look at the comfort_food% columns trying to figure out how they would be used and what I needed to do for them. I ended up just replacing the null values with a new value called 'missing'. Then I wrote the *runNullFixer()* function to iterate through the categorical fields that had a null value % less than 10% and replace all null values with the mode. Most of these fields have 2,3,4,or 5 discrete values, so I went with the mode because the average is 'meaningless'. When the null value % was greater than 10% I had it randomly select a unique value from the exisiting values for each column. I felt that adding the mode to these fields with a higher null % would add more bias to the results than randomly sampling from the existing pool. 

I made a kind of risky call with how I handled type_sports by collapsing all the rows that had a response that included more than one sport into a 'Multi' category. I mostly chose to do this because it felt easier than other ways of handling it, and I knew after reviewing the options in the code book that I didn't want to do the text analysis on the type_sports field. It wasn't directly relevant to any of the objectives, although it is indirectly related to health conscious, and lumping into the Multi category, while accounting for the relationship with health concious, it feels like it might make sense to do that (actually). The main idea behind the process was to just map all the fields that meant the same thing into a smaller number, but still diverse group, of categories. 

I designed the data cleaner to produce a cleaned version of the data set at `material/data/food_cleaned.csv`. It also exports two versions of `material/data_report_*.txt` that capture the initial data exporation and sumamry before and after cleaning as a receipt (and a useful tool in the split pane view).

The second notebook file is `J2_data_analysis.ipynb`. It starts by walking through some Exploratory Data Analysis. I like the process of cleaning and moving data around better in python. I know more of the options and I know how to look up what I'm trying to do. However, I think R made the text analysis really easy AFTER the data was parsed and tokenized and in the perfect condition for the libraries' methods. I decided to use the python to make the data how I want it, then import it into Rstudio to do the text analysis component. To assist me with this, and to provide a refernce tool for the jump into a new IDE, data_analysis produces `material/unique_text_inputs.txt` as a receipt of all the unique values in the 'object' datatype columns. Once I got there, I became frustrated with the tokenization process splitting foods like frozen yogurt into two seperate tokens. I remember that there is the library that handles tokenization more on a phrase basis, but I'm running out of time and would have had to dive back through all the weeks material and assignments to find it. 

For the most part I stuck with a recipe and made distribution plots. I realize this is a fairly surface level analysis, but when I started this yesterday I didn't fully understand the scope of the project and I'm at deadlines (and ETL is looming). I believe many of these questions can be addressed with the visualizations I created, and could be a strong set up for further analysis with more sophisticated methods. 

## Quick Answers

1) Answered in presentation.
2) Its seem like, generally speaking, students eating habits have gotten worse since the came to college. The two worse habits most reported were 'worse quality' and 'bigger quantity'. The two best habits most reported were 'Healthier' and 'Drink more water'. 
3) Yes, students are very interested in ethnic food offerings.
4) Icecream, pizza, chocolate, chips, cookies
5) *skipping due to time constraint*
6) Yes, fruit should be offered.
7) Yes, vegetables should be offered.
8) I would add more protein options in a home-cooked style. Traditional dinners.
9) The overwhleming majority of students live on campus. 
10) The $10-$20 range is the most voted for acceptable prices for a meal. 