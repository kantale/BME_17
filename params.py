
class Params:

    GREETING = '''
Hello,

These are your grades for the exercises {START}-{END} in the course: 
'''

    MAIL_PATTERN = '''
{GREETING}

BME-17  Bio-Informatics

Mail: {AM}


{EXERCISES}

================================
Summary:

{SUMMARY}

For questions please send email to: kantale@ics.forth.gr

Regards,
Alexandros Kanterakis
'''

    MAIL_EXERCISE_PATTERN = '''
================================
  Exercise: {EXERCISE}
================================
  You submitted:
--------------------------------
{SOLUTION}
--------------------------------
Comments:
{COMMENT}
--------------------------------
Grade: {GRADE}
--------------------------------
'''



    MAIL_SUBJECT = 'BME-17 - Grades for exercises {START}-{END}'

    SUBMIT_NOTHING = 'You did not submit anything for this exercise'
    AVERAGE_EXERCISES = 'Average exercise grade' #  'Μέσος όρος ασκήσεων'
    PROJECT_GRADE = "Project's Grade" # Βαθμός Project
    FINAL_FLOAT_GRADE = 'Final float grade' # 'Τελικός δεκαδικός βαθμός''
    FINAL_ROUNDED_GRADE = 'Final rounded grade' # 'Τελικός στρογγυλοποιημένος βαθμός'


    START_AGGREGATE_MAIL = '''
Hello, below is your detailed grade in the course:

BME-17 Bio-Informatics

Mail: {AM}

Exercises:
'''

    END_AGGREGATE_MAIL = 'Regards,\n' 'Alexandros Kanterakis\n' # 'Χαιρετώ,\n' 'Αλέξανδρος Καντεράκης\n'

    EXERCISE = 'Exercise' # Άσκηση 
    GRADE = 'Grade' # Βαθμός 
    AVERAGE = 'Average' # Μέσος όρος

    WEIGHT_FUN = lambda *, exercises, final, project : (
        (0.5 * exercises) + 
        (0.0 * final) + 
        (0.5 * project)
    )


    WEIGHT_FUN_2 = lambda *, exercises, final, project : (
        (0.33 * exercises) + 
        (0.34 * final) + 
        (0.33 * project)
    )

    #FINAL_GRADE_FUN = lambda *, exercise_average, final_average, project_average, decimal_grade :  f'0.33*{exercise_average} + 0.34*{final_average} + 0.33*{project_average} = {decimal_grade}\n\n'
    FINAL_GRADE_FUN = lambda *, exercise_average, final_average, project_average, decimal_grade :  f'0.5*{exercise_average} + 0.5*{project_average} = {decimal_grade}\n\n'

    TOTAL_EXERCISES = 25
    #TOTAL_EXERCISES = 100 





